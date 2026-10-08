---
title: Intercompany transactions and charges
---

# Intercompany transactions and charges

<div class="page-meta" markdown>
**Applies to:** all entities · **Owner:** Group Finance · **Last reviewed:** 2026-10-08
</div>

## Rule

Intercompany balances are reviewed, matched and reconciled with the counterparty at every close (checklist point 23). Use the group accounts below with the group company as element 6 (R code).

| Receivable | | Payable | |
|---|---|---|---|
| 13564 | Loan receivable group current | 27125 | Loans group current |
| 11535 | Loans receivable group non-current | 25110 | Loan payable group non-current |
| 13532 | Interest receivable group | 27402 | Interest payable group |
| 13130 | Trade receivables group | 27120 | Trade payables group |
| 13561 | Other receivables group current | 27565 | Other current payables group |
| 11557 | Other receivables group non-current | 25555 | Other payables group non-current |
| 13554 | Accrued income group | 27530 | Accrued liability group |

Intercompany interest is booked with `JV-ICINTREST` at the rate communicated by HQ cash management.

## Recharge agreements

VAT is shown without reverse charge for simplicity; adjust where applicable.

| Agreement | From → to | Basis | Charging entity books | Receiving entity books |
|---|---|---|---|---|
| **ACAA (HQ)** Advanced cost allocation | HQ → local service company | Specific costs paid by HQ on behalf of SCMs, allocated pro rata FTE. No mark-up. | Cr original expense account (EL6 = original supplier), Cr 27521 VAT, Dr 13130 | Dr expense account, Dr VAT, Cr 27120 |
| **CAA / CAF** Cost allocation fee | HQ → local service company | HQ organisation cost less shareholder costs plus mark-up, pro rata, annual minimum €250.000, charged at quarter ends | Cr 45910 CAF income holding, Cr VAT, Dr 13130 | Dr 45915 CAF expense holding, Dr VAT, Cr 27120 |
| **PMSA** Project management | Service company → asset company (group or third party) | 7,5% of incurred project cost (C3 / C5) | Cr 45880 / 45881 development fee income, Cr VAT, Dr debtor | Dr 11111 / 11340 capex, Dr VAT, Cr creditor |
| **PLSA** Property, leasing and services | Service company → asset company | Percentage of NRI plus actual on-site staff cost. Split: 65% property management (recoverable), 20% asset management, 15% statutory services (guideline, may vary) | Cr 45810/1 AM fee, 45820/1 PM fee, 45830/1 statutory fee, Cr VAT, Dr debtor | Dr 44570 AM fee, 42570 PM fee (recharge to tenants via 46934 to be assessed locally), 44580 statutory fee, Dr VAT, Cr creditor |
| **IGSA** Intra-group services | Service company → service company | Pro rata direct staff cost plus allocable indirect cost plus mark-up | Cr 44198 CAF IGS recharge salary (PQ), Cr 44610 recharge genex (PR11), Cr VAT, Dr 13130 | Dr 44198, Dr 44610, Dr VAT, Cr 27120 |
| **ACAA (SCM)** | Service company → HQ / SCM / SPV | Pro rata supplier cost paid on behalf of another entity, no mark-up. Items below €2.500 per year (excluding recurring salary items) are not recharged. | Cr original expense, Cr VAT, Dr 13130 | Dr expense, Dr VAT, Cr 27120 |

Salary recharges in detail: [Salary bookkeeping](salary-bookkeeping.md). Fee income accounts: [Fee income](fee-income-recharges.md).

## Deadlines

[Milestone 7](closing-calendar.md).

## Open points

- Current intercompany interest rate (old wiki: 4,60% for 2019 and 2020) to be confirmed.

## Change log

| Date | Change | Source |
|------|--------|--------|
| 2026-10-08 | Page created from "Intercompany Transactions", "Intercompany Charges" (instruction 1 July 2019) and "Closing general information". | `sources/wiki/pages/intercompany-charges.md` |
