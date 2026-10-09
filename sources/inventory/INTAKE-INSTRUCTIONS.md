# Intake instructions (Microsoft 365 connector → sources/)

Applies to every e-mail or file pulled from Outlook / SharePoint into this repo.

## E-mails

1. `read_resource` on `mail:///messages/<id>` (ids are in `MANIFEST.md`).
2. Save `body.content` (HTML) unchanged to the scratch dir as `<file-stem>.html`.
3. Convert with the repo tool (run from the repo root):

   ```
   python3 -I tools/mail_html_to_md.py <scratch>/<stem>.html --out sources/emails/<stem>.md \
     --date <sentDateTime as YYYY-MM-DD> --subject "<subject>" \
     --from "<Name> <address>" --to "<recipient names, or 'Country FDs and accounting teams (N recipients)' when more than 8>" \
     --cc "<cc names>" --status <current|superseded|reference> [--superseded-by <newer stem>.md] \
     --topics <comma separated page slugs> --weblink "<webLink>" --message-id "<internetMessageId>" \
     --attachments "<names from the attachments array, skip inline images>" [--strip-quoted] [--note "<one line>"]
   ```

   * `--strip-quoted` only for replies whose quoted history is NOT the instruction.
     For a FW whose forwarded text IS the instruction, do not strip; add `--note` saying who
     originally sent it and when.
   * Status: monthly closing instructions older than the newest one are `superseded`
     (`--superseded-by` = next month's stem). The newest closing mail is `current`.
     Q&A / background threads are `reference`.
4. Never edit the converted body by hand. If the converter output is unusable, say so in the
   inventory note instead.

File stems: `YYYY-MM-DD_<slug>` with the sent date, e.g. `2026-09-25_closing-instructions-2026-09`.

## Page slugs for `--topics`

closing-calendar, closing-checklist, control-file, bank-cash, matching, suspense-dummy-accounts,
bad-debt, writing-off-receivables, tenant-guarantees, investment-property, capex,
development-b-codes, loans-interest, intercompany, currency-revaluation, equity-result-dividends,
taxes, revenue-structure, erv-vacancy, discounts-incentives, turnover-rent,
service-marketing-charges, accruals, salary-bookkeeping, redundancy-provision,
fee-income-recharges, non-recurring-expenses, below-nri-cashflow, document-codes, coda-elements,
booking-structure, approvals-segregation, reports-available-budget, budget-instructions,
ifrs-memos, newsletter-archive, contacts.

## Inventory file per batch (`sources/inventory/<batch>.md`)

For every source saved, in date order:

```
## <stem>.md — <subject> (<author>, <date>)
Deadline: <closing deadline date> | Period: <YYYY/MM>
Timetable: <date — step — reference codes>; ... (one line per row of the milestone table)
Rules:
- [<page slug>] <rule, close to verbatim, with account / doc / map codes>
- ...
Changes vs previous mail: <what is new or different, or "none visible">
Open points: <anything unclear or contradictory>
```

Keep the rules factual and verbatim-ish; do not paraphrase numbers, codes or dates.
