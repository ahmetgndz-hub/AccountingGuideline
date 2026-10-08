---
title: "C11 Dummy and suspence accounts"
source_file: "C11 Dummy and suspence accounts.aspx"
sharepoint: "https://multieu.sharepoint.com/sites/Wiki/Paginas/C11 Dummy and suspence accounts.aspx"
contact: "Ahmet Gunduz"
categories: ""
converted: 2026-10-08
status: old-wiki
---

# C11 Dummy and suspence accounts

### In principle each and every transaction we booked in system should be link to proper element6 (employee, debtor, creditor, bank etc.) to make readable for every stake holders. However there are some exemptions which we cannot assign element 6 as follows

- **Property valuation bookkeeping (with combination 11111 and 054 movement code and 4331X)**
- **ERV booking (41101 and 41111 accounts)**
- **Current year net result bookkeeping (21180, 21210, 9998) **
- **Vacancy (41130)**
- **Some equity accounts (21130,21140,21170)**
- **Depreciation accounts (11xx3 with movement code 015, 045 and 130 / 42910,42911,44910,53910)**
- **FX result from un realized revaluation (52825, 54825)**
- **Deferred tax (11605,25511,53300)**
- **Current tax (27570, 53100,53900**

### Besides that all transactions which booked dummy accounts or suspense account and has not been matched will be shown on this list and needs to be cleaned up before each month closing. 

### ![C11 Control and dummy.jpg](/sites/Wiki/PublishingImages/c11-dummy-and-suspence-accounts/C11%20Control%20and%20dummy.jpg)

### few examples from above print screen are

### point1 share capital should be always in line with trade registry and assigned to proper element6

### point2 suspense account needs to be matched and cleaned before q closing. (in this case is 0 but has not been matched)

### point3 tax accounts has been assigned to dummy element6. 

| [Control Document](/sites/Wiki/Paginas/Control%20file.aspx) | [Accounting Manual](/sites/Wiki/Paginas/Accounting%20Manual.aspx) | [Multi Wiki](/sites/Wiki/Paginas/Multi%20Wiki.aspx) |
|---|---|---|
