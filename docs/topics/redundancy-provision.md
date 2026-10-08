---
title: Redundancy provision
---

# Redundancy provision (employee severance provision)

<div class="page-meta" markdown>
**Applies to:** all Multi Group entities (closed entities excluded) · **Owner:** Group Finance (HQ); reviewed by the CFO · **Policy:** Group Accounting Policy v1.2, effective 2026/12 close, methodology applied from the 2026/6 run · **Last reviewed:** 2026-10-08
</div>

## Rule

1. **Scope.** A provision is recognised in the **MAN** book for the statutory severance that current employees on permanent or fixed-term contracts would be entitled to under local law. It does not cover notice-period pay, holiday allowance or vacation money. It is a management reporting policy.
2. **Central calculation and booking.** Group Finance calculates and books the provision **per employee** (el6 = `E<employee number>`) at every **quarter end**. Local entities never post provision entries; they only process actual severance payments through payroll (point 6).
3. **Salary basis (since 1 January 2026).** Monthly salary = total contracted annual compensation in **Sympa** ÷ 12, refreshed via API each period. Local HR keeps Sympa current.
4. **Target provision** = country severance multiplier × (capped) monthly salary, in the home currency of the entity. Country multipliers and exclusions: see below.
5. **Only the difference is posted.** At each quarter end the target is compared with the **booked balance** of GL 27527 (MAN, per employee, intray documents included); payroll payments, earlier corrections and FX effects are therefore picked up automatically and nothing is released twice.
6. **Severance payments** go through payroll in the month of payment: gross amount **Dr 27527** with the employee element (not staff costs); credits follow the normal payroll lines (27515 net pay, 27523 wage tax and social security). See [Salary bookkeeping](salary-bookkeeping.md).
7. **Release restriction (above / below the line).** The **prior-year layer** (the employee's calculated provision at the previous year end, frozen in the final snapshot) may never be released above the line: it goes to **GL 43011 Redundancy provision (non-asset)**, reporting group PU, below RMA result. Only the **in-year layer** (booked provision above the prior-year layer) is released through **GL 44125 Redundancy** (PQ8, above the line). Releases take the in-year layer first, then the prior-year layer, never more than the prior-year layer. The layers come from the calculation, not from the Coda year-end balance.
8. **Books (layer map).** The MAN booking is reversed in LOC and/or FSM per the layer map; a principle not reversed is booked to zero, a principle marked "not touched" gets no lines. See the layer map below and [Books](booking-structure.md).

## Country multipliers (months of contracted monthly salary)

| Country | Entitlement | Formula |
|---|---|---|
| NL, HQ, AA | 1/3 month per year of service | years ÷ 3 |
| DE | 1/2 month per full year of service | years ÷ 2 |
| TR | 1 month per year; monthly salary capped at the SGK ceiling in force at quarter end (TRY 64.948,77 from 1 Jan 2026; TRY 73.729,87 from 1 Jul 2026; updated every January and July, loaded before the first quarter-end run of the half-year) | years |
| CH | None | 0 |
| IT | Tiered by completed years (from 30 Apr 2026): 1 yr 2,0; 2 yrs 3,5; 3 yrs 5,0; 4 yrs 6,5; 5 yrs 8,0; 6 yrs 9,5; 7 yrs 11,0; 8 yrs 12,0; 9 yrs 13,0; 10+ yrs 14,0. Three employees with individual terms: 4 / 8 / 12 / 18 / 24 months (< 2 / < 6 / < 10 / < 15 / 15+ yrs), two of them plus 5 months | tiered |
| DK | < 12 yrs pro rata; 12+ yrs 1 month; 15+ yrs 3 months (under review, see open items) | tiered 0 / 1 / 3 |
| GB | Age-weighted weekly salary × years, max 20 years, 1,5× weighting applied to all (no birth dates); office staff only | tiered weekly |
| UA | 3 months | 3 |
| FR | ≤ 10 yrs 1/4 month per year; > 10 yrs 1/3 month per year | tiered |
| ES | 20 days per year, capped at 12 months | min(years × 20 ÷ 30, 12) |
| SK | < 2 yrs 0; 2–5 1; 5–10 2; 10–20 3; 20+ 4 | tiered 0–4 |
| HU | < 3 yrs 0; 3–5 1; 5–10 2; 10–15 3; 15–20 4; 20–25 5; 25+ 6 | tiered 0–6 |
| PL | < 2 yrs 1; 2–8 2; > 8 3 | tiered 1–3 |
| PT | Pre-Nov 2012: 30 days/yr; Nov 2012–Apr 2023: 18 days/yr for the first 3 years then 12; from May 2023: 14 days/yr; total capped at 12 months | per period, cap 12 |

### Exclusions and adjustments (provisioned at zero or adjusted; each one visible as a comment in the calculation and confirmed with local HR)

- Interns; management contracts without severance (for example Poland); Germany Minijob (FTE ≤ 0,22); Ukraine definitive contracts without severance clause; group directors.
- Temporary / fixed-term contracts only where local law grants severance at contract end.
- United Kingdom: from 2026/6 only office staff (Wilmslow, Somerset); asset-location employees at zero (earlier provision of 82 employees reversed in 2026/6, document RP202606-GBC).
- Closed entities are outside calculation, journal and comparisons; their 27527 balances stay unchanged (TR BS901, BS003, BS006, BS007, BS102, BS103, BS105, BS107, BS112, BS117, BS120, BS125, BS129; IT ITS003).
- Leavers at quarter end: zero (payment via payroll). Leavers during the quarter: zero, booked balance released per point 7.
- Retirees continuing to work: service counted from the start of the retiree contract.

## How to (Coda)

**Journal entries (HQ, el3 MAN, el6 = employee)**

| Case | Dr | Cr |
|---|---|---|
| Recognition / increase | 44125 Redundancy (PQ8) | 27527 Accrual redundancy (BE5) |
| Decrease / release | 27527 | 44125 for the in-year layer, 43011 Redundancy provision non-asset (PU) for the prior-year layer |
| Severance payment (country, payroll run) | 27527 | 27515 salary suspense, 27523 wage tax and social security |

Examples (calculated year-end provision 100): booked 110, target 0 → Dr 27527 110 / Cr 44125 10 / Cr 43011 100. Booked 110, target 60 → Dr 27527 50 / Cr 44125 10 / Cr 43011 40. Booked 80, target 0 → Dr 27527 80 / Cr 43011 80. Payment above the provision leaves a debit on 27527 that the quarter-end booking charges to 44125.

**Layer map (el3)**

| Entities | LOC | FSM | Valid from |
|---|---|---|---|
| HQ, NL, AA, FR, SK | Reversed | Reversed | 2026/7 |
| TR | Reversed, in the same document as MAN | Not touched (local Finance) | 2026/6 |
| BE, CH, CY, CZ, DE, DK, ES, FI, GB, HU, IE, IT, LU, LV, PL, PT, UA | Zero (provision visible in the local view) | Reversed | 2026/7 |

Reporting views: management = MAN; local GAAP = MAN + LOC; fiscal = MAN + FSM. Each quarter the LOC and FSM balance per employee is booked to its own target; historical differences are aligned with the same above / below split.

**Posting:** document code **`JV-REDUND`**, one document per legal entity and entity code with MAN, LOC and FSM lines together; period and date = quarter end; home currency with EUR dual value at the closing rate (EUR entities without dual value); rounding difference on the largest line so every principle balances to 0,00 in both currencies; ExtRef2 = `RP<yyyymm>-<el1>` (unique per company), ExtRef3 = main movement driver, comment = employee name and bridge; el5 per GL account from the Coda link list (default el5 of the entity code where allowed, otherwise the most-used allowed code; for example ES / PT 915, IT 961, PL 900, UA 920 on 44125). Documents are generated by `dbo.AGz_RedundancyProvision_CodaXml`, delivered to the Coda intray through Fluxygen (15 to 45 minutes) and posted by Group Finance; status is tracked in `AGz_RedundancyProvision_PostLog` (generated, sent, posted, failed, void). The posting period must be open for the integration user.

**Transition:** until 2026 Q2 the provision sat on the pooled element E6188. In 2026/6 it was reclassified once to the employees (RP-RECLASS, mirrored in LOC for TR and SK); residuals on the pool were released in 2026/9. The pool's booked year-end balance counts as prior-year layer until cleared.

## Controls

| Control | What |
|---|---|
| Headcount reconciliation | Population in the model vs active headcount in Sympa every period; joiners, leavers and contract changes reflected before posting. |
| Run and sign-off | Preview (`AGz_RedundancyProvision_v4`, `@commit = 0`) → review of employee detail, movement bridge, booked 27527 bridge, LOC / FSM layer check, journal lines and balance checks (0,00 per principle in home and EUR), exceptions confirmed with local HR → freeze (`@commit = 1`, final snapshot, PostLog "generated"; a quarter is never generated twice) → delivery and follow-up until posted. |
| Currency | Calculated and posted in home currency, EUR dual value at closing rate; foreign-currency salaries converted at closing rate (FX driver); retranslation of the opening provision shown as translation difference; real-terms assessment for strongly depreciating currencies. |
| Movement bridge | Change in target per employee and entity vs previous quarter end and previous year end, by driver: new joiner, leaver, entity change, service, salary, ceiling, FX, override, other (plus translation difference in EUR). Booked side: previous balance + payroll payments + other postings + quarter-end booking = target. |
| Reconciliation after posting | 27527 (MAN) per employee equals the target except cent rounding; pool residual reported separately; 27527, 44125 and 43011 compared per entity between quarter ends and explained with the bridge. |

## Deadlines

Quarter-end runs (periods 3, 6, 9, 12), before the closing deadline of the quarter month in the [closing calendar](closing-calendar.md). Payroll severance payments follow the monthly salary milestone.

## Open items (policy §7)

| # | Item | Owner | Status |
|---|---|---|---|
| 1 | Turkey: load the SGK ceiling valid from 1 Jan 2027 before the 2026/12 run. | A. Gunduz / TR HR | Open |
| 2 | Leavers during the quarter whose payment follows next quarter: keep the provision until payment or release at quarter end? | Group Finance | Open |
| 3 | HU (7,9 million HUF) and UA (−0,65 million UAH) postings on the pool after 2026/6, released in 2026/9: nature to be confirmed. | HU / UA Finance | Open |
| 4 | DE employee E5878 salary drop in Sympa; AA employee E5998 without salary in Sympa, not provisioned. | DE HR / AA HR | Open |
| 5 | Denmark multiplier vs Salaried Employees Act (1 / 2 / 3 months after 12 / 15 / 18 years). | A. Gunduz / DK HR | Open |
| 6 | Payroll instruction per country: severance Dr 27527 with el6 = employee in MAN. | Local Finance / Payroll | Open |
| 7 | Fully automatic Fluxygen transfer instead of manual copy to the pick-up folder. | Group Finance / IT | Open |
| 8 | Duplicate employee numbers (ES E5098 / E6512): HR to avoid; booking on the unused number released as error. | HR / Group Finance | Open |
| 9–11 | Layer map agreed; JV-REDUND created and proven; pool transition posted. | | Closed |

## Change log

| Date | Change | Source |
|---|---|---|
| 2026-10-08 | Page created from Group Accounting Policy "Redundancy Provision" v1.2 (Oct 2026 revision for the 2026/12 close). Supersedes the old wiki accrual table row "Redundancy: no booking in MAN / FSM / UST". | `sources/emails/2026-10_redundancy-provision-policy-v1-2.md` |
