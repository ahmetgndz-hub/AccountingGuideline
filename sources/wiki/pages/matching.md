---
title: "Matching"
source_file: "Matching.aspx"
sharepoint: "https://multieu.sharepoint.com/sites/Wiki/Paginas/Matching.aspx"
contact: "Ahmet Gunduz"
categories: ""
converted: 2026-10-08
status: old-wiki
---

# Matching

Description:

 

"Matching" is; to assign the "invoice produced as a result of a purchase/sales of a product/service" to the "payment made through the bank for that invoice". Matching should be done for all monetary items.

 

**Our goals from matching are:**

 

-          The information if the invoice is paid or not,

-          Real time and efficient follow-up of open(outstanding) balances of the debtors/creditors,

-          To know with which bank payment the invoice was paid with,

-          To monitor the payment performance of the debtors (through correct aging figures, calculate accurate bad debt provisions according to Multi policies),

-          In countries where the local currency is different than the reporting currency (in MULTI: EUR) to do the matching in the monetary items helps:

- Posting the realized foreign exchange difference to the related account while doing the matching,
- Posting the unrealized foreign exchange difference to the related account through currency revaluation process at end of periods.

 

**The accounts subject to matching in MULTI: **

All accounts having the exact same account codes can be subject to matching. But, it is more important to do the matching in all monetary items (ex. cash, marketable securities, accounts receivable, accounts payable, sales taxes payable, and notes payable).

 

**Issues to be considered while matching is done: **

- Account codes should be the same: El 1/2/3/4/5/6 (el2 can be ignored)

- 1 invoice can be matched with 1 bank payment.

 

Multiple invoices can be matched with 1 bank payment.

               

                1 invoice can be matched with multiple bank payments (partial matching), but,

multiple bank payments should **not** be matched with multiple invoices (no proper assignment can be done).

 

General rule is to match with a bank receipt.

But, an invoice can be matched with a credit invoice or by a discount invoice (taking into account the possible time differences).

 

There can be a JV (journal voucher) as a collection or an invoice posted to the account to be matched (ex. an amount reclassified from another account for correction both on invoice and payment sides).

Remark: all reclassifications concerning "ingoing-outgoing bank transactions" should be done using the specific document code: "JV-CFCORR" in coda; so that the cash-flow reports can detect them properly.

 

- In coda, there are different headings found under "General Ledger" (Matching-Assets / Matching Holding & Service) to be used for matching depending on the item to be matched and works with different master codes.

While matching is done, sub-headers have to be chosen properly.

 
![image](file:///C:/Users/agunduz/AppData/Local/Temp/msohtmlclip1/01/clip_image002.jpg)

![image](file:///C:/Users/agunduz/AppData/Local/Temp/msohtmlclip1/01/clip_image004.jpg)

**For AR (Accounts Receivable) matching; **

1)      If there is **a** specification/explanation by the sender either on the bank receipt or sent separately => must be taken into account for matching.

 

2)      If there is **no** specification/explanation by the sender either on the bank receipt or sent separately =>

 

1. Ideally; collection department will try to reach out the sender to find out the details for matching to ease the reconciliation process. 

 
1. If collection dept can't reach the sender or can't receive an explanation; it is better to leave the amount unmatched till a specification can be received.

Remark: Bad debt provision query will be taking into account this over payment amount while calculating bad debt provisions, so no need to match without knowing exactly.

If there is a partial matching; first of all rent base invoice is matched, then if there is a remaining amount, service invoice is matched.    

Matching should be done with the date (and period) of the received/outgoing payment when settling. If the period of posting concerning the payment has already been closed to posting, matching can be made to the 1st day of the open period.

**The different types of payment status in coda:   **

Once the invoices are approved in coda, the status of the invoice is "Available".

Till the matching is executed, the postings are labelled as "Available" and seen in account details when browsed.

When the matching is completed, the status is converted to "Paid".

