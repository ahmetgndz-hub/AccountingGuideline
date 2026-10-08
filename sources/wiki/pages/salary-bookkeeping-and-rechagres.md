---
title: "Salary Bookkeeping and rechagres"
source_file: "Salary Bookkeeping and rechagres.aspx"
sharepoint: "https://multieu.sharepoint.com/sites/Wiki/Paginas/Salary Bookkeeping and rechagres.aspx"
contact: "Ahmet Gunduz"
categories: ""
converted: 2026-10-08
status: old-wiki
---

# Salary Bookkeeping and rechagres

### With this guideline, we aim to give proper guideline and examples to accountants who bookkeeps salary costs in Multi and accountants who recharges them to related cost categories or recharge to other entities. 

### By following this guideline, we will be sure that reports and analyses created over this information are shown adequately on reports and comparable over the years.

## **Salary bookkeeping**

### Example bookkeeping at the salary payment/accrual date.

- **In the below example, the employer is "Multi Italy" and the employee works for Forum Palermo**

### -          Document code to be used is JV-SALARY

### -          Document date should be the date of Payroll Run

 

| **Reporting Group** | **Elm 1** | **Elm 2** | **SCoA and name** | **Elm 6** | **Elm 7** | **Amount** | **Description** |
|---|---|---|---|---|---|---|---|
| PQ1 Salaries | ITS002 | ITIP004 | 44111 Wages and salaries | E5338 | D490 | 300 DR | Gross salary of employee accrued on this payroll run |
| PQ9 Other staff costs | ITS002 | ITIP004 | 44113 Social security | E5338 | D490 | 30 DR | Social security premiums paid by the employer |
| PR7 Travel and car costs | ITS002 | ITIP004 | 44130 Travel expenses | E5338 | D490 | 25 DR | Travel allowance paid by the employer |
| PQ7 Pension costs | ITS002 | ITIP004 | 44115 Pensions | E5338 | D490 | 10 DR | Pension premium paid by the employer |
| BF5 Current tax liabilities | ITS002 | ITSZ002 | 27523 Wage tax and social security | E5338 |  | 110 CR | Income tax payable from payroll at the employee level (separate element5 usage is encouraged to do the split between income tax and insurance premium or any other kind of taxes) |
| BF5 Current tax liabilities | ITS002 | ITSZ002 | 27523 Wage tax and social security | E5338 |  | 45 CR | Total insurance premium payable from payroll at the employee level (separate element5 usage is encouraged to do the split between income tax and insurance premium or any other kind of taxes) |
| BB2 Trade and other receivables third parties | ITS002 | ITSZ002 | 13567 Prepayment staff current | E5338 |  | 15 CR | Any other salary deductions which will be withheld from salary payable |
| BF3 Trade and other payables | ITS002 | ITSZ002 | 27515 Salary suspense account | E5338 |  | 195 CR | Net salary payable to the bank account of an employee |

### **Footnotes and remarks**

1. **Element2 should be the actual asset code where the employee works. (e.g., SKBP952 for Max Trencin)

If an employee works for all assets or works for a Local Service company (e.g., finance expert), then element2 code of service company needs to be used. (e.g. SKSZ001 for Multi Slovakia service company)**
1. **Element1 should always be equal to the payroll entity**
1. **Element6 is code created in line with Workday, and generally, a four-digit number starts with E, which represents "employee." E code in coda for an employee should be equal to the workday id of this employee.**
1. **ADP or her service providers should be able to provide the above data in a format that can be upload to coda financials via coda-xl without manual intervention. (you can find the latest version of coda-xl at the following share drive. "\\storage-dfs\shares\NLMAH\Collaboration\CODA Templates and Documents" )**

 

### **Regular controls at month-end**

- **The balance of account 27515 should be 0 and matched to proof all payments processed to the employee bank account**
- **The month-end balance of account 27523 should be equal to taxes to be paid to the tax office.**
- **The balance of account 13567 at the employee level should be 0 and matched after posting salary posting. **
- **Consistency of el2 usage for employee level**

## **Recharges and Fee Income over Salary**

## **a)  Salary recharge as fee income to an asset company**

### Charge type                          Vertical (downwards / Service Co. => Asset Co.)

### Party charges cost               Service Company

### Party receives cost              Asset Company (3rd, Group or Related Party)

### If a certain cost of employees needs to be charged to the assets company (in line with management agreement) directly below bookkeeping should be followed. This is classified as fee income and should not be netted off from accouent where cost incurred directly

### Booking example for Service Company

| **Reporting Group** | **Elm 1** | **Elm 2** | **SCoA and name** | **Elm 6** | **Elm 7** | **Amount** | **Description** |
|---|---|---|---|---|---|---|---|
| PP5 Salary and employee recharges | ITS002 | ITIP004 | 44129 Recharged salary costs | E5338 | D490 | 340 CR | Total recharge for per employee which is booked initially to reporting groups PQ (staff cots) at the employee level |
| PP5 Salary and employee recharges | ITS002 | ITIP004 | 44611 Recharged employee cost | E5338 | D490 | 25 CR | Total recharge which booked initially to reporting groups PR (General costs) at the employee level |
| BF5 Current tax liabilities | ITS002 | ITSZ002 | 27521 VAT | TITS21 |  | 76 CR | VAT stemming from this charge |
| BB2 Trade and other receivables third parties | ITS002 | ITSZ002 | 13111 Trade receivable non-group | D code of Asset Co. |  | 441 DR | Total payable line |

 

 

Booking example for Asset Company

