---
title: "Below NRI items"
source_file: "Below NRI items.aspx"
sharepoint: "https://multieu.sharepoint.com/sites/Wiki/Paginas/Below NRI items.aspx"
contact: "Ahmet Gunduz"
categories: ""
converted: 2026-10-08
status: old-wiki
---

# Below NRI items

### Per Q1 2019 the 2nd page of the cash flow in the QAR reporting is populated with data coming from Coda (Below NRI project).
Below the steps are explained how the data from Coda is populating the cash flow in the QAR report.

## **How is the cash flow populated in the QAR report**

### The report is looking for mutations in Coda for a specific period (for example Q1 2019, periods 2019/1 till 2019/3 is retrieved from Coda) which contain cash movements.
Cash movements are recognized by the report if the mutation in Coda contains a Cash SCoA or is booked with a specific document code.

- **Cash SCoA's: 13311, 13332, 13340, 13345, 13312, 13313, 13317 / BO reporting group BB5 Cash and cash equivalents.**
- **Document code: JV-CFCORR (or before 2020, GE-JV-MAN-CF was used).**

### The document code can be used to rebook, incorrect booked cash movements.

## **How are the cash movements presented in the cash flow of the QAR report**

### In the below overview a mapping is shown how cash movements should be booked to be retrieved by the cash flow of the QAR report.

     | **Map Code** | **Map Name** | **el4** | **el5** | **el8** | **cash** |
|---|---|---|---|---|---|
| CA1 | C1 - Regular Capex | 11112 | C01 | 070 | 0 |
| CA1 | C1 - Regular Capex | 11111 | C01 | 070 | 0 |
| CA2 | C2 - Legal Compliance | 11111 | C02 | 070 | 0 |
| CA2 | C2 - Legal Compliance | 11112 | C02 | 070 | 0 |
| CB1 | C3 - Redevelopment | 11340 | * | 070 | 0 |
| CB1 | C3 - Redevelopment | 11112 | C03 | 070 | 0 |
| CB1 | C3 - Redevelopment | 11111 | C03 | 070 | 0 |
| CB2 | C4 - Tenant Fitout/Incentives | 11112 | C04 | 070 | 0 |
| CB2 | C4 - Tenant Fitout/Incentives | 11111 | C04 | 070 | 0 |
| CB3 | C5 - Extensions | 11111 | C05 | 070 | 0 |
| CB3 | C5 - Extensions | 11112 | C05 | 070 | 0 |
| CD1 | Sale proceeds | 55800 | * | * | 0 |
| CD1 | Sale proceeds | 11112 | * | 050 | 0 |
| CD1 | Sale proceeds | 11111 | * | 050 | 0 |
| CE1 | Corporate income tax | 53100 | * | * | 0 |
| CE2 | VAT | 27521 | * | * | 0 |
| CE2 | VAT | 11575 | * | * | 0 |
| CE2 | VAT | 13565 | * | * | 0 |
| CH1 | Interest | 52130 | * | * | 1 |
| CH1 | Interest | 51130 | * | * | 1 |
| CH1 | Interest | 27401 | * | * | 1 |
| CH1 | Interest | 27402 | * | 920 | 1 |
| CH2 | Amortization | 25330 | * | 830 | 1 |
| CH2 | Amortization | 27330 | * | 830 | 1 |
| CH2 | Amortization | 25120 | * | 930 | 1 |
| CH3 | Repayment | 25330 | * | 820 | 1 |
| CH3 | Repayment | 27330 | * | 820 | 1 |
| CH3 | Repayment | 25120 | * | 920 | 1 |
| CH4 | Drawdown | 25330 | * | 810 | 1 |
| CH4 | Drawdown | 27330 | * | 810 | 1 |
| CH4 | Drawdown | 25120 | * | 910 | 1 |
| CH5 | Agency fees | 51780 | * | * | 0 |
| CH6 | One-off Banking Fees | 51782 | * | * | 0 |
| CI2 | Equity contributions | 21110 | * | 525 | 1 |
| CJ1 | Equity distributions | 27380 | * | * | 1 |
| CJ1 | Equity distributions | 21180 | * | 570 | 1 |
| CJ1 | Equity distributions | 21110 | * | 570 | 1 |
| CJ2 | Shareholder loan repayment | 27402 | * |  | 1 |
| CJ2 | Shareholder loan repayment | 11535 | * | 810 | 1 |
| CJ2 | Shareholder loan repayment | 11535 | * | 820 | 1 |
| CJ2 | Shareholder loan repayment | 25110 | * | 820 | 1 |
| CJ2 | Shareholder loan repayment | 25120 | * | 820 | 1 |
| CJ2 | Shareholder loan repayment | 27125 | * | 820 | 1 |
| CJ2 | Shareholder loan repayment | 25110 | * | 830 | 1 |
| CJ3 | Shareholder loan drawdown | 13532 | * | * | 1 |
| CJ3 | Shareholder loan drawdown | 25110 | * | 810 | 1 |
| CJ3 | Shareholder loan drawdown | 25120 | * | 810 | 1 |
| CJ3 | Shareholder loan drawdown | 27125 | * | 810 | 1 |
| CJ3 | Shareholder loan drawdown | 11535 | * | 830 | 1 |

 

## **Examples of the workings of the cash movements** 

![2019-10-16_10-31-51.jpg](/sites/Wiki/PublishingImages/Paginas/Below%20NRI%20items/2019-10-16_10-31-51.jpg)
 

![2019-10-16_10-32-09.jpg](/sites/Wiki/PublishingImages/Paginas/Below%20NRI%20items/2019-10-16_10-32-09.jpg)
 

| **[Multi Wiki](/sites/Wiki/Paginas/Multi%20Wiki.aspx) ** | **[Accounting Manual](/sites/Wiki/Paginas/Accounting%20Manual.aspx) ** | **[System Setup](/sites/Wiki/Paginas/System%20Setup.aspx)** |
|---|---|---|
