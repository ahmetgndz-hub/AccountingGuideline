---
title: Control file
---

# Control file

<div class="page-meta" markdown>
**Applies to:** all entities · **Owner:** Group Finance · **Last reviewed:** 2026-10-08
</div>

## Rule

The control file is an automated check of the bookkeeping per country against the accounting policies and system rules. Countries review it before every close and clear every exception or explain it to HQ accounting. It also serves as training material: it shows past mistakes and how to correct them.

## Controls

| Control | What it checks | Expected outcome |
|---|---|---|
| **C01 Legal entity list** | All entities (EL1) per Coda company / country with their settings. Settings drive reporting. | Details reconcile; otherwise contact HQ accounting. |
| **C02 Asset list** | All assets (Multi, BX, third party). | No sold assets; no missing assets. |
| **C11 Dummy and suspense accounts** | Unmatched transactions on suspense accounts; use of dummy element 6. | Suspense accounts empty and matched daily; the only accepted exception is a transfer booked on day 0 that arrives on day 1. Dummy element 6 (`0`, `xxxDUMMY9`, `Cxx99999`, `Dxx99999`, "technical", "temporary") not used, except `0` for depreciation and result transfer. Allowed exceptions without element 6: valuation (11111 with movement 054 and 4331X), ERV (41101, 41111), result transfer (21180, 21210, 99998), vacancy (41130), equity accounts 21130 / 21140 / 21170, depreciation (11xx3 with 015 / 045 / 130, 42910, 42911, 44910, 53910), unrealised FX (52825, 54825), deferred tax (11605, 25511, 53300), current tax (27570, 53100, 53900). |
| **C12 Valuation** | Horizon valuation (SOL) vs Coda booking (IST) per asset and book. | No difference against the agreed valuation at the reporting date. |
| **C13 Document code level** | Documents not in balance per EL1 + EL3; documents still in the intray; documents denied in workflow and not handled. | Zero in all three. |
| **C14 Account code level** | Dummy property code on NRI accounts (PA to PG excluding PD5A and PGH); employee code on employment cost accounts (PQ, PR7, PR8, PR9); accounts without element 6. | Zero exceptions. |
| **C15 AP matching** | EL1 + EL6 combinations with an unmatched invoice **and** an unmatched payment above €100. | None: risk of double payment. |
| **C16 AR matching** | EL1 + EL6 combinations on receivables with at least one unmatched credit. | Credits matched against open invoices. |
| **C17 Bank booking target date** | Bank statement booked on the next working day (statement date + 1 WD). Buckets: on time, within 4 days, after 4 days. | Average close to 1 day. |
| **C20 ERV booking** | Full-year ERV in Horizon (A) vs budget (B); YTD ERV booked (D), ERV reversal (E), TO rent only (F); control points C = A−B, I = G+D, J = H+D, K = D+E+F. | K differs only by agreed rent minus ERV. See [ERV and vacancy](erv-vacancy.md). |
| **C21 Bank booking without Crescendo** | Bookings on cash accounts (except 13332, 13312) made outside Crescendo. | Move those bank accounts to Crescendo. |
| **C23 Capex reporting** | All lines on 11111 and 11340 with their capex id (PO, line or reporting hub) against the reporting hub. | Every line has a valid capex id. See [Capex](capex.md). |
| **C24 Loan overview** | Loan and interest accounts carry a loan code (element 7). | No line without loan code. |
| **C25 Bank booking after deadline** | Cash transactions booked after the bank booking deadline (3 WD after period end, set by the cash manager). | None, unless agreed with the cash manager. |
| **C26 Booking after closing deadline** | Bookings in MAN and FSM after the closing deadline. | None, unless communicated to HQ accounting. |
| **C27 Valuation bookkeeping** | Movement on 11111 with movement code 054 equals the valuation accounts 4331X in P&L, per EL1 + EL2 + EL3. | Control column = 1 on every total line. |
| **C28 Document codes vs element 4** | Document code used on allowed accounts only; no 2019-and-earlier codes used in 2020 or later. | No warnings. See [Document codes](document-codes.md). |
| **C29 Matching quality** | Matching on 13111 and 27310: one invoice to many bank lines, or one bank line to many invoices of the same counterparty. Warns on multiple EL1, EL3 or EL6 in one match, matching date outside the period, or payment and matching in different periods. | No warnings. See [Matching](matching.md). |
| **C30 Employee costs** | Employee-cost accounts booked with an employee code (EL6) and the expected property code (EL2); dummy employee codes E9998 / E9999 only where a cost cannot be attributed. | See [Salary bookkeeping](salary-bookkeeping.md). |
| **C31 Result booking** | Result transferred from P&L to equity per EL1 and EL3 up to the refreshed period. | Done in every book. |

The file itself (`Control file v4.2 2021Q1` on the old wiki) is distributed by HQ accounting; end-user access to the closing control file was announced on 23 June 2020.

## Change log

| Date | Change | Source |
|------|--------|--------|
| 2026-10-08 | Page created from the "Control file" page and the C01 to C31 pages. The two C11 pages were merged. | `sources/wiki/pages/control-file.md`, `c*.md` |

## Open points

- Control file version on the old wiki is v4.2 (2021 Q1). Confirm the current version and whether any controls were added since.
