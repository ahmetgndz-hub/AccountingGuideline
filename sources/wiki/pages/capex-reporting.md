---
title: "Capex Reporting"
source_file: "Capex Reporting.aspx"
sharepoint: "https://multieu.sharepoint.com/sites/Wiki/Paginas/Capex Reporting.aspx"
contact: "Ahmet Gunduz"
categories: ""
converted: 2026-10-08
status: old-wiki
---

# Capex Reporting

## **What is capex id?**

### Capex id is a generic code assigned to budget lines which approved by shareholder. E.g. shareholder has agreed capex budget for FY2018 for 400k for C01 but there are several components of this budget. Each specific line described as capex line item and assigned unique capex id. Looks like 'C01_2018_DEBP936_146'. Capex id's maintained in reporting Hub

 ![Capexid.jpg](/sites/Wiki/PublishingImages/capex-reporting/Capexid.jpg)

## **How can we assign capex id to Purchase Order?**

### There is 2 way to assign capex id to a purchase order

1. **Selecting capex id from drop down list during creation of purchase orders.**
1. **Linking po vs capex id via reporting hub. (this overwrites first bullet too)**

### After this all invoices booked under this PO will be assigned to capex id automatically.

## **How can we assign capex id to existing transaction? (without PO)**

### Even we don't expect to see manual transactions and invoices without purchase orders capex id can be assigned to these lines via updating external reference 3 on specific line.

 

## **Do we have to assign capex id to each and every transaction in 1111 account?**

### In principle yes. However we don't expect to see capex id on valuation bookings which needs to be booked el5 = C99

 

## **Specific issues and proposed solutions.**

### Transferring actual expenditure to PnL or another account: for reporting purpose actual expenditure should contain proper capex id however transfer bookings shouldn't have. Otherwise actual capex progress will have less realization.

### Expenditure from previous year capex budgets :  should be link to previous year capex id.

### Expenditure without proper capex id: New capex id needs to be created with consulting capex team

### Capex tool should have always reconciling with budget approved by shareholder. If adjustment needed then decrease and increase budged should be done in column adjustment without adjusting budget.

 

| **[Multi Wiki](/sites/Wiki/Paginas/Multi%20Wiki.aspx) ** | **[Accounting Manual](/sites/Wiki/Paginas/Accounting%20Manual.aspx) ** | **[System Setup](/sites/Wiki/Paginas/System%20Setup.aspx)** |
|---|---|---|
