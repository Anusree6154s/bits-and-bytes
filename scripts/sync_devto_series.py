
import os
import re
import json
import time
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

import requests
import yaml

API = "https://dev.to/api"
API_KEY = os.environ["DEVTO_API_KEY"]
SITE_BASE_URL = "https://anusree6154s.github.io/bits-and-bytes/"
APPLY_CHANGES = os.getenv("APPLY_CHANGES", "false").lower() == "true"

HEADERS = {
    "api-key": API_KEY,
    "Accept": "application/vnd.forem.api-v1+json",
    "Content-Type": "application/json",
    "User-Agent": "Jekyll-Series-Sync/1.0",
}

session = requests.Session()
session.headers.update(HEADERS)


def normalize_url(url):
    """Normalize URLs for reliable canonical URL matching."""
    parts = urlsplit(url.strip())

    return urlunsplit((
        parts.scheme.lower(),
        parts.netloc.lower(),
        parts.path.rstrip("/"),
        "",
        "",
    ))


def read_frontmatter(content):
    match = re.match(
        r"\A---[ \t]*\r?\n(.*?)\r?\n---",
        content,
        re.DOTALL,
    )

    if not match:
        return None

    return yaml.safe_load(match.group(1)) or {}


def get_jekyll_articles():
    """Create canonical URL -> parent mapping from _docs."""
    articles = {}

    for file in Path("_docs").rglob("*.md"):
        content = file.read_text(encoding="utf-8")
        metadata = read_frontmatter(content)

        if not metadata:
            continue

        title = metadata.get("title")
        parent = metadata.get("parent")
        permalink = metadata.get("permalink")

        if not title or not parent or not permalink:
            continue

        if not isinstance(parent, str):
            raise ValueError(f"Invalid parent in {file}")

        if permalink.startswith(("http://", "https://")):
            canonical_url = permalink
        else:
            canonical_url = (
                SITE_BASE_URL.rstrip("/")
                + "/"
                + permalink.strip("/")
                + "/"
            )

        key = normalize_url(canonical_url)

        if key in articles:
            raise ValueError(
                f"Duplicate canonical URL in Jekyll: {canonical_url}"
            )

        articles[key] = {
            "title": title,
            "series": parent,
            "file": str(file),
        }

    return articles


def fetch_all_dev_articles():
    articles = []
    page = 1

    while True:
        response = session.get(
            f"{API}/articles/me/all",
            params={"page": page, "per_page": 100},
            timeout=30,
        )
        response.raise_for_status()

        batch = response.json()

        if not batch:
            break

        articles.extend(batch)

        if len(batch) < 100:
            break

        page += 1

    return articles


def update_body_series(body, series):
    """Update series in existing DEV Markdown frontmatter."""
    match = re.match(
        r"\A(---[ \t]*\r?\n)(.*?)(\r?\n---[ \t]*(?:\r?\n|\Z))",
        body,
        re.DOTALL,
    )

    if not match:
        return body

    opening, frontmatter, closing = match.groups()

    pattern = re.compile(
        r"^series\s*:\s*.*$",
        re.MULTILINE,
    )

    value = "series: " + json.dumps(series, ensure_ascii=False)

    if pattern.search(frontmatter):
        frontmatter = pattern.sub(value, frontmatter)
    else:
        frontmatter += "\n" + value

    return opening + frontmatter + closing + body[match.end():]


def update_dev_article(article, series):
    article_id = article["id"]
    title = article["title"]

    payload = {"series": series}

    # If DEV provides the body, update its frontmatter too.
    # DEV gives embedded frontmatter precedence over API parameters.
    body = article.get("body_markdown")

    if isinstance(body, str):
        payload["body_markdown"] = update_body_series(body, series)

    if not APPLY_CHANGES:
        print(
            f"[DRY RUN] {title}: "
            f"series -> {series}"
        )
        return

    response = session.put(
        f"{API}/articles/{article_id}",
        json={"article": payload},
        timeout=45,
    )
    response.raise_for_status()

    print(f"[UPDATED] {title}: series -> {series}")

    # DEV update endpoint: 30 requests per 30 seconds.
    time.sleep(1.1)


def main():
    print("Reading Jekyll documents...")

    jekyll_articles = get_jekyll_articles()

    print(f"Jekyll documents with parent: {len(jekyll_articles)}")

    print("\nFetching DEV articles...")

    dev_articles = fetch_all_dev_articles()

    print(f"DEV articles fetched: {len(dev_articles)}")

    matched = 0
    unmatched = 0

    for article in dev_articles:
        canonical_url = article.get("canonical_url")

        if not canonical_url:
            unmatched += 1
            print(f"[SKIPPED] No canonical URL: {article['title']}")
            continue

        key = normalize_url(canonical_url)
        source = jekyll_articles.get(key)

        if not source:
            unmatched += 1
            print(f"[SKIPPED] No Jekyll match: {article['title']}")
            continue

        matched += 1
        update_dev_article(article, source["series"])

    print("\nSummary")
    print(f"Matched articles: {matched}")
    print(f"Unmatched articles: {unmatched}")

    if not APPLY_CHANGES:
        print("\nDRY RUN: No DEV articles were changed.")


if __name__ == "__main__":
    main()
