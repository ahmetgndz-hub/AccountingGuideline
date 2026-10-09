# Batch D — other guideline threads (inventory)

Source: Outlook, fetched 2026-10-09 via the Microsoft 365 connector (read-only). Ids in `MANIFEST.md`,
converted files in `sources/emails/`. None of these are monthly closing instructions, so
Deadline / Period / Timetable are "n/a" unless the mail itself sets a date.

Attachment texts extracted by the connector are saved next to the mail as `<stem>-attachment-1.md`
(three redundancy policy versions, the Budgeted RMA 2026 instruction PDF and the Budget 2027 macro
assumptions PDF). Binary workbooks (`Book3.xlsb`, `RMA Pack Version @20260728.xlsb`, the two Excel
annexes of the 2025-10-13 instructions) and the external EPC guidance PDF were not extracted.

## 2026-04-28_redundancy-calculation-methodology.md — Re: redundancy calculation methodology (Ahmet Gunduz, 2026-04-28)
Deadline: n/a | Period: n/a
Timetable: n/a
Attachment: Redundancy_Provision_Policy_v1.0.docx → 2026-04-28_redundancy-calculation-methodology-attachment-1.md
Rules:
- [redundancy-provision] (Ahmet, 2026-04-23) As of 23 Apr 2026 HQ has access to Sympa salary and benefits data via API; the redundancy calculation file is adjusted accordingly. Previously the calculation was based on the actual salary paid in the current month, which relied on correct element-code usage and ignored country differences (e.g. Italy 13th/14th month: monthly × 12 ≠ annual salary). Going forward the total contracted amount from Sympa divided by 12 is used.
- [redundancy-provision] (Steven Poelman, 2026-04-24, CEO view) notice pay / holiday allowance and vacation monies: Dr salary cost / Cr bank; severance and settlement payments: Dr redundancy provision / Cr bank.
- [redundancy-provision] (Steven Poelman) HQ will centrally book and maintain the build-up and release of the redundancy provisions; a release can never lead to a credit amount above the line.
- [redundancy-provision] Policy v1.0 (attachment): scope = all employees on permanent or fixed-term contracts with a statutory severance entitlement; calculated centrally by Group Finance with local HR; notice-period pay, holiday allowances and vacation monies are NOT covered (expensed through payroll).
- [redundancy-provision] Policy v1.0: Monthly Salary = Total Contracted Annual Compensation (Sympa) ÷ 12, effective Jan 2026 (definitions say "effective May 2026"); Sympa data refreshed each reporting period; local HR responsible for Sympa salary data.
- [redundancy-provision] Policy v1.0 country multipliers (months of contracted monthly salary): NL/HQ TotalInYears/3; DE TotalInYears/2; TR TotalInYears capped at TRY 64,948.77 per year of service; CH 0; IT 9; DK tiered 0/1/3 (<12 yrs pro-rata, ≥12 yrs 1 month, ≥15 yrs 3 months); GB age-weighted weekly salary × years, max 20 yrs, 1.5× cap applied to all (no birth-date data); UA 3; FR ≤10 yrs 1/4 per month, >10 yrs 1/3; ES 20 days/year capped at 12 months = Min(TotalYrs×20/30, 12); SK 0/1/2/3/4 months at <2 / 2–5 / 5–10 / 10–20 / 20+ yrs; HU 0–6 months at <3 / 3–5 / 5–10 / 10–15 / 15–20 / 20–25 / 25+ yrs; PL 1/2/3 months at <2 / 2–8 / >8 yrs; PT three legislative periods (pre-Nov 2012 30 days/yr; Nov 2012–Apr 2023 18 days/yr first 3 yrs then 12 days/yr; May 2023 onwards 14 days/yr), aggregate capped at 12 months.
- [redundancy-provision] Policy v1.0 overrides: PT cap SeveranceMultiplier at 12; DELIVE FTE ≤ 0.22 (mini-job) → 0; PLLIVE employee ID 5588 → 0 (management contract); PL interns EmpIDs 6382, 6598, 6599 → 0 from period 202509.
- [redundancy-provision] Policy v1.0 accounts: provision GL 27527 "Accrual redundancy" (BE5 Provisions); expense GL 44125 "Redundancy" (PQ8 Staff costs, above the line); below-the-line release GL 43011 "Redundancy provision" (PU Depreciation and bad debtors); bank GL 13311 (BB5).
- [redundancy-provision] Policy v1.0 journals: recognition / upward adjustment Dr 44125 / Cr 27527; payment equal to provision Dr 27527 / Cr 13311 (no P&L); payment above provision: shortfall Dr 44125; payment below provision or voluntary leaver: excess Dr 27527 / Cr 43011 (below the line). Downward adjustment above the line only allowed for non-EUR currencies where depreciation reduced the real-terms obligation.
- [redundancy-provision] Controls: headcount reconciled to Sympa each period; multiplier calculated by stored procedure dbo.AGz_RedundancyProvision_v2 (nl-amsterdm-164 / dm_finance), reviewed by Group Finance and confirmed with local HR before posting; non-EUR provisions retranslated at closing rate each period; a release may never result in a credit above the line.
Changes vs previous mail: first policy draft; replaces the payroll-element based salary basis.
Open points: Steven asks whether timing of employee movements (in/out) matches the provision calculation; policy open item 1: Turkey cap TRY 64,948.77 to be validated against quarterly FX rates; "effective Jan 2026" (§3) vs "effective May 2026" (§2) inconsistent inside the policy.

