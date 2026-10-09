---
date: 2026-07-27
subject: "ISO 20022 Structured Address Requirements – Required Review of Supplier and Debtor Master Data"
from: "Ahmet Gunduz <agunduz@multi.eu>"
to: "Izzet Ensoy, Harold van Riel, Erdem Dilber, Ozcan Kurt, Patryk Zuk, Marco Colombo, Marcel Brouwer, Jonathan Ablett"
cc: "Steven Poelman, Sudipta Dash, Rob Uytdewillegen, Marc Peltenburg"
status: current
superseded_by: 
topics: [bank-cash, coda-elements]
outlook: "https://outlook.office365.com/owa/?ItemID=AAMkADliMmJiZjQwLTZiYzAtNGVmYy1iZDJmLWQ0ZjczMjU1NjMwMwBGAAAAAAAEotGQSOkcTYClUcdLGf8KBwBuY3bEqWtqSL0H9kIX4CbNAAAAAAEJAABuY3bEqWtqSL0H9kIX4CbNAA5LrOvuAAA%3D&exvsurl=1&viewmodel=ReadMessageItem"
message_id: "<GV2PR02MB8674E24F6E5D0E4C9845BD6FDBCC2@GV2PR02MB8674.eurprd02.prod.outlook.com>"
attachments: "EPC153-22 v2.0 EPC guidance document - Provision of Addresses under the EPC Payment Schemes.pdf"
fetched: 2026-10-09 via Microsoft 365 connector (read-only)
---

> Sent with high importance. The attached EPC guidance PDF is an external reference document and was not extracted.

Dear All,
As part of the ISO 20022 migration, new postal address requirements will become mandatory for cross-border and high-value payment messages.

By **14 November 2026**, SWIFT and major market infrastructures will no longer accept fully unstructured addresses. Address information must be provided either in a fully structured or hybrid format.

**Key points:**

- **Fully Structured Address: **All address components (street, building number, postal code, city, country, etc.) are stored in dedicated fields.

- **Hybrid Address**: Requires at least Town/City and Country Code in structured fields, while allowing limited free-text address lines for additional details.

- **Fully Unstructured Address**: Free-text address lines only. This format will no longer be accepted after 14 November 2026.

**Required Actions**
To ensure compliance, all countries are requested to review their supplier and debtor master data and update records where necessary.

Minimum requirements for all supplier and customer records:

- Country must be completed (mandatory field in CODA and selectable via dropdown list only).

- City/Town information must be reviewed and corrected where required.

- Additional address elements should be completed and structured whenever possible.

Please coordinate the review and cleansing of your master data as soon as possible to ensure readiness before the regulatory deadline.

If you have any questions or require support, please let us know.

Kind regards,
Ahmet Gündüz