The matching creates a disperse booking with "Z-DISPERSE" document code.

 

The following balance should be maintained at the end of matching (local or reporting currency: EUR) :

 

| Balance of an account | **=** | Line Items with status • Available • Held • Proposed • Payment suppressed | **+** | Line items with status • Paid • Cancelled AND **Payment Date > Reporting Date** |
|---|---|---|---|---|

 

**Frequency of matching:**

- For AR (Accounts Receivable) => on daily basis after posting the bank statements & before each Debtors Meeting so as to be able to follow correct outstanding balance on the AR accounts.

Daily matching is done by AR team, the main responsibility is with senior accountants.

- For AP (Accounts Payable) => on daily basis after posting the bank statements and before running the payment proposals so as to be able to follow correct outstanding balance on the AP accounts.

Daily matching is done by AP team, the main responsibility is with senior accountants.

- Other Balance Sheet accounts => on daily basis and specially before revaluation is to be done at the end of periods. The main responsibility is with senior accountants.

 

 

**Tips for follow-up of matching :**

 

- "Outstanding ledger" B.O. report is used for finding the list of available items to be matched by scoa, debtor/creditor. 

 

- In the accounting "Control File", a check on matching quality is created in tab "R C17c AP and AR match quality" to review.

 

What happens if the matching is not done properly in monetary items in entities having different local currency than Multi's reporting currency (EUR) or if the invoice and payment currency are different:

 

Ex: scoa 13111-Trade Receivables matching/different currencies

|  |  | Currency code | Document value | Home value TRL |  | Exchange rate EUR/TRL | Dual Value € |  |
|---|---|---|---|---|---|---|---|---|
| 5.4.22 | SI Invoice | EUR | 100 | TRL | + 1,000 | 10.00 | € | + 100 |
| 5.4.22 | BA collection | TRL | 1,000 | TRL | - 1,000 | 10.00 | € | - 100 |
|  | Exchange rate diff |  |  | TRL | 0 |  | € | 0 |

 

Matching should be done using the date of BA record -> 5.4.22 in the ex.

If the matching is not done with the date of 5.4.22, at the end of the month: 30.04.22, revaluation will be calculated on EUR invoice with exchange rate of ex. EUR/TRL 12; whereas the collection is still same as TRL 1.000. This will cause a foreign exchange rate loss of TRL 200 in P&L and unbalance the Balance Sheet.  So, the proper matching is vital.

                 

 

**Examples for VALID matchings**:

**Example of matching 1 payment with 1 invoice ->VALID **

