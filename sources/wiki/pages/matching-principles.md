---
title: "Matching principles"
source_file: "Matching principles.aspx"
sharepoint: "https://multieu.sharepoint.com/sites/Wiki/Paginas/Matching principles.aspx"
contact: "Dennis Pieterson"
categories: ""
converted: 2026-10-08
status: old-wiki
---

# Matching principles

#  Matching principles in Unit4 Financials / Coda

### In this matching guideline the general matching principals are explained and how to handle credit notes and back invoices.
 To support in a proper matching in Coda and accurate presentation of data in reporting.

## **General principals**

### Goals of matching:

### Improve the quality of accounting

- **Follow which debtors paid their invoices;**
- **Follow which invoices are paid to creditors;**
- **For accruals/suspense accounts to show clean outstanding balance positions.**
- **Show correct FX results when foreign currencies are applicable;**

### By improving the quality of accounting, also improving the quality of reporting;

- **Making it possible to atomize reporting;**
- **For example: generating a cashflow report based on data from the accounting system.**

### To be able to determine what is being paid, with a specific payment we use the following general principles of matching.

### General principles of matching:

- **General:**

  - **Matching to be done per EL1/2/3/4/5/6;**
  - **EL1 till EL6, should be the same and in balance before matching.**
  - **Matching to be done and with the date (and period) of the received/outgoing payment/when settling or write off takes place.**

- **Invoices:**

  - **One invoice can be matched with multiple payments (if paid in instalments/part matching);**
  - **Multiple invoices can be matched with one payment (debtor pays multiple outstanding invoices with one bank transaction).
**

### **Example of matching 1 payment, with 1 invoice.**
 Matching done on 2 lines (1 payment, 1 invoice) with all same elements 1 till 6.

![Matching_01.PNG](/sites/Wiki/PublishingImages/Paginas/Matching%20principles/Matching_01.PNG)

### ![image]() 

### **Example of matching 1 payment, with 1 invoice of foreign currency with Euro FX difference.**
 Matching done on 2 lines (1 payment, 1 invoice) with all same elements 1 till 6. Matching is done on the document currency PLN, amounts in PLN reconcile so full payment, due to FX changes the amount in Euro is not equal.
 So the matching creates a disperse booking for the FX difference to the P&L.

![Matching_02.PNG](/sites/Wiki/PublishingImages/Paginas/Matching%20principles/Matching_02.PNG)

 **Invalid matching**

### In the books we see various possibilities passing by that are not in line with the described general matching principals:

- **Multiple EL1's (different entities) are matched in 1 match;**
- **Multiple EL3's (different books) are matched in 1 match;
**
- **Multiple EL6's (debtors/creditors/relations) are matched in 1 match;**
- **Matching date is not in line with matching year/period of time transaction;**
- **Amount received on bank and booked on debtor in different period then matching took place (amount received in March, matched in April, invoice will be registered as paid in April)**
- **Bank payment booked on creditor in different period then matching took place (payment booked in March, matched in April, invoice will be registered as paid in April) **
- **Multiple bank payments are matched with multiple invoices (not clear anymore which payment belongs to which invoice)**
- **Etc.**

### These kinds of matchings may cause differences in the outcome of reporting and are very time consuming to find the issue and solve.
After the explanation about 'Credit notes / back invoices' some examples are added to show the effects of the invalid matching.

## **Credit notes / Back invoices**

### Below a working instruction is prepared how to handle matching of credit notes and back invoices.
 For credit notes / back invoices we expect the following order of matching:

1. **Invoice sent to the debtor;**
1. **Debtor pays the invoice;**
1. **Credit note sent regarding original invoice;**
1. **The credit note should be matched against the original invoice;**
1. **Balance amount should exist on the payment of the tenant (if applicable);**

### For step 4, in the situation that the invoice is already paid, and the payment is matched to the invoice.
First the payment needs to be unmatched from the invoice, then credit note will be matched to the invoice.
If a balance amount of the invoice is left on the invoice after the credit note, part of the payment can be matched to the invoice.

### Below two examples are created of the expected matching as descripted above and what mainly is seen in the books at the moment (current matching).

### **Example 1:**

![Matching_03.PNG](/sites/Wiki/PublishingImages/Paginas/Matching%20principles/Matching_03.PNG) 

###  * Current matching:

1. **Payment of 80 is matched with the outstanding invoice of 100. (balance amount 20).**
1. **Credit note of 50 is matched with the outstanding invoice of 20. (balance amount -30).**
1. **Outstanding balance amount is -30 on the credit note.
**