## 2026-05-05_redundancy-calculation-methodology-2.md — Re: redundancy calculation methodology (Ahmet Gunduz, 2026-05-05)
Deadline: n/a | Period: n/a
Timetable: n/a
Attachment: Redundancy_Provision_Policy_v1_1.docx (still labelled 1.0 inside) → 2026-05-05_redundancy-calculation-methodology-2-attachment-1.md
Rules:
- [redundancy-provision] All redundancy provision movements are booked centrally by Group Finance; local entities do not post provision entries independently. Countries are only required to process actual severance payments: Dr GL 27527 / Cr GL 13311.
- [redundancy-provision] Provisions are not tracked at individual employee level.
- [redundancy-provision] Quarter-end movements posted by HQ: increase Dr 44125 / Cr 27527; release (employees left) split by vintage — amounts accrued in the current year released through GL 44125 (above the line), amounts carried forward from prior years released through GL 43011 (below the line).
Changes vs previous mail: §5 rewritten — country bookings reduced to the cash payment; the v1.0 alternative journal examples (payment above/below provision, voluntary leaver) removed; vintage split 44125/43011 introduced. Sections 1–4, 6–7 unchanged.
Open points: Turkey cap (open item 1) still open; "Reviewed by" still blank.

## 2026-07-14_redundancy-provision-booking-2026q2.md — redundancy provision booking 2026Q2 (Ahmet Gunduz, 2026-07-14)
Deadline: n/a | Period: 2026/06 (Q2 books)
Timetable: n/a
Attachment: Redundancy_Provision_Policy_v1_1.docx (v1.1) → 2026-07-14_redundancy-provision-booking-2026q2-attachment-1.md
Rules:
- [redundancy-provision] Multi Germany (Harold van Riel / Olcay Demirci, cc Sudipta Dash) asked to book the 2026 Q2 redundancy provisions, amounts in EUR: DELIVE / DES001 623,985.38; DELIVE / DES005 182,441.58.
- [redundancy-provision] Policy v1.1 §5.3 — severance payments by countries in three steps so that the gross (pre-tax) amount is cleared from 27527: (a) payroll entry gross: Dr 44125 / Cr 27523 wage tax payable / Cr 27515 salaries payable; (b) net payment: Dr 27515 / Cr 13311; (c) provision release at gross: Dr 27527 / Cr 44125.
- [redundancy-provision] Policy v1.1 §5.4/5.5 — quarter-end increase Dr 44125 / Cr 27527 booked centrally; quarter-end release current year Dr 27527 / Cr 44125, prior years Dr 27527 / Cr 43011; no country-level provision postings; no employee-level bookings.
- [redundancy-provision] Policy v1.1 version note: centralised all provision bookings (HQ only); countries limited to severance payment entry; quarter-end increases via 44125; releases split by vintage; provision not tracked at employee level.
Changes vs previous mail: v1.1 replaces the single-step country payment (Dr 27527 / Cr 13311) of the 2026-05-05 file with the three-step gross method via payroll (44125 → 27515/27523 → 13311, then 27527 → 44125). This is the version the countries were given. Note: this mail asks Germany to book the provision itself although the policy says HQ books centrally — the JV-REDUND upload (2026-10-01) later moves this to an HQ upload.
Open points: whether the provision is posted by the country (as asked here) or by HQ (as the policy says) — resolved later by policy v1.2 / JV-REDUND.

