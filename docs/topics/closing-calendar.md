---
title: Closing calendar and deadlines
---

# Closing calendar and deadlines

<div class="page-meta" markdown>
**Applies to:** all entities (Multi service companies, Multi- and third-party-owned asset companies) · **Owner:** Group Finance · **Last reviewed:** 2026-10-09
</div>

## Rule

1. Multi closes the books **every month**. Group Finance sends the *Closing and Reporting Instructions* e-mail with the key closing milestones before each close. Those dates are binding; they are counted in working days from month end (ME) and follow the standing timetable below.
2. **Operational closing** ends at ME + 10. The **closing deadline** (final review, sign-off and submission) is ME + 12. Quarter ends add two to three days; the December close runs about one week longer.
3. Since the September 2026 close the period is **closed automatically in Coda at 23:59 (Amsterdam time) on deadline day**. No postings are possible after that moment. The next morning an automated status notification goes to the country and to management ([Accounting Control File](control-file.md)).
4. **Late adjustments are not accepted once results have been communicated.** Any expected delay is reported to Group Finance **before** the deadline is missed, with the bookings that will come after it. Bookings after the deadline are reported by control 99 *Booking after Deadline* and need prior agreement with HQ accounting.
5. The group dates are the hard deadlines for the Multi service companies and Multi-owned assets. For third-party mandates with their own reporting calendar they are guidance, but the asset bookkeeping must still be complete in time to close the service companies.
6. Closing on time gates the RMA submission and, in budget season, the Budget presentation. Closing deadlines take priority over forecast and budget work.

## Standing timetable

Dates are working days relative to month end (ME). Codes are the Coda document codes, map codes (BO groups) and accounts named in the instruction e-mails.

| # | When | Milestone | Code / account | Page |
|---|---|---|---|---|
| 1 | ME − 3 to − 5 | Issue asset invoices (rent, service and marketing charge advances) | Doc code `SI%`; EL4 PB, PC2%, PD%, PE1 | [Revenue structure](revenue-structure.md) |
| 2 | ME + 1 | ERV and vacancy booking | 41101 / 41111 (ERV), 41130 / 41110 (vacancy) | [ERV and vacancy](erv-vacancy.md) |
| 3 | ME + 1 | Cleanse all suspense account balances: zero in home and reporting value, matched and reclassified where needed | EL4 group 4SUSPENCE | [Suspense and dummy accounts](suspense-dummy-accounts.md) |
| 4 | ME + 2 | **Bank and cash booking deadline** | Map code BB5 | [Bank and cash](bank-cash.md) |
| 5 | ME + 4 | FX valuation of cash items; last day of A/R review and matching; bad debt booking | BB5 with `GE-CR` / Disperse; 13111 / 13130; 13113, 42593, 43001 | [Matching](matching.md), [Bad debt](bad-debt.md) |
| 6 | ME + 5 | Salary and employee costs, depreciation, recharges (IC and third party) | Map code PQ*, 27515; 11313, 11323, 11423, 42911, 53910, 44910; 13553, 13554 | [Salary bookkeeping](salary-bookkeeping.md) |
| 7 | ME + 6 | **Last day of invoice bookkeeping**; last day of intercompany transactions; fee income at the management company | Doc code `*PI*`; EL6 = R*; map code PP* | [Intercompany](intercompany.md), [Fee income](fee-income-recharges.md) |
| 8 | ME + 7 | Property valuation bookkeeping (mainly capex and impairment) | BA2, PK1 | [Investment property](investment-property.md), [Capex](capex.md) |
| 9 | ME + 8 | All accruals: rent, MSC, genex, opex, FinEx, turnover rent, bonus | Doc code `JV` (`JV-REVERSAL`); genex PQ% / PR%, opex PG%; bonus 27526 / 44124 | [Accruals](accruals.md) |
| 10 | ME + 10 | Operational closing ends. Quarter ends: current and deferred taxes booked and tax file confirmed to Group Tax; result of the period transferred to equity in every book (MAN, LOC, FSM, FSE, UST); forecast uploaded to Coda | `JV-TAXES`; `JV-RESULT`; balance code BUD / FCST | [Taxes](taxes.md), [Result transfer](equity-result-dividends.md), [Budget and forecast instructions](budget-instructions.md) |
| 11 | ME + 12 | **Closing deadline**: review of the Control File, trial balance and FPR; last day of corrections; full FX valuation; sign-off and submission of a clean Control File by the Director of Finance; **period closes at 23:59** | Map code ALL; `99 Closing` | [Accounting Control File](control-file.md), [Currency revaluation](currency-revaluation.md) |
| 12 | ME + 13 | Status notification to Country Controller, Country FD and Group Financial Controlling | | [Accounting Control File](control-file.md) |

**Example, September 2026 close** (month end Wednesday 30 September): asset invoices 28 Sep, ERV / vacancy / suspense 1 Oct, bank and cash 2 Oct, FX cash / A/R / bad debt 6 Oct, salary / depreciation / recharges 7 Oct, invoices / IC / fee income 8 Oct, valuation 9 Oct, accruals 12 Oct, operational closing until 14 Oct, closing deadline 16 Oct 23:59.

