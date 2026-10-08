---
title: BO reports: available budget
---

# BO reports: available budget

<div class="page-meta" markdown>
**Applies to:** all entities · **Owner:** FAM · **Last reviewed:** 2026-10-08
</div>

## Available budget calculation (purchase requests)

The Coda purchase request module checks available budget as **budget − actuals current year − commitments − non-approved PRs**. The calculation supports budget periods that differ from the calendar year (for example April to March for third-party assets), keeps previous-year actuals out of the current budget when a previous-year PR exists, counts accruals (`JV-REVERSAL`, old `GE-JV-RV`), uses the PR date to pick the budget period, and works at group level. Per PO group the budget basis differs (elements, capex ids, B codes).

## Available budget BO report

Location: Country, All, Financial Reporting, "Available budget - Asset / Service / Capex" (service and capex versions were under development). Year-to-date only; intray items are not included. Prompts: company and year (mandatory), EL2, EL4, BO code.

| Column | Content |
|---|---|
| Budget | Coda budget per EL4 |
| Actuals | Total actuals, equal to the P&L |
| Actuals current | Transactions of the year plus invoices matched to this year's PRs |
| Actuals previous | Invoices of this year matched to previous-year PRs |
| Accruals | `JV-REVERSAL` documents |
| Commitments | Approved PRs of the year |
| Commitments previous year | Earlier PRs with remaining budget |
| Non-approved | PRs pending in workflow |
| Available | Budget − actuals current − commitments − non-approved; % of budget |

Sheets: overview, genex, opex, SC, details budget, details actuals, purchase requests (status 01 posted invoices, 03 non-approved, 05 commitments previous years, 06 invoices against previous-year commitments).

## Change log

| Date | Change | Source |
|---|---|---|
| 2026-10-08 | Page created from "Available budget" and "Available budget calculation on purchase request" (newsletter 9 April 2020). | `sources/wiki/pages/available-budget.md` |