## 2026-07-27_iso-20022-structured-addresses.md — ISO 20022 Structured Address Requirements – Required Review of Supplier and Debtor Master Data (Ahmet Gunduz, 2026-07-27)
Deadline: 14 November 2026 (regulatory) | Period: n/a
Timetable: n/a
Rules:
- [bank-cash] By 14 November 2026 SWIFT and major market infrastructures will no longer accept fully unstructured postal addresses in cross-border and high-value payment messages; addresses must be fully structured or hybrid.
- [bank-cash] Fully structured = all components (street, building number, postal code, city, country) in dedicated fields; hybrid = at least Town/City and Country Code in structured fields plus limited free-text lines; fully unstructured (free text only) not accepted after 14 Nov 2026.
- [coda-elements] All countries must review and clean supplier and debtor master data in CODA. Minimum per record: Country completed (mandatory field in CODA, dropdown only); City/Town reviewed and corrected; other address elements completed and structured whenever possible.
- [bank-cash] Review and cleansing to be coordinated as soon as possible, before the deadline. Reference: EPC153-22 v2.0 guidance document (attached, not extracted).
Changes vs previous mail: n/a (new topic).
Open points: none.

## 2026-07-28_rma-report-format-macabacus.md — RMA format with usage Macabacus (Ahmet Gunduz, 2026-07-28)
Deadline: n/a | Period: n/a
Timetable: n/a
Rules:
- [reports-available-budget] A standard RMA automation file for Macabacus is introduced; after country testing Sam Foster adds it to Macabacus, and going forward this format is used for RMA meeting presentations.
- [reports-available-budget] Phase 1 content of the pack: Profit and Loss Statement, Balance Sheet, Direct Cash Flow Statement.
- [reports-available-budget] Tabs to be added manually until phase 2: Details of Accounts Receivable (aging list); FTE overview by asset and by department (Actual vs Budget); NRI Waterfall from Budget FY to Forecast FY; Fee income details per asset and margin analysis.
- [reports-available-budget] Countries test the password-protected Excel ("RMA Pack Version @20260728.xlsb") and return findings and improvement requests.
Changes vs previous mail: n/a.
Open points: feedback was requested before 11 Aug 2026; phase 2 timing not given.

