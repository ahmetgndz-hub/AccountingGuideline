---
date: 2026-10
subject: Group Accounting Policy - Redundancy Provision (Employee Severance Provision) v1.2
from: A. Gunduz - Group Finance (reviewed by Steven Poelman)
to: Group Finance, country Finance and HR
status: current
superseded_by:
topics: [redundancy-provision, accruals, salary-bookkeeping, document-codes, non-recurring-expenses]
---

Pasted into the Claude session on 2026-10-08 as the first guideline to load. Text verbatim (table layout flattened by the paste).

MULTI
Group Accounting Policy

Redundancy Provision (Employee Severance Provision)

Version 1.2
Effective Date: 2026/12 close (31 Dec 2026); methodology as applied from the 2026/6 run
Prepared by: A. Gunduz - Group Finance
Reviewed by: Steven Poelman
Applies to: All entities within the Multi Group (closed entities excluded, §4.1)
Policy type: Management reporting policy

1. Objective & Scope

This policy establishes the uniform approach for recognising, measuring and adjusting the redundancy provisions across all Multi Group entities for management reporting purposes. All redundancy provisions calculated under this policy are fully recognised in management books and form part of internal performance reporting and cost analysis.
It covers:
All employees on permanent or fixed-term contracts where local legislation grants a statutory severance entitlement under certain circumstances.
Provisions are calculated centrally by Group Finance (HQ) in close coordination with local HR and Finance teams.
The Redundancy Provision does not cover notice-period pay, holiday allowances, or vacation monies.
Employees, contract types and entities that are excluded from the provision, and other adjustments to the standard calculation, are defined in §4.1.

2. Key Definitions

Redundancy Provision: A liability recognised for the estimated obligation to pay statutory severance to current employees, calculated based on service length and contracted gross salary.
Severance Multiplier: Country-specific coefficient (expressed in months of salary) used to determine the provision amount per employee.
Contracted Salary Basis: Total gross annual salary (sourced from the Sympa HR system via API).
Severance Multiplier x Monthly Salary: The provision value per employee for a given reporting period.
Above the Line (P&L): Income and expense items reported within RMA Result - e.g. Staff costs (PQ8 - Redundancy, GL 44125).
Below the Line: Items reported below RMA Result - e.g. release of provisions that relate to previous years and that does not generate a P&L credit above the line (PU - Depreciation and bad debtors, GL 43011).
Stored Procedure / PQ: dbo.AGz_RedundancyProvision_v4 (calculation, movement bridge and journal) with dbo.AGz_RedundancyProvision_Calc (per-employee calculation), dbo.AGz_RedundancyProvision_CodaXml (Coda intray documents) and dbo.AGz_RedundancyProvision_PostStatus (posting status), on nl-amsterdm-164 / dm_finance.
Target Provision: The provision per employee calculated at a quarter end (Severance Multiplier x capped Monthly Salary), in the home currency of the legal entity.
Booked Provision: The balance of GL 27527 in Coda (el3 MAN) for the employee (el6 = E<employee number>), after all payroll and HQ postings. Documents in the Coda intray are included.
Calculated Year-End Provision: The Target Provision of the employee at the previous year end, as frozen in the final snapshot (dbo.AGz_RedundancyProvision_Snapshot).
Prior-Year Layer: The part of the provision that relates to previous years: the Calculated Year-End Provision of the employee (for the pooled element E6188: its booked balance at the previous year end). Releases of this layer are booked below the line (GL 43011).
In-Year Layer: The part of the Booked Provision above the Prior-Year Layer (Booked Provision - Calculated Year-End Provision, if positive), i.e. accrued in the current year. Releases are booked above the line (GL 44125).
Movement Bridge: Explanation of the change in the Target Provision versus the previous quarter end and versus the previous year end, split per driver (§6.5).
Layer Map: Per legal entity: in which accounting principles (el3 LOC and/or FSM) the MAN booking is reversed (§5.4).
Element 5 mapping: Per legal entity and GL account the local element 5 (el5) codes that Coda accepts for the Group account (link list oas_rllist). A line with a code outside the list is rejected on posting (§5.7).
Document JV-REDUND: Coda document code of the quarter-end booking: one document per legal entity and entity code (el1), §5.5.
Dual value: The EUR amount of a line at the closing rate, posted next to the home-currency amount (§5.5).

