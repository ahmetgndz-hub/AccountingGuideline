---
title: "Available budget"
source_file: "Available budget.aspx"
sharepoint: "https://multieu.sharepoint.com/sites/Wiki/Paginas/Available budget.aspx"
contact: "Dennis Pieterson"
categories: ""
converted: 2026-10-08
status: old-wiki
---

# Available budget

# Available budget BO report

### The available budget report is created to provide an overview of the available budgets used for the purchase request calculations taking in to budget, actuals, (pending) commitments.
To show overviews for specific parts of the budgets 3 reports are created.

### The report is created for the following categories:

- **Asset entity;
**
- **Service entity (under development);
**
- **Capex (under development).
**

### The reports can be found in the 'Country' -  'All' - 'Financial Reporting' folder in BO, 'Available budget - Asset / Service or Capex'.

 

## **Report**

### **Data**

### Which data is picked when you run the report?

- **The report can only be refreshed with year to date information;
**

  - **For example, if year 2020 is selected the data of 2020 till current date will be shown;
**
  - **Running the report for a specific period in the year is **not** possible.
**

- **Only data that is posted to the Books in Coda will be shown by the report, items that are in the Intray of Coda are **not** included in the report. 
**

 

### **Prompts**

### In the below overview the prompts that can be selected for this report are shown, only the first 2 prompts are mandatory to run the reports. 
The other prompts can be used to run specific data.

- **Company;
**
- **Year;
**
- **Element 2 (property code), search can be done base on EL2 code or property name (not mandatory);
**
- **Element 4, to run the report on a specific scoa (not mandatory);
**
- **BO Code, to run the report on a specific BO code (not mandatory);
**

![prompts.png](/sites/Wiki/SiteCollectionImages/available-budget/prompts.png)
 

### **Sheets**

### In the report various sheets are created to show different detail levels of the available budget data:

- **Overview;**

  - **Total overview of all scoa's linked to the category of the report (Asset, Service or Capex);
**

- **Genex;
**

  - **Detailed overview of only Genex scoa's;
**

- **Opex;
**

  - **Detailed overview of only Opex scoa's;
**

- **SC;
**

  - **Detailed overview of only Service Charge scoa's;
**

- **Details Budget;
**

  - **Detailed overview of uploaded budget to Coda;
**

- **Details Actuals;
**

  - **Detailed overview of all actuals on transaction level;
**

- **Purchase requests;
**

  - **Detailed overview of all outstanding PR's on EL4/6 level.
**

 

## **Available budget calculation**

### In the below screenshot an example of the available budget calculation is show.
In the bullets below the screenshot the logic of the different columns and calculation of the available budget is explained.

![Availalbebudget.png](/sites/Wiki/SiteCollectionImages/Paginas/Available%20budget/Availalbebudget.png) 

- **Budget;
**

  - **Coda budget per Element 4;
**

- **Actuals;
**

  - **Total actuals, actuals in the year of the overview equal to actuals in the P&L;
**

- **Actuals current;**

  - **Actuals relating to the current year (year of the overview), transactions booked in the year of the overview + invoices matched to PR's of the year of the overview;
**

- **Actuals previous;
**

  - **Invoices received in the year of the overview, but matched to PR's created/approved in previous year;
**

- **Accruals;
**

  - **Transactions booked with the following document codes:
**

    - **GE-JV-RV;
**
    - **JV-REVERSAL;
**

- **Commitments;
**

  - **Approved PR's in the year of the overview;
**

- **Commitments previous year;
**

  - **PR's approved in the years before the year of the overview with available budget on the PR;
**

- **Non-Approved;
**

  - **PR's pending in the workflow process;
**

- **Available; **

  - **Budget currently available;
**
  - **Calculation: Budget -/- Actuals Current -/- Commitments -/- Non-Approved = Available budget;
**
  - **%: Available budget / Budget * 100%.
**

## **Purchase requests**

### As the purchase request sheet shows data of various years below an explanation of the various status of the lines and some examples how amounts are calculated/settled.

### Status of the PR lines (last column in the PR overview):

- **01 - Posted invoices;
**

  - **The lines show a PR for the current year, original PR amount, amount of received invoices and balance total of the outstanding commitment/PR (see example 1);
**

- **03 - Non approved purchase requests;
**

  - **PR's pending in the workflow (see example 2).
**

- **05 - Commitments previous years;
**

  - **PR's created in previous years with outstanding amounts (see example 3/4);
**

- **06 - Invoices posted against commitments previous years;
**

  - **Invoices received in the year of the report and matched against PR's of previous years (see example 3).
**

### **Examples**

### Example 1: PR of current year matched with an invoice of current year:

- **Committed purchase: Original PR amount;
**
- **Invoiced: Received invoices on this specific PR (details of the invoices can be found on the 'Details Actuals' sheet;
**
- **Outstanding amount: Committed purchase -/- Invoiced;
**
![Example1.png](/sites/Wiki/SiteCollectionImages/Paginas/Available%20budget/Example1.png)
 

### Example 2: 

- **Non-Approved PR's on PR level;
**
- **PR's pending in the workflow.
**
![Example2.png](/sites/Wiki/SiteCollectionImages/Paginas/Available%20budget/Example2.png)

### Example 3: Invoice received in current year for PR from previous year

- **Status 05: Commitment approved in previous year. In this example the PR is approved in 2019 (Commitment year) and € 20,96 is available on this PR;
**
- **Status 01: Invoice received in 2020 for the PR from 2019;
**
- **Status 06: Settling of the invoice received in 2020 for the PR of 2019. After settling all lines in Current year are € 0 (so no impact on current year budget) and the commitment previous year is settled with the received invoice.
**
![Example3.png](/sites/Wiki/SiteCollectionImages/Paginas/Available%20budget/Example3.png)

### Example 4: PR current and previous year, no invoices received yet;

- **Status 05: Commitment approved in previous year. In this example the PR is approved in 2019 (Commitment year) and € 2.322,63 is available on this PR;
**
- **Status 01: In 2020 a new PR is created for € 3.000, no invoices received yet.**
![Example41.JPG](/sites/Wiki/SiteCollectionImages/Paginas/Available%20budget/Example41.JPG)
 

 

| **[Multi Wiki](/sites/Wiki/Paginas/Multi%20Wiki.aspx) ** | **[Accounting Manual](/sites/Wiki/Paginas/Accounting%20Manual.aspx) ** | **[System Setup](/sites/Wiki/Paginas/System%20Setup.aspx)** |
|---|---|---|
