---
date: 2026-07-14
subject: "redundancy provision booking 2026Q2"
attachment: "Redundancy_Provision_Policy_v1_1.docx"
source_email: 2026-07-14_redundancy-provision-booking-2026q2.md
status: reference
superseded_by: 2026-10_redundancy-provision-policy-v1-2.md
topics: [redundancy-provision, salary-bookkeeping, accruals, document-codes]
fetched: 2026-10-09 via Microsoft 365 connector (read-only), text extracted from DOCX by the connector; table layout flattened
---

> Note: this is the policy as sent to the countries (Harold van Riel / Olcay Demirci) with the 2026 Q2 booking request. Version 1.1 inside. Sections 1–4 (scope, definitions, Sympa salary basis, country multipliers, overrides) are identical to the 2026-04-28 version and are summarised; §5 is the version countries were asked to follow and is given in full. Superseded by policy v1.2 (2026-10, see 2026-10_redundancy-provision-policy-v1-2.md).

MULTI
Group Accounting Policy
Redundancy Provision (Employee Severance)
Version 1.1
Effective Date 1 Jan 2026
Prepared by A. Gunduz – Group Finance
Reviewed by (blank)
Applies to All entities within the Multi Group
Standard IAS 19 – Employee Benefits

1. Objective & Scope – uniform approach for recognising, measuring, adjusting, and releasing redundancy provisions across all Multi Group entities, in accordance with IAS 19 and local statutory requirements. Covers all employees on permanent or fixed-term contracts where local legislation grants a statutory severance entitlement. Provisions are calculated centrally by Group Finance (HQ) with local HR. The policy does not cover notice-period pay, holiday allowances, or vacation monies – these are expensed as incurred through normal payroll.

2. Key Definitions – as v1.0: Contracted Salary Basis = total contracted annual compensation (Sympa via API) ÷ 12, effective May 2026; Above the Line = within RMA Result (PQ8 – Redundancy, GL 44125); Below the Line = below RMA Result (PU – Depreciation and bad debtors, GL 43011); Stored procedure dbo.AGz_RedundancyProvision_v2 on nl-amsterdm-164/dm_finance.

3. Salary Basis – Migration to Sympa Data (Effective Jan 2026): Monthly Salary = Total Contracted Annual Compensation (Sympa) ÷ 12. Local HR teams remain responsible for ensuring contracted salary data in Sympa is current and accurate.

4. Country-Specific Severance Multipliers (months of contracted monthly salary): NL/HQ TotalInYears/3; DE TotalInYears/2; TR TotalInYears (capped at TRY 64,948.77); CH 0; IT 9; DK tiered 0/1/3 (<12 yrs pro-rata, ≥12 yrs 1 month, ≥15 yrs 3 months); GB age-weighted weekly salary × years (max 20 yrs, 1.5x cap, max weighting applied as no birth-date data); UA 3; FR ≤10 yrs 1/4 per month, >10 yrs 1/3; ES 20 days per year capped at 12 months = Min(TotalYrs×20/30, 12); SK tiered 0–4 (2 yrs 0; 2–5 1m; 5–10 2m; 10–20 3m; 20+ 4m); HU tiered 0–6 (3 yrs 0; 3–5 1m; 5–10 2m; 10–15 3m; 15–20 4m; 20–25 5m; 25+ 6m); PL tiered 1–3 (<2 yrs 1m; 2–8 yrs 2m; >8 yrs 3m); PT three legislative periods (pre-Nov 2012: 30 days/yr; Nov 2012–Apr 2023: 18 days/yr first 3 years then 12 days/yr; May 2023 onwards: 14 days/yr), aggregate capped at 12 months.
4.1 Override Rules: PT provision > 12 months → cap multiplier to 12; DELIVE FTE ≤ 0.22 (mini-job) → 0; PLLIVE Employee ID 5588 → 0 (management contract); PL interns EmpIDs 6382, 6598, 6599 → 0 effective from period 202509.

5. Accounting Treatment – Journal Entries
All redundancy provision movements are booked centrally by Group Finance. Local entities do not post redundancy provision entries independently. Countries are only required to process actual severance payments by debiting GL 27527 and crediting GL 13311.

5.1 Initial Recognition
A provision is recognised when a constructive obligation exists and the amount can be reliably estimated. The amount is determined by Group Finance in line with the country multiplier (§4) and the contracted salary basis (§3). Provision increases at quarter-end are booked via GL 44125. Provisions are not tracked at individual employee level.
Journal Entry 5.1 – Initial recognition of provision
Dr PQ Staff costs / PQ8 Redundancy / GL 44125 Redundancy 100.00
Cr BE Non-Current Liabilities / BE5 Provisions / GL 27527 Accrual redundancy 100.00

