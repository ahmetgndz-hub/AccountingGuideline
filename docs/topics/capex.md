---
title: Capex and capex id
---

# Capex and capex id

<div class="page-meta" markdown>
**Applies to:** asset companies · **Owner:** Group Finance · **Last reviewed:** 2026-10-08
</div>

## Rule

Capex works identified in the business plan are grouped in five categories and two cost types: **Maintenance** (keeps the property in its current state or secures continued income) and **Capex** (adds value).

| Category | Content | Type | Valuation |
|---|---|---|---|
| **C1 Regular capex** | Major repairs, improvements, replacements (floors, escalators) | Maintenance | Expensed |
| **C2 Legal compliance** | Works required by law, permits, licences (wheelchair access) | Maintenance | Expensed |
| **C3 Renovation / redevelopment** | Refurbishment that generates quantifiable NRI return (new interior, façade) | Capex | Capitalised, in BX and Multi valuation |
| **C4 Tenant incentives** | Fit-out, relocation, unit split agreed in lease negotiations (stepped rent and rent-free are discounts, not C4) | Capex | Expensed through market value changes |
| **C5 Extensions** | Enlarging the property, more GLA | Capex | Capitalised, in valuation |

Every capex transaction on 11111 and 11340 carries a **capex id** (format `C01_2018_DEBP936_146`): the shareholder-approved budget line maintained in the reporting hub. Exception: valuation bookings (EL5 = C99). Development projects use B codes on 11340, see [Development budget codes](development-b-codes.md).

- Assign the capex id on the purchase order (drop-down) or link PO to capex id in the reporting hub (overrides the PO). All invoices on that PO inherit it.
- Lines without PO: fill external reference 3 on the line.
- Expenditure from a previous year's budget links to that year's capex id. Expenditure without a matching id: create a new id with the capex team.
- Transfers to P&L or other accounts must **not** carry a capex id, otherwise actual progress is understated.
- The capex tool always reconciles with the shareholder-approved budget; adjustments go in the adjustment column, never by changing the budget.

PMSA (re)development management fee of 7,5% on project cost is booked as income at the service company and capitalised at the asset company, see [Intercompany](intercompany.md).

## Deadlines

Checklist point 9; control C23.

## Change log

| Date | Change | Source |
|------|--------|--------|
| 2026-10-08 | Page created by merging "Capital Expenditures", "Capex Reporting", "Capex" and C23. | `sources/wiki/pages/capital-expenditures.md`, `capex-reporting.md` |