## 2026-08-27_instructions-budgeted-result-management-activities-2026.md — FW: Instructions Budgeted Result from Management Activities 2026 (Egbert van Zomeren 2025-10-13, forwarded by Ahmet Gunduz 2026-08-27)
Deadline: see timetable | Period: Budget 2026 (incl. Forecast Q4 2025)
Timetable: 13 Oct 2025 — instruction Budget 2026 to countries; 24 Oct 2025 — HQ shares assumptions on inflation, FX, GDP, CAF and Genex recharges; 14 Nov 2025 — country submits Draft Budget 2026 incl. Salary file and Bonus proposal; 17–28 Nov 2025 — comments/questions and Board meetings with MD/FDs; 5 Dec 2025 — Final Budget 2026 based on approved Salaries 2026; 9 Dec 2025 — consolidated budget review meeting Board; 12 Dec 2025 — final consolidated and country budgets
Attachment: 2025-10-13 Instructions Budgeted RMA 2026.pdf → 2026-08-27_instructions-budgeted-result-management-activities-2026-attachment-1.md (Annex 1 / Annex 2 xlsx not extracted)
Rules:
- [budget-instructions] Preparation principle: budgeted fee income of the Service Companies is based on the budget of the underlying real estate portfolio managed by Multi; fee income based on 2026 NOI, service charges, capex, collections etc. as agreed with the Property Owner; only include new business to the extent signed; do not anticipate asset disposals unless the Owner provided exclusivity; outline (re)letting fee assumptions (frictional vacancy, vacancy management, structural vacancy).
- [budget-instructions] Present in local currency with an estimate of the EUR FX rate per quarter; HQ provides official CPI per country and CAF assumptions per quarter; budgeted redundancy cost is provided by HQ.
- [fee-income-recharges] Staff and Genex recharges must be reconciled within the group before final submission (HQ coordinates); use the IC Charges File per country; HQ signals when cross-country charges are final.
- [budget-instructions] Gross margin per asset = Fee income −/− Staff cost direct employees −/− Indirect staff and Genex; indirect staff and Genex allocated to mandates on the average of % of leases and % of fee income (example in Annex 1).
- [coda-elements] Level of detail: fee income at asset (el2), fee type (el4), fee description (el5) and client (el6); staff costs at SCOA level (el4) only, not per employee; Genex upload at SCOA (el4) with counterparty (el6). Use the attached RMA presentation format, not prior versions.
- [salary-bookkeeping] Staff cost budget is a separate process between MDs and the Multi Board; Salaries 2026 and Bonuses 2025 proposed to the Board must match the submitted budget; FTE overview split direct/indirect per year-end 2025 and 2026; new hires only with Board approval unless approved and paid by the 3rd-party Owner; assume staff recharges to assets whenever the management contract permits.
- [fee-income-recharges] Annex 1 allocation notes: time charges between countries (employee of country A working for country B) are part of staff costs; Genex contracted locally on the respective cost line, HQ recharges (Coda/Horizon/BO licences) on "Costs recharged from/to group companies"; HQ time charges to countries only to the extent not already charged.
- [coda-elements] Annex 2 upload sheet coding examples (el1 NLS001, el3 MAN): 45811 AM fee (el5 444), 45821 PM fee (445), 45831 statutory services (446), 45881 (re)development fee (784), 44129 employee recharges (437), 44700 other recharges; staff cost SCOAs 44111 salaries, 44124 bonuses, 44115 pension, 44125 redundancy, 44180 external personnel, 44200 time charges between countries, 44250 car/other staff, 44130 travel; Genex 44311 office, 44720 IT, 44110 contributions/insurance, 44981 advisors, 44450 marketing, 45825 external management, 44900 cost recharged from/to group companies, 44589 other general; el5/el6 "not needed" for staff and Genex lines; pink part = Forecast'25, blue = Budget'26.
Changes vs previous mail: n/a (previous cycle; superseded by the Budget 2027 instructions of 2026-09-10).
Open points: none; kept as reference for the Budget 2026 cycle and SCOA coding examples.

