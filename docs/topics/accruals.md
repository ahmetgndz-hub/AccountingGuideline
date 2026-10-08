---
title: Accruals
---

# Accruals

<div class="page-meta" markdown>
**Applies to:** all entities · **Owner:** Group Finance · **Last reviewed:** 2026-10-08
</div>

## Rule

Accrue when goods or services were received or delivered before the reporting date and no invoice or accrual is booked yet (checklist point 28). Release an accrual booked in a previous financial year below NRI on 43000 Accrual releases, never against the original cost line.

| # | Do / Don't | Rule | Why |
|---|---|---|---|
| 1 | DO | Always specify the proper element 6 (counterparty) | Everyone can follow the accrual and its effect |
| 2 | DON'T | Use dummy codes on the accrual account or the counter line, except service / marketing charge reconciliation accruals that stem from more than ten tenants | |
| 3 | DO | Book accruals with the **automatic reversal journal** `JV-REVERSAL` (auto-matched since October 2020) | No forgotten reversals, no manual follow-up, no false overrun in the PO available budget |
| 4 | DO | One document per accrual | Easy follow-up, faster workflow approval |
| 5 | DO | Write a clear line description | Faster approval |
| 6 | DON'T | Attach Excel calculation sheets; attach a PDF with a clear explanation | Approvers need the nature of the booking, not the workings |
| 7 | DON'T | Aggregate several cost lines in one accrual line; accruals are 1 = 1 with the cost line | Automatic movement and follow-up |
| 8 | DON'T | Close accruals with the incoming or outgoing invoice | Blurs follow-up and distorts cash flow reporting |
| 9 | DO | Use the lease reference on tenant-related accruals and discounts | Needed for OCR calculation |

## Standard accruals

| Nature | P&L line | Booking | MAN | FSM | UST |
|---|---|---|---|---|---|
| Employee bonus | PQ2 | Cr 27526 / Dr 44124 | No | No | No |
| Redundancy provision | PQ8 | Cr 27527 / Dr 44125, booked centrally by Group Finance per employee at quarter end; see [Redundancy provision](redundancy-provision.md) | Yes (MAN) | per layer map | No |
| Seniority / leaving indemnity | PQ | Covered by the redundancy provision policy where it is a statutory severance; otherwise Cr 27527 / Dr 44123 | see policy | | |
| Unused vacation days | PR9 | Cr 27515 / Dr 44190 | No | No | No |
| Marketing invoices not yet issued | PE1, PE2 | Dr 13553 / Cr 46810, 46820 | Yes | Yes | Yes |
| Service charge reconciliation: additional invoices | PE1, PE2 | Dr 13553 / Cr 46810, 46820 | Yes | Yes | Yes |
| Service charge reconciliation: credit notes | PE1, PE2 | Cr 27560 / Dr 46810, 46820 | Yes | Yes | Yes |
| Shortfall from caps and vacancy | net PE and PF | No booking; disclosed in QAR | No | No | No |
| Goods or services received, not invoiced | PF | Cr 27560 / Dr 46xxx | Yes | Yes | Yes |
| Current income tax | PX | Cr 27570 / Dr 53100 | Yes | Yes | Yes |
| Deferred tax asset / liability | PX | Dr 11605 or Cr 25511 / 53300 | No | Yes | No |
| Turnover rent | PD1 | Dr 13553 / Cr 41140 | Yes | Yes | Yes |
| Base rent | PB | Dr 13553 / Cr 41110 | Yes | Yes | Yes |
| Kiosk rent | PD3 | Dr 13553 / Cr 41160 | Yes | Yes | Yes |
| Back-dated discounts to tenants | PCx | Cr 27560 / Dr 414xx | Yes | Yes | Yes |
| Real estate tax (asset) | PG3 | Cr 27520 / Dr 42521 | Yes | Yes | Yes |
| Bad debt | PG1 | Cr 13113 / Dr 42593 | Yes | Yes | Yes |
| Real estate tax (genex) | PR11 | Cr 27520 / Dr 44231 | Yes | Yes | Yes |
| Interest | PI2 | Cr 27401 / Dr 52130 | Yes | Yes | Yes |
| HQ cost allocation fee | PW | Cr 27565 / Dr 45915 | Yes | Yes | Yes |
| Capex C1, C2, C4, C3a (operations) | n/a | Cr 27560 / Dr 11111 | Q4 only | Q4 only | Q4 only |
| Capex C3b, C5 (development) | n/a | Cr 27562 / Dr 11340 | No | No | No |

The available-budget calculation counts `JV-REVERSAL` (and the old `GE-JV-RV`) documents as accruals.

## Deadlines

[Milestone 9](closing-calendar.md): all accruals.

## Change log

| Date | Change | Source |
|------|--------|--------|
| 2026-10-08 | Redundancy and seniority rows updated per the Redundancy Provision policy v1.2 (provision now booked in MAN by Group Finance). | `sources/emails/2026-10_redundancy-provision-policy-v1-2.md` |
| 2026-10-08 | Page created from "Accruals" (instructions 17 September 2019, 6 November 2019, 5 October 2020). | `sources/wiki/pages/accruals.md` |
