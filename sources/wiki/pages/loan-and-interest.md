---
title: "Loan and interest"
source_file: "Loan and interest.aspx"
sharepoint: "https://multieu.sharepoint.com/sites/Wiki/Paginas/Loan and interest.aspx"
contact: "Ahmet Gunduz"
categories: ""
converted: 2026-10-08
status: old-wiki
---

# Loan and interest

### Effective from 1st of 2019 we have decided to introduce new element7 concept for 3rd party loans. Reason for this further improve our reporting cycle and make our books clearer for every stakeholder who reads trial balances and further automating reporting.

### **New element 7 3rd party loans**

### As part of automatization of data used in reports, we are introducing new element 7 groups for 3rd party loans (bank loans).
The setup of the new EL7 will be as follows:

### L          Stands for Loan
 DE       Stands for ISO code of country
 000             3-digit sequential number.

### EL7: LDE001

### For 3rd party loans the following Elements 4 are mandatory:

- **25330   External loan non-current**
- **27330   External loan current**
- **27401   Interest Payable**
- **52130   Interest expense non-group      
**

### **Movement codes usage for Loan payable**

### For the loans payable the following elements 8 are created.

- **810       Drawdown**
- **820       Repayment**
- **830       Amortization
**

### The elements 8 are applicable for the following elements 4 (not only 3rd party):

- **27330   External loan current**
- **25330   External loan non-current**
- **25110   Loan group non-current
**
- **25120   Loan related non-current
**
- **27125   Loans group current
**

| **SCoA code** | **SCoA name** | **Explanation** |
|---|---|---|
| ***52330*** | ***Interest expenses group*** |  |
| PI1 | Interest costs group companies |  |
| ***52130*** | ***Interest expense non-group*** | ***Interest cost to bank with regards to loan facility link to asset. Has to be sub analysed at el7 level.*** |
| PI2 | Interest costs banks |  |
| ***52820*** | ***Other financial expenses*** |  |
| PI3 | Interest costs other |  |
| ***51780*** | ***Loan Agency fees*** |  |
| ***51782*** | ***One-off banking fees* ** |  |
| ***52821*** | ***Bank costs (asset co.)*** | ***Negative interest on overnight account and other regular bank costs (transaction costs, account cost etc.)* ** |
| PI4 | Bank fees and charges |  |
| PI | Financial costs |  |

| **[Multi Wiki](/sites/Wiki/Paginas/Multi%20Wiki.aspx) ** | **[Accounting Manual](/sites/Wiki/Paginas/Accounting%20Manual.aspx) ** | **[System Setup](/sites/Wiki/Paginas/System%20Setup.aspx)** |
|---|---|---|