## 2026-09-10_budget-2027-instructions-and-guidelines.md — Budget 2027 - Instructions and Guidelines (Ahmet Gunduz, 2026-09-10)
Deadline: see 2026-09-22 clarification (accounting close 16 Oct 2026, RMA budget presentations two weeks later) | Period: Budget 2027
Timetable: n/a in this mail
Rules:
- [budget-instructions] Applies to all countries and all entities in scope and replaces any guidance from previous budget cycles. Part A = Service Companies (entities employing staff and managing assets for Property Owners); Part B = Owned Assets (assets owned or partly owned by Multi in Ukraine, Italy and the Netherlands, full shopping-centre budget required, partly owned assets on a 100% basis); Part C = all entities.
- [budget-instructions] Three points for every submission: use the attached RMA Presentation template only (prior-year versions rejected); submit in both EUR and local currency as two separate uploads with identical coding; respect the minimum Coda coding levels of section 11 (aggregated uploads rejected).
- [budget-instructions] Reporting periods in every submission: Actuals 2025 full year; Budget 2026 full year as approved; Forecast 2026 Q4 only (Q1–Q3 2026 actuals not repeated); Budget 2027 by quarter (Annex 1).
- [budget-instructions] Currency/FX: all figures in local currency; estimate of the quarterly EUR exchange rates for 2027; corresponding EUR figures as an annex. HQ parameters: official country CPI (inflation), country-specific quarterly CAF, redundancy cost assumptions calculated centrally by HQ (§3.3).
- [fee-income-recharges] Part A §2.1 basis of preparation: fee income derived directly from the approved budget of the underlying portfolio actively managed by Multi, strictly faithful to the signed management agreements; each fee at its contractual definition, rate, calculation base, cap/floor and billing frequency; simplified, blended or rule-of-thumb assumptions not acceptable; drivers (NOI, rental income, service charges, collections, capex/project spend, leasing transactions) must be identical to the approved asset budget so fee income and the asset's fee expense reconcile.
- [fee-income-recharges] §2.2 fees budgeted at individual fee type = el4 + el5 combination; mandatory upload level for fee income el1 + el2 (asset) + el4 + el5; submissions missing a dimension or aggregated are rejected.
- [fee-income-recharges] §2.3 reporting categories (automatic, no country action): PP1 Asset Management Fee Income; PP2 Property Management Fee Income; PP3 Statutory Services Fee Income; PP4 (Re-)Development Fee Income; PP5 Salary and Employee Recharges; PP6 Other Recharges; PP7 Fund Management Fees.
- [budget-instructions] §2.4 new business only where agreements are formally signed; do not anticipate asset disposals unless the Owner granted exclusivity. §2.5 outline leasing/re-letting fee assumptions: frictional vacancy, active vacancy management, structural vacancy.
- [salary-bookkeeping] §3.1 staff cost budgeting is managed separately between Country MDs and the Multi Board; salaries and bonuses proposed to the Board must exactly match the budget submission; submit salary levels as they are plus CPI, subject to change. §3.2 FTE schedule split direct/indirect for Actual Q3 2026, year-end 2026 (forecast), year-end 2027 (budget). §3.3 new hires only if Board-approved or pre-approved and funded by a third-party Owner; redundancy costs provided by HQ. §3.4 staff cost recharges aligned with management contracts and submitted to the counter country wherever permitted.
- [intercompany] §3.5 use the IC Charges file previously circulated; HQ confirms when cross-country charges are final; all budgeted staff and Genex recharges fully reconciled within the group before final submission, coordinated by HQ.
- [budget-instructions] §4 Gross Margin = Fee Income − Direct Staff Costs − Allocated Indirect Staff Costs and Genex; indirect staff and Genex allocated to mandates with the standard key based on average lease count relative to total portfolio leases (margin model slide).
- [revenue-structure] Part B §5.1 rental income at tenant and unit level from the contracted rent roll; re-assess annual ERV per unit (total ideally up with CPI); indexation per lease clause using HQ CPI; turnover rent budgeted separately from projected tenant sales. §5.2 reflect 2027 expiries and break options with renewal probability, ERV and downtime; incentives (rent-free, temporary discounts, fit-out contributions) separately with assumptions; vacancy assumptions consistent with Part A.
- [service-marketing-charges] §6.1 detailed service charge budget per asset, recoverable income vs recoverable costs; owner's share separately (void/vacancy costs, caps, leakage) with assumed recovery rate per asset. §6.2 other income separately: parking; specialty leasing and mall income; media/advertising; other with description.
- [budget-instructions] §7 opex at asset level consistent with the asset business plan and service charge budget; split recoverable vs non-recoverable; categories separately (property taxes and insurance, utilities, repairs and maintenance, marketing and promotion, property and asset management fees, letting and legal, bad debt provisions); HQ CPI for indexation, deviations documented; management fees charged to the asset reconcile with Part A fee income.
- [capex] §8 capex at project level with description, total cost and 2027 phasing by quarter; split maintenance / development and improvement / leasing capex (tenant incentives, fit-out); status committed / approved / proposed and expected income impact; phasing consistent with the cash reconciliation (§10).
- [taxes] Part C §9 budget current tax on the projected taxable result at the applicable CIT rate; bridge from accounting result to taxable result (permanent and temporary differences: non-deductible expenses, tax depreciation, provisions); utilisation of tax losses carried forward; cash tax payments by quarter (advance payments and settlements).
- [below-nri-cashflow] §10 cash reconciliation Cash BoP → Cash EoP by quarter per entity: BoP = year-end 2026 forecast balance; net result per budgeted P&L; working capital movements (receivables, payables, accruals, intercompany) with commentary; cash taxes paid (link §9); capex and other investments (link §8); other items (FX, non-cash) explained; EoP = closing balance. Checks: BoP agrees to YE 2026 forecast; quarterly EoP ties to the budget balance sheet.
- [coda-elements] §11 general rule: lines not listed may be uploaded at el1 + el4; EUR and local currency uploaded as separate submissions with identical coding. Forecasting file = build-up level; Coda upload = minimum coding, the level reported and compared to actuals.
- [coda-elements] §11.1 Service Companies minimum Coda upload coding: fee income PP1–PP4, PP6 → el1 + el2 (asset) + el4 + el5; salary/employee recharges PP5 → el1 + el2 + el4 + el6 (intercompany); staff costs PQ1, PQ2, PQ3, PQ7, PQ8, PQ10, PQ11 → el1 + el2 + el4 (SCOA only, no employee level); time charges between countries PQ12 → + el6; general costs PR1–PR13 → el1 + el2 + el4 + el5; cost recharged from/to group companies PR14 → + el6; non-recurring PT → el1 + el2 + el4 + el5 per item with explanation; accrual releases and depreciation PU → el1 + el2 + el4; time charges from/to HQ PW, PWe (PWe = non-consolidated entities) → + el6; financial income/expenses PV → el1 + el2 + el4; corporate income tax PX → el1 + el2 + el4, current and deferred separately; working capital and cash movements (balance sheet) → el1 + el2 + el4 + el5.
- [coda-elements] §11.2 Owned Assets: rental income PA, PB → el1 + el2 + el4 + el6 (tenant); vacancy, discounts, rent free PC1, PC2T, PC2B → + el6 (tenant); other rent PD1, PD2, PD3T → + el6 where attributable; service and marketing charge income PE1, PE2 → el1 + el2 + el4; service/marketing charge costs PF1–PF16 → + el5; opex PG1–PG4X → + el5; capex → el1 + el2 + el4 + el5 + Capex ID (linked to the Hub); CIT PX → el1 + el2 + el4; balance sheet → el1 + el2 + el4 + el5. Partly owned assets on a 100% basis, same coding.
- [coda-elements] §11.3 specific: fee income lines need el2, el4 and el5, the el4 + el5 combination must be unique, no counterparty code on fee lines; staff costs per employee only in the country's own file, Coda upload at el4 only; Genex at el4 with el5; all intercompany (PP5, PQ12, PR14, PW, PWe) carry the counterparty in el6 and must agree with the central IC Charges workbook; asset income tenant/unit level in the forecasting file, upload at el4 + el2 (+ el6 where attributable to a tenant); asset opex/service charges at el2 + el4 + el5 (el5 needed for the recoverable / non-recoverable split); capex per project with Capex ID; CIT current and deferred coded separately for P&L and balance sheet; cash lines at el1 + el2 + el4 + el5.
Changes vs previous mail: replaces the Budget 2026 instructions (2025-10-13): adds Part B owned assets (UA, IT, NL), Part C tax and cash reconciliation, the full coding matrix per BO code, Forecast 2026 = Q4 only, FTE schedule incl. Actual Q3 2026, allocation key now lease count only (2026 cycle: average of % leases and % fee income), fee income upload without el6 (2026 cycle required client el6).
Open points: template "will be shared shortly"; no timetable in the mail itself (see 2026-09-22); deadlines for draft/final submission not stated.

