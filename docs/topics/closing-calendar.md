---
title: Closing calendar and deadlines
---

# Closing calendar and deadlines

<div class="page-meta" markdown>
**Applies to:** all entities · **Owner:** Group Finance · **Last reviewed:** 2026-10-08
</div>

## Rule

Multi closes the books **every month**. Group Finance sends the closing instruction e-mail with the key closing milestones before each close; those dates are binding. The milestones follow a fixed order, counted in working days (WD) after period end. The base offsets below are the standing default; the monthly e-mail may move individual dates.

| Order | Milestone | Default | Document / map code | Page |
|---|---|---|---|---|
| 1 | Issue asset invoices | WD −5 (before period end) | `SI%` | [Revenue structure](revenue-structure.md) |
| 2 | ERV and vacancy booking | WD +1 | `JV-ERV` | [ERV and vacancy](erv-vacancy.md) |
| 3 | Bank and cash booking deadline | WD +2 (cash manager: 3 WD) | BB5 | [Bank and cash](bank-cash.md) |
| 4 | Suspense accounts cleansed | WD +4 | 4SUSPENCE group | [Suspense and dummy accounts](suspense-dummy-accounts.md) |
| 5 | A/R review, matching and bad debt booking | WD +4 | `JV-BADDEBT` | [Bad debt](bad-debt.md), [Matching](matching.md) |
| 6 | Salary, employment costs and depreciation | WD +5 | `JV-SALARY`, `JV-DEPR` | [Salary bookkeeping](salary-bookkeeping.md) |
| 7 | Intercompany transactions, invoice bookkeeping, fee income | WD +6 | `*PI*` | [Intercompany](intercompany.md), [Fee income](fee-income-recharges.md) |
| 8 | Investment property valuation | WD +7 | `JV-VALUATION` | [Investment property](investment-property.md) |
| 9 | All accruals | WD +8 | `JV-REVERSAL` | [Accruals](accruals.md) |
| 10 | FX valuation | WD +11 | | [Currency revaluation](currency-revaluation.md) |
| 11 | Closing: control file and trial balance review, result transfer | WD +12 | `JV-RESULT` | [Closing checklist](closing-checklist.md), [Accounting Control File](control-file.md) |

Deviations: when a deadline cannot be met, tell the cash manager (bank) or HQ accounting (all other items) **before** the deadline and list the bookings that will come after it. Controls C25 and C26 report every booking made after the bank or closing deadline.

## Change log

| Date | Change | Source |
|------|--------|--------|
| 2026-10-08 | Page created. Replaces the old wiki "Closing general information" (quarterly close on the 5th working day, intercompany interest rates 2019 and 2020), which is superseded by the monthly closing instruction e-mails. | `sources/wiki/pages/closing-general-information.md`, closing instruction e-mails |

## Open points

- The old wiki stated a quarterly closing deadline of the 5th working day after quarter end. The current practice is a monthly close with milestones as above; Group Finance to confirm the default offsets.
- Intercompany interest rate (4,60% in 2019 and 2020 on the old wiki): current rate to be confirmed by HQ cash management and added to [Intercompany](intercompany.md).
