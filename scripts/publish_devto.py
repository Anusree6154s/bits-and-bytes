
import os
import re
import sys
import time
import requests

API = "https://dev.to/api"
API_KEY = os.environ["DEVTO_API_KEY"]
PUBLISH = os.getenv("PUBLISH", "false").lower() == "true"

HEADERS = {
    "api-key": API_KEY,
    "Accept": "application/vnd.forem.api-v1+json",
    "Content-Type": "application/json",
    "User-Agent": "Jekyll-DEVTO-Publisher/1.0",
}

session = requests.Session()
session.headers.update(HEADERS)


def fetch_articles(endpoint):
    """Fetch every page from an authenticated DEV endpoint."""
    articles = []
    page = 1
    per_page = 100

    while True:
        response = session.get(
            f"{API}{endpoint}",
            params={"page": page, "per_page": per_page},
            timeout=30,
        )
        response.raise_for_status()

        batch = response.json()

        if not isinstance(batch, list):
            raise RuntimeError(f"Unexpected response from {endpoint}")

        articles.extend(batch)

        if len(batch) < per_page:
            break

        page += 1

    return articles


def fix_frontmatter(body):
    """Correct published:false only in initial YAML frontmatter."""
    if not body.startswith("---"):
        return body

    match = re.match(
        r"\A---[ \t]*\r?\n(.*?)(\r?\n---[ \t]*(?:\r?\n|\Z))",
        body,
        flags=re.DOTALL,
    )

    if not match:
        raise ValueError("Could not parse article YAML frontmatter")

    frontmatter = match.group(1)
    closing = match.group(2)

    pattern = re.compile(
        r"^published\s*:\s*false\s*(?:#.*)?$",
        flags=re.MULTILINE | re.IGNORECASE,
    )

    corrected = pattern.sub("published: true", frontmatter)

    return body[:match.start(1)] + corrected + closing + body[match.end():]


def publish_draft(article):
    article_id = article["id"]
    title = article["title"]

    if "body_markdown" not in article or not isinstance(
        article["body_markdown"], str
    ):
        raise RuntimeError(
            f"DEV did not return body_markdown for draft {article_id}: {title}. "
            "Stopping rather than publishing without checking frontmatter."
        )

    body = fix_frontmatter(article["body_markdown"])

    if not PUBLISH:
        print(f"[DRY RUN] Would publish: {title} (ID: {article_id})")
        return

    response = session.put(
        f"{API}/articles/{article_id}",
        json={
            "article": {
                "body_markdown": body,
                "published": True,
            }
        },
        timeout=45,
    )
    response.raise_for_status()

    print(f"[SUBMITTED] {title} (ID: {article_id})")

    # Stay below the observed DEV API rate limit.
    time.sleep(3.5)


def main():
    print("Fetching all DEV articles...")

    articles = fetch_articles("/articles/me/all")

    print(f"Total articles fetched: {len(articles)}")

    # Require the API to provide the publication status.
    if any("published" not in article for article in articles):
        raise RuntimeError(
            "The DEV API response did not include the published field. "
            "Cannot safely identify drafts."
        )

    drafts = [
        article for article in articles
        if article["published"] is False
    ]

    print(f"Unpublished drafts found: {len(drafts)}")

    if not drafts:
        print("No drafts to publish.")
        return

    for draft in drafts:
        publish_draft(draft)

    if not PUBLISH:
        print("\nDry run completed. No articles were changed.")
        return

    print("\nChecking remaining drafts...")

    remaining = fetch_articles("/articles/me/unpublished")
    remaining_ids = {article["id"] for article in remaining}

    failed = [
        article["title"]
        for article in drafts
        if article["id"] in remaining_ids
    ]

    if failed:
        print("These articles are still unpublished:")
        for title in failed:
            print(f"- {title}")

        raise RuntimeError("Some articles could not be verified as published.")

    print(f"Verified: {len(drafts)} drafts are no longer unpublished.")


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(1)