## 2026-09-21_redundancy-provision-as-per-2026-06.md — redundancy provision as per 2026/6 (Ahmet Gunduz, 2026-09-21)
Deadline: n/a | Period: 2026/06
Timetable: n/a
Rules:
- [redundancy-provision] No text; the 2026/6 redundancy provision calculation (Book3.xlsb) was shared with Sudipta Dash on 2026-09-21. Converter output is empty by nature (empty body), not a conversion failure.
Changes vs previous mail: n/a.
Open points: workbook content not available (binary); the 2026/6 run is the methodology reference cited by policy v1.2.

## 2026-09-22_budget-2027-clarification-q3-close.md — Re: Budget 2027 - Instructions and Guidelines (Ahmet Gunduz, 2026-09-22; includes his reply of 2026-09-11)
Deadline: accounting close 16 October 2026 | Period: 2026/09 (Q3) / Budget 2027
Timetable: 16 Oct 2026 — accounting close 2026 Q3 (budget cycle is part of the Q3 close); +2 weeks (≈ end Oct 2026) — countries present their 2027 budgets at the RMA meeting, scheduled by Gerdien; by ≈ 2 Oct 2026 ("end of next week" from 22 Sep) — RMA presentation template circulated
Attachment: Budget_2027_Macro_Assumptions_Instruction_v1.1.pdf → 2026-09-22_budget-2027-clarification-q3-close-attachment-1.md (see that file for the macro assumptions)
Rules:
- [budget-instructions] (2026-09-11) The budget cycle forms part of the 2026 Q3 close; accounting close on 16 October; two weeks after, countries present their 2027 budgets at the RMA meeting (scheduled by Gerdien).
- [budget-instructions] (2026-09-22) Macro assumptions (CPI, FX, CAF etc.) are issued by HQ in the attached PDF; the presentation template follows by the end of the following week.
- [budget-instructions] Macro PDF §1: mandatory, Board-approved and frozen inflation and FX assumptions for Q4 2026 forecast and FY 2027, data cut-off 14 Sep 2026; apply to both the local-currency and EUR versions; apply the rates exactly as stated and confirm this in the budget narrative; only official sources (ECB, EC, IMF, OECD, national central banks).
- [budget-instructions] Macro PDF §2 inflation, FY 2027 average (Q4 2026 / Q1–Q4 2027 in the attachment): Euro area 2,5%; NL 2,5%; DE 2,7%; FR 1,8%; IT 1,8%; ES 2,5%; PT 2,3%; BE 2,6%; IE 2,6%; SK 3,2%; DK 1,9%; UK 2,5%; CH 0,6%; PL 2,8%; HU 3,0%; TR 24,0% (FY 2026 year-end 28,4%); UA 8,0% (FY 2026 year-end 10,0%). FY 2027 average is the rate for non-contracted cost lines; HICP for EU states and Denmark, national CPI elsewhere.
- [currency-revaluation] Macro PDF §3 FX per EUR 1, FY 2027 average / 31 Dec 2026 / 31 Dec 2027: USD 1,16 / 1,16 / 1,16; DKK 7,46 throughout; GBP 0,87 / 0,86 / 0,87; CHF 0,93 / 0,94 / 0,92; PLN 4,38 / 4,35 / 4,40; HUF 375,00 / 370,00 / 380,00; TRY 65,00 / 60,00 / 70,00; UAH 56,00 / 53,00 / 58,00 (quarterly averages in the attachment; EUR/TRY = USD/TRY × 1,16, EUR/UAH = USD/UAH × 1,16; DKK = ERM II central rate).
- [budget-instructions] Macro PDF §4: do not substitute local forecasts — budget at the Group rate and list any quantified alternative as an item requiring management decision; keep all rates in one "Assumptions" sheet. FX translation: Q4 2026 forecast P&L and cash flow at the Q4 2026 average rate; FY 2027 P&L and cash flow at quarterly average rates (or FY 2027 average if the model is annual); balance sheet and Cash BoP→EoP reconciliation at the 31 Dec 2026 and 31 Dec 2027 closing rates.
- [erv-vacancy] Macro PDF §4 rent indexation and index-linked fees: apply the contractual index, reference month and indexation date with actual published index values; most 2027 indexation references 2026 index values, so the effective eurozone rate is about the FY 2026 figure (~3%; FR 2,4% to SK 4,3%) — do not apply the 2027 rate to 2027 indexation; reflect caps, collars and waivers at tenant/unit level.
Changes vs previous mail: adds the timing (Q3 close 16 Oct, RMA +2 weeks) and the macro assumptions missing from the 2026-09-10 instruction.
Open points: exact RMA meeting date and draft/final submission dates not given; the macro PDF is labelled v1.0 inside while the file is named v1.1.

