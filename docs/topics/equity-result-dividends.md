---
title: Result transfer and dividends
---

# Result transfer and dividends

<div class="page-meta" markdown>
**Applies to:** all entities · **Owner:** Group Finance · **Last reviewed:** 2026-10-08
</div>

## Rule

- The result of the period is transferred from P&L to equity in **every book** (MAN, LOC, FSM, FSE, UST) at each close with `JV-RESULT` (21180 retained earnings / 99998 transfer account result). Control C31 checks this per EL1 and EL3. The booking of the current year net result was automated in Coda in November 2019.
- Equity reconciles with the trade registry and the shareholder ledger (checklist point 15); share capital carries the shareholder as element 6.
- Dividends: on the registration date book the gross dividend out of retained earnings, legal reserves, dividend tax and the net amount on **27380 Dividend payable** (BF4). At payment, 27380 against the bank. 27380 maps to cash flow line CJ1 equity distributions (cash documents only).

| Step | Dr | Cr |
|---|---|---|
| Registration date | 21180 retained earnings (EL8 575) 500 | 21170 legal reserves 50, 27570 taxes payable 25, 27380 dividend payable 425 |
| Payment date | 27380 425 | 13111 / bank 425 |

## Change log

| Date | Change | Source |
|------|--------|--------|
| 2026-10-08 | Page created from "Dividend payment" (newsletter 16 October 2019), C31 and the result transfer document code. | `sources/wiki/pages/dividend-payment.md` |
