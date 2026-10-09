---
title: Salary bookkeeping and employee costs
---

# Salary bookkeeping and employee costs

<div class="page-meta" markdown>
**Applies to:** all entities with payroll · **Owner:** Group Finance · **Last reviewed:** 2026-10-09
</div>

## Rule

- Document code `JV-SALARY`, document date = payroll run date. The payroll provider (ADP or local) delivers a file that loads through CodaXL without manual intervention.
- **EL1** = payroll entity. **EL2** = the asset where the employee works; service company code if the employee works for all assets or for the service company. **EL6** = employee code (`E` + Workday id), created for internal, external and temporary staff via the FAM mailbox. Dummy employee codes E9998 / E9999 only where a cost cannot be attributed (control C30). **EL7** = department.
- Employee-related accounts that require an employee code: PQ1 salaries (44111, 44122, 44123, 44127, 44128, 44198), PQ2 bonus 44124, PQ3 independent workers 44120, PQ4 temporary staff 44180, PQ6 social security 44112 / 44113, PQ7 pensions 44115, PR7 travel (44130 to 44135), PR8 car costs (44170 to 44174), PR9 other staff costs (44140, 44150, 44160, 44190).

**Example payroll booking** (service company ITS002, employee at asset ITIP004)

| BO | SCoA | EL6 | Amount |
|---|---|---|---|
| PQ1 | 44111 Wages and salaries | E5338 | 300 Dr |
| PQ6 | 44113 Social security | E5338 | 30 Dr |
| PR7 | 44130 Travel expenses | E5338 | 25 Dr |
| PQ7 | 44115 Pensions | E5338 | 10 Dr |
| BF5 | 27523 Wage tax and social security (separate EL5 for tax and insurance) | E5338 | 110 Cr, 45 Cr |
| BB2 | 13567 Prepayment staff | E5338 | 15 Cr |
| BF3 | 27515 Salary suspense | E5338 | 195 Cr |

**Severance payments**: in the payroll run of the month of payment, book the gross severance **Dr 27527 Accrual redundancy** with the employee element (el6), never to staff costs; the net pay and taxes follow the normal payroll lines. Group Finance releases the remaining provision at the next quarter end. See [Redundancy provision](redundancy-provision.md).

**Bonus accrual** (PQ2, accounts 27526 bonus accrual / 44124 bonus):

- During the year, accrue the bonus **straight-line, 1/12 per month**, based on the approved bonus amount (for 2026: the FY2025 bonus approved for payment). Apply the same method in every country (instruction 4 February 2026).
- At year end the accrual reflects the expected bonus; when the actual bonus is approved and paid in the following year, **true up the accrual in period 12 of the bonus year** (ask FAM to re-open the period) by Dr 44124 / Cr 27526 (or the reverse) so that the bonus cost of the year equals what is paid; then clear 27526 against the bank in the month of payment. **Never** book the difference as an accrual release (43010 / 43011) in the new year (revision 8 April 2025, which replaced the March 2025 example).
- Bonus accruals are reviewed YTD against actual or budget at every close (checklist point 29) and cleaned up at year end (no other bonus accrual positions).

**Month-end controls**: 27515 is zero and matched against the bank payments; 27523 equals the tax to be paid; 13567 is zero per employee; EL2 is consistent per employee.

## Recharges of salary cost

| Case | From → to | Charging entity | Receiving entity | Control |
|---|---|---|---|---|
| **a. Fee income** (management agreement) | Service company → asset company | Cr 44129 Recharged salary costs and Cr 44611 Recharged employee cost (PP5), Cr 27521 VAT, Dr 13111 (or 13130 for group) | Dr 46933 Staff costs (PF12), Dr VAT, Cr 27310 / 27120 | Employee cost for that asset is zero at the service company |
| **b. Transfer within the entity** (asset company runs its own payroll and recharges to service charges) | Asset company → same entity | Cr 44198 Recharge salary (PQ1), Cr 44610 Recharge genex (PR11); optional transfer via 13500 | Dr 46933 Staff costs | Employee cost at asset level (PQ, PR) fully in the service charge line |
| **c. Between service companies** (payroll entity has no agreement with the asset) | Service company A → service company B | Cr 44198, Cr 44610, Cr VAT, Dr 13130 | Dr 44198 CAF IGS recharge salary, Dr 44610 CAF IGS recharge genex, Dr VAT, Cr 27120 | Does not distort the cost of the payrolling company |

If the asset company keeps the cost as landlord cost instead of recharging it to tenants, use the fee cost accounts. External personnel invoices are booked per the instruction of 3 February 2020 (PQ3 / PQ4 accounts with an employee code).

## Deadlines

[Milestone 6](closing-calendar.md) (ME + 5): salary and employee costs, depreciation and recharges; bonus accrual with the other accruals at milestone 9 (ME + 8).

## Change log

| Date | Change | Source |
|------|--------|--------|
| 2026-10-09 | Bonus accrual rules added: 1/12 straight-line (4 Feb 2026) and prior-year true-up in period 12 via FAM, never via accrual release (8 Apr 2025). | `sources/emails/2026-02-04_bonus-accrual-approach-2026.md`, `2025-04-08_closing-instructions-2025-03-revision-bonus.md` |
| 2026-10-08 | Severance payment treatment added per the Redundancy Provision policy v1.2 (§5.3). | `sources/emails/2026-10_redundancy-provision-policy-v1-2.md` |
| 2026-10-08 | Page created from "Salary Bookkeeping and recharges" (31 October 2019), C30 and C14. | `sources/wiki/pages/salary-bookkeeping-and-rechagres.md` |
