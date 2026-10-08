---
title: "Accruals"
source_file: "Accruals.aspx"
sharepoint: "https://multieu.sharepoint.com/sites/Wiki/Paginas/Accruals.aspx"
contact: "Ahmet Gunduz"
categories: ""
converted: 2026-10-08
status: old-wiki
---

# Accruals

| **Nature of accrual** | **Effected P&L Line** | **Expected booking** | **MANBooks** | **FSMbooks** | **UST Books** |
|---|---|---|---|---|---|
| Employment related costs |  |  |  |  |
| **Employee bonus ** | **PQ2 Bonuses ** | **CR 27526 Accrual bonus DR 44124 Bonus ** | **No ** | **No ** | **No ** |
| **Redundancy ** | **PQ5 reorganisation cost (s) ** | **CR 27527 Accrual redundancy DR 44125 Redundancy ** | **No** | **No** | **No** |
| **Employee seniority indemnity** | **PQ Salaries** | **CR 27527 Accrual redundancyDR 44123 Leaving indemnity** | **No** | **No ** | **No** |
| **Unused vacation days** | **PR9 Other staff costs** | **CR 27515 Salary suspenseDR 44190 Other staff costs** | **No** | **No** | **No** |
| Service and Marketing charges / income |  |
| **Marketing charge invoices has not been issued yet ** | **PE1 Service Charge IncomePE2 Marketing Income** | **DR 13553 Accrued income non groupCR 46810 Service charge incomeCR 46820 Marketing charges income** | **yes ** | **Yes** | **Yes** |
| **Service and marketing charge reconciliation (interim) result** • **Additional invoices ** | **PE1 Service Charge IncomePE2 Marketing Income** | **DR 13553 Accrued income non groupCR 46810 Service charge incomeCR 46820 Marketing charges income ** | **yes ** | **Yes** | **Yes** |
| **Service and marketing charge reconciliation (interim) result** • **Credit notes (back invoices) ** | **PE1 Service Charge IncomePE2 Marketing Income** | **CR 27560 Other current payablesDR 46810 Service charge incomeDR 46820 Marketing charges income** | **yes ** | **Yes** | **Yes** |
| **Service and marketing charge reconciliation (interim) results ** • **Shortfall caps** • **Shortfall vacancy** | **Net balance of PE and PF(After above bookings net balance of PE and PF reporting lines should be equal to shortfall caps and shortfall vacancy and this needs to be disclosed to service charge page of QAR reporting) ** | **No ** | **No** | **No** |
| **Any other goods or service has been utilized / benefitted during period but has not been invoiced ** | **PFX Service and Marketing costs** | **CR 27560 Other current payables DR 46XXX Relevant expense SCoA ** | **Yes** | **Yes** | **Yes** |
| Taxes |  |  |  |  |  |
| **Current income tax** | **PX Income tax** | **CR 27570 Income taxDR 53100 Current income tax** | **Yes** | **Yes** | **Yes** |
| **Deferred tax asset ** | **PX Income tax** | **DR 11605 Deferred tax assetCR 53300 Deferred tax** | **No ** | **Yes** | **No** |
| **Deferred tax Liability** | **PX Income tax** | **CR 25511 Deferred tax liabilityDR 53300 Deferred tax** | **No ** | **Yes** | **No** |
| Income |  |  |  |  |  |
| **Turnover Rent ** | **PD1 Turnover Rent** | **DR 13553 Accrued income non groupCR 41140 Turnover rent** | **Yes** | **Yes** | **Yes** |
| **Base Rent** | **PB Reversionary Potential** | **DR 13553 Accrued income non groupCR 41110 Potential base rent** | **Yes** | **Yes** | **Yes** |
| **Kiosk rent ** | **PD3 Mall Income** | **DR 13553 Accrued income non groupDR 41160 Mall income** | **Yes** | **Yes** | **Yes** |
| **Discounts to tenant provided with back dated** | **PCx Discounts** | **CR 27560 Other current payablesDR 414XX Relevant discount category** | **Yes** | **Yes** | **Yes** |
| Opex |  |  |  |  |  |
| **Real estate tax** | **PG3 Taxes** | **CR 27520 Real estate taxDR 42521 Real estate taxes (landlord)** | **Yes** | **Yes** | **Yes** |
| **Bad debt ** | **PG1 Collection Losses** | **CR 13113 Provision on Trade receivablesDR 42593 Doubtful debt provision (opex)** | **Yes** | **Yes** | **Yes** |
| Others |  |  |  |  |  |
| **Real estate tax ** | **PR11 Other general expenses** | **CR 27520 Real estate taxDR 44231 Real estate taxes (genex)** | **Yes ** | **Yes** | **Yes** |
| **Interest accrual** | **PI2 Interest costs banks** | **CR 27401 Interest payable DR 52130 Interest expense non-group** | **Yes ** | **Yes ** | **Yes ** |
| **Cost allocation fee of HQ ** | **PW Recharged from/to group co. ** | **CR 27565 Other current payables groupDR 45915 CAF expense holding** | **Yes ** | **Yes ** | **Yes ** |
| Capex and Development |  |  |  |  |
| **C1, C2, C4 and C3a(Operation)** | **n/a ** | **CR 27560 Other current payablesDR 11111 Investment properties** | **Only at Q4** | **Only at Q4** | **Only at Q4** |
| **C3b and C5 (development)** | **n/a** | **CR 27562 Project costs payableDR 11340 B code WIP** | **No** | **No** | **No ** |

|  |  | **What** | **Why** |
|---|---|---|---|
| 1 | DO | **Always specify **proper element6** (counterparty) ** | **With this all stakeholders can easily follows accruals and measure effect on books** |
| 2 | DON'T | Do not use dummy** codes in accrual account and counter posting line ** | **unless its related with service and marketing charge reconciliation and can be stemming from more than 10 tenants** |
| 3 | DO | **Always book accruals with **automatic reversal journal** (JV-REVERSAL) ** | **With this we can eliminate** • **Risk of double count being forgotten to reverse** • **Manual work to follow accruals ** • **Possible overrun stemming from accruals in PO available budget calculation** |
| 4 | DO | **Use **one document code one accrual | **Then we can easily follow accruals and its nature and workflow approval gets faster** |
| 5 | DO | **Use** clear line description** while accruing any item** | **This will speed up approval process in workflow** |
| 6 | DON'T | **Do not make **excel** calculation sheet **attachments** to the journal ** | **Excel documents most of the time is too much information to just approve workflow and understand booking nature. Always make attachment of PDF with clear explanation.** |
| 7 | DON'T | **Do not make accrual for multiple cost line in one accrual line in other word** aggregation in accrual line is not allowed | **To be able to create automatic movement and proper follow up all accruals needs to be 1=1 cost line vs accrual line. ** |
| 8 | DON'T | **Do not close **accruals with incoming/outgoing invoice | **This will blur follow up and it will affect cash flow reporting. ** |
| 9 | DO | **Consider to using **lease reference** for accruals **to include OCR calculation | **For proper OCR calculation all costs or discount of tenants needs to be part of cost. This only possible to have proper lease reference at all costs. ** |

| **[Multi Wiki](/sites/Wiki/Paginas/Multi%20Wiki.aspx) ** | **[Accounting Manual](/sites/Wiki/Paginas/Accounting%20Manual.aspx) ** | **[System Setup](/sites/Wiki/Paginas/System%20Setup.aspx)** |
|---|---|---|
