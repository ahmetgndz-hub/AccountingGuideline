---
title: "Fee analysis"
source_file: "Fee analysis.aspx"
sharepoint: "https://multieu.sharepoint.com/sites/Wiki/Paginas/Fee analysis.aspx"
contact: "Ahmet Gunduz"
categories: ""
converted: 2026-10-08
status: old-wiki
---

# Fee analysis

#### Separate power query (location is NL-AMSTERDM-164\DM_FINANCE [dbo].[AGz_RMAAnalysis]) created to automate fee analysis reporting and below you can find definition per column and accounting instruction to reach this reporting. 

#### General remarks are;

#### - Analysis done on service company level (coding of el1 like __S% or for Turkey BS901 and BS009)

#### - Consist only for MAN books

#### - Consist of only one financial year which can be selected before run power query

| Report Column | Definition | Accounting instruction / description |
|---|---|---|
| cmpcode | company code of which fee charging service company belongs to. Only Italy has been separated in to two as Malls and MOMI as their RMA is evaluated separately too |  |
| Asset | Asset is real asset which used in bookkeeping to charge fee with using BO reporting codes PP1, PP2, PP3, PP4 and PP5. These codes searched at global asset id table and name and portfolio information grabbed from this table too. | BO reporting groups PP% should be always booked to real asset codes which has link at global asset id table. |
| Asset Name | for presenting asset name global asset id table used |  |
| Ownership | it maintained in reporting hub by HQ and shows ownership of asset (e.g. Union, CRI) |  |
| Asset Management Fee | Combination of BO reporting group PP1 and PP3 | please follow [Intercompany Charges](/sites/Wiki/Paginas/Intercompany%20Charges.aspx) for internal charges and 3rd party SCoA 's for 3rd party management fees to have proper reporting with combination el2 which is charged to |
| Property Management Fee | BO reporting group PP2 | please follow [Intercompany Charges](/sites/Wiki/Paginas/Intercompany%20Charges.aspx) for internal charges and 3rd party SCoA 's for 3rd party management fees to have proper reporting with combination el2 which is charged to |
| Development Fee | BO reporting group PP4 | please follow [Intercompany Charges](/sites/Wiki/Paginas/Intercompany%20Charges.aspx) for internal charges and 3rd party SCoA 's for 3rd party management fees to have proper reporting with combination el2 which is charged to |
| Recharged staff cost | Cost charged to managed asset (or its owner) as reimbursement of salary cost of employee works on this asset Recently BO reporting group PP5 has been created. | This cost charge needs to be done with combination el4 = 44129 and el2 asset which we charged |
| Total Fee Income | Total fee charged |  |
| NRI | NRI of assets as per Multi definition. In case we don’t have full accounting for specific assets (e.g. Forum Bornova in TR) then this field skipped. (this is only field this analysis which picks up data from different than service companies | [Net Rental Income - NRI](/sites/Wiki/Paginas/Net%20Rental%20Income%20-%20NRI.aspx) |
| fee % as of NRI | Total fee income minus development fee (with argument that it’s not recurring) divided by Net rental income of asset |  |
| Direct Employee Costs | Recurring employment costs (PQ group) and other genex which linked to employee (E% code at el6 level other than dummy) (PR7 to PR9) which booked at el2 level to specific asset | [Salary bookkeeping](/sites/Wiki/Paginas/Salary%20bookkeeping.aspx) |
| Indirect Employee Costs | Recurring employment costs (PQ group) and other genex which is **NOT** link to employee (E% code at el6 level other than dummy) (PR7 to PR9) which booked at el2 level to specific asset spread out fee income percentage over RMA country | [Salary bookkeeping](/sites/Wiki/Paginas/Salary%20bookkeeping.aspx) |
| Remaining G&A | Total G&A (PQ group <> PQ5 (as non-recurring) + PR group <> PR12 (as non-recurring)) + PS1 Depreciation subtracted by direct and indirect employment cost spread out fee income percentage over RMA country |  |
| Total recurring cost | Total G&A (PQ group <> PQ5 (as non-recurring) + PR group <> PR12 (as non-recurring)) + PS1 Depreciation |  |
| recurring margin | fee income minus total recurring cost |  |
| Gross margin | recurring margin divided by total fee income |  |
| Average FTE | Average full time employee is calculated at salary account (44111) bigger than €100 cost at element2 level of specific asset counted at employee level. |  |
