---
title: "Journal Vouchers"
source_file: "Journal Vouchers.aspx"
sharepoint: "https://multieu.sharepoint.com/sites/Wiki/Paginas/Journal Vouchers.aspx"
contact: "Ahmet Gunduz"
categories: ""
converted: 2026-10-08
status: old-wiki
---

# Journal Vouchers

| **Code or Logic** | **Purpose of usage** | **Workflow applicable in coda** | **SCoA restriction / Control with BO trigger** |  |
|---|---|---|---|---|
| **JV-ERV** | ERV booking for operational assets | Exempt | 41101 Estimated Rental Value |  |
|  |  |  | 41111 Estimated rental value reversal |  |
|  |  |  | 41416 TO rent only |  |
| **JV-RESULT** | Quarterly (or monthly) result transfer from P&L to equity or partition booking on shareholder level | Exempt | 21180 Retained earnings | 11550 Investments in associates and joint ventures |
|  |  |  | 99998 Transfer account result | 55991 Result from participations |
|  |  |  | 11540 Participations in group companies | 21220 Non-controlling interests |
|  |  |  | 55995 Result group companies non-assets | 55980 Non controlling interest |
| **JV-VALUATION** | Valuation booking for investment bookings (e.g. BX, Multi, US Tax, 3rd party etc.) | Exempt | 11111 Investment property | 43315 Fair value adjustment IP |
|  |  |  | 43312 Market value changes | 43314 Impairment Lease incentives |
|  |  |  | 43313 Impairment Capex |  |
| **JV-ICINTREST** | This code will be used for intercompany interest calculation and booking | Exempt | 13532 Interest Receivable Group | 27402 Interest Payable Group |
|  |  |  | 13561 Other Receivables Group Current | 52310 Interest income group |
|  |  |  | 25110 Loan payable group non-current | 52330 Interest expenses group |
|  |  |  | 25555 Other payables group non-current | 53310 Interest income group (service comp) |
|  |  |  | 27125 Loans group current | 54330 Interest expenses group (service comp) |
|  |  |  | 27330 Loans payable current |  |
| **JV-ELM** | Elimination booking for consolidation | Exempt | EL3 = ELM only | EL3 = ELM only |
| **JV-CFCORR** | Below NRI presentation corrections. This will be count as cash transaction at QAR reporting (formerly known as GE-JV-MAN-CF) | Yes – Via manual journal WF | n/a | n/a |
| **JV-BADDEBT** | Bad debt bookings | Exempt | 13113 Provision on Trade receivables | should be reversal document |
|  |  |  | 42593 Doubtful debt provision (opex) |  |
| **JV-TAXES** | To book and reclass all type of taxes like VAT return, WHT return, Deferred tax, «accruals where applicable» will be done via this document code | Exempt Write off allowed up to € 5 | 11575 VAT Receivable non-current | 27570 Income tax |
|  |  |  | 27521 VAT | 53100 Current income tax |
|  |  |  | 27523 Wage tax and social security |  |
|  |  |  | 11650 Deferred tax asset | 53300 Deferred tax |
|  |  |  | 25511 Deferred tax liability |  |
| **NF-GUARANTEE** | Tenant or supplier guarantees which will effect tenant guarantee BO report as well as QAR reporting | Yes – Via manual journal WF | 99100 Tenant Guarantees (off balance sheet) |  |
| **JV-DEPR** | Depreciation bookings of tangible and intangible assets | Yes – Via manual journal WF | 11313 Land and buildings cum depreciation | 42911 Depreciation investment property |
|  |  |  | 11323 Other Fixed assets cum depreciation | 42912 Depreciation |
|  |  |  | 11423 Goodwill cum depreciation | 42910 Depreciation |
|  |  |  | 44910 Depreciation (man.co.) | 53910 Depreciation |
| **JV-MANUAL** | General transfer can be used as stated below but not limited | Yes – Via manual journal WF | All will be manual control |  |
|  | -Write off from specific account |  |  |  |
|  | -Interest accrual in different books |  |  |  |
|  | -Correction or reclass |  |  |  |
|  | -Interest accrual for current account |  |  |  |
|  | -Accrual of income in books other than MAN |  |  |  |
|  | -Accrual of Capex at year end |  |  |  |
|  | -Classification of short term vs long term |  |  |  |
|  | -Etc. |  |  |  |

| **[Multi Wiki](/sites/Wiki/Paginas/Multi%20Wiki.aspx) ** | **[Accounting Manual](/sites/Wiki/Paginas/Accounting%20Manual.aspx) ** | **[System Setup](/sites/Wiki/Paginas/System%20Setup.aspx)** |
|---|---|---|
