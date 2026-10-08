---
title: Fee income (service companies)
---

# Fee income (service companies)

<div class="page-meta" markdown>
**Applies to:** service companies · **Owner:** Group Finance · **Last reviewed:** 2026-10-08
</div>

## Rule

Management fee income is split in four categories and booked on separate accounts for group and third-party assets, always on the real asset code (EL2) that is charged, so that the fee analysis works.

| BO | Group assets | Third-party assets | Category |
|---|---|---|---|
| PP1 | 45810 | 45811 | Asset management fee |
| PP2 | 45820 | 45821 | Property management fee |
| PP3 | 45830 | 45831 | Statutory services fee |
| PP4 | 45880 | 45881 | (Re)development fee |
| PP5 | 44129, 44611 | | Recharged salary and employee cost (see [Salary bookkeeping](salary-bookkeeping.md)) |

The agreements behind each fee (PLSA, PMSA, IGSA, CAA, ACAA) and the counter-bookings at the asset company are on the [Intercompany](intercompany.md) page. Management fees are booked on the 35% / 65% logic (asset management and statutory vs property management) with proper EL2 (checklist point 32).

## Fee analysis (RMA)

A power query (`DM_FINANCE.dbo.AGz_RMAAnalysis`) produces the fee analysis per service company (EL1 like `__S%`, plus BS901 and BS009 for Turkey; Italy split into Malls and MOMI), MAN book only, one financial year.

| Column | Definition |
|---|---|
| Asset management fee | PP1 + PP3 |
| Property management fee | PP2 |
| Development fee | PP4 |
| Recharged staff cost | PP5, booked with 44129 and the charged asset on EL2 |
| Fee % of NRI | (total fee − development fee) / NRI of the asset |
| Direct employee cost | PQ and PR7 to PR9 with an employee code, booked on the asset's EL2 |
| Indirect employee cost | Same accounts without employee code, spread by fee share |
| Remaining G&A | PQ (excluding PQ5) + PR (excluding PR12) + PS1 depreciation, minus employee costs, spread by fee share |
| Recurring margin / gross margin | Fee income − total recurring cost; margin / fee income |
| Average FTE | Employees with more than €100 on 44111 at the asset's EL2 |

## Change log

| Date | Change | Source |
|---|---|---|
| 2026-10-08 | Page created from "Fee Income", "Fee analysis" and the non-recurring expenses e-mail (new 3rd-party accounts per 1 September). | `sources/wiki/pages/fee-income.md`, `fee-analysis.md` |
