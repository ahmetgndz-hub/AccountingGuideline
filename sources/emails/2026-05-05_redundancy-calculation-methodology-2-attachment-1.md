---
date: 2026-05-05
subject: "Re: redundancy calculation methodology"
attachment: "Redundancy_Provision_Policy_v1_1.docx"
source_email: 2026-05-05_redundancy-calculation-methodology-2.md
status: reference
superseded_by: 2026-07-14_redundancy-provision-booking-2026q2-attachment-1.md
topics: [redundancy-provision, salary-bookkeeping, accruals]
fetched: 2026-10-09 via Microsoft 365 connector (read-only), text extracted from DOCX by the connector; table layout flattened
---

> Note: the file sent on 2026-05-05 is still labelled "Version 1.0" inside, but the booking section (§5) already differs from the 2026-04-28 file: bookings are centralised at HQ, countries only post the severance payment (Dr 27527 / Cr 13311), and releases are split by vintage (44125 current year, 43011 prior years). Sections 1–4 and 6–7 are identical to the 2026-04-28 version and are not repeated here in full.

MULTI
Group Accounting Policy
Redundancy Provision (Employee Severance)
Version 1.0 (file name v1_1)
Effective Date 1 Jan 2026
Prepared by A. Gunduz – Group Finance
Reviewed by (blank)
Applies to All entities within the Multi Group
Standard IAS 19 – Employee Benefits

1.–4. Objective & Scope, Key Definitions, Salary Basis (Sympa, contracted annual ÷ 12), Country-Specific Severance Multipliers and 4.1 Override Rules: identical to the 2026-04-28 version (see 2026-04-28_redundancy-calculation-methodology-attachment-1.md).

5. Accounting Treatment – Journal Entries
All redundancy provision movements are booked centrally by Group Finance. Local entities do not post redundancy provision entries independently. Countries are only required to process actual severance payments by debiting GL 27527 and crediting GL 13311.

5.1 Initial Recognition
A provision is recognised when a constructive obligation exists and the amount can be reliably estimated. The amount is determined by Group Finance in line with the country multiplier (§4) and the contracted salary basis (§3). Provisions are not tracked at individual employee level.
Journal Entry 5.1 – Initial recognition of provision (booking by HQ)
Dr PQ Staff costs / PQ8 Redundancy / GL 44125 Redundancy 100.00
Cr BE Non-Current Liabilities / BE5 Provisions / GL 27527 Accrual redundancy 100.00

5.2 Quarter-End Provision Movements
At each quarter-end, Group Finance reviews the provision balance and posts any movements centrally.
Journal Entry 5.2a – Increase of provision (booking by HQ)
Dr PQ8 / GL 44125 Redundancy 10.00
Cr BE5 / GL 27527 Accrual redundancy 10.00
Journal Entry 5.2b – Release of provision (booking by HQ) (employees left)
The split depends on the vintage of the provision being released: amounts accrued in the current year are released through GL 44125 (above the line); amounts carried forward from prior years are released through GL 43011 (below the line).
Dr BE5 / GL 27527 Accrual redundancy 110.00
Cr PQ8 / GL 44125 Redundancy 10.00
Cr Below the Line (prior years) / PU Depreciation and bad debtors / GL 43011 Prior year release below the line 100.00

5.3 Severance Payments by Countries
Countries are responsible only for processing actual severance payments when an employee leaves. The booking is: Debit GL 27527 (Accrual redundancy) / Credit GL 13311 (Bank). No other provision entries are made at country level.
Journal Entry 5.3 – Severance payment by country
Dr BE5 / GL 27527 Accrual redundancy 110.00
Cr BB5 Cash and cash equivalents / GL 13311 Bank 110.00

6. Controls & Governance
6.1 Headcount Reconciliation – Group Finance reconciles the employee population in the provision model against the active headcount in Sympa each period. Movements (new joiners, leavers, contract changes) must be reflected in the calculation before the provision entry is posted.
6.2 Calculation Sign-off – The SeveranceMultiplier calculation is run via the dbo.AGz_RedundancyProvision_v2 stored procedure. Output is reviewed by Group Finance and confirmed with local HR before posting.
6.3 Currency – Provisions denominated in non-EUR currencies are retranslated at the closing rate each period. For currencies subject to significant depreciation, the real-terms obligation is assessed to determine whether a downward adjustment above the line is warranted (see §5.2).
6.4 Release Restriction – A downward adjustment to the provision may never result in a credit above the line (i.e. it cannot reduce Staff costs). All releases that are not offset by an actual payment must be processed below the line.

7. Open Items & Questions Requiring Resolution
1 | Turkey: Confirm the statutory cap (TRY 64,948.77) is applied per year of service in the multiplier output, and validate against quarterly FX rates. | A. Gunduz / TR HR | Open

8. Version History
1.0 | April 2026 | A. Gunduz | Initial Draft
