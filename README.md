<div align='center'>
  <h2>Blog Website</h2>
<img src='https://github.com/user-attachments/assets/1601b23c-58d3-4d18-a8f7-51dfd5b9287d' width=500/>
</div>

### Techstack

1. Jekyll: Website skeleton
2. SASS: Styling

### To Run Locally

1. Clone website to your IDE by running `git clone https://github.com/Anusree6154s/documentation.git`
2. Run `bundle exec jekyll serve` or `npm start` in terminal
3. Visit the url that appears in your terminal
   > **To stop application**: Press `Ctrl+C` and then press y

### Adding Docs

- To add a doc manually, create a Markdown file under `_docs/<slug>/readme.md` (or `content/<slug>/README.md`) with frontmatter (title, permalink, date, tags, parent, etc.) followed by the body.
  Eg: 
  ```
  ---
  layout: default
  date: 26 apr 2026
  title: OOP
  excerpt: Learning object oriented programming
  permalink: oop
  tags: [oop, software design, computer basics]
  parent : Computer Science Concepts
  ---
  ```

- To add a doc via UI, add docs through the Decap CMS at `/admin` (GitHub OAuth). [Not working currently]
