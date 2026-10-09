---
date: 2026-10-07
subject: "Re: [Request ID :##RE-535943##] : Coda: Intercompany Receivables – Automatic Transfer to Intercompany Loan After 45 Days"
from: "Ahmet Gunduz <agunduz@multi.eu>"
to: "Rob Uytdewillegen"
status: reference
superseded_by: 
topics: [intercompany, loans-interest, document-codes, control-file]
outlook: "https://outlook.office365.com/owa/?ItemID=AAMkADliMmJiZjQwLTZiYzAtNGVmYy1iZDJmLWQ0ZjczMjU1NjMwMwBGAAAAAAAEotGQSOkcTYClUcdLGf8KBwBuY3bEqWtqSL0H9kIX4CbNAAAAAAEJAABuY3bEqWtqSL0H9kIX4CbNAA9xKGbtAAA%3D&exvsurl=1&viewmodel=ReadMessageItem"
message_id: "<BESPR02MB9815815FF513E005EE1829604FDB942@BESPR02MB981581.eurprd02.prod.outlook.com>"
fetched: 2026-10-09 via Microsoft 365 connector (read-only)
---

> Quoted thread kept: Marcel Brouwer's request to Servicedesk (allocation rules for the automatic IC receivable to IC loan transfer after 45 days, document code JV-ICALLOC) and Ahmet Gunduz's reply of 2026-10-07 13:12 'Please not do that yet. First lets discuss'. The automation is on hold, not a rule.

Going forward, please do not make any essential changes to the system without first discussing them with me, regardless of who asked for it. I am not only referring to content control files, obviously.

---

**From:** Ahmet Gunduz <agunduz@multi.eu>
**Sent:** 07 October 2026 13:12
**To:** Servicedesk <servicedesk@multi.eu>
**Cc:** Mailbox-FAM <fam@multi.eu>; Marcel Brouwer <MBrouwer@multi.eu>
**Subject:** Re: [Request ID :##RE-535943##] : Coda: Intercompany Receivables – Automatic Transfer to Intercompany Loan After 45 Days

Please not do that yet. First lets discuss

---

**From:** Servicedesk <servicedesk@multi.eu>
**Sent:** 07 October 2026 13:01
**To:** Ahmet Gunduz <agunduz@multi.eu>
**Cc:** Mailbox-FAM <fam@multi.eu>; Marcel Brouwer <MBrouwer@multi.eu>
**Subject:** Re: [Request ID :##RE-535943##] : Coda: Intercompany Receivables – Automatic Transfer to Intercompany Loan After 45 Days

Hi Ahmet,

Steven asked to implement an allocation process in Coda for the intercompany reconciliation. Please note that a new document code 'JV-ICALLOC' will be used for this process. I do not know whether a new document code has impact on the control file but know oyu also know aobut this.

BR, Rob

---

Hi Rob,

As just discussed;

Can you please setup an allocation to transfer automatically the outstanding IC invoices when:

- The current date is invoice date + 45 days

- El1 are the service companies in all Coda companies and where el6 is RHQH001 + RHQH005

- El1 is HQH001 + HQH005 and el6 is a service company in any country

- Scoa are 13130 and 27210 and should be transferred to 13564

- Pay status for invoices at 27210 is held or available (when status is proposed it’s in payment process and we will not transfer for now)

- Only take into account SI + PI documents. Banks and JV’s to be excluded. Those documents should have been matched.

Think this is it for now. Please let me know if I forgot smth.

Thanks.

Best regards,

Marcel Brouwer
