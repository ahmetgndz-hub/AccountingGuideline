---
title: "C29 Matching quality"
source_file: "C29 Matching quality.aspx"
sharepoint: "https://multieu.sharepoint.com/sites/Wiki/Paginas/C29 Matching quality.aspx"
contact: "Dennis Pieterson"
categories: ""
converted: 2026-10-08
status: old-wiki
---

# C29 Matching quality

# C29 Matching quality

The control matching quality is looking at the quality on matching done on the outgoing and incoming invoices/banktransactions.
For now, it's only looking at the external invoices, so SCoA 13111 Trade receivable non-group and 27310 Trade payables non-group are checked in this control.

For invoices we expect the following matching:

- 1 invoice against multiple bank lines;
- 1 bank line against multiple invoices (same debtor/creditor)

The report will give a warning if matching is performed that is not in line with above, for example in the following situations:

- Multiple elements 1 (different entities) are matched in 1 match.
- Multiple elements 3 (different books) are matched in 1 match.
- Multiple elements 6 (debtors/creditors) are matched in 1 match.
- Matching date is not in line with matching year/period.
- Amount received on bank and booked debtor in different period then matching took place (amount received in March, matched in April)
- Bank payment booked on creditor in different period then matching took place (payment booked in March, matched in April)

Example of report:

![matchingq.JPG](/sites/Wiki/SiteCollectionImages/c29-matching-quality/matchingq.JPG) 

| **[Control file](/sites/Wiki/Paginas/Control%20file.aspx)** | **[Accounting Manual](/sites/Wiki/Paginas/Accounting%20Manual.aspx)** | **[Multi Wiki](/sites/Wiki/Paginas/Multi%20Wiki.aspx)** |
|---|---|---|
