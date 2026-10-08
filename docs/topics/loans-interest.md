---
title: Loans and interest
---

# Loans and interest

<div class="page-meta" markdown>
**Applies to:** asset companies · **Owner:** Group Finance / HQ cash management · **Last reviewed:** 2026-10-08
</div>

## Rule

Since 1 January 2019 every third-party loan has its own **element 7 loan code**: `L` + ISO country + three digits (`LDE001`). All loan and interest accounts must carry it (control C24). Loans are classified short / long term in line with HQ cash management (checklist point 19); interest is accrued every period (point 20).

**Mandatory accounts for third-party loans**

| SCoA | Name |
|---|---|
| 25330 | External loan non-current |
| 27330 | External loan current |
| 27401 | Interest payable |
| 52130 | Interest expense non-group (sub-analysed at EL7) |

**Movement codes (EL8)** on 25330, 27330, 25110, 25120, 27125: 810 drawdown, 820 repayment, 830 amortisation. These drive the cash flow lines CH2 to CH4 and CJ2 / CJ3.

**Financial cost accounts**

| BO | SCoA | Use |
|---|---|---|
| PI1 | 52330 | Interest expenses group |
| PI2 | 52130 | Interest to banks on the asset facility |
| PI3 | 52820 | Other financial expenses |
| PI4 | 51780, 51782, 52821 | Loan agency fees, one-off banking fees, bank costs (negative interest, transaction and account costs) |

Service companies use the 54xxx / 53xxx equivalents (PV2, PV3).

Intercompany loans and interest: see [Intercompany](intercompany.md).

## Change log

| Date | Change | Source |
|------|--------|--------|
| 2026-10-08 | Page created from "Loan and interest" (newsletters 3 March 2019 and 7 November 2019) and C24. | `sources/wiki/pages/loan-and-interest.md` |
