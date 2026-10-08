---
title: "Bad debt provisions"
source_file: "Bad debt provisions.aspx"
sharepoint: "https://multieu.sharepoint.com/sites/Wiki/Paginas/Bad debt provisions.aspx"
contact: "Ahmet Gunduz"
categories: ""
converted: 2026-10-08
status: old-wiki
---

# Bad debt provisions

### For the calculation of the bad debt provision the below described Multi/BX policy is created to be processed in the MAN books.

## **Accounting policy**

### For the accounting policy of the bad debt provision, we are not looking at the single receivables of the tenant but at the overall financial condition or relationship of/with the tenant.
A provision is created if 1 of the receivables exceeds 60 days overdue;

### This provision is created for the full outstanding amount of this tenant, taking into account below;

- **Invoices send for future periods should be excluded from the bad debt calculation;
**
- **Exceptional situations like invoices send in Covid-19 period with manually extended due dates to be excluded from the bad debt calculation (allowed exceptions will be communicated by HQ);
**
- **Guarantees with security level 1 and 2, can be deducted on the calculated provision;
**

  - **If a guarantee from security level 1 or 2 are deemed not to be secure, they can be excluded from the calculation.
**

### If there is need to apply a more strict policy then above, for example in the situation that is foreseen that issues in collection will occur.
Then the country FD can decide to apply a more strict policy and create a provision which wouldn't be needed following above guidelines.

### **Exemptions to be less strict**

### Country FD's can use their own discrection to be 'less strict' compared to the above described policy, this is only allowed if both below criteria are fulfilled:

1. **There needs to be prove why the policy should be applied less strict on a tenant;
**
1. **The decision to be less strict needs to be confirmed by documentation/mail with HQ (pre-approval needed from Group-FD or CFO).
**

### If above criteria are not met, the policy as above needs to be followed without exemption.

### **Local gaap**

### Be aware that the above policy probably is not in line with local accounting regulations. 
To adjust the bad debt provision to the local regulations a correction in the LOC books can be made (see [Booking Structure](/sites/Wiki/Paginas/Booking%20Structure.aspx)).

## **Guarantees:**

### Guarantees with security level 1 and 2 are: 

- **Bankers guarantees;
**
- **Cash deposits (for utilities);**
- **Legal deposit;
**
- **Letter of credit;**
- **Notarial agreement;**

### All other types of guarantees are not allowed to be included in the bad debt calculation.
For more information about the tenant guarantees see: [Tenant Guarantees](/sites/Wiki/Paginas/Tenant%20Guarantees.aspx)

## **Examples**

![2020-07-08_18-07-05.jpg](/sites/Wiki/PublishingImages/Paginas/Bad%20debt%20provisions/2020-07-08_18-07-05.jpg)

### Tenant A: No need to book a provision as the full receivable is within 60 days overdue.

### Tenant B: Full receivable is provided for, as a part of the receivable is overdue for more than 60 days. As there are no securities in place, the full balance is shown in provision for bad debtors

### Tenant C: Full receivable is provided for, as a part of the receivable is overdue for more than 60 days. We decrease the Provision by the securities that are in place. 

>

>

### (Provision = 110 gross receivable minus 75 of securities, equals 35)

### Tenant D: Full receivable is provided for, as a part of the receivable is overdue for more than 60 days. We decrease the Provision by the securities that are in place. We do not take corporate guarantees into account as

>

- **It is security from the same group where Tenant D belongs to, and there is apparently an issue;
**
- **A corporate guarantee is not directly accessible by Multi / BX;
**
- **Cheque is included in this calculation as they mainly will be cashed and transferred to cash deposits, in this situation we deem the cheque to be safe;**

>

### (Provision = 165 gross receivables minus 115 of securities, equals 50)

### Tenant E: Based on the ground principle, we would not book a Provision for Bad Debtors. However, we know that this tenant is in financial difficulty and the collection will be problematic.
Per the policy, we have the discretion to be stricter than the ground policy informing the provision. As such, we provide for the full amount.

(Provision = 60 gross receivable minus 0 (at discretion of Country FD), equals 60)

### Tenant F: Full receivable is provided for, minus the Cash deposit minus the bank guarantee.

>

### (Provision = 100 gross receivables minus 50 Cash deposit, equals 50)

### Note in this case, we do not include the Banking or Corporate Guarantee nor the Cheque as we doubt the collectability of the Guarantees and Cheque. The Cash deposit is a security that we can access anytime. This is an example where we have the discretion to be stricter than the ground policy).

## **Booking instructions**

### Example bookings of bad debt provision movements:

### **Bad debt provision**

| **Recognizing bad debt provision: ** |  |
|---|---|
| d/c | el4 | el6 | el8 | ref3 | amount |
| cr | 13113 | tenant | 440 | lease ref | (100) |
| dr | **42593** | tenant | n/a | lease ref | 100 |
| **Recovering bad debt within the same financial year: ** |
| d/c | el4 | el6 | el8 | ref3 | amount |
| dr | 13113 | tenant | 420 | lease ref | 40 |
| cr | **42593** | tenant | n/a | lease ref | (40) |
| **Recovering bad debt not in the same financial year: ** |
| d/c | el4 | el6 | el8 | ref3 | amount |
| dr | 13113 | tenant | 420 | lease ref | 40 |
| cr | **43000** | tenant | n/a | lease ref | (40) |

### **Write off receivable**

### Write off receivable with bad debt within same financial year:

| d/c | el4 | el6 | el8 | ref3 | amount |
|---|---|---|---|---|---|
| dr | 13113 | tenant | 410 | lease ref | 60 |
| cr | **42593** | tenant | n/a | lease ref | (60) |

| dr | 13111 | tenant | n/a | lease ref | (60) |
|---|---|---|---|---|---|
| cr | **42594** | tenant | n/a | lease ref | 60 |

### Write off receivable with bad debt not in the same financial year:

| d/c | el4 | el6 | el8 | ref3 | amount |
|---|---|---|---|---|---|
| dr | 13113 | tenant | 410 | lease ref | 60 |
| cr | **43000** | tenant | n/a | lease ref | (60) |

| dr | 13111 | tenant | n/a | lease ref | (60) |
|---|---|---|---|---|---|
| cr | **42594** | tenant | n/a | lease ref | 60 |

## **PQ Bad debt calculation**

### A control file is created to calculated and check the bad debt provision as described.
Contact the HQ accounting team to receive this file.

| **[Multi Wiki](/sites/Wiki/Paginas/Multi%20Wiki.aspx) ** | **[Accounting Manual](/sites/Wiki/Paginas/Accounting%20Manual.aspx) ** | **[System Setup](/sites/Wiki/Paginas/System%20Setup.aspx)** |
|---|---|---|
