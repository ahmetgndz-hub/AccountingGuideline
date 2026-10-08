---
title: Below NRI and cash flow mapping
---

# Below NRI and cash flow mapping

<div class="page-meta" markdown>
**Applies to:** asset companies · **Owner:** Group Finance · **Last reviewed:** 2026-10-08
</div>

## Rule

Since Q1 2019 the second page of the QAR cash flow is built directly from Coda. The report picks every mutation in the period that touches a **cash SCoA** (13311, 13312, 13313, 13317, 13332, 13340, 13345; BO group BB5) or is booked with document code **`JV-CFCORR`** (before 2020 `GE-JV-MAN-CF`). Use `JV-CFCORR` to rebook a cash movement to the right line; never use `JV-MANUAL` for cash reclassifications.

| Map | Line | EL4 | EL5 | EL8 |
|---|---|---|---|---|
| CA1 | C1 regular capex | 11111, 11112 | C01 | 070 |
| CA2 | C2 legal compliance | 11111, 11112 | C02 | 070 |
| CB1 | C3 redevelopment | 11111, 11112 (C03), 11340 | | 070 |
| CB2 | C4 tenant fit-out / incentives | 11111, 11112 | C04 | 070 |
| CB3 | C5 extensions | 11111, 11112 | C05 | 070 |
| CD1 | Sale proceeds | 55800; 11111, 11112 | | 050 |
| CE1 | Corporate income tax | 53100 | | |
| CE2 | VAT | 27521, 11575, 13565 | | |
| CH1 | Interest | 52130, 51130, 27401, 27402 (920) | | |
| CH2 | Amortisation | 25330, 27330 (830); 25120 (930) | | |
| CH3 | Repayment | 25330, 27330 (820); 25120 (920) | | |
| CH4 | Drawdown | 25330, 27330 (810); 25120 (910) | | |
| CH5 | Agency fees | 51780 | | |
| CH6 | One-off banking fees | 51782 | | |
| CI2 | Equity contributions | 21110 | | 525 |
| CJ1 | Equity distributions | 27380; 21180, 21110 | | 570 |
| CJ2 | Shareholder loan repayment | 27402; 11535 (810, 820); 25110, 25120, 27125 (820); 25110 (830) | | |
| CJ3 | Shareholder loan drawdown | 13532; 25110, 25120, 27125 (810); 11535 (830) | | |

Movement codes on loans and equity therefore matter: see [Loans and interest](loans-interest.md) and [Result transfer and dividends](equity-result-dividends.md).

## Change log

| Date | Change | Source |
|---|---|---|
| 2026-10-08 | Page created from "Below NRI items". | `sources/wiki/pages/below-nri-items.md` |
