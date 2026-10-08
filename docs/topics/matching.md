---
title: Matching principles
---

# Matching principles

<div class="page-meta" markdown>
**Applies to:** all entities · **Owner:** Group Finance / Shared Service Center · **Last reviewed:** 2026-10-08
</div>

## Rule

Matching assigns an invoice to the payment that settled it. It is mandatory for all monetary items (cash, receivables, payables, taxes payable, loans). Its purpose: know which invoices are paid, keep clean outstanding balances on debtors, creditors, accruals and suspense accounts, show correct FX results, and allow automated reporting (cash flow, collection rate, bad debt).

**Valid matching**

- Match per EL1 / EL2 / EL3 / EL4 / EL5 / EL6; all elements identical and in balance before matching (EL2 may be ignored).
- One invoice against one payment; one invoice against several payments (instalments); several invoices against one payment (same debtor or creditor).
- Matching date and period equal the date of the payment / settlement / write-off. If that period is closed, use the first day of the open period.
- A/R: if the sender gives a specification, follow it. Without specification, collections tries to reach the sender; if unsuccessful leave the amount **unmatched** (the bad debt query takes overpayments into account). For partial payments match the base rent invoice first, then service invoices.

**Invalid matching** (flagged by control C29)

- Several EL1 (entities), EL3 (books) or EL6 (counterparties) in one match: Coda creates automatic `Z-DISPERSE` balancing lines that are impossible to trace. First reclass by journal (for example 13111 to 25550) so each EL4 / EL6 balances, then match per EL4 and per EL6.
- Several bank lines against several invoices in one match.
- Matching date before the bank document date.
- Payment booked in one period and matched in another (received in March, matched in April).
- Matching date in a different period than the settlement booking.

**Credit notes and back invoices**

1. Invoice sent. 2. Debtor pays. 3. Credit note sent. 4. Match the credit note against the original invoice (unmatch the payment first if needed). 5. Any balance stays on the **payment**, not on the credit note. This keeps the collection rate correct: an overpayment does not count as payment of the invoice.

**Frequency and ownership**

| Area | Frequency | Responsible |
|---|---|---|
| A/R | Daily after bank posting and before each debtors meeting | A/R team, senior accountants |
| A/P | Daily after bank posting and before each payment proposal | A/P team, senior accountants |
| Other balance sheet accounts | Daily, and always before currency revaluation | Senior accountants |

**Balance rule after matching** (local or EUR): balance of the account = lines with status available / held / proposed / payment suppressed + lines with status paid / cancelled whose payment date is after the reporting date.

**FX**: match foreign currency items on the bank document date. A missed match leaves the invoice to be revalued at month end while the collection is not, producing a false FX result and an unbalanced balance sheet.

## How to (Coda)

- Matching masters under General Ledger: "Matching - Assets" and "Matching - Holding & Service"; choose the correct sub-header.
- Status after approval: `Available`; after matching: `Paid`. Matching creates a `Z-DISPERSE` document.
- BO report "Outstanding ledger" lists open items per SCoA and counterparty; control file tab "R C17c AP and AR match quality" and control C29 review quality.
- "How to make matching" videos are in Coda under Instruction videos.

## Change log

| Date | Change | Source |
|------|--------|--------|
| 2026-10-08 | Page created by merging "Matching principles" and the Shared Service Center "Matching" page. | `sources/wiki/pages/matching-principles.md`, `matching.md` |
