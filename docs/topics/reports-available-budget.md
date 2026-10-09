---
title: BO reports: available budget
---

# BO reports: available budget

<div class="page-meta" markdown>
**Applies to:** all entities · **Owner:** FAM · **Last reviewed:** 2026-10-09
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

## RMA pack (Financial Performance Review)

Since July 2026 the RMA meeting presentation is produced from the standard **RMA automation file for Macabacus** (`RMA Pack Version @20260728.xlsb`, maintained by Group Finance). Phase 1 content: profit and loss statement, balance sheet, direct cash flow statement. Until phase 2 the countries add by hand: accounts receivable ageing, FTE overview by asset and department (actual versus budget), NRI waterfall from budget to forecast, fee income per asset and margin analysis. The quarter-end instruction of June 2026 made this the standardised RMA format; since September 2026 the FPR is integrated into the online [Accounting Control File](control-file.md).

## Change log

| Date | Change | Source |
|---|---|---|
| 2026-10-09 | RMA pack (Macabacus format, July 2026) section added. | `sources/emails/2026-07-28_rma-report-format-macabacus.md`, `2026-06-23_closing-instructions-2026-06-q2.md` |
| 2026-10-08 | Page created from "Available budget" and "Available budget calculation on purchase request" (newsletter 9 April 2020). | `sources/wiki/pages/available-budget.md` |
