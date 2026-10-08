---
title: "Capital Expenditures"
source_file: "Capital Expenditures.aspx"
sharepoint: "https://multieu.sharepoint.com/sites/Wiki/Paginas/Capital Expenditures.aspx"
contact: "Ahmet Gunduz"
categories: ""
converted: 2026-10-08
status: old-wiki
---

# Capital Expenditures

# Capital Expenditure (CAPEX)

### Following acquisition of Multi by Blackstone in 2013, the new strategy for Multi became to focus primarily on asset management as its core activity, supported by property management and (re-)development management to improve the value of the properties it is managing. Driven by this repositioned strategy, Multi's management teams are continuously looking for different asset management initiatives to increase shareholder value. To that end, vital to the new strategy is keeping assets well maintained and ensuring the best tenant mix.

### Maintenance and lease up of assets can require further investment depending on each asset's individual situation. In the annual business plans, local teams identify Capex works required for each budget year. For the sake of fast and clear communication, identified Capex works are grouped in 5 different categories and two types of costs

- **Costs that bring additional value to the shopping centers (like extensions) regarded as Capex;
**
- **Recurring expenses to maintain the property in the current state (like repairs) or to ensure continued rental income (like obtaining permits) regarded as Maintenance.** 

## **Capex Groups**

### **C1 – Regular Capex**

### General expenditure concerning (major) repairs, improvements and replacements. These are regarded as non-value adding expenditure to maintain the property in the current state like replacing a floor in a center, repairing the escalators, etc. C1 is regarded as Maintenance

### **C2 – Legal Compliance**

### This type of expenses needs to be incurred to ensure we keep in business, but do not bring additional (rental) income. Works that arise because we need to comply with local law and regulations, like wheelchair access or works to comply with permits or licenses. C2 is regarded as Maintenance.

### **C3 – Renovation Works**

### These expenses should generate a (quantifiable) return in terms of NRI. Refurbishment or redevelopment of the existing property, like a new look and feel of the interior or upgrade in the façade of the property. C3 is regarded as Capex.

### **C4 – Tenant Incentives**

### These expenses do not influence future rental income, like stepped rent or rent fee periods. Tenant incentives with an effect on future rental income are dealt with in MAPP 505.02. Works that are part of the negotiations we have with tenants in the process of signing new leases or extending existing leases. Those works include a tenant fit out, relocation of a tenants or split of a unit. C4 is regarded as Capex

### **C5 – Extensions**

### Expenses for an extension to an existing property, by which we enlarge the property and essentially construct more GLA's. C5 is regarded as Capex

### Expected booking for incurring capex

![capex booking.jpg](/sites/Wiki/PublishingImages/Paginas/Capital%20Expenditures/capex%20booking.jpg)

### Each transaction booked as capex needs to be assigned to proper capex id for capex reporting build up in BO. 

## **What is capex id?**

### Capex id is a generic code assigned to budget lines which approved by shareholder. E.g. shareholder has agreed capex budget for FY2018 for 400k for C01 but there are several components of this budget. Each specific line described as capex line item and assigned unique capex id. Looks like 'C01_2018_DEBP936_146'. Capex id's maintained in reporting Hub

## **How can we assign capex id to Purchase Order?**

### There is 2 way to assign capex id to a purchase order

- **Selecting capex id from drop down list during creation of purchase orders**
- **Linking po vs capex id via reporting hub. (this overwrites first bullet too)
**

### After this all invoices booked under this PO will be assigned to capex id automatically.

## **How can we assign capex id to existing transaction? (without PO)**

### Even we don't expect to see manual transactions and invoices without purchase orders capex id can be assigned to these lines via updating external reference 3 on specific line. 

## **Do we have to assign capex id to each and every transaction in 1111 account?**

### In principle yes. However, we don't expect to see capex id on valuation bookings which needs to be booked el5 = C99

| **[Multi Wiki](/sites/Wiki/Paginas/Multi%20Wiki.aspx) ** | **[Accounting Manual](/sites/Wiki/Paginas/Accounting%20Manual.aspx) ** | **[System Setup](/sites/Wiki/Paginas/System%20Setup.aspx)** |
|---|---|---|
