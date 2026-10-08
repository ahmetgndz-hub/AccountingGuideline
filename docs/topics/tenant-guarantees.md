---
title: Tenant guarantees
---

# Tenant guarantees

<div class="page-meta" markdown>
**Applies to:** asset companies · **Owner:** Group Finance · **Last reviewed:** 2026-10-08
</div>

## Rule

A tenant guarantee is the security the lease requires the tenant to provide. It is recorded twice: in **Horizon** (what the lease requires) and in **Coda** (what was received). The BO report "Deposits and guarantees (agreed / received)" compares both. Guarantee data feeds the [bad debt](bad-debt.md) calculation, debtor exposure and QAR reporting.

| Code | Guarantee type | SCoA | Security level (1 most secure) |
|---|---|---|---|
| G01 | Bankers guarantee | 99100 | 2 |
| G02 | Cheque | 99100 | 4 |
| G03 | Company bond | 99100 | 4 |
| G04 | Company guarantee | 99100 | 4 |
| G05 | Cash deposit for utilities | 25550 | 1 |
| G06 | Cash deposit | 25550 | 1 |
| G07 | Holding guarantee | 99100 | 3 |
| G08 | Legal deposit | 99100 | 2 |
| G09 | Letter of credit | 99100 | 2 |
| G10 | No deposit applicable | | |
| G11 | Notarial agreement | 99100 | 1 |
| G12 | Other | 99100 | 3 |
| G13 | Personal guarantee | 99100 | 5 |
| G14 | Promissory note | 99100 | 5 |

"Guarantee for": G51 rent / marketing / service charge, G52 rent, G53 service charges, G54 utilities.

## How to (Coda)

**Cash guarantees (G05, G06)**: book on 25550 Received guarantees and deposits non-current (Dr 13311 bank / Cr 25550). Fill **external reference 3** with the 8-digit lease reference. No dummy property code on EL2. To add the reference later: Browse details, select the line, Actions, View / edit line, tab References, External reference 3, save.

**Non-cash guarantees**: off balance sheet on 99100 Tenant guarantees via the CodaXL import (max 400 per import), document code `NF-GUARANTEE` (workflow; before 2020 `GE-JV-MAN-GU`). Document date = issue date, due date = expiry (31/12/2099 if unlimited), document number = serial number of the guarantee, attachment = PDF in the country attachment folder `GU` named `EL1_number_name.pdf`. Expired guarantees are cleared by **matching** on 99100 with the dedicated matching master (EL4 fixed, EL2 and EL6 mandatory); no counter booking.

**Horizon**: fill the deposit fields per lease (type, amount, currency, dates). Never use deposit type "additional guarantee".

**Liquidating a cash guarantee** to cover outstanding debt: book with `JV-CFCORR` (Dr 25550 / Cr 13111) so the cash flow and fee calculations pick it up. A cash-backed guarantee (for example a bank letter of guarantee) that lands on the bank account needs no such booking. If loan agreements require a separate deposit account, make the real bank transfer to the current account.

**BO report sheets**: Tenant guarantee (all Horizon guarantees with Coda data), No deposit (required but not received), With deposit (amount check Horizon vs Coda), Due date approaching (next 8 months), Different deposit (type differs), No Horizon (Coda booking without lease).

## Deadlines

Checklist point 5 at every close.

## Change log

| Date | Change | Source |
|------|--------|--------|
| 2026-10-08 | Page created from "Tenant Guarantees" and "Liquidation of cash guarantees" (newsletter 26 November 2020). | `sources/wiki/pages/tenant-guarantees.md`, `liquidation-of-cash-guarantees.md` |