## Deliverables

Since September 2026 **the only deliverable is the submitted online Control File in the [Multi Reporting Hub](https://multireportinghub.multi.eu)**. The Balance Sheet and the FPR (Financial Performance Review) are integrated into it. No separate e-mail or attachments; comments and explanations go into the Control File. The Director of Finance signs off on (i) completeness of the closing, (ii) accuracy of the numbers and (iii) quality of the Control File.

## Year-end and quarter-end specifics

- **Quarter end** (March, June, September, December): tax file finalised and confirmed to Group Tax (Erik van Eysden) by ME + 10; CIT accrual booked; result transferred to equity in each book; 12-month rolling forecast uploaded to Coda before the country–HQ review meetings; intercompany charges planned for other group companies listed in the dedicated tab of the RMA report; RMA and QAR reporting follow the separate instruction ([Budget and forecast instructions](budget-instructions.md)).
- **Year end** (December): deadline about one week longer than a normal month (2025: 21 January). Attention items from the year-end instruction: all fee income of the year charged to clients or accrued; no suspense accounts and no dummy positions; accurate cost accruals; recharges to other Multi service companies communicated to the counterpart in time; Group Finance reconciles actual genex and CAF per country against the advances sent, and countries do the same for time recharges between countries to prevent intercompany differences. Coda is closed for consolidation on the date announced by Group Finance (2025 books: 27 January 2026, 12:00 Amsterdam).
- **Summer**: deadlines may be extended by a few days (July 2026: sign-off 19 August).

## How the timetable evolved

| From | Change | Source |
|---|---|---|
| Oct 2024 | Monthly instruction e-mail with a key-milestone table (asset invoices, ERV, bank and cash BB5, A/R and bad debt, salary PQ*, depreciation, recharges, IC, invoices `*PI*`, fee income PP*, valuation, accruals, FD review and sign-off). Coda access closed centrally the day after the deadline. | `sources/emails/2024-11-04_closing-instructions-2024-10.md` |
| Nov 2024 | Milestones expressed in working days versus month end (ME ± n); asset invoices moved to ME − 5; bank and cash at ME + 2. | `2024-11-28_closing-instructions-2024-11.md` |
| Dec 2024 | Year-end: bonus accrual row (27526 / 44124); redundancy accruals coordinated by HQ; tax file confirmed to Group Tax. | `2024-12-24_closing-instructions-2024-12.md` |
| Mar 2025 | Quarter-end additions: forecast upload to Coda, settle intercompany positions in cash before quarter end, FD review spread over three days. | `2025-03-27_closing-instructions-2025-03.md` |
| Apr 2025 | FD e-mails three deliverables: Control File, Trial Balance / Management Hierarchy, FPR (renamed RMA file in January 2026). | `2025-04-29_closing-instructions-2025-04.md` |
| Jun 2025 | "Result of the period transferred to equity in each book" added at quarter end. | `2025-06-25_closing-instructions-2025-06-q2.md` |
| Aug–Dec 2025 | Control File standard: clean without exceptions, otherwise the closing is not finalised; Coda books closed the day after the deadline. | `2025-09-01_closing-instructions-2025-08.md` and following |
| Jun 2026 | Quarter-end: 12-month rolling forecast with a fixed Coda upload date, intercompany charge form as RMA tab, Macabacus-based RMA format, review meetings with re-upload within five business days. | `2026-06-23_closing-instructions-2026-06-q2.md` |
| Jul 2026 | Control File moves from Excel to the online Reporting Hub. | `2026-07-28_closing-instructions-2026-07.md` |
| Aug 2026 | ERV / vacancy booking and suspense cleanse made an explicit ME + 1 milestone; accruals with doc code `JV`. | `2026-08-28_closing-instructions-2026-08.md` |
| Sep 2026 | Automatic period closure at 23:59 on deadline day; Balance Sheet and FPR integrated into the Control File; the online Control File is the only deliverable; closing gates the RMA submission and the Budget presentation. | `2026-09-25_closing-instructions-2026-09-q3.md` |

## Change log

| Date | Change | Source |
|------|--------|--------|
| 2026-10-09 | Page rewritten from the 23 closing instruction e-mails October 2024 to September 2026: standing ME ± n timetable with codes, automatic close, single deliverable, quarter-end and year-end specifics, evolution table. Open point on the default offsets closed. | `sources/emails/*closing-instructions*`, `sources/inventory/batch-A.md`, `batch-B.md`, `batch-C.md` |
| 2026-10-08 | Page created. Replaces the old wiki "Closing general information" (quarterly close on the 5th working day, intercompany interest rates 2019 and 2020). | `sources/wiki/pages/closing-general-information.md` |

## Open points

- Intercompany interest rate (4,60% in 2019 and 2020 on the old wiki): current rate to be confirmed by HQ cash management and added to [Intercompany](intercompany.md).
- The March 2026 (Q1) instruction exists only as the draft sent to Egbert van Zomeren on 30 March 2026; the distributed version was not found in the mailbox.
