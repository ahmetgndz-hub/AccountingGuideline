---
date: 2026-04-28
subject: "Re: redundancy calculation methodology"
attachment: "Redundancy_Provision_Policy_v1.0.docx"
source_email: 2026-04-28_redundancy-calculation-methodology.md
status: reference
superseded_by: 2026-05-05_redundancy-calculation-methodology-2-attachment-1.md
topics: [redundancy-provision, salary-bookkeeping, accruals]
fetched: 2026-10-09 via Microsoft 365 connector (read-only), text extracted from DOCX by the connector; table layout flattened
---

MULTI
Group Accounting Policy
Redundancy Provision (Employee Severance)
Version 1.0
Effective Date 1 Jan 2026
Prepared by A. Gunduz – Group Finance
Reviewed by (blank)
Applies to All entities within the Multi Group
Standard IAS 19 – Employee Benefits

1. Objective & Scope
This policy establishes the uniform approach for recognising, measuring, adjusting, and releasing redundancy provisions across all Multi Group entities, in accordance with IAS 19 Employee Benefits and local statutory requirements.
It covers:
All employees on permanent or fixed-term contracts where local legislation grants a statutory severance entitlement.
Provisions are calculated centrally by Group Finance (HQ) in close coordination with local HR teams.
The policy does not cover notice-period pay, holiday allowances, or vacation monies – these are expensed as incurred through normal payroll.

2. Key Definitions
Redundancy Provision: A liability recognised for the estimated obligation to pay statutory severance to current employees, calculated based on service length and contracted salary.
Severance Multiplier: Country-specific coefficient (expressed in months of salary) used to determine the provision amount per employee.
Contracted Salary Basis: Total contracted annual compensation (as sourced from Sympa HR system via API) divided by 12, used as the monthly salary reference for all calculations effective May 2026.
Severance Multiplier × Monthly Salary: The provision value per employee for a given reporting period.
Above the Line (P&L): Income and expense items reported within RMA Result – e.g. Staff costs (PQ8 – Redundancy).
Below the Line: Items reported below RMA Result – e.g. release of excess provisions that does not generate a P&L credit above the line (PU – Depreciation and bad debtors, GL 43011).
Stored Procedure / PQ: dbo.AGz_RedundancyProvision_v2 located on the server nl-amsterdm-164/dm_finance server

3. Salary Basis – Migration to Sympa Data (Effective Jan 2026)
Prior to Jan 2026, the monthly salary reference was derived from actual payroll elements paid in the current month. This approach had two material limitations:
It depended on correct element-code usage by local payroll teams.
It did not fully account for 13th/14th-month salary structures (e.g. Italy), causing the annualised figure to differ from contracted compensation.
From 1 Jan 2026, the salary basis for all countries is:
Monthly Salary = Total Contracted Annual Compensation (Sympa) ÷ 12
The Sympa data is accessed via API and refreshed each reporting period. Local HR teams remain responsible for ensuring contracted salary data in Sympa is current and accurate.

4. Country-Specific Severance Multipliers
The table below summarises the statutory severance methodology applied per entity. All multipliers are expressed in months of the contracted monthly salary.
(Country | Legal Entitlement | Multiplier Formula | Salary Basis)
NL / HQ | 1/3 of monthly salary for each year of service | TotalInYears / 3 | Contracted annual / 12
DE | 1/2 of monthly salary for every full year of service | TotalInYears / 2 | Contracted annual / 12
TR | 1 month salary per year of service (capped at TRY 64,948.77) | TotalInYears | Contracted annual / 12
CH | Not applicable | 0 | –
IT | 9 times the monthly salary | 9 | Contracted annual / 12
DK | < 12 yrs: pro-rata; ≥ 12 yrs: 1 month; ≥ 15 yrs: 3 months | Tiered (0/1/3) | Contracted annual / 12
GB | Age-weighted weekly salary × years (max 20 yrs, 1.5x cap) | Tiered weekly | Contracted annual / 12
UA | 3 months salary | 3 | Contracted annual / 12
FR | ≤ 10 yrs: 1/4/month; > 10 yrs: 1/3/month | Tiered (1/4 or 1/3) | Contracted annual / 12
ES | 20 days per year, capped at 12 months | Min(TotalYrs×20/30, 12) | Contracted annual / 12
SK | 2 yrs: 0; 2–5: 1m; 5–10: 2m; 10–20: 3m; 20+: 4m | Tiered (0–4) | Contracted annual / 12
HU | 3 yrs: 0; 3–5: 1m; 5–10: 2m; 10–15: 3m; 15–20: 4m; 20–25: 5m; 25+: 6m | Tiered (0–6) | Contracted annual / 12
PL | < 2 yrs: 1m; 2–8 yrs: 2m; > 8 yrs: 3m | Tiered (1–3) | Contracted annual / 12
PT | 3 periods (pre-2012 / 2012–2023 / post-2023) with different rates; capped at 12 months | Complex – see §4 | Contracted annual / 12
Portugal note: Three legislative periods apply. Period 1 (pre-Nov 2012): 30 days per year. Period 2 (Nov 2012 – Apr 2023): 18 days/year for first 3 years, then 12 days/year. Period 3 (May 2023 onwards): 14 days per year. The aggregate is capped at 12 months.
UK note: In the absence of employee birth-date data, the maximum weighting (1.5×) is applied for all employees. Service is capped at 20 years.
Turkey note: The statutory cap per year of service (TRY 64,948.77) applies. Provision is reviewed against this cap quarterly.

