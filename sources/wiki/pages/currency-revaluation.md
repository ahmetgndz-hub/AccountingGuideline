---
title: "Currency revaluation"
source_file: "Currency revaluation.aspx"
sharepoint: "https://multieu.sharepoint.com/sites/Wiki/Paginas/Currency revaluation.aspx"
contact: "Ahmet Gunduz"
categories: ""
converted: 2026-10-08
status: old-wiki
---

# Currency revaluation

# Currency Revaluation logic in Coda

### For sake of consolidation Multi has intention to convert all transactions to EUR (as reporting currency) to achive this following logic set-up in sytem to reflect logic to financials. Besides that every single transaction automaticly calculates home (country local currency) and dual values (group reporting currency) during transaction booking. On top of this monetary items needs to be revaluated with following logic. 

## **Non EUR + Functional Currency EUR countries (PL, TR, HU)**

- **Monetary items (4CURREV account group)
**

  - **Document currency x document value to Home value 
**
  - **Document currency x document value to Dual Value (EUR)**

- **Tax Monetary items (4CURREV-TAX account group)
**

  - **Home value to Dual Value (assuming that taxes always payable in local currency)**

## **Non EUR + Functional Currency Local currency countries (GB, UA, CZ, CH)**

- **Monetary items (4CURREV account group)**

  - **Document currency x document value to Home value**

-
- Tax Monetary items (4CURREV-TAX account group)

  - Home value to Dual Value (assuming that taxes always payable in local currency)

## **EUR countries (NL, BE, IE, SK, LV, IT, DE, PT, ES, CY, HQ)**

- **Monetary items (4CURREV account group)
**

  - **Document currency x document value to Home value
**

| **[Multi Wiki](/sites/Wiki/Paginas/Multi%20Wiki.aspx) ** | **[Accounting Manual](/sites/Wiki/Paginas/Accounting%20Manual.aspx) ** | **[System Setup](/sites/Wiki/Paginas/System%20Setup.aspx)** |
|---|---|---|
