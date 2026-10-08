---
title: Coda element structure
---

# Coda element structure

<div class="page-meta" markdown>
**Applies to:** all entities · **Owner:** Group Finance / FAM · **Last reviewed:** 2026-10-08
</div>

## Rule

Every Coda transaction line carries elements 1 to 8. Use them consistently; the BO reports, the control file and the cash flow are built on them.

| Element | Content | Rule |
|---|---|---|
| **EL1** | Legal entity | Always the entity that owns the transaction (for payroll: the payroll entity). |
| **EL2** | Property / cost centre | The real asset the cost or income belongs to. Service company code when it concerns the service company as a whole. **Dummy property codes are not allowed on anything that hits NRI** (reporting groups PA to PG). |
| **EL3** | Book | MAN, FSM, FSE, LOC, TAX, UST, LUX, ELM. See [Books](booking-structure.md). |
| **EL4** | SCoA (account) | Group chart of accounts. Mapping to BO reporting groups: [P&L accounts and BO codes](pl-accounts-bo-codes.md). |
| **EL5** | Sub-analysis | Capex category (C01 to C05, C99 for valuation), tax code, Covid or other special codes, discount sub-codes. |
| **EL6** | Counterparty | Debtor (D), creditor (C), employee (E, equal to the Workday id), bank, tax code (T), group company (R). **Dummy element 6 is not allowed**, except `0` for depreciation and result transfer. See [Suspense and dummy accounts](suspense-dummy-accounts.md). |
| **EL7** | Department / loan / contract | Loans: `L` + ISO country + 3 digits (for example `LDE001`), mandatory on all loan and interest accounts. Departments for staff costs. |
| **EL8** | Movement code | Cash flow and roll-forward logic: 810 drawdown, 820 repayment, 830 amortisation, 070 capex, 050 sale, 054 valuation, 015/045/130 depreciation, 410/420/440 bad debt movements, 525/570 equity movements. |

Reference fields:

- **External reference 3**: lease reference (8 digits, as in Horizon) on tenant guarantees, bad debt and write-off lines; capex id on capex lines without a PO.
- **Document date / due date / document number**: see the specific pages (guarantees, salary).

## Tax codes (element 6 on tax accounts)

Standard structure, agreed to unify accounting and allow a direct cash flow from BO:

```
T  DE  S  21
|  |   |  └─ percentage of tax (99 = payable or deferred)
|  |   └──── S sales, P purchase, A VAT asset, L VAT liability
|  └──────── ISO country code
└─────────── tax
```

At each month end (or declaration period) reclass purchase and sales VAT to the proper VAT asset / liability account with the matching `A` / `L` element 6, and match the lines against the settlement booking. See [Taxes](taxes.md).

## Change log

| Date | Change | Source |
|------|--------|--------|
| 2026-10-08 | Page created from "Tax codes", "Loan and interest", "C11", "C14", "C30" and "Salary bookkeeping" wiki pages. | `sources/wiki/pages/` |
