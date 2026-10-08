---
title: Books and booking structure
---

# Books and booking structure

<div class="page-meta" markdown>
**Applies to:** all entities · **Owner:** Group Finance · **Last reviewed:** 2026-10-08
</div>

## Rule

Multi runs one set of financials in Unit4 Financials (Coda) with several **books** (element 3). The **MAN** book is the basis for everything; every other book only holds the adjustments needed for its own reporting purpose.

| Book (EL3) | Purpose | Investment property value | Lease incentives and loan fees |
|---|---|---|---|
| **MAN** | Shareholder reporting and management decision making. Basis for all reporting of all Multi and BX owned companies (Multi Group Accounting Policies). Used for management and shareholder reporting, cash flow forecasting, distribution process. Follows cash as much as possible. | BX investment value | Rent-free and stepped-rent incentives directly in P&L. Tenant fit-out and direct cash contributions capitalised, then through P&L via market value changes. Loan arrangement fees directly in P&L. |
| **FSM** | Multi IFRS consolidated financial statements. | Multi internal valuation | Straight-lined over the remaining term of the lease / loan. |
| **FSE** | IFRS financial statements submitted to the banks. | Valuation used for bank reporting (external appraiser, basis for LTV). | Straight-lined over the remaining term. |
| **LOC** | Statutory financial statements under local GAAP. | Local value (for example purchase price). | Per local GAAP. |
| **TAX** | Numbers used in the income tax filing. | | |
| **UST** | Specific adjustments to the US tax packs (see [US tax reporting](us-tax-reporting.md)). | BX purchase price | |
| **LUX** | Bridge to Luxembourg GAAP, where applicable. | | |
| **ELM** | Elimination bookings for consolidation only (document code `JV-ELM`). | | |

Rules that follow from this:

1. Book every transaction in **MAN**. Book in another book only the difference that book needs.
2. Never book a correction in FSM/FSE/LOC that belongs in MAN.
3. The result of the period is transferred to equity in **each** book (MAN, LOC, FSM, FSE, UST) at every close (see [Result transfer and dividends](equity-result-dividends.md)).

## How to (Coda)

- Element 3 selects the book. Document code restrictions per book are listed in [Document codes](document-codes.md).
- A separate overview of the FSM and FSE accounting adjustments is maintained by Group Finance; ask Group Finance for the current version.

## Change log

| Date | Change | Source |
|------|--------|--------|
| 2026-10-08 | Page created from the old wiki page "Booking Structure". ELM book added from the document code list. | `sources/wiki/pages/booking-structure.md`, `journal-vouchers.md` |
