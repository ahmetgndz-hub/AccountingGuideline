# How to update this site

The guideline lives in the GitHub repository `ahmetgndz-hub/AccountingGuideline`. The published site is rebuilt automatically
on every push to `main`.

## When a new guideline e-mail is sent

1. Save the e-mail as a Markdown file in `sources/emails/` named `YYYY-MM-DD_<short-subject>.md`.
   Keep the text verbatim; add the front matter shown in `sources/README.md`.
2. If the e-mail replaces an earlier instruction, set the earlier file's `status` to `superseded`
   and add `superseded_by: <new file name>`.
3. Update the affected topic page in `docs/topics/`:
   - change the rule text,
   - update **Last reviewed** in the page header,
   - add a row to the page's **Change log** section.
4. Add the same row to `docs/changelog.md`.
5. Commit and push to `main`. The site rebuilds within a few minutes.

## Adding a new topic

1. Copy `docs/topics/_template.md` to `docs/topics/<slug>.md`.
2. Fill in every section; delete a section only if it genuinely does not apply.
3. Add the page to `nav` in `mkdocs.yml` and to the table in `docs/topics/index.md`.

## Previewing locally

```bash
pip install -r requirements.txt
mkdocs serve
```

Open <http://127.0.0.1:8000>. `mkdocs build --strict` must pass before pushing; it fails on broken links.

## Linking from SharePoint

Replace the content of the Multi Wiki page with a short introduction and a link to the published site.
The site is the source of truth; do not copy rules back into SharePoint.