4.1 Override Rules
The following entity-level overrides are applied after the standard formula:
(Entity | Condition | Treatment)
PT (all) | Provision > 12 months | Cap SeveranceMultiplier to 12.
DELIVE (DE) | FTE ≤ 0.22 (mini-job) | Set SeveranceMultiplier to 0 – mini-job contracts are not entitled to severance.
PLLIVE (PL) | Employee ID 5588 | Set to 0 – management contract does not entitle to severance.
PL (interns) | EmpIDs 6382, 6598, 6599 | Effective from period 202509: Set to 0 – interns are not entitled to severance.

5. Accounting Treatment – Journal Entries
All redundancy provision movements are booked centrally by Group Finance. Local entities do not post redundancy provision entries independently.

5.1 Initial Recognition
A provision is recognised when a constructive obligation exists and the amount can be reliably estimated. The amount is determined by Group Finance in line with the country multiplier (§4) and the contracted salary basis (§3).
Journal Entry 5.1 – Initial recognition of provision
Dr PQ Staff costs / PQ8 Redundancy / GL 44125 Redundancy 100.00
Cr BE Non-Current Liabilities / BE5 Provisions / GL 27527 Accrual redundancy 100.00

5.2 Adjustment of Provision
Provisions are reviewed each reporting period and adjusted for changes in headcount, salary, or service length.
Upward adjustments are always permitted.
Downward adjustments above the line are only permitted for non-EUR currencies where the local currency has depreciated by more than the elapsed service period warrants (i.e. the real-terms obligation has decreased).
All other downward adjustments must be routed below the line (see §5.4 and §5.5).
Journal Entry 5.2 – Upward adjustment of provision
Dr PQ8 / GL 44125 Redundancy 10.00
Cr BE5 / GL 27527 Accrual redundancy 10.00

5.3 Termination Payment – Exact Match to Provision
Where the actual termination payment equals the provision held, the provision is released against the cash payment with no P&L impact.
Journal Entry 5.3 – Termination payment equal to provision (no P&L hit)
Dr BE5 / GL 27527 Accrual redundancy 110.00
Cr BB5 Cash and cash equivalents / GL 13311 Bank 110.00

5.4 Termination Payment – Exceeds Provision
Where the actual payment exceeds the provision, the shortfall is charged to the P&L above the line as an additional redundancy cost.
Journal Entry 5.4 – Termination payment exceeds provision (additional P&L charge)
Dr BE5 / GL 27527 Accrual redundancy 110.00
Dr PQ8 / GL 44125 Redundancy 20.00
Cr BB5 / GL 13311 Bank 130.00

5.5 Termination Payment – Less Than Provision (Actual Payment)
Where the actual payment is less than the provision, the excess provision is released below the line. This ensures a release does not generate a credit above the line, in line with group policy.
Journal Entry 5.5 – Termination payment less than provision (below-the-line release)
Dr BE5 / GL 27527 Accrual redundancy 110.00
Cr Below the Line / PU Depreciation and bad debtors / GL 43011 Redundancy provision 20.00
Cr BB5 / GL 13311 Bank 90.00

5.6 Employee Leaves Voluntarily – No Termination Payment
Where an employee resigns without any contractual entitlement to severance, the full provision is released below the line. No credit is recognised above the line.
Journal Entry 5.6 – Voluntary departure, full provision release below the line
Dr BE5 / GL 27527 Accrual redundancy 110.00
Cr PU / GL 43011 Redundancy provision 110.00
Note: Notice-period pay, holiday allowances, and vacation monies are NOT processed through the redundancy provision. These are booked directly: Dr Salary cost (PQ) / Cr Bank (BB5 13311) in the period they arise.

6. Controls & Governance
6.1 Headcount Reconciliation
Group Finance reconciles the employee population in the provision model against the active headcount in Sympa each period. Movements (new joiners, leavers, contract changes) must be reflected in the calculation before the provision entry is posted.
6.2 Calculation Sign-off
The SeveranceMultiplier calculation is run via the dbo.AGz_RedundancyProvision_v2 stored procedure. Output is reviewed by Group Finance and confirmed with local HR before posting.
6.3 Currency
Provisions denominated in non-EUR currencies are retranslated at the closing rate each period. For currencies subject to significant depreciation, the real-terms obligation is assessed to determine whether a downward adjustment above the line is warranted (see §5.2).
6.4 Release Restriction
A downward adjustment to the provision may never result in a credit above the line (i.e. it cannot reduce Staff costs). All releases that are not offset by an actual payment must be processed below the line.

7. Open Items & Questions Requiring Resolution
1 | Turkey: Confirm the statutory cap (TRY 64,948.77) is applied per year of service in the multiplier output, and validate against quarterly FX rates. | A. Gunduz / TR HR | Open

8. Version History
1.0 | April 2026 | A. Gunduz | Initial draft – incorporates SQL-based country multiplier logic and Sympa salary migration; aligned with CEO guidance on above/below-the-line release.
