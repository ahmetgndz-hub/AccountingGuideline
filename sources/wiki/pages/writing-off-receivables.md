---
title: "Writing off Receivables"
source_file: "Writing off Receivables.aspx"
sharepoint: "https://multieu.sharepoint.com/sites/Wiki/Paginas/Writing off Receivables.aspx"
contact: "Ahmet Gunduz"
categories: ""
converted: 2026-10-08
status: old-wiki
---

# Writing off Receivables

### As Multi, we are generally hesitant in writing off receivables, as in writing off, we lose track of receivables in our Management Books (MAN). We only write off the receivable when all the below conditions or actions have been taken.

### Writing off receivables requires a Write off Approval Form (WAF) (2.3-16) ([https://multieu.sharepoint.com/sites/BSF/SitePages/2.3-Lease-contract-to-cash.aspx](https://eur01.safelinks.protection.outlook.com/?url=https://multieu.sharepoint.com/sites/BSF/SitePages/2.3-Lease-contract-to-cash.aspx&data=04%7c01%7cagunduz%40multi.eu%7c52084ae30d994701f9ad08d88c6f3494%7cebbd3cdca8e64e55b6add15663769232%7c0%7c0%7c637413756544015892%7cUnknown%7cTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7c1000&sdata=0mUM/UHlns457l1D81pEm6I87FHW%2B0L6U5gmWtCoRK4%3D&reserved=0)) which is signed off by the Asset Manager, Country MD, and FD. Write-offs exceeding (individual or in aggregate) EUR 100,000 require additional approval by the Multi's Group CFO.

## **Conditions**

| **Criteria ** | **Current policy** |  |
|---|---|---|
| **The financial condition of the tenant ** | **Tenant is deemed insolvent by a Court Procedure or otherwise external evidence ** | **Must ** |
| **Proceeding** | **Proceeding against the tenant, or the group where the tenant belongs to, to collect the receivable, or decided from a cost/benefit assessment not to start a proceeding.** | **Judgment ** |
| **Securities provided** | **The bank guarantee / (rental) deposit, cheques, etc. have been thoroughly used for settlement of the receivable. ** | **Must** |
| **VAT collection** | **All VAT was prepaid to the local taxation authorities on the outstanding receivable, if any, has been recovered from the tax authorities to the maximum extent.** | **Must** |
| **Presence of the tenant in the shopping center** | **The tenant has already vacated the shopping center. When the tenant is still in the center, we increase collection efforts.** | ** Must ** |
| **Number of days outstanding** | **The receivable is more than 720 days overdue.** | **n/a ** |

### For example, bookkeeping for written-off receivables is as follows. 

    | Writing off receivable  |  |
|---|---|
| d/c | el4 | el6 | el8 | ref3 | amount |
| dr | 13113 | tenant | 410 | lease ref | 60 |
| cr | 42593 | tenant |  | lease ref | (60) |
| cr | 13111 | tenant |  | lease ref | (60) |
| dr | 42594 | tenant |  | lease ref | 60 |

| **[Multi Wiki](/sites/Wiki/Paginas/Multi%20Wiki.aspx) ** | **[Accounting Manual](/sites/Wiki/Paginas/Accounting%20Manual.aspx) ** | **[System Setup](/sites/Wiki/Paginas/System%20Setup.aspx)** |
|---|---|---|
