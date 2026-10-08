---
title: "Tax codes"
source_file: "Tax codes.aspx"
sharepoint: "https://multieu.sharepoint.com/sites/Wiki/Paginas/Tax codes.aspx"
contact: "Ahmet Gunduz"
categories: ""
converted: 2026-10-08
status: old-wiki
---

# Tax codes

### As part of unification of accounting and easiness of direct cash flow creation from BO we have agreed to use following standard structure on tax accounts.

T                      stands for tax
DE                   stands for Country code
S, P, A, L           Sales, Purchase. VAT Asset, VAT Liability
00                    For determining percentage of tax (99 for payable or deferred)

However, this is only applicable for VAT of incoming and outgoing vat. In settlement, there should be such a logic to determine VAT deferred or payable as well. Currently TDE99 using for vat liability and payable and hard to determine in direct cash flow setting. VAT asset and VAT liability codes already created in coda for each country and this element6 needs to be used at each month end (or declaration period) purchase and sales vat reclassed to proper account and matched. 

| **[Multi Wiki](/sites/Wiki/Paginas/Multi%20Wiki.aspx) ** | **[Accounting Manual](/sites/Wiki/Paginas/Accounting%20Manual.aspx) ** | **[System Setup](/sites/Wiki/Paginas/System%20Setup.aspx)** |
|---|---|---|
