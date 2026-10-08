---
title: "Tenant Guarantees"
source_file: "Tenant Guarantees.aspx"
sharepoint: "https://multieu.sharepoint.com/sites/Wiki/Paginas/Tenant Guarantees.aspx"
contact: "Ahmet Gunduz"
categories: ""
converted: 2026-10-08
status: old-wiki
---

# Tenant Guarantees

## **Tenant Guarantee**

### A Tenant Guarantee is a guarantee that the tenant needs to supply according to the lease agreement. 
The tenant guarantee information will be used to calculate [bad debt calculation](/sites/Wiki/Paginas/Bad%20debt%20provisions.aspx) as well as tenant exposure and QAR reporting. 

### Guarantee types recognized in Multi as follows 

| Guarantee type |  SCoA for bookkeeping |  Security level  (1 Most Secure, 5 Least Secure) |
|---|---|---|
| **G01 Bankers Guarantee G02 Check G03 Company Bond G04 Company Guarantee G05 Cash Deposit for Utilities G06 Cash Deposit G07 Holding Guarantee G08 Legal Deposit G09 Letter of Credit G11 Notarial agreement G12 Other G13 Personal Guarantee G14 Promissory Note ** | **[99100](/sites/Wiki/Paginas/99100.aspx) [99100](/sites/Wiki/Paginas/99100.aspx) [99100](/sites/Wiki/Paginas/99100.aspx) [99100](/sites/Wiki/Paginas/99100.aspx) [25550](/sites/Wiki/Paginas/25550.aspx) [25550](/sites/Wiki/Paginas/25550.aspx) [99100](/sites/Wiki/Paginas/99100.aspx) [99100](/sites/Wiki/Paginas/99100.aspx) [99100](/sites/Wiki/Paginas/99100.aspx) [99100](/sites/Wiki/Paginas/99100.aspx) [99100](/sites/Wiki/Paginas/99100.aspx) [99100](/sites/Wiki/Paginas/99100.aspx) [99100](/sites/Wiki/Paginas/99100.aspx) ** | **2 4 4 4 1 1 3 2 2 1 3 5 5 ** |

 **[Liquidation of cash guarantees](/sites/Wiki/Paginas/Liquidation%20of%20cash%20guarantees.aspx)**

## **Tenant guarantee check**

### To make sure that the tenant guarantees are received according to the lease agreements the guarantees are recorded in Horizon and Coda.
Horizon: Guarantee to be received according to the lease agreement.
Coda: Guarantee received from the tenant.
To do a check between expected and received guarantee a BO report is created (see below).

## **Horizon**

### In Horizon various fields need to be filled per lease with the tenant guarantee data according to the lease contract (so the tenant guarantee that should be provided). In the below screenshot of Horizon the data that is important for the tenant guarantee check is highlighted in yellow. 
Under 'Deposit Type' the option 'additional guarantee' can't be used, always choose which kind of deposit should be received.

![HZN.png](/sites/Wiki/PublishingImages/Paginas/Tenant%20Guarantees/HZN.png)
 

## **Coda **

### There are 2 accounts used for storing tenant guarantees information in coda with split cash and non-cash. Important that the following fields used during bookkeeping.

### **Cash Guarantees**

- **Booking should be made to [25550](/sites/Wiki/Paginas/25550.aspx) account;
**
- **External reference 3 should be filled as lease id in the horizon (e.g. 00002852);
**
- **Dummy property code shouldn't be used for el2.
**

### **Non-Cash Guarantees**

- **Non-cash guarantees can be booked via a special CodaXL, the CodaXL/ITD are shared via the general folder for CodaXL of FAM .
**
- **Document code: the year 2019 and before: GE-JV-MAN-GU (excluding workflow) / from year 2020 NF-Guarantee (workflow)
**
- **Booking should be made to [99100](/sites/Wiki/Paginas/99100.aspx) account as off-balance sheet;
**
- **Due date should be filled as due date of guarantee. If due date is unlimited, please use 31/12/2099;
**
- **Document date should be issue date of guarantee; 
**
- **Serial number of guarantees should be recorded as document number (e.g. BLoG serial number).
**

 

## **BO Report**

### The BO report for the 'Tenant guarantees' can be found under Country – All – Lease management – Deposits and guarantees (agreed/received). In this report the data imported before to Coda and filled in Horizon comes together in one report. From Horizon the data will be loaded of the tenant guarantees we should receive according to the lease contract and in Coda the tenant guarantees are uploaded that are received from the tenants.

### The BO report exists of the following sheets: Tenant guarantee, no deposit, with deposit, due date approaching, different deposit, no horizon. In these sheets various checks are made between the data of Horizon and Coda. See below after the variables an explanation per sheet.