3. Salary Basis - Migration to Sympa Data (Effective Jan 2026)

Prior to Jan 2026, the monthly salary reference was derived from actual payroll elements paid in the current month. This approach had two material limitations:
It depended on correct element-code usage by local payroll teams.
It did not fully account for 13th/14th-month salary structures (e.g. Italy), causing the annualised figure to differ from contracted compensation.
From 1 Jan 2026, the salary basis for all countries is:
Monthly Salary = Total Contracted Annual Compensation (Sympa) / 12
The Sympa data is accessed via API and refreshed each reporting period. Local HR teams remain responsible for ensuring contracted salary data in Sympa is current and accurate.

4. Country-Specific Severance Multipliers

Country | Legal Entitlement | Multiplier Formula | Salary Basis
NL / HQ / AA | 1/3 of monthly salary for each year of service | Total Years / 3 | Contracted annual / 12
DE | 1/2 of monthly salary for every full year of service | TotalInYears / 2 | Contracted annual / 12
TR | 1 month salary per year of service; monthly salary capped at the statutory ceiling in force at the quarter end (updated in January and July) | TotalInYears | Contracted annual / 12
CH | Not applicable | 0 | -
IT | Tiered by completed years of service (methodology of 30 Apr 2026) | Tiered 2.0 - 14.0 (see notes) | Contracted annual / 12
DK | < 12 yrs: pro-rata; >= 12 yrs: 1 month; >= 15 yrs: 3 months | Tiered (0/1/3) | Contracted annual / 12
GB | Age-weighted weekly salary x years (max 20 yrs, 1.5x cap); office staff only (§4.1) | Tiered weekly | Contracted annual / 12
UA | 3 months salary | 3 | Contracted annual / 12
FR | <= 10 yrs: 1/4 month; > 10 yrs: 1/3 month per year | Tiered (1/4 or 1/3) | Contracted annual / 12
ES | 20 days per year, capped at 12 months | Min(TotalYrs x 20/30, 12) | Contracted annual / 12
SK | < 2 yrs: 0; 2-5: 1m; 5-10: 2m; 10-20: 3m; 20+: 4m | Tiered (0-4) | Contracted annual / 12
HU | < 3 yrs: 0; 3-5: 1m; 5-10: 2m; 10-15: 3m; 15-20: 4m; 20-25: 5m; 25+: 6m | Tiered (0-6) | Contracted annual / 12
PL | < 2 yrs: 1m; 2-8 yrs: 2m; > 8 yrs: 3m | Tiered (1-3) | Contracted annual / 12
PT | 3 periods (pre-2012 / 2012-2023 / post-2023) with different rates; capped at 12 months | Complex - see notes | Contracted annual / 12

