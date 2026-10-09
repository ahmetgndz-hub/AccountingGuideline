# Batch E — SharePoint Wiki files not in the Paginas zip

Fetched 2026-10-09 via the Microsoft 365 connector (read-only). Site
`https://multieu.sharepoint.com/sites/Wiki` (siteId `e1156cb8-48f2-486f-8a2f-18ecacb816fa`).
The `PublishingImages` library is the drive titled "Afbeeldingen"
(`b!uGwV4fJIb0iKLxjsrLgW-hdyzmeXg6pEmm08m8LsaBOKaOtbYr_MT6Zff4U0uER8`); its
`Paginas/` folder holds one sub-folder per old Wiki page (Accounting Manual,
Newsletters, Closing check list, Booking Structure, Discounts, ...). All four
files were fetched; raw text is in `sources/wiki/attachments/`.

## 1. ifrs16-office-and-car-leases-2021.md

- **File:** `PublishingImages/Paginas/Accounting Manual/20210408 IFRS 16 Accounting for Office and Car Leases_for Accounting Manual.pdf`
- **What:** 4-page memo "Accounting Treatment of Leases under IFRS 16", PDF of Word doc "..._v2". Attached to the Accounting Manual page.
- **Date:** V 08-04-2021 (modified 2021-04-08). **Author:** none shown (HQ Group Financial Control).
- **Rules:**
  - Scope at Multi: office rent, car leases, office equipment leases (copiers/printers).
  - On commencement recognise a right-of-use asset and a lease liability; ROU asset = lease liability + initial direct costs, adjusted for incentives, pre-payments and restoration obligations; measured at cost less depreciation and impairment.
  - Lease liability = NPV of lease payments over the lease term, discounted at the rate implicit in the lease, else the incremental borrowing rate.
  - Index-/rate-based variable payments go into the liability at commencement-date values; other variable payments hit P&L when triggered. Remeasure on changes in term or purchase-option assessment (revised rate) and in residual value guarantees or index (unchanged rate).
  - Lease term = non-cancellable period plus reasonably-certain extension / non-exercised termination periods.
  - Exemptions: leases ≤ 12 months without purchase option (per asset class) and low-value assets (per lease) may be expensed straight-line.
  - **Multi policy choices:** no detailed split of non-lease (service) components; term = contract term (no extension/purchase options assumed; no estimate for early termination on employee leaving); ROU asset = total contract value depreciated over the contract; lease liability = remaining contract value.
  - Disclosure: movements of lease asset and liability in the PP&E movement schedule; Lease Arrangements note with opening/closing carrying value, depreciation, lease payments and interest charge.
- **Guideline page:** `ifrs-memos`.

## 2. newsletter-2019-11-06-accruals-and-provisions.md

- **File:** `PublishingImages/Paginas/Newsletters/06-11-2019 how to book accruals and provisions in coda.pdf`
- **What:** PDF of the e-mail "FW: how to book accruals and provisions in Coda" to all country accounting leads; nine DO/DON'T rules that supplement the Wiki `accruals` page.
- **Date:** 6 November 2019. **Author:** Ahmet Gündüz, Director Finance and Accounting. (SharePoint modified date not retrievable — search index has no entry.)
- **Rules:**
  - DO always specify the proper **element6** (counterparty) on accruals.
  - DON'T use **dummy** codes on the accrual account or counter-posting line, except for service & marketing charge reconciliation stemming from more than 10 tenants.
  - DO book accruals with the automatic reversal journal, document code **JV-REVERSAL** (avoids forgotten reversals, manual follow-up, and PO available-budget overrun).
  - DO use **one document code per accrual**.
  - DO write a clear line description (speeds workflow approval).
  - DON'T attach Excel calculation sheets to the journal; attach a PDF with a clear explanation.
  - DON'T aggregate: one cost line = one accrual line (needed for automatic movement and follow-up).
  - DON'T close accruals with incoming/outgoing invoices (blurs follow-up and distorts cash-flow reporting).
  - DO use the **lease reference** on accruals so tenant costs/discounts enter the OCR calculation.
- **Guideline page:** `newsletter-archive` (rules also feed the accruals section of `booking-structure`).

## 3. closing-checklist-2020.md

