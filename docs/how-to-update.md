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

## Pulling e-mails with the Microsoft 365 connector

When the connector is available in the Claude session, e-mails are fetched read-only from Outlook: find the message, read it, save the HTML body and convert it with `python3 -I tools/mail_html_to_md.py <body.html> --out sources/emails/<YYYY-MM-DD_slug>.md --date ... --subject ... --from ... --status ...`. The full procedure, the page slugs for `--topics` and the per-batch inventory format are in `sources/inventory/INTAKE-INSTRUCTIONS.md`; `sources/inventory/MANIFEST.md` lists the messages pulled so far with their Outlook ids.

## Adding a new topic

1. Copy `docs/topics/_template.md` to `docs/topics/<slug>.md` (the template is not part of the site navigation).
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

## Live preview page (Claude artifact)

While the site is not yet on GitHub Pages, the latest build is published as a private Claude artifact:
<https://claude.ai/artifact/PCbv2b93BcMBJ79ejqKx6N>. It is republished after every change pushed to the branch.
To rebuild it by hand: `python3 tools/build_artifact.py <out-dir>` and publish `artifact-root.html`
with the files under `site-artifact/` to that URL.
