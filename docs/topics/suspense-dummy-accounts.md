---
title: Suspense and dummy accounts
---

# Suspense and dummy accounts

<div class="page-meta" markdown>
**Applies to:** all entities · **Owner:** Group Finance · **Last reviewed:** 2026-10-08
</div>

## Rule

- Every transaction is linked to a proper element 6 (employee, debtor, creditor, bank, tax code). Dummy element 6 is **not allowed**; the only exception is `0` on depreciation and result transfer. The accounts that structurally have no counterparty (valuation, ERV, result transfer, vacancy, certain equity, depreciation, unrealised FX, deferred and current tax) are listed on the [Accounting Control File](control-file.md) page under C11.
- Suspense accounts (4SUSPENCE group: 13500, 13313, 13332, 27325 and similar) are **zero and matched every day**. At the reporting date they are zero in home and reporting value. The only accepted open item is a transfer booked on day 0 that arrives on day 1.
- Share capital and other equity lines carry the shareholder as element 6 and reconcile with the trade registry.
- Tax accounts carry the tax element 6, never a dummy.

## Deadlines

Suspense accounts cleansed by [milestone 3](closing-calendar.md) (ME + 1), again at year end (no suspense accounts, no dummy positions); control C11 lists every open item.

## Change log

| Date | Change | Source |
|------|--------|--------|
| 2026-10-08 | Page created from the two C11 pages (merged). | `sources/wiki/pages/c11-dummy-and-suspence-accounts.md`, `c11-dummy-and-suspense-accounts.md` |