- **File:** `Documents/Closing checklist.xlsx` (drive `b!...BPZ2ZhROUF2RYeauZVpv_ir`, item `01BLB362B52ODCYU557NAIG7OGRFPVBB2H`)
- **What:** one-sheet checklist, 37 confirmation points with entity type (All / Prop.Co. / Man.Co.) and the BO reporting group(s) involved. Newer versions V2 (2020-06-30), V2.1 (2020-07-08) and V2.2 (2020-07-15, uploaded by Ahmet) exist on the same site and should be compared before the page is finalised.
- **Date:** modified 2020-03-10. **Author:** not visible.
- **Rules (with BO groups):**
  - Bank: all statements booked and reconciled, all mutations via Crescendo, accounts classified by content (BB5); no pending statements in the Crescendo portal.
  - Bad debt per group policy and write-off analysis/proposal to HQ Group FD (BB2, PG1); tenant guarantees up to date (BB2, BE7).
  - Investment property value updated per book: MAN = Blackstone valuation, FSM = Multi internal valuation, UST = BX purchase price (BA2, PK1); capex recorded with proper capex id (BA2).
  - FX revaluation of monetary items, transaction→home and transaction→EUR.
  - ERV booked (PA, PB); vacancy booked and reconciled (PC1); lease discounts classified and recorded in Horizon (PC2, PC2A).
  - Period result transferred to equity in every book type MAN, LOC, FSM, FSE, UST (PZ, BC8); equity reconciles to trade registry and shareholder ledger (BC).
  - Suspense account zero in home and reporting value (`4Suspence`); dummy el6 accounts (`6DUMMY`) nil and unused.
  - Coda pay status (available/held/proposed/suppressed/paid after date) represents the balance — must for monetary items.
  - Loans IC and external classified short/long term with HQ cash team (BE1, BE2, BF1); interest accrual up to date (BF3, BF4, accounts **27401, 27402**; PI1, PI2).
  - System control: nothing pending in Coda intray, no WIP invoices in Invoice Matching; all invoices via Coda workflow, manual transactions signed by FD in hard copy, no denied or stuck workflow transactions.
  - IC accounts matched and reconciled with the related party.
  - GRI and service/marketing advances reconciled to prior 2 months and charged sqm vs GLA (PE1, PE2, PA–PC); net PE/PF balance shows only vacancy shortfall, cap shortfall and to-be-invoiced accrual (PE, PF).
  - Tax: el6 usage per instruction, period-end settlement to payable/deferred reconciled to the declaration (BF5, BA12); current tax for all SPVs, deferred tax only in FSM books for Multi-owned assets, none in MAN or UST (BF5, BA10, BE3, PX).
  - A/R confirmations: tenants in top 10% of sales (OCR) or balance > € 10k. A/P confirmations: suppliers in top 10% of cost (Genex, opex, capex, SC), negative balances, or > € 50k.
  - Accrue where service/goods received before period end and not yet invoiced; release unneeded prior-year accruals below the NRI line on account **43300**.
  - Bonus accrual YTD vs actual/budget (PQ2, BF3); fair value of financial instruments per HQ cash team.
  - Management fees on proper element2 with the 35% / 65% logic and IC vs third-party SCoA split (PP1–PP4, PF13, PF14, PG4D, PH5); non-recurring costs classified (PQ5, PR12).
  - Tenant monthly sales uploaded to Horizon for OCR; all turnover-rent invoices issued or accrued (PC2C, PD1); tax accounting in MAN agrees to the tax file.
- **Guideline page:** `closing-checklist`.

## 4. workflow-change-invoice-recording-2020.md

- **File:** `Documents/workflow change - check of invoice recording.pdf` (same drive, item `01BLB362HARRIYXQ63LBC24CPNVFGQDXYC`)
- **What:** PDF print (Dennis Pieterson, 26-02-2020) of Frank Trees' e-mail of 18-02-2020 announcing that the country head of accounting is added to the Coda invoice workflow.
- **Date:** 18 February 2020 (modified 2020-02-26). **Author:** Frank Trees (cc Ahmet Gunduz).
- **Rules:**
  - Journal vouchers were already approved by the country head of accounting; from the following week the same input check applies to **all invoices** entered by the country accounting team.
  - Minimum checks: document date within the reporting period; SCoA in line with the cost; VAT correctly reflected (reimbursable or not); counterparty correct; invoice amounts correct; description correct and in English; attachment correct.
  - Purpose: invoices recorded correctly the first time, in line with the Multi accounting manual, no inefficient corrections.
  - Names the head of accounting per country (IT, PL, PT, TR, DE, GB, IE, NL/BE, ES, HU, SK via CBRE, UA) as of Feb 2020.
- **Guideline page:** `approvals-segregation` (workflow roles) with a cross-reference from `booking-structure` (invoice content rules).
