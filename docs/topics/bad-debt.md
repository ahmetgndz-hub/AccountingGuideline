---
title: Bad debt provision
---

# Bad debt provision

<div class="page-meta" markdown>
**Applies to:** asset and service companies, MAN books · **Owner:** Group Finance · **Last reviewed:** 2026-10-08
</div>

## Rule

The provision looks at the overall relationship with the tenant, not at single invoices.

1. **Trigger:** one receivable of the tenant is more than **60 days overdue**.
2. **Amount:** the **full outstanding balance** of that tenant, minus:
    - invoices issued for future periods;
    - exceptions communicated by HQ (for example invoices with manually extended due dates);
    - guarantees with security level 1 and 2 (bankers guarantee, cash deposit, cash deposit for utilities, legal deposit, letter of credit, notarial agreement), unless deemed not secure. No other guarantee type may be deducted. See [Tenant guarantees](tenant-guarantees.md).
3. **Stricter is always allowed:** the country FD may provide more (for example a tenant known to be in difficulty) without approval.
4. **Less strict needs pre-approval:** only with documented proof per tenant **and** written confirmation from HQ (Group FD or CFO).
5. **Local GAAP** differences are booked in the LOC book only.

Overpayments left unmatched are taken into account by the bad debt query, so do not match them to unrelated invoices.

## How to (Coda)

Document code `JV-BADDEBT` (exempt from workflow, reversal document). Element 6 = tenant, external reference 3 = lease reference.

| Event | Dr | Cr | EL8 |
|---|---|---|---|
| Recognise provision | 42593 Doubtful debt provision (opex) | 13113 Provision on trade receivables | 440 |
| Recovery, same financial year | 13113 | 42593 | 420 |
| Recovery, later financial year | 13113 | 43000 Accrual releases (below NRI) | 420 |
| Write-off, same year | 13113 (410) and 42594 | 42593 and 13111 | 410 |
| Write-off, later year | 13113 (410) and 42594 | 43000 and 13111 | 410 |

Service companies book the movement on 44586 Bad debt provision (man.co.) (PR10).

Group Finance maintains the PQ bad debt calculation file that computes and checks the provision; request it from HQ accounting.

## Worked examples (from the policy)

| Tenant | Situation | Provision |
|---|---|---|
| A | All receivables within 60 days | 0 |
| B | Part over 60 days, no securities | full balance |
| C | Part over 60 days, securities 75 against 110 receivable | 35 |
| D | Part over 60 days; corporate guarantee from the tenant's own group not deducted, cheque deemed safe | 165 − 115 = 50 |
| E | Within 60 days but known collection problem | full balance, at the FD's discretion |
| F | Over 60 days; only the cash deposit deducted, bank guarantee and cheque doubted | 100 − 50 = 50 |

## Deadlines

[Milestone 5](closing-calendar.md): A/R review, matching and bad debt booking.

## Open points

- The IFRS 9 memo (2018) describes an expected-credit-loss provision matrix for FSM. Confirm whether the 60-day policy above is the only policy applied in MAN and whether an ECL adjustment is booked in FSM.

## Change log

| Date | Change | Source |
|------|--------|--------|
| 2026-10-08 | Page created from "Bad debt provisions". | `sources/wiki/pages/bad-debt-provisions.md` |