## 2026-09-25_redundancy-reserve-scope.md — Re: Redundancy reserve (Ahmet Gunduz, 2026-09-25)
Deadline: n/a | Period: n/a
Timetable: n/a
Rules:
- [redundancy-provision] The redundancy provision is explicitly for the redundancy (severance) payment only. A termination penalty of three months' pay for not working, as well as garden leave / paid notice period, is not part of the redundancy calculation and may not be booked out of the redundancy reserve (Harold van Riel's proposal to charge the three-month notice period to the reserve was declined).
Changes vs previous mail: confirms policy §1 (notice-period pay excluded) for a concrete German case.
Open points: none.

## 2026-09-28_cleaning-balance-matching.md — Re: Cleaning balance matching (Ahmet Gunduz, 2026-09-28)
Deadline: n/a | Period: n/a
Timetable: n/a
Rules:
- [control-file] A write-off matching of old unknown balances dating from the previous manager's time (Multi Germany, request by Izzet Ensoy, cc Nicola Baumann) was excluded from the control file by HQ on request ("Done"). Exclusions from the control file are made by HQ (Ahmet) on a documented request from the country FD.
- [writing-off-receivables] Such historical clean-up write-offs are done via matching and should not keep being flagged as findings.
Changes vs previous mail: n/a.
Open points: the list of excluded items was a screenshot (not in the text); no criteria stated for when an exclusion is granted.