| **Reporting Group** | **Elm 1** | **Elm 2** | **SCoA and name** | **Elm 6** | **Elm 7** | **Amount** | **Description** |
|---|---|---|---|---|---|---|---|
| PF12 Staff costs | ITI004 | ITIP004 | 46933 Staff costs | C code of Man. Co. |  | 365 DR | Total recharge for per employee which is booked initially to reporting groups PQ (staff cots) at the employee level |
| BF5 Current tax liabilities | ITI004 | ITSZ002 | 27521 VAT | TITS21 |  | 76 DR | VAT stemming from this charge |
| BF3 Trade and other payables | ITI004 | ITSZ002 | 27310 Trade payables non-group | C code of Man Co. |  | 441 CR | Total payable line |

### **Footnotes and remarks**

1. **For the sake of simplicity, examples are for 3rd party assets. If the counterparty is a related party, please use appropriate SCoA (element4) and counterparty code (element 6)**
1. **The asset company and her investor may decide to keep as landlord cost and not to reflect tenants. In this case, please consider using "fee cost" scoa**

### **Regular controls at month-end**

- **The cost of employees works for specific assets should be zero at the service company level.  **

## **b) Transferring salary cost to another cost line**

### Charge type                          within same entity

### Party charges cost               Asset company A

### Party receives cost              Asset company A

### In case of an asset, the company holds the payroll of her employees, and these cost needs to be reflected service and marketing charge; then following bookkeeping methodology needs to be followed.

 

| **Reporting Group** | **Elm 1** | **Elm 2** | **SCoA and name** | **Elm 6** | **Elm 7** | **Amount** | **Description** |
|---|---|---|---|---|---|---|---|
| PQ1 Salaries | ITI004 | ITIP004 | 44198 Recharge salary | E5338 | D490 | 340 CR | Total recharge for per employee which is booked initially to reporting groups PQ (staff cots) at the employee level |
| PR11 Other expenses | ITI004 | ITIP004 | 44610 Recharge genex | E5338 | D490 | 25 CR | Total recharge which booked initially to reporting groups PR (General costs) at the employee level |
| BB2 Trade and other receivables third parties | ITI004 | ITIP004 | 13500 Suspense account | C code of Asset Co. |  | 441 DR | Transfer account at an aggregate level / using a suspense account is not mandatory can be skipped. |
| BB2 Trade and other receivables third parties | ITI004 | ITIP004 | 13500 Suspense account | C code of Asset Co. |  | 441 CR | Transfer account at an aggregate level / using a suspense account is not mandatory can be skipped. |
| PF12 Staff costs | ITI004 | ITIP004 | 46933 Staff costs | C code of Asset Co. |  | 441 DR | Ultimate cost account |

### **Footnotes and remarks**

1. **For the sake of simplicity, examples are for 3rd party assets. If the counterparty is a related party, please use appropriate SCoA (element4) and counterparty code (element 6)**
1. **The asset company and her investor may decide to keep as landlord cost and not to reflect tenants. In this case, please consider using "fee cost" scoa**

### **Regular controls at month-end**

- **The cost of employees at the asset level (reporting group PQ and PR) should be fully reflected in the related cost line.**

## **c)   Charges between service companies**

### Charge type                       Horizantal (Service Co. => Service Co. )

### Party charges cost              Service Company A

### Party receives cost              Service Company B

### In some countries, employees are employed by a service company with no management agreement directly with the asset company where the employee works or serves. For this reason, the cost of these employees needs to be recharged to a related service company that holds a management agreement with the managed asset. (e.g., Multi Italy to MOMI) This recharge should not distort the cost of employees in the initial payrolling company.

### Booking example for Service Company A

| **Reporting Group** | **Elm 1 ** | **Elm 2** | **SCoA and name** | **Elm 6** | **Elm 7** | **Amount** | **Description** |
|---|---|---|---|---|---|---|---|
| PQ1 Salaries | ITS002 | ITIP004 | 44198 Recharge salary | E5338 | D490 | 340 CR | Total recharge for per employee which is booked initially to reporting groups PQ (staff cots) at the employee level |
| PR11 Other expenses | ITS002 | ITIP004 | 44610 Recharge genex | E5338 | D490 | 25 CR | Total recharge which booked initially to reporting groups PR (General costs) at the employee level |
| BF5 Current tax liabilities | ITS002 | ITSZ002 | 27521 VAT | TITSXX |  | 76 CR | VAT stemming from this charge |
| BB3 Trade and other receivables group companies | ITS002 | ITSZ002 | 13130 Trade receivables group | R Code of Asset Co. |  | 441 DR | Total payable line |

 

### Booking example for Service Company B

| **Reporting Group** | **Elm 1** | **Elm 2** | **SCoA and name** | **Elm 6** | **Elm 7** | **Amount** | **Description** |
|---|---|---|---|---|---|---|---|
| PQ1 Salaries | ITS003 | ITIP004 | 44198 CAF IGS recharge salary | E5338 | D490 | 340 DR | Total recharge for per employee which is booked initially to reporting groups PQ (staff cots) at the employee level |
| PR11 Other expenses | ITS003 | ITIP004 | 44610 CAF IGS recharge genex | E5338 | D490 | 25 DR | Total recharge which booked initially to reporting groups PR (General costs) at the employee level |
| BF5 Current tax liabilities | ITS003 | ITSZ003 | 27521 VAT | TITSXX |  | 76 DR | VAT stemming from this charge |
| BF3 Trade and other payables | ITS003 | ITSZ003 | 27120 Trade payables group | R Code of Asset Co. |  | 441 CR | Total payable line |

 

| **[Multi Wiki](/sites/Wiki/Paginas/Multi%20Wiki.aspx) ** | **[Accounting Manual](/sites/Wiki/Paginas/Accounting%20Manual.aspx) ** | **[System Setup](/sites/Wiki/Paginas/System%20Setup.aspx)** |
|---|---|---|