- Tab1 Tenant Guarantee: **On the sheet 'Tenant guarantee' a total overview of all the guarantees that are filled in Horizon are presented. On the left side of the report all the data from Horizon is presented and on the right side the data from Coda regarding the specific guarantee is shown.
**

- Tab2 No deposit: **On the sheet ‘No deposit’ all the leases are shown where in Horizon is shown that a guarantee should be provided by the tenant, but no guarantee has been provided (according to the information in Coda)
**

- Tab3 With deposit: **On the sheet ‘With deposit’ all the leases are shown where in Horizon is shown that a guarantee should be provided by the tenant and a guarantee is provided according to Coda. On the right side in the Coda section a check is done between the provided amount of the tenant guarantee as filled in Horizon and Coda (see screenshot below) If the calculation field shows an amount, this can mean that the provided guarantee according to Horizon is not in line with the guarantee in Coda. Or the data in Horizon or Coda is not filled completely
**

>

 ![guarantee2.png](/sites/Wiki/PublishingImages/Paginas/Tenant%20Guarantees/guarantee2.png) 

- Tab4 Due date approaching:** On the sheet 'Due date approaching' all the tenant guarantees are presented that are due within the upcoming 8 months.**
- Tab5 Different deposit: **On the sheet 'Different deposit' a check is done on the deposit type between Horizon and Coda. If a different deposit type is selected in Horizon and Coda it will show in this sheet
**
- Tab6 No Horizon: **On the sheet No Horizon amounts are shown that are booked in Coda on the tenant guarantees but are not matching with any lease in Horizon
**

 

# Extensive manual 

### Below a more extensive manual regarding processing guarantees and maintenance can be found:

 

## **Import file off-balance tenant guarantees (Coda)**

###  Below a description of the use of the import file for the **off-balance** tenant guarantees.

### **Use of the Excel import file**

###  The Excel import file will be used to import the tenant guarantee information into Coda (link to template above).
 The information that is imported into Coda are the tenant guarantees that are actually provided to property.

###  In column B till R of the Excel file the data of the tenant guarantees need to be filled per lease reference (column H). See ‘Variable Excel import file’ for more information per column.

###  After filling the data in the columns, the import to Coda can be done via CodaXL. In hidden rows in the Excel document the data is converted to the proper format for a CodaXL document.
 Importing the data works as a regular CodaXL through the ‘Journal Loader Process’.

![journal.png](/sites/Wiki/PublishingImages/Paginas/Tenant%20Guarantees/journal.png)

### **Variables import file**

### In the import file various columns need to be filled, see yellow marked columns in the CodaXL.

### *Property code/Property name (column B):*
All the property codes are included in the import file, the name of the property will automatically be found after filling the property. The name field is optional as Coda will find the name after import.

### *'Guarantee for' (column D):*
The following options are available via a dropdown menu:

- **G51 Rent/Marketing/Service Charge**
- **G52 Rent
**
- **G53 Service Charges**
- **G54 Utilities

**

### *'Guarantee via' (column E):*
The following options are available via a dropdown menu:

- **G01 Bankers Guarantee
**
- **G02 Check**
- **G03 Company Bond**
- **G04 Company Guarantee**
- **G05 Cash Deposit for Utilities**
- **G06 Cash Deposit**
- **G07 Holding Guarantee**
- **G08 Legal Deposit**
- **G09 Letter of Credit**
- **G10 No Deposit applicable**
- **G11 Notarial agreement
**
- **G12 Other
**
- **G13 Personal guarantee**
- **G14 Promissory Note
**

### *Tenant code / name (column F,G):*
Tenant code is a mandatory field to link the guarantee to the correct tenant. 
Tenant name is an option to fill, Coda will pick the name based on the tenant code in Coda.

### *Lease ref (column H):*
Lease ref code to be filled, this code is used to make the match with the Horizon data. Pay attention to the 8-digit format, to be in line with Horizon.

### *Effective date of guarantee (column I):*
Date that the guarantee became effective. 

### *Due date of guarantee (column J):*
Date that the guarantee will expire.

### *Serial number (column K):*
If applicable fill the external reference number of the guarantee.

### *Guarantor (column L):*
Name of the bank, parent, company, person, etc who is providing the guarantee.

### *Currency (column M):*
Applicable currency of the guarantee.
The following options are available via a dropdown menu:

- **EUR**
- **USD**
- **YTL**
- **PLN**
- **HUF**
- **GBP**
- **UAH
**

### *Amount (column N):*
Amount of the guarantee, in the currency the guarantee is provided.

### *Description/comment (column O,P):*
A description or comment can be added.

### *Date of delivery (column Q):*
Date that the guarantee is provided. 

### First open date (column W)
Fill here the first 'open' date in Coda. (The last year open will be automatically filled based on the first 'open' date).