Notes:
Portugal: Three legislative periods apply. Period 1 (pre-Nov 2012): 30 days per year. Period 2 (Nov 2012 - Apr 2023): 18 days/year for first 3 years, then 12 days/year. Period 3 (May 2023 onwards): 14 days per year. The aggregate is capped at 12 months.
United Kingdom: In the absence of employee birth-date data, the maximum weighting (1.5x) is applied for all employees. Service is capped at 20 years. The provision is calculated for office staff only (§4.1).
Turkey: The statutory severance ceiling caps the monthly salary per year of service. The ceiling in force at the quarter-end date is applied: TRY 64,948.77 from 1 Jan 2026 and TRY 73,729.87 from 1 Jul 2026 (SGK). The ceiling is published twice a year (January and July); the new figure is loaded in the calculation (table #Help_SeverenceCeiling in dbo.AGz_RedundancyProvision_Calc) before the first quarter-end run of the new half-year. The figure valid from 1 Jan 2027 must be loaded before the 2026/12 run (§7).
Italy: From 30 Apr 2026 the multiplier is tiered by completed years of service: >= 1 yr 2.0; >= 2 yrs 3.5; >= 3 yrs 5.0; >= 4 yrs 6.5; >= 5 yrs 8.0; >= 6 yrs 9.5; >= 7 yrs 11.0; >= 8 yrs 12.0; >= 9 yrs 13.0; >= 10 yrs 14.0. Three employees with individual contractual terms follow the schedule 4 / 8 / 12 / 18 / 24 months (< 2 / < 6 / < 10 / < 15 / >= 15 yrs), two of them with an additional 5 months.
Denmark: The formula (pro-rata below 12 years, 1 month from 12 years, 3 months from 15 years) is under review against the Salaried Employees Act (1 / 2 / 3 months after 12 / 15 / 18 years), see §7.

4.1 Exclusions and Adjustments

The following employees and entities are provisioned at zero or with an adjusted service period. Every exclusion is visible as a comment in the calculation output and is confirmed with local HR before posting.
Interns: no statutory severance entitlement.
Management contracts: no severance entitlement under the contract (e.g. Poland).
Germany - Minijob: employees with FTE <= 0.22 are not entitled.
Ukraine: definitive contracts without a severance clause.
Temporary / fixed-term contracts: only provisioned where local law grants a severance entitlement at the end of the contract.
Group directors: excluded from the provision.
United Kingdom - asset locations: from the 2026/6 closing only office staff (locations Multi-Realm: Wilmslow and Somerset) are provisioned. Employees at asset locations (shopping centres) are provisioned at zero. The provision of the 82 employees concerned that was booked before was reversed in the 2026/6 period (document RP202606-GBC): the 2026 part through GL 44125, the remainder through GL 43011.
Closed entities: entity codes (el1) of closed companies are outside the calculation, the journal and every comparison; their GL 27527 balances remain unchanged: TR BS901, BS003, BS006, BS007, BS102, BS103, BS105, BS107, BS112, BS117, BS120, BS125, BS129 and IT ITS003.
Leavers at the quarter end: employees whose termination date equals the quarter-end date are provisioned at zero (payment follows via payroll, §5.3).
Leavers during the quarter: an employee who left before the quarter end is no longer in the active population. The target is zero and the booked provision is released under §5.2b. If the payment only follows after the quarter end, see §7.
Retirees continuing to work: service is counted from the start of the retiree contract.
Portugal: the aggregate entitlement is capped at 12 months.

5. Accounting Treatment - Journal Entries

All redundancy provision movements are booked centrally by Group Finance, per employee (el6 = E<employee number>) and in accounting principle el3 MAN, with reversed copies in LOC and/or FSM where the layer map requires it (§5.4). Documents are delivered to the Coda intray (§5.5). Local entities do not post redundancy provision entries; they only process actual severance payments through payroll (§5.3).

5.1 Initial Recognition
A provision is recognised when a constructive obligation exists and the amount can be reliably estimated. The amount is determined by Group Finance in line with the country multiplier (§4) and the contracted salary basis (§3). Provisions are tracked at individual employee level: every GL 27527, 44125 and 43011 line carries the employee element (el6 = E<employee number>).
Journal Entry 5.1 - Initial recognition of provision (booking by HQ): BE5 Provisions 27527 Accrual redundancy Cr 100.00; PQ8 Redundancy 44125 Redundancy Dr 100.00.

5.2 Quarter-End Provision Movements
At each quarter end the target provision of every employee is compared with the booked provision of that employee (GL 27527, el3 MAN, within the legal entity and entity code). Only the difference is posted. Because the comparison is made against the booked balance, severance payments processed by payroll, earlier corrections and exchange-rate effects are taken into account automatically and a release can never be booked twice.
Journal Entry 5.2a - Increase of provision (booking by HQ): 27527 Cr 10.00; 44125 Dr 10.00.
Journal Entry 5.2b - Decrease / release of provision (booking by HQ)
The split depends on the layer being released. The prior-year layer of an employee is the provision calculated at the previous year end (final snapshot); the in-year layer is the booked provision above it. A decrease - for a leaver, a lower salary or multiplier, an exclusion or an exchange-rate change - is released first from the in-year layer through GL 44125 (above the line); only the remainder, never more than the prior-year layer, is released through GL 43011 (below the line). The layers are taken from the calculation, not from the year-end balance in Coda: a difference between the booked year-end balance and the calculated year-end provision does therefore not move a release between above and below the line.
27527 Accrual redundancy Dr 110.00; PQ8 44125 Redundancy Cr 10.00; PU 43011 Redundancy provision (non-asset) Cr 100.00.
Example 1: calculated year-end provision 100, booked 110, new target 0 -> Dr 27527 110 / Cr 44125 10 / Cr 43011 100.
Example 2: calculated year-end provision 100, booked 110, new target 60 -> Dr 27527 50 / Cr 44125 10 / Cr 43011 40. New target 105 -> Dr 27527 5 / Cr 44125 5.
Example 3: calculated year-end provision 100, booked 80 (below the year-end provision), new target 0 -> Dr 27527 80 / Cr 43011 80; nothing is released above the line.
Example 4 (leaver, Spain, 2026/9): calculated year-end provision 3,407.04, booked 4,068.01, new target 0 -> Dr 27527 4,068.01 / Cr 44125 660.97 / Cr 43011 3,407.04.
Pooled element: the element E6188 has no calculated year-end provision; its booked year-end balance is the prior-year layer until the pool is cleared (§5.6).

5.3 Severance Payments via Payroll
Countries process the actual severance payment in the payroll run of the month of payment. In the payroll document the gross severance amount is not charged to staff costs but debited to GL 27527 (Accrual redundancy) with the employee element (el6 = E<employee number>), in accounting principle el3 MAN like all other payroll lines. The credit side follows the normal payroll entries (net pay via the salary suspense account, wage tax and social security). No other provision entries are made at country level; in the principles where the provision is reversed (§5.4) the payment is turned into staff cost by the quarter-end layer booking.
At the next quarter end the target provision of the leaver is zero. The remaining booked balance is released in line with §5.2b. If the payment exceeded the provision, the resulting debit balance on GL 27527 is charged to GL 44125 (above the line) by the quarter-end booking.
Journal Entry 5.3 - Severance payment in payroll (booking by country, el3 MAN): 27527 Accrual redundancy (el6 = E<employee>) Dr 110.00; 27515 Salary suspense account (net pay) Cr 80.00; 27523 Wage tax and social security Cr 30.00.

5.4 Accounting Principles (el3 Layers)
Reporting views: management = MAN; local GAAP = MAN + LOC; fiscal = MAN + FSM. The HQ booking is made in el3 MAN. Per legal entity the layer map (dbo.AGz_RedundancyLayerMap) defines in which principle the provision is reversed (target = minus the MAN target). A principle that is not reversed is booked to zero; a principle that is marked as not touched receives no lines.
HQ, NL, AA, FR, SK | LOC reversed | FSM reversed | valid from 2026/7
TR | LOC reversed (in the same document as MAN) | FSM not touched (maintained by local Finance) | 2026/6
BE, CH, CY, CZ, DE, DK, ES, FI, GB, HU, IE, IT, LU, LV, PL, PT, UA | LOC zero (provision stays visible in the local view) | FSM reversed | 2026/7
Each quarter the LOC and FSM balance of GL 27527 per employee is booked to its own target. Differences from the past (payments booked in MAN only, earlier manual reversals) are aligned with the same split as §5.2b: in-year part through GL 44125, prior-year part through GL 43011; in a reversed principle the layers follow the calculated layers of MAN. The LOC and FSM lines of an entity code are in the same document as its MAN lines and every principle balances on its own. An entity without a layer map receives no posting.

5.5 Posting to Coda
The quarter-end booking is generated as a Coda eFinance PostToIntray document (XML, via Fluxygen) by dbo.AGz_RedundancyProvision_CodaXml:
Document: one document per legal entity and entity code (el1), document code JV-REDUND. The MAN, LOC and FSM lines of the entity code are in the same document (e.g. Turkey: MAN + LOC). Period = quarter-end period, date = quarter-end date (2026-09-30T00:00:00.000Z).
Currency: the document is in the home currency of the entity (DocValue), with the EUR amount at the period-end rate as dual value (DualValue). Entities with the EUR as home currency (AA, DE, ES, FR, HQ, IT, NL, PT, SK) post in EUR without dual value. Home and EUR amounts are rounded per line; the rounding difference is put on the largest line so that every principle balances to 0.00 in both currencies.
Account code: el1.el2.el3.el4.el5.el6. El2 and the default el5 come from the latest quarter with MAN GL 27527 lines of the entity code (dispersal documents Z-% are ignored); el5 per GL account follows §5.7.
Line details: description, ExtRef2 = RP<yyyymm>-<el1> (RP<yyyymm>-RC-<el1> for a transition document), ExtRef3 = main movement driver and a comment with the employee name and the movement bridge. Coda rejects an ExtRef2 that is already used by another document of the same company; the reference therefore carries the entity code, and a corrected document gets a new reference or is sent after the old document has been deleted.
Period: the posting period must be open for the integration user. Otherwise the document is rejected (message "You do not have access to period").
Delivery and status: the XML files are copied with the service account to the Fluxygen pick-up folder (\\nl-amsterdm-127\Input); Fluxygen delivers them to the Coda intray, normally within 15 to 45 minutes. Group Finance reviews and posts the documents in Coda. The result is followed in dbo.AGz_RedundancyProvision_PostLog (generated - sent - posted - failed - void) with dbo.AGz_RedundancyProvision_PostStatus. It reads the Coda documents (intray, posted, deleted) and the process log of the posting job (integration.dbo.logging, application "31z - Post to Coda", severity 2 = failures only). A rejected or deleted document is corrected and sent again; the old PostLog row is set to void.

5.6 Transition to Employee Level (2026/6 closing)
Until 2026 Q2 the provision was booked on a pooled element (el6 E6188). In the 2026/6 closing (documents posted in October 2026) the balance of the pool was reclassified once to the employees (Dr / Cr 27527, description RP-RECLASS, ExtRef2 RP202606-RC-<el1>), based on the target provision of each employee at 2026/6. The part up to the employee's year-end 2025 provision counts as prior-year layer, pro rata if the pool is insufficient. For Turkey and Slovakia the reclass was mirrored in LOC.
Residuals on the pool after the reclass (e.g. DE, ES, PL, TR, HQ/NL) were left on E6188 and are released to the P&L in the 2026/9 run under §5.2b. The LOC and FSM balances of the pool (HQ) were aligned in the 2026/9 run as well.

5.7 Element 5 (el5) per GL Account
Coda only accepts the el5 codes that are linked to the Group account of the line (link list oas_rllist, element 5; the same source as procedure AGz_El5Mapping). The default el5 of the entity code (taken from GL 27527) is used for GL 27527, 44125 and 43011 as long as it is allowed for that account or the account has no link rows. Otherwise the code that was most used in the latest quarter for that entity code, principle and account is used (allowed codes only), then the code of MAN, then the lowest allowed code. Examples (GL 44125 does not accept el5 0 in these entities):
ES | 44125 allowed 915, 916, 917, 918, 948 | used 915 | 27527 allowed 0, 915 | 43011 allowed 0
IT | 961 | 961 | 0, 486 | 0
PL | 900, 901 | 900 (LOC 901) | 0, 282 | 0
PT | 915, 916, 917, 918, 948 | 915 | 0, 915 | 0
UA | 920 | 920 | 0, 661 | 0
Other entities | Includes 0 (DE: 179 or 0; TR: 774 family; HU, GB, SK: 0) | Default el5 of the entity code | 0 (TR 774, DE 179) | 0 (TR 774, DE 179)

6. Controls & Governance

6.1 Headcount Reconciliation
Group Finance reconciles the employee population in the provision model against the active headcount in Sympa each period. Movements (new joiners, leavers, contract changes) must be reflected in the calculation before the provision entry is posted.
6.2 Calculation Sign-off
The quarter-end run follows these steps:
Preview: dbo.AGz_RedundancyProvision_v4 (@commit = 0) and dbo.AGz_RedundancyProvision_CodaXml are run under the service account that has access to the Sympa salary data. Nothing is booked or stored.
Review: Group Finance reviews the employee detail, the movement bridge per entity, the booked 27527 bridge, the layer check (LOC / FSM), the journal lines and the balance checks (every principle 0.00 in home and in EUR), and confirms exceptions with local HR.
Freeze: after approval the run is repeated with @commit = 1: the calculation is frozen as final snapshot and the documents are registered in the PostLog as generated. A quarter that already has documents in the PostLog is not generated twice.
Delivery: the XML files are exported per document, copied to the pick-up folder (§5.5) and followed up until they are posted in Coda.
6.3 Currency
Provisions are calculated in the home currency of the legal entity and posted in that currency, with the EUR amount at the closing rate as dual value (§5.5). Salaries contracted in another currency are converted at the closing rate (FX driver in the bridge). The retranslation of the opening provision is shown separately as translation difference in EUR. For currencies subject to significant depreciation, the real-terms obligation is assessed to determine whether an additional adjustment is warranted.
6.4 Release Restriction
The prior-year layer of the provision (§2) may never be released above the line: releases of that layer are booked through GL 43011 (below the line). Only amounts accrued in the current year may be reversed through GL 44125 (§5.2b). Severance payments are charged to the provision (§5.3), not to staff costs.
6.5 Movement Explanation (Bridge)
Each quarter the change in the target provision is explained per employee and per entity, versus the previous quarter end and versus the previous year end, with the following drivers:
New joiner: employee not in the previous calculation.
Leaver: employee no longer in the calculation or terminated at the quarter end.
Entity change: employee moved to another legal entity code (el1).
Service: higher multiplier from additional service at the previous salary.
Salary: change of the (capped) monthly salary at the new multiplier.
Ceiling: change of a statutory salary ceiling (Turkey).
FX: salary contracted in a currency other than the home currency.
Override: exclusion or adjustment added or removed (§4.1).
Other: remaining difference (e.g. missing salary data, rounding).
In EUR reporting the translation difference of the opening provision is shown as an additional driver. The booked side is reconciled as: booked balance previous quarter end + payroll payments + other postings + quarter-end booking = target provision.
6.6 Reconciliation after Posting
After the documents are posted, the GL 27527 balance (el3 MAN) of every employee equals the target provision; only differences of cents from rounding may remain. The residual on the pooled element is reported separately. Group Finance compares the balances of GL 27527 (period end) and of GL 44125 and 43011 (year to date) per entity and entity code between the previous and the current quarter end, and explains the movement with the bridge.

7. Open Items & Questions Requiring Resolution
1 | Turkey: load the SGK severance ceiling valid from 1 Jan 2027 in the calculation before the 2026/12 run (TRY 73,729.87 applies until 31 Dec 2026). | A. Gunduz / TR HR | Open
2 | Leavers during the quarter whose payment follows in the next quarter (e.g. leaver 15 Sep 2026, payment in October): decide whether the provision is kept until the payment instead of being released at the quarter end (§4.1, §5.3). | A. Gunduz / Group Finance | Open
3 | Hungary and Ukraine: postings on the pooled element after 2026/6 (HU 7.9 million HUF, UA -0.65 million UAH) were released in 2026/9; local Finance to confirm their nature. | HU / UA Finance | Open
4 | Germany: salary drop of employee E5878 in Sympa to be confirmed. AA: employee E5998 has no salary in Sympa and is not provisioned. | DE HR / AA HR | Open
5 | Denmark: validate the multiplier against the Salaried Employees Act (1 / 2 / 3 months after 12 / 15 / 18 years). | A. Gunduz / DK HR | Open
6 | Payroll instruction per country: severance payments debited to GL 27527 with el6 = employee in el3 MAN (§5.3). | Local Finance / Payroll | Open
7 | Fluxygen channel: the files are copied to the pick-up folder by Group Finance with a service account; fully automatic transfer to be built. | Group Finance / IT | Open
8 | The same person with two employee numbers (Spain E5098 / E6512): HR to avoid duplicate numbers; the booking on the unused number is treated as an error and released in the quarter-end run. | HR / Group Finance | Open
9 | Layer map agreed per entity (§5.4), including Turkey (LOC reversed, FSM not touched) and FR / SK (LOC and FSM reversed). | A. Gunduz / Group Finance | Closed
10 | Document code JV-REDUND created in Coda; ExtRef2 / ExtRef3, currency and el5 mapping proven by the postings of 2026/6 and 2026/9. | Coda administration | Closed
11 | Transition of the pooled element E6188 to the employees posted (2026/6, §5.6). | Group Finance | Closed

8. Version History
1.0 | April 2026 | A. Gunduz | Initial Draft
1.2 | Sep 2026 | A. Gunduz | Employee-level provision (el6), booking against the booked 27527 balance, payroll payment treatment, el3 layer map, Coda intray posting, movement bridge, IT methodology, exclusions, transition of pool E6188, procedure v4.
1.2 | Oct 2026 | A. Gunduz | Revised for the 2026/12 close: prior-year layer = calculated year-end provision (§2, §5.2b, §6.4); one Coda document per entity code, home currency with EUR dual value, ExtRef2 per entity code, posting monitoring (§5.5); layer map FR / SK / TR (§5.4); el5 mapping per GL account (§5.7); transition executed in 2026/6 (§5.6); exclusions for GB asset locations and closed entities (§4.1); TR ceiling from 1 Jul 2026 (§4); run steps and reconciliation (§6.2, §6.6); updated open items.
