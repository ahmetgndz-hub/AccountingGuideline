---
title: Taxes
---

# Taxes

<div class="page-meta" markdown>
**Applies to:** all entities · **Owner:** Group Finance / Group Tax · **Last reviewed:** 2026-10-08
</div>

## Rule

1. **Element 6** on tax accounts follows the standard tax code structure (`T` + country + S/P/A/L + rate), see [Coda element structure](coda-elements.md). No dummy element 6 on tax accounts.
2. At each month or quarter end (declaration period) book the **settlement**: reclass purchase and sales VAT to the VAT asset (`A`) or liability (`L`) code, transfer the balance to payable or deferred, reconcile with the declaration, and **match** all lines against the settlement booking.
3. **Current income tax** is calculated and booked for all SPVs (Dr 53100 / Cr 27570). **Deferred tax** only in FSM for Multi-owned assets (11605 / 25511 / 53300); never in MAN or UST.
4. Document code `JV-TAXES` (exempt from workflow, write-off allowed up to €5).
5. At quarter end the current (and, where applicable, deferred) tax accrual is booked by ME + 10 and the **finalisation of the tax file is confirmed to Group Tax (Erik van Eysden)** for review ([milestone 10](closing-calendar.md)); CIT accruals are booked every quarter, not only at year end.
6. The local FD confirms quarterly that the TCIS procedures are up to date: trackers (compliance and audit), Tvar (tax value at risk), TaxMan tax calculation, VAT outstanding balances, QAR key tax data.

Cash flow: 53100 maps to CE1 corporate income tax; 27521, 11575 and 13565 map to CE2 VAT.

## Change log

| Date | Change | Source |
|------|--------|--------|
| 2026-10-08 | Page created from "Tax codes", the closing checklist points 35 to 37 and the document code list. | `sources/wiki/pages/tax-codes.md`, `closing-check-list.md` |
