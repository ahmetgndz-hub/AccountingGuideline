---
date: 2026-04-28
subject: "Re: redundancy calculation methodology"
from: "Ahmet Gunduz <agunduz@multi.eu>"
to: "Steven Poelman, Egbert van Zomeren"
cc: "Martijn Hunfeld"
status: reference
superseded_by: 
topics: [redundancy-provision, salary-bookkeeping]
outlook: "https://outlook.office365.com/owa/?ItemID=AAMkADliMmJiZjQwLTZiYzAtNGVmYy1iZDJmLWQ0ZjczMjU1NjMwMwBGAAAAAAAEotGQSOkcTYClUcdLGf8KBwBuY3bEqWtqSL0H9kIX4CbNAAAAAAEJAABuY3bEqWtqSL0H9kIX4CbNAAykELonAAA%3D&exvsurl=1&viewmodel=ReadMessageItem"
message_id: "<AS2PR02MB10430FF1951820A2AA69B154DDB372@AS2PR02MB10430.eurprd02.prod.outlook.com>"
attachments: "Redundancy_Provision_Policy_v1.0.docx"
fetched: 2026-10-09 via Microsoft 365 connector (read-only)
---

> Quoted thread kept: Ahmet Gunduz's original mail of 2026-04-23 (switch of the salary basis to Sympa contracted amount / 12) and Steven Poelman's reply of 2026-04-24 (how countries book severance, notice and settlement payments; HQ books provision build-up and release centrally) carry the rules. Attachment text saved in 2026-04-28_redundancy-calculation-methodology-attachment-1.md.

Egbert / Steven,

May I ask for your assistance in reviewing the attached redundancy accounting policy to confirm it aligns with your understanding?

Once confirmed, I will share it with the country finance teams.

Ahmet

---

**From:** Steven Poelman <spoelman@multi.eu>
**Sent:** Friday, April 24, 2026 09:16
**To:** Ahmet Gunduz <agunduz@multi.eu>; Egbert van Zomeren <EvanZomeren@multi.eu>; Martijn Hunfeld <mhunfeld@multi.eu>
**Subject:** Re: redundancy calculation methodology

Thanks Ahmet, this is a great improvement!

Did we instruct the countries on how to book the severance and notice and settlement payments? What was instructed?

In my view:

- notice pay/ holiday allowance and vacation monies: dt salary cost / ct bank

- severance and settlement payments: dt redundancy provision / ct bank

We will centrally book and maintain the build up and further release of the redundancy provions, whereby a release can never lead to a credit amount above the line.

Are we sure that the timing of movement / number of employees (in and out) and the calculation of the redundancy provision matches?

Thx
Steven

Sent from [Outlook for iOS](https://eur01.safelinks.protection.outlook.com/?url=https%3A%2F%2Faka.ms%2Fo0ukef&data=05%7C02%7Cagunduz%40multi.eu%7Cddd7d40feff746187d7b08dea1d16cd8%7Cebbd3cdca8e64e55b6add15663769232%7C0%7C0%7C639126118018247605%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=rT9CwDD0soSryg11VF772dtAONmAE7KI8zTotA%2BpXfI%3D&reserved=0)

---

**From:** Ahmet Gunduz <agunduz@multi.eu>
**Sent:** Thursday, April 23, 2026 5:36 PM
**To:** Steven Poelman <spoelman@multi.eu>; Egbert van Zomeren <EvanZomeren@multi.eu>; Martijn Hunfeld <mhunfeld@multi.eu>
**Subject:** redundancy calculation methodology

Dear All,

As of today, we have access to Sympa salary and benefits data via API. I will therefore adjust our redundancy calculation file accordingly.

Previously, the calculation was based on the actual salary paid to the employee in the current month. This approach relied heavily on the correct use of element codes and, in addition, did not fully account for country-specific differences. For example, in some countries (e.g. Italy), a 13th and 14th month salary is paid, meaning that monthly amounts × 12 differ from the total annual salary.

Going forward, I will switch to using Sympa data, and the total contracted amount divided by 12 will be used for the calculation.

Please let me know if you have any objections to this change.

Best regards,
Ahmet