Matching done on 2 lines (1 payment, 1 invoice) with all same elements 1 till 6.

 ![Checkmark with solid fill](file:///C:/Users/agunduz/AppData/Local/Temp/msohtmlclip1/01/clip_image006.png)![image](file:///C:/Users/agunduz/AppData/Local/Temp/msohtmlclip1/01/clip_image008.jpg)
![image](file:///C:/Users/agunduz/AppData/Local/Temp/msohtmlclip1/01/clip_image010.jpg)

**Example of matching 1 payment with 1 invoice of foreign currency with Euro FX difference ->VALID**

Matching done on 2 lines (1 payment,1 invoice) with all same elements 1 till 6.

Matching is done on the document currency GBP, amounts in GBP reconcile. For payment, due to FX changes, the amount in Euro is not equal. So, the matching transaction creates a disperse booking for the FX difference with Z-DISPERSE code to P&L.  
![Checkmark with solid fill](file:///C:/Users/agunduz/AppData/Local/Temp/msohtmlclip1/01/clip_image006.png)![image](file:///C:/Users/agunduz/AppData/Local/Temp/msohtmlclip1/01/clip_image012.jpg)![image](file:///C:/Users/agunduz/AppData/Local/Temp/msohtmlclip1/01/clip_image014.jpg)

Details of Z-DISPERSE booking :
![image](file:///C:/Users/agunduz/AppData/Local/Temp/msohtmlclip1/01/clip_image016.jpg)

 

**Examples of INVALID matchings : -Matching multiple element 4s -> INVALID**

In the below match1, EL6 is matched, but outstanding amounts on different EL4.

As can be seen by looking at the last 2 lines (Z-DISPERSE bookings), coda makes an automatic booking to balance the matching on EL4. This type of mistake can easily be made by this kind of matching; coda create automatic journals to make it difficult to follow-up/check, this is why this type of matching is invalid. In this situation correct matchings will be : first to reclass by a JV from 13111 to 25550 to balance the EL6 per EL4. Then, 2 matches are made 1 per EL4 to match the amounts on EL6 level.
![Close with solid fill](file:///C:/Users/agunduz/AppData/Local/Temp/msohtmlclip1/01/clip_image018.png)![image](file:///C:/Users/agunduz/AppData/Local/Temp/msohtmlclip1/01/clip_image020.jpg)

 

**-Matching multiple element 6s -> INVALID **

Similar with previous example, but the matching is done including different EL6 on debtor position. Coda makes an automatic booking to balance the amounts on EL6. In this case, an invoice of debtor A can be matched with the payment of debtor B and it will be difficult to detect the mistake and will cost a lot of time. First a JV has to be posted to balance the amounts in the individual EL6 and then matching to be made per EL6.
![Close with solid fill](file:///C:/Users/agunduz/AppData/Local/Temp/msohtmlclip1/01/clip_image021.png)![image](file:///C:/Users/agunduz/AppData/Local/Temp/msohtmlclip1/01/clip_image023.jpg)

 

 

 

 

**-Matching multiple EL4 and EL6s -> INVALID **

A matching of multiple EL4 and multiple EL6s; causing 3 disperse lines to balance the EL4 and EL6. Afterwards it is very difficult to follow why these different EL6 are matched with each other especially as the matching goes through 2 balance positions.
![Close with solid fill](file:///C:/Users/agunduz/AppData/Local/Temp/msohtmlclip1/01/clip_image018.png)![image](file:///C:/Users/agunduz/AppData/Local/Temp/msohtmlclip1/01/clip_image025.jpg)

 

**-Matching multiple bank documents with multiple invoices -> INVALID **

In below example, multiple bank payments are matched with multiple outstanding invoices.

By matching all these lines in 1 go it is not possible anymore to follow which payment is done for which invoice and the reconciliation with the debtor will be difficult.

 
![Close with solid fill](file:///C:/Users/agunduz/AppData/Local/Temp/msohtmlclip1/01/clip_image026.png)![image](file:///C:/Users/agunduz/AppData/Local/Temp/msohtmlclip1/01/clip_image028.jpg)

**-Matching date before document date of the bank document -> INVALID **

Matching date can't be a date before the bank transfer is made.
![Close with solid fill](file:///C:/Users/agunduz/AppData/Local/Temp/msohtmlclip1/01/clip_image029.png)![image](file:///C:/Users/agunduz/AppData/Local/Temp/msohtmlclip1/01/clip_image031.jpg)

 

**-Matching date in different period then timing of settlement booking-> INVALID **

The settlement transaction of outstanding invoices with a deposit was made in 2019/8, matching was done in 2020/3.

Invoices are shown as settled in 2020/3 instead of in the period when the settlement took place in 2019/8.
![Close with solid fill](file:///C:/Users/agunduz/AppData/Local/Temp/msohtmlclip1/01/clip_image026.png)![image](file:///C:/Users/agunduz/AppData/Local/Temp/msohtmlclip1/01/clip_image033.jpg)

 

**CODA – "How to make matching" tutorial videos can be found in coda under "Instruction video's":  **
![Graphical user interface, text, application, email    Description automatically generated](file:///C:/Users/agunduz/AppData/Local/Temp/msohtmlclip1/01/clip_image035.jpg)