5.2 Quarter-End Provision Movements
At each quarter-end, Group Finance reviews the provision balance and posts any movements centrally. Provision increases are booked via GL 44125 (Dr 44125 / Cr 27527). Provision releases at quarter-end are split by vintage: amounts relating to the current year are released through GL 44125, while amounts carried forward from prior years are released through GL 43011. No individual employee-level bookings are made for provisions.

5.3 Severance Payments by Countries
When an actual severance payment is made, countries process the transaction in three steps. The purpose of this approach is to ensure that the full gross amount (pre-tax) is cleared from the provision account (GL 27527), rather than only the net cash payment.
Step 1 – Payroll entry (gross amount). The gross severance amount is included in the payroll run for the period, capturing the full pre-tax obligation as a staff cost.
Journal Entry 5.3a – Payroll inclusion of severance (gross)
Dr PQ8 / GL 44125 Redundancy – gross severance 100
Cr Taxes Payable / GL 27523 Wage tax payable 10
Cr Salaries Payable / GL 27515 Salaries payable 90
Step 2 – Bank payment (net amount). The net amount after tax withholding is paid to the employee, clearing the salaries payable account.
Journal Entry 5.3b – Net payment to employee
Dr GL 27515 Salaries payable 90
Cr BB5 / GL 13311 Bank 90
Step 3 – Provision release at gross. The full gross amount is transferred from the provision account (GL 27527) to GL 44125, clearing the provision at gross value. This ensures the provision is released on a gross basis, not net.
Journal Entry 5.3c – Provision release at gross (Dr 27527 / Cr 44125)
Dr BE5 / GL 27527 Accrual redundancy 100
Cr PQ8 / GL 44125 Redundancy 100

5.4 Quarter-End Provision Increase
When the calculated provision exceeds the current balance at quarter-end, Group Finance posts an upward adjustment. The entry is booked centrally and does not involve any country-level posting.
Journal Entry 5.4 – Quarter-end provision increase (Dr 44125 / Cr 27527)
Dr PQ8 / GL 44125 Redundancy provision increase X
Cr BE5 / GL 27527 Accrual redundancy X

5.5 Quarter-End Provision Release
When the calculated provision is lower than the current balance, a release is posted centrally. The split depends on the vintage of the provision being released: amounts accrued in the current year are released through GL 44125 (above the line); amounts carried forward from prior years are released through GL 43011 (below the line).
Journal Entry 5.5 – Quarter-end provision release (current year: Dr 27527 / Cr 44125; prior years: Dr 27527 / Cr 43011)
Dr BE5 / GL 27527 Accrual redundancy X
Cr PQ8 (current year) / GL 44125 Current year release above the line X
Cr Below the Line (prior years) / PU / GL 43011 Prior year release below the line X

6. Controls & Governance
6.1 Headcount Reconciliation – Group Finance reconciles the employee population in the provision model against the active headcount in Sympa each period. Movements (new joiners, leavers, contract changes) must be reflected in the calculation before the provision entry is posted.
6.2 Calculation Sign-off – The SeveranceMultiplier calculation is run via the dbo.AGz_RedundancyProvision_v2 stored procedure. Output is reviewed by Group Finance and confirmed with local HR before posting.
6.3 Currency – Provisions denominated in non-EUR currencies are retranslated at the closing rate each period. For currencies subject to significant depreciation, the real-terms obligation is assessed to determine whether a downward adjustment above the line is warranted (see §5.2).
6.4 Release Restriction – A downward adjustment to the provision may never result in a credit above the line (i.e. it cannot reduce Staff costs). All releases that are not offset by an actual payment must be processed below the line.

7. Open Items & Questions Requiring Resolution
1 | Turkey: Confirm the statutory cap (TRY 64,948.77) is applied per year of service in the multiplier output, and validate against quarterly FX rates. | A. Gunduz / TR HR | Open

8. Version History
1.0 | April 2026 | A. Gunduz | Initial draft – incorporates SQL-based country multiplier logic and Sympa salary migration; aligned with CEO guidance on above/below-the-line release.
v1.1: Centralised all provision bookings (HQ only); countries limited to severance payment entry (Dr 27527 / Cr 13311); quarter-end increases via 44125; releases split by vintage (44125 current year, 43011 prior years); provision not tracked at employee level; removed alternative journal entry examples.
