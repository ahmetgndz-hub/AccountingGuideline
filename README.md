# Multi Accounting Guideline

Knowledge center and accounting guideline for Multi Group Finance. Replaces the outdated Multi Wiki
page on SharePoint and the guideline e-mails sent over time.

- **Site:** built with MkDocs Material in Multi house style; deployed to GitHub Pages from `main`.
- **Content:** `docs/` (one Markdown page per topic).
- **Sources:** `sources/emails/` holds every guideline e-mail verbatim; `sources/wiki/` holds the old wiki text.
- **Rule of precedence:** the newest e-mail wins. Superseded instructions are removed from the guideline
  and archived in `sources/`.

## Local preview

```bash
pip install -r requirements.txt
mkdocs serve
```

## Updating

See [docs/how-to-update.md](docs/how-to-update.md).