### Attachment (column U)
The supporting document (in PDF format) for the guarantee needs to be placed in the country attachment folder. 
For the this purpose a specific subfolder is created in the attachment folder named: GU.

### Proposed logic for the filename: EL1/number/name.pdf – SKB001_16_TNT.PDF or EL2/number/name.pdf - SKBP001_16_TNT.PDF.

### In the CodaXL only the PDF name (example SKB001_16_TNT.PDF) needs to be place in the cell. 
The link to the location on the server is generated automatically.

### **Checks in the CodaXL**

### In the CodaXL there are 2 checks build in to support filling the data for uploading.

### Columns R/S (orange cells): The first open date/period is 1-1-2020/2020 in the example, the effective date is filled with 31-12-2025, so the guarantee will be booked in 2025 period 12.
 The cell will be highlighted orange if the effective date of the guarantee is in a later year then the first open date/period. This is a warning to be checked, but could be correct.

### Column I/J (red cells): If the due date is an earlier date then the effective then the due date cell will be red. This check should be solved as the due date can’t be earlier then the effective date.

![checkguarantee.png](/sites/Wiki/PublishingImages/Paginas/Tenant%20Guarantees/checkguarantee.png) 

### **Restriction import file**

### The import file is restricted to import 400 guarantees in one time.
If you need to import more than 400 guarantees, then upload the guarantees in multiple sessions.

## **Maintenance of the off-balance tenant guarantees (Coda)**

### If off-balance tenant guarantees expire the bookings in Coda need to be updated.
 As all the off-balance tenant guarantees are imported on one EL4 99100 ‘Tenant Guarantees’, expired tenant guarantees can be cleared by matching the booking made on this EL4.
 No counter booking needs to be made to reverse the guarantee, Coda will match the different EL5’s that are used automatically.

### A specific matching master is created for matching on this account (available in every country). The following steps need to be followed to match/delete a specific tenant guarantee in Coda.

### *Step 1:*

![11.png](/sites/Wiki/PublishingImages/Paginas/Tenant%20Guarantees/11.png)

### *Step 2:*
Select date and period of matching:

![12.png](/sites/Wiki/PublishingImages/Paginas/Tenant%20Guarantees/12.png) 

### *Step 3:*
Fill property and Counterparty if you want to cancel a specific tenant guarantee.

![13.png](/sites/Wiki/PublishingImages/Paginas/Tenant%20Guarantees/13.png) 

### Both folder 1 and 2 need to be filled. This can be used to fill different variables, but if you need to match only 1 guarantee just fill the same variables in both folders.

### *Step 4: *
Select the items to match, press include selected and then disperse.

![14.png](/sites/Wiki/PublishingImages/Paginas/Tenant%20Guarantees/14.png) 

### In this matching master EL4 is fixed on 99100 and EL2/6 are mandatory to be filled.

## **Processing cash guarantees in Coda**

### Cash guarantees (G05/G06) need to be booked on the balance on EL4 25550 (Received guarant. & deposits N.C.). Use of different EL5's is not restricted.
 It's important to use this specific EL4 as it is picked up by the BO-reports.

### *Example:*
 EL4 13311 Bank                                                                            € 10.000
 To/      EL4 25550 Received guarant. & deposits N.C.                   € 10.000

### On the amount booked on EL 25550 also 'External reference 3' needs to be filled in Coda with the lease reference (8-digit number).

### Adding 'External Reference 3' to cash guarantees

### Follow the steps below to add the lease reference to 'External reference 3' in Coda.

### *Step 1:*
Go to browse details:

### ![1.png](/sites/Wiki/PublishingImages/Paginas/Tenant%20Guarantees/1.png)
 

### *Step 2:*

### Select the entity, optional property code, SCoA and counterparty.

![2.png](/sites/Wiki/PublishingImages/Paginas/Tenant%20Guarantees/2.png)
 

### *Step 3:*
Click on actions of the transaction where you want to update the External reference 3.
![3.png](/sites/Wiki/PublishingImages/Paginas/Tenant%20Guarantees/3.png)

### *Step 4:*
Click on ‘View/Edit line’

![4.png](/sites/Wiki/PublishingImages/Paginas/Tenant%20Guarantees/4.png)

### *Step 5:*
Go to the sheet References, fill the lease reference in the box ‘External Reference – 3’ and press ‘Save Changes’. 

## ![5.png](/sites/Wiki/PublishingImages/Paginas/Tenant%20Guarantees/5.png)

| **[Accounting Manual](/sites/Wiki/Paginas/Accounting%20Manual.aspx)** | **[Multi Wiki](/sites/Wiki/Paginas/Multi%20Wiki.aspx)** |
|---|---|
