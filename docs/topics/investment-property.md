---
title: Investment property valuation
---

# Investment property valuation

<div class="page-meta" markdown>
**Applies to:** asset companies · **Owner:** Group Finance · **Last reviewed:** 2026-10-08
</div>

## Rule

1. Investment property is measured at **fair value** at every reporting date.
2. **All capex is first booked on 11111 Investment property** with the capex category on element 5 (C01 to C05); other codes on the IP account are blocked. Capex that does not increase capacity (C1, C2, C4) is then expensed through "loss on fair value of investment property"; C3 redevelopment and C5 extensions are capitalised and taken into account in the valuation. See [Capex](capex.md).
3. Between valuations, with yields and unobservable inputs unchanged, fair value stays at the last valuation (unless C3 / C5 adds value).
4. Values communicated by HQ are rounded **down** to €10.000: `ROUNDDOWN(value, -4)`.
5. After booking: 11111 IP + 11340 WIP = valuation.

| Valuation | Frequency | Book |
|---|---|---|
| BX valuation | Quarterly | MAN |
| Multi internal valuation | Yearly (Q4) | MAN + FSM (FSM only for Multi-owned assets or on request) |
| External appraiser | When needed | MAN + FSE |
| Local value (purchase price, straight-lining) | | LOC |
| BX purchase price | | UST (see [US tax reporting](us-tax-reporting.md)) |

## How to (Coda)

Document code `JV-VALUATION`, element 5 = C99, movement code 054 on 11111; P&L accounts 43312 market value changes, 43313 impairment capex, 43314 impairment lease incentives, 43315 fair value adjustment IP (BO group PK1). Controls C12 (Horizon vs Coda) and C27 (11111/054 vs 4331X) must reconcile.

## Deadlines

[Milestone 8](closing-calendar.md): valuation bookkeeping.

## Change log

| Date | Change | Source |
|------|--------|--------|
| 2026-10-08 | Page created from "Investment properties", C12 and C27. | `sources/wiki/pages/investment-properties.md` |