## 2026-10-01_jv-redund-document-code-created.md — Re: [RE-535680] new document code for redundancy provision (Servicedesk / Rob Uytdewillegen, 2026-10-01)
Deadline: n/a | Period: n/a
Timetable: n/a
Rules:
- [document-codes] New Coda document code JV-REDUND exists (created 2026-10-01 on Ahmet Gunduz's request RE-535680) for redundancy provision bookings; to be used only via upload; no workflow (no approval wf) attached.
- [redundancy-provision] Redundancy provision journals are posted by HQ through an upload under JV-REDUND, consistent with the centralised booking in policy v1.1/v1.2.
Changes vs previous mail: formalises the HQ upload channel for the provision; replaces the ad-hoc request to the country (2026-07-14).
Open points: none.

## 2026-10-05_e-code-usage-not-in-line-with-sympa.md — e code usage not in line with Sympa (Ahmet Gunduz, 2026-10-05)
Deadline: n/a | Period: n/a
Timetable: n/a
Rules:
- [coda-elements] The employee element codes (E-codes in el6) used in Coda salary bookings must correspond to the actual employee id defined in Sympa; Spain (Erdem Dilber, Roksolana Shumylo, cc Tiemo Kroontje) was asked to correct its Coda bookings to align with the Sympa employee ids.
- [salary-bookkeeping] Because the redundancy provision and headcount reconciliation are driven by Sympa data (policy §3, §6.1), a mismatch between the Coda E-code and the Sympa id breaks the link between payroll bookings and the provision model.
Changes vs previous mail: n/a.
Open points: the two screenshots with the concrete mismatches are not in the text; the mapping rule (E + Sympa id?) is implied, not spelled out.

## 2026-10-05_control-file-booking-in-the-intray.md — Re: Control file - Booking in the Intray (Ahmet Gunduz, 2026-10-05)
Deadline: n/a | Period: n/a
Timetable: n/a
Rules:
- [control-file] A control-file finding can originate from an HQ booking sitting in the Coda Intray (unposted); in this case the booking was Ahmet's and he posted it the same day. Countries should ask HQ before acting on Intray items they did not create.
Changes vs previous mail: n/a.
Open points: the booking itself was a screenshot; no general rule on Intray hygiene stated.

## 2026-10-07_ic-receivables-to-ic-loan-after-45-days.md — Re: [RE-535943] Coda: Intercompany Receivables – Automatic Transfer to Intercompany Loan After 45 Days (Ahmet Gunduz, 2026-10-07)
Deadline: n/a | Period: n/a
Timetable: n/a
Rules:
- [approvals-segregation] (Ahmet to Rob Uytdewillegen, 2026-10-07) No essential changes to the system (Coda set-up, allocations, document codes — not only control-file content) may be made without first discussing them with Ahmet, regardless of who asked for it.
- [intercompany] NOT A RULE YET — proposal by Marcel Brouwer / Steven Poelman (Servicedesk ticket RE-535943): automatic allocation transferring outstanding IC invoices to IC loan when current date = invoice date + 45 days; scope el1 = service companies in all Coda companies with el6 = RHQH001 + RHQH005, and el1 = HQH001 + HQH005 with el6 = a service company in any country; SCOA 13130 and 27210 to be transferred to 13564; pay status at 27210 "held" or "available" only ("proposed" = in payment process, not transferred); only SI + PI documents, banks and JVs excluded (those should have been matched); new document code JV-ICALLOC.
- [document-codes] JV-ICALLOC was announced by Servicedesk for this process but the process is on hold.
Changes vs previous mail: n/a.
Open points: Ahmet put the automation on hold ("Please not do that yet. First lets discuss") — whether/when the 45-day IC receivable → IC loan (13130 / 27210 → 13564) transfer and JV-ICALLOC go live is undecided; impact of JV-ICALLOC on the control file unknown.
