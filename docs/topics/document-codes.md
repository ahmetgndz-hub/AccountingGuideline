---
title: Document codes
---

# Document codes

<div class="page-meta" markdown>
**Applies to:** all entities · **Owner:** Group Finance / FAM · **Last reviewed:** 2026-10-08
</div>

## Rule

Since 2020 Coda has one document code per purpose. Use the code that matches the nature of the booking; control C28 flags every document code used on an account it is not meant for, and every pre-2020 code (`GE-JV-MAN-*`) used in 2020 or later.

## Journal vouchers

| Code | Purpose | Workflow | Allowed accounts (EL4) |
|---|---|---|---|
| `JV-ERV` | ERV booking for operational assets | Exempt | 41101 ERV, 41111 ERV reversal, 41416 TO rent only |
| `JV-RESULT` | Monthly / quarterly result transfer from P&L to equity, or partition booking at shareholder level | Exempt | 21180, 99998, 11540, 55995, 11550, 55991, 21220, 55980 |
| `JV-VALUATION` | Valuation of investment property (BX, Multi, US tax, third party) | Exempt | 11111, 43312, 43313, 43314, 43315 |
| `JV-ICINTREST` | Intercompany interest calculation and booking | Exempt | 13532, 13561, 25110, 25555, 27125, 27330, 27402, 52310, 52330, 53310, 54330 |
| `JV-ELM` | Elimination booking for consolidation | Exempt | EL3 = ELM only |
| `JV-CFCORR` | Below NRI / cash flow presentation corrections. Counts as a cash transaction in QAR reporting (formerly `GE-JV-MAN-CF`) | Manual journal workflow | any |
| `JV-BADDEBT` | Bad debt provision bookings | Exempt | 13113, 42593. Must be a reversal document |
| `JV-TAXES` | VAT return, WHT return, deferred tax, tax accruals and reclasses | Exempt, write-off allowed up to €5 | 11575, 27521, 27523, 11650, 25511, 27570, 53100, 53300 |
| `JV-DEPR` | Depreciation of tangible and intangible assets | Manual journal workflow | 11313, 11323, 11423, 42910, 42911, 42912, 44910, 53910 |
| `JV-SALARY` | Payroll bookings | | see [Salary bookkeeping](salary-bookkeeping.md) |
| `JV-REVERSAL` | Accruals with automatic reversal (auto-matched) | | see [Accruals](accruals.md) |
| `NF-GUARANTEE` | Tenant or supplier guarantees, off balance sheet (formerly `GE-JV-MAN-GU`) | Manual journal workflow | 99100 |
| `JV-MANUAL` | Everything else: write-offs, corrections and reclasses, interest accruals in other books, accrual of income in books other than MAN, year-end capex accrual, short/long term classification | Manual journal workflow | all, manual control |

Other document families: incoming invoices (`*PI*`), outgoing / asset invoices (`SI%`), bank documents via Crescendo (`BA`), system documents (`Z-DISPERSE` from matching). The old wiki pages that listed those families were deleted; the current list is maintained by FAM.

## Change log

| Date | Change | Source |
|------|--------|--------|
| 2026-10-08 | Page created from "Journal Vouchers", "Document codes in use", "C28". JV-SALARY and JV-REVERSAL added from the salary and accrual pages. | `sources/wiki/pages/journal-vouchers.md` |
