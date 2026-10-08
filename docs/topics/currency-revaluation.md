---
title: Currency revaluation
---

# Currency revaluation

<div class="page-meta" markdown>
**Applies to:** all entities · **Owner:** Group Finance · **Last reviewed:** 2026-10-08
</div>

## Rule

Every transaction carries a home value (local currency) and a dual value (EUR). At period end, monetary items are revalued so that consolidation in EUR is correct. Match before revaluing: an unmatched foreign-currency invoice is revalued while its payment is not, which creates a false FX result.

| Country group | Monetary items (4CURREV group) | Tax monetary items (4CURREV-TAX group) |
|---|---|---|
| Non-EUR, functional currency EUR (PL, TR, HU) | Document → home value **and** document → dual (EUR) | Home → dual (taxes payable in local currency) |
| Non-EUR, functional currency local (GB, UA, CZ, CH) | Document → home value | Home → dual |
| EUR countries (NL, BE, IE, SK, LV, IT, DE, PT, ES, CY, HQ) | Document → home value | |

Unrealised FX results go to 52825 (asset companies) or 54825 (service companies) without element 6; realised results arise from matching (`Z-DISPERSE`).

## Monetary items (4CURREV account group)

11210, 11213, 11535, 11552, 11555, 11556, 11557, 11560, 11565, 13111, 13130, 13140, 13311, 13312, 13313, 13317, 13332, 13340, 13345, 13500, 13510, 13523, 13531, 13532, 13541, 13553, 13554, 13560, 13561, 13562, 13563, 13567, 13568, 23590, 25110, 25120, 25210, 25330, 25331, 25530, 25550, 25551, 25553, 25555, 25556, 25557, 27120, 27122, 27125, 27210, 27310, 27320, 27325, 27330, 27401, 27402, 27515, 27520, 27525, 27526, 27527, 27528, 27529, 27530, 27560, 27562, 27564, 27565, 27580 to 27586, 27588, 27590.

## Deadlines

[Milestone 10](closing-calendar.md): FX valuation on closing day. Cash items may be revalued earlier as instructed in the closing e-mail.

## Change log

| Date | Change | Source |
|------|--------|--------|
| 2026-10-08 | Page created from "Currency revaluation" and "Monetary Items". | `sources/wiki/pages/currency-revaluation.md`, `monetary-items.md` |
