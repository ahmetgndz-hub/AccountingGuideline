---
title: Bank and cash
---

# Bank and cash

<div class="page-meta" markdown>
**Applies to:** all entities · **Owner:** Group Finance / cash management · **Last reviewed:** 2026-10-09
</div>

## Rule

1. **Book every bank statement on the next working day** after the statement date (Monday's statement on Tuesday; Friday's on Monday). Control C17 measures this.
2. **Book all bank mutations through Crescendo.** Direct bookings on cash accounts are only accepted for accounts that cannot be loaded into Crescendo (control C21). Suspense accounts 13332 (Crescendo) and 13313 (banks / cash) must be cleared daily.
3. **Bank booking deadline** at month end: 3 working days after period end, communicated by the cash manager. Bookings after that date appear in control C25; agree them with the cash manager beforehand.
4. **Match after every bank run** (A/R and A/P daily, before the debtor meeting and before the payment proposal). See [Matching](matching.md).
5. **Classify bank accounts by content** (checklist point 31). Tenant deposit accounts that loan agreements require to be kept separately stay separate; move utilised deposits to the current account by an actual transfer.
6. **Cash flow corrections** (rebooking a cash movement to the right cash flow line) use document code `JV-CFCORR`, never `JV-MANUAL`, so the QAR cash flow picks them up. See [Below NRI and cash flow mapping](below-nri-cashflow.md).

Cash SCoAs recognised by the cash flow: 13311, 13312, 13313, 13317, 13332, 13340, 13345 (BO group BB5).

## Deadlines

Bank and cash deadline: see [Closing calendar](closing-calendar.md), milestone 3.

## Structured addresses in master data (ISO 20022)

From **14 November 2026** SWIFT and the major payment infrastructures no longer accept fully unstructured postal addresses in cross-border and high-value payments. Every supplier and debtor record in Coda must therefore have at least a **hybrid** address: Country filled from the Coda dropdown (mandatory field) and City / Town reviewed and correct, with street, number and postal code completed in their own fields wherever possible. Countries review and clean their master data before the deadline; reference document EPC153-22 v2.0 (instruction 27 July 2026). Master data changes follow the four-eyes rule on the [Approvals](approvals-segregation.md) page.

## Change log

| Date | Change | Source |
|------|--------|--------|
| 2026-10-09 | ISO 20022 structured address requirement for supplier and debtor master data added. | `sources/emails/2026-07-27_iso-20022-structured-addresses.md` |
| 2026-10-08 | Page created from C17, C21, C25, "Liquidation of cash guarantees" and "Below NRI items". | `sources/wiki/pages/` |