### ** Expected matching

1. **Credit note of 50 is matched with the outstanding invoice of 100. (balance amount 50).**
1. **Payment of 80 is matched with the outstanding invoice of 50. (balance amount -30).**
1. **Outstanding balance amount is -30 on the payment.**

### The difference between the 2 ways of matching is that in the first option we are left with a balance amount on the credit note and with the second option a balance amount is left on the payment.
 In the books we would like to see the outstanding amount on the payment.

### **Example 2:**

### In below example the impact on the collection rate is shown:
Current matching:

![Matching_04.PNG](/sites/Wiki/PublishingImages/Paginas/Matching%20principles/Matching_04.PNG) 

### Invoice amount is reduced by the Credit note, but full payment is taken in account in the calculation as the amount is matched with the invoice. Causing a collection rate of 300%.

### Expected matching:

![Matching_05.PNG](/sites/Wiki/PublishingImages/Paginas/Matching%20principles/Matching_05.PNG)

### In this example the Credit note is first settled with the original invoice, lowering the invoice amount. The payment is matched with the balance amount of the invoice, the overpayment is left as outstanding amount. 

###  This overpayment doesn’t count as payment off the invoice, so is not influencing the collection ratio calculation which shows now an expected 100%.

## **Examples of invalid matching**

### **Matching multiple elements 4**
In the below match 1 EL6 is matched, but outstanding amounts on different EL4.
 As can been seen by the last 2 lines (z-disperse bookings), Coda makes an automatic booking to balance the matching on EL4. Mistakes are easily made by this kind of matching and Coda makes automatic journals on the background, this will be hard to follow/check, that’s why we see this kind of matching as invalid.
In this situation first a journal needs to be made from 131111 to 25550 to balance the EL 6 per EL4. After that 2 matches are made 1 per EL4, to match the amounts on EL6 level.

![Matching_06.PNG](/sites/Wiki/PublishingImages/Paginas/Matching%20principles/Matching_06.PNG)

### **Matching multiple elements 6**
Same kind of example as above, only in this situation a match is done including different EL6 on the debtor position.
Coda makes an automatic booking to balance the amounts on EL6. In this situation it could also happen that a payment from debtor A is matched with the invoice of debtor B. After this match it will be hard to trace what happened and will cost a lot of time. In this situation also first, a journal needs to be made to balance the amounts in the individual EL6 and then a match needs to be made per EL6.

![Matching_07.PNG](/sites/Wiki/PublishingImages/Paginas/Matching%20principles/Matching_07-1.PNG)

### **Matching multiple EL4 and EL6**
Below an example of a match with multiple EL4 and EL6. This combination is causing 3 disperse lines to balance on the EL4 and then on the EL6. Afterwards it very hard to follow why these different EL6 are matched with each other especially as the matching goes through 2 balance positions.

![Matching_08.PNG](/sites/Wiki/PublishingImages/Paginas/Matching%20principles/Matching_08.PNG)

### **Matching multiple bank documents with multiple invoices**
In below example multiple bank payments to a creditor are matched with multiple outstanding invoices.

### By matching all these lines in 1 go it is not possible anymore to follow which payment is done for which invoice.

![Matching_09.PNG](/sites/Wiki/PublishingImages/Paginas/Matching%20principles/Matching_09.PNG)

### **Matching date before document date of the bank document**
Matching date is a date before the actual payment, this match says that the invoice is paid before the bank transfer was done. As the status of invoices is followed by matching, these invoices show paid to early.

![Matching_10.PNG](/sites/Wiki/PublishingImages/Paginas/Matching%20principles/Matching_10.PNG)

### **Matching date in different period then timing of settlement booking**
The settlement transaction of outstanding invoices with a deposit was made in 2019/8, matching was done in 2020/3. Invoices are shown as settled in 2020/3 instead of in the period when the settlement took place in 2019/8.

![Matching_11.PNG](/sites/Wiki/PublishingImages/Paginas/Matching%20principles/Matching_11.PNG) 

## **Control file**

###  In the accounting control file, a check on matching quality is created. This is control C29. Please see below link for more information:

### [C29 Matching quality](/sites/Wiki/Paginas/C29%20Matching%20quality.aspx)

 

| **[Multi Wiki](/sites/Wiki/Paginas/Multi%20Wiki.aspx) ** | **[Accounting Manual](/sites/Wiki/Paginas/Accounting%20Manual.aspx) ** | **[System Setup](/sites/Wiki/Paginas/System%20Setup.aspx)** |
|---|---|---|
