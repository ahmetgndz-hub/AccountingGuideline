---
title: Approvals and segregation of duties
---

# Approvals and segregation of duties

<div class="page-meta" markdown>
**Applies to:** all entities · **Owner:** Group Finance · **Last reviewed:** 2026-10-09
</div>

## Rule

Every commitment, invoice, manual journal, master data change and payment goes through a Coda workflow. The four-eyes principle always applies. The person who maintains master data (supplier or tenant details, IBAN, payee) must never be involved in the payment process.

### Manual journal entries

| Hierarchy level | Approval limit | Who |
|---|---|---|
| Position 0 | 0 | Preparer |
| Position 1 | Up to €25k | Chief / Head of Accounting (country) |
| Position 2 | More than €25k | Country FD |
| Position 3 | Up to €200k | Director Finance and Accounting HQ |
| Position 4 | Up to €500k | Group FD |
| Position 5 | More than €500k | CFO |

If a country fills neither position 0 nor position 1, position 0 is used to keep four eyes in the loop. Journals exempt from workflow are listed per document code in [Document codes](document-codes.md).

### Master data change and pay proposals

| Role | Right | Restriction |
|---|---|---|
| Master data change | Create and amend supplier / tenant data in Coda (IBAN, address, payee). Country wide. | Must not create or approve pay proposals. |
| Approval of master data change | Approve changes made by someone else via Coda workflow. Country wide. Creation and amendment are also subject to Legal department approval (KYC). | |
| Creation of pay proposal | Create or amend payment proposals over due and approved invoices. In practice the cash accountant or treasurer. Country or entity level. | Must not have access to master data. |
| Approval of pay proposal | Approve and process payment orders according to the power of attorney. Country FD and MD initially; above their limit the company board and BX. | |

Each country keeps the segregation of duties sheet up to date (`Segregation of duties v02.xlsx` on the old wiki; ask Group Finance for the current location).

### Invoice recording check by the country head of accounting

Since February 2020 the country head of accounting is a step in the Coda workflow for **every invoice** entered by the country accounting team, as was already the case for journal vouchers. Before approving, the head of accounting checks at least:

- document date falls within the reporting period;
- SCoA is in line with the nature of the cost;
- VAT is reflected correctly (reimbursable or not);
- counterparty (element 6) is correct;
- invoice amounts are correct;
- description is correct and in English;
- the attachment is the right document.

The aim is that invoices are recorded correctly the first time, in line with this guideline, so that no corrections are needed later.

### Commitments and invoices (purchase requests)

Approval blueprints exist per cost type: Service charge, Opex, Genex (asset company), Genex (service company and legacy), Capex, Development, Expense reports. The blueprints are workflow diagrams (`WF Matrix Blue Print @20190920.xlsx` and images on the old wiki); they are not reproduced here.

Invoices on the accounts below require a purchase order; booking without a PR is only allowed below the threshold communicated in the newsletter of 21 October 2020 (ask Group Finance for the current threshold).

| SCoA | Name |
|---|---|
| 11111 | Investment property |
| 11321 | Leasehold improvements at cost |
| 11340 | Projects under construction |
| 11341 | Fixed assets under construction |
| 11411 | Other intangible assets |
| 42530 | Marketing expenses (landlord) |
| 42540 | Maintenance and repair (opex) |
| 42560 | Legal advisors (opex) |
| 42590 | Other non-recoverable costs |
| 44120 | Independent workers |
| 44170 | Lease cost cars |
| 44311 | Rent office and parking |
| 44320 | Maintenance and repair (genex) |
| 44321 | Cleaning expenses |
| 44390 | Other costs (genex) |
| 44410 | Public relations general |
| 44450 | Fairs and expositions |
| 44490 | Other marketing expenses |
| 44550 | Auditors (genex) |
| 44560 | Other advisors (genex-asset) |
| 44620 | Brokerage fees |
| 44630 | Appraisers |
| 44720 | ICT costs |
| 44981 | Auditors (overhead) |
| 44983 | Fiscal advisors |
| 44985 | Legal advisors |
| 44989 | Other advisors (genex) |
| 46921 to 46926 | Recoverable service charge costs (security, inspections, elevators, maintenance, cleaning, waste) |
| 46931 | Other advisors (recoverable) |
| 46935 | Other recoverable costs |
| 46936 | Marketing expenses (recoverable) |

44180 Temporary staff was removed from the PO-required list on 1 March 2019.

## Open points

- The approval matrix in the old wiki named individuals (HQ F&A Director, Group FD, CFO). Names are replaced by roles here; confirm current limits.

## Change log

| Date | Change | Source |
|------|--------|--------|
| 2026-10-09 | Invoice recording check by the head of accounting added from the workflow-change instruction of 18 February 2020 (fetched from the wiki site). | `sources/wiki/attachments/workflow-change-invoice-recording-2020.md` |
| 2026-10-08 | Page created from "Manual Journal Entries", "Master Data change and Pay proposals", "Approval Setup", "PO Required SCoA list". | `sources/wiki/pages/` |
