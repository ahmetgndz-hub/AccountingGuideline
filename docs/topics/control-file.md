---
title: Accounting Control File
---

# Accounting Control File

<div class="page-meta" markdown>
**Applies to:** every control group (country) · **Owner:** Group Financial Controlling · **Where:** [Multi Reporting Hub](https://multireportinghub.multi.eu) · **Last reviewed:** 2026-10-09
</div>

## Rule

The Accounting Control File is the **online, monthly sign-off of the bookkeeping** against Multi's accounting policies and Coda system rules. It runs in the Multi Reporting Hub, not in Excel. Every control group (normally one country, defined by Group Financial Controlling as a set of Coda company and legal entity codes) must:

1. **Run** the control file for the period after the bookkeeping is complete (**Refresh All**, with all legal entities selected).
2. **Clear or explain every finding.** A finding is a row a control flags as not in line with the rules. It is cleared by correcting the books and refreshing, or explained with a **comment** on that row. A control stays **red** while it has findings without a comment; it turns **green** when every finding is explained; **grey** means the control could not run.
3. **Submit** the control file before the closing deadline. Submitting is a declaration: the submitter confirms the disclaimer shown on screen, and if unexplained findings remain, must explicitly acknowledge them. Submission covers the whole group (all legal entities), never a single entity.
4. **Get it approved by a second person.** The submitter can never approve their own file. Group Financial Controlling reviews each finding in Admin › Approvals › Review findings and gives **Accept** or **Reject** per finding; a reject carries a mandatory counter-note that appears in red under the country's own comment, so the country knows what to correct. A rejected closing goes back to the country with the reason.
5. **Respect the deadline.** The closing deadline is the "99 Closing" milestone of the [closing calendar](closing-calendar.md) (month end + standing offset + any extension for the period, country-specific extension first). At **23:59 Amsterdam time on deadline day the period is closed in Coda for every country without exception.** The next morning at 09:00 each group's Country Controller and Country FD receive a status mail (submitted / approved / not submitted, and the number of unexplained findings), and Group Financial Controlling receives one summary for all groups.

Bookings after the deadline are reported by control **99 Booking after Deadline** and must be agreed with HQ accounting beforehand (see [closing calendar](closing-calendar.md)).

**Standard at sign-off** (closing instructions, restated every month since August 2026): the online Control File must be clean at sign-off. Any remaining issue must be (i) clearly identified, (ii) properly explained and (iii) actively remediated in the Reporting Hub. A Control File with unexplained issues is not acceptable. Since September 2026 the Balance Sheet and the FPR (Financial Performance Review) are integrated into the Control File and **the submitted online Control File is the only closing deliverable**: no separate e-mail, no attachments; all comments and explanations are written in the Control File. The Director of Finance signs off on completeness of the closing, accuracy of the numbers and quality of the Control File.

## How the screen works

| Element | Meaning |
|---|---|
| **Selection** | Control group (company), legal entity (All or one), year, period. Defaults to the period of ten days ago. Submit is only possible with **All** legal entities. |
| **Refresh All** | Runs every control of the group for the selection, one run per member company, and stores the summary (info rows, findings, explained findings, last refresh, who ran it). The last run overwrites earlier ones for the same selection. Submit is enabled only after a complete Refresh All in the current session. |
| **Finding / Info** | Each control returns rows flagged as *finding* (needs action or explanation) or *info* (context only). Statement reports such as 29 Standard P&L and 30 Balance Sheet are *Info* reports: they never block submission. |
| **Comment** | Free text per flagged row, kept per row key across periods, written by the country. Writing needs the role flag *Comment*. A finding with a comment counts as explained. |
| **Colour** | Red = findings > explained; green = all explained; grey = error. |
| **Closing status** | Open → Submitted (awaiting approval by someone else) → Approved, or Rejected with reason. |
| **Closing Progress** | Group Control › Closing Progress: the matrix of all groups and periods, read from the stored run results. Group FD, Group CFO and Group FC roles see this tab only. |
| **Requests** | Re-opening a closed period or changing the auto-close is requested in Group Control › Requests and approved by Group Financial Controlling. |

Access is role-based and enforced server-side: a user only sees the control groups assigned to them, and the controls granted to their role. Data in every control is read with the user's own Coda rights.

## History

| Period | Process | Source |
|---|---|---|
| until June 2026 | Excel control file (v4.2) run per country; FD e-mails the Control File, the Trial Balance / Management Hierarchy and the FPR file (called RMA file from January 2026) to HQ. Standard: "clean, or issues flagged and explained" (July 2025, January–June 2026); "clean without exceptions, otherwise the closing is not finalised" (August–December 2025). | `sources/emails/2025-*closing-instructions*`, `2026-0[1-6]*closing-instructions*` |
| July 2026 | Control File no longer distributed in Excel; review, remediation and sign-off in the online Reporting Hub. Other two deliverables still by e-mail. | `2026-07-28_closing-instructions-2026-07.md` |
| September 2026 | Period closes automatically in Coda at 23:59 on deadline day; Balance Sheet and FPR integrated; the online Control File is the only deliverable. | `2026-09-25_closing-instructions-2026-09-q3.md` |

## Control catalogue

The controls below are the ones documented on the old wiki (Excel control file v4.2, 2021). The **numbering and the set of controls in the Reporting Hub differ** (for example Reporting Hub control 28 is *Unmatched BS Items*, 29 *Standard P&L*, 30 *Balance Sheet*, 99 *Booking after Deadline*). The catalogue will be replaced by the live list from the Reporting Hub, see the open point at the end of this page. Until then, the descriptions remain valid as the rules behind the controls.

| Old control | What it checks | Expected outcome |
|---|---|---|
| **C01 Legal entity list** | All entities (EL1) per Coda company with their settings. | Details reconcile; otherwise contact HQ accounting. |
| **C02 Asset list** | All assets (Multi, BX, third party). | No sold assets; no missing assets. |
| **C11 Dummy and suspense accounts** | Unmatched transactions on suspense accounts; use of dummy element 6. | Suspense accounts empty and matched daily; the only accepted exception is a transfer booked on day 0 that arrives on day 1. Dummy element 6 (`0`, `xxxDUMMY9`, `Cxx99999`, `Dxx99999`, "technical", "temporary") not used, except `0` for depreciation and result transfer. Accounts allowed without element 6: valuation (11111 with movement 054 and 4331X), ERV (41101, 41111), result transfer (21180, 21210, 99998), vacancy (41130), equity 21130 / 21140 / 21170, depreciation (11xx3 with 015 / 045 / 130, 42910, 42911, 44910, 53910), unrealised FX (52825, 54825), deferred tax (11605, 25511, 53300), current tax (27570, 53100, 53900). |
| **C12 Valuation** | Horizon valuation (SOL) vs Coda booking (IST) per asset and book. | No difference against the agreed valuation at the reporting date. |
| **C13 Document code level** | Documents not in balance per EL1 + EL3; documents in the intray; documents denied in workflow and not handled. | Zero in all three. |
| **C14 Account code level** | Dummy property code on NRI accounts (PA to PG excluding PD5A and PGH); employee code on employment cost accounts (PQ, PR7, PR8, PR9); accounts without element 6. | Zero exceptions. |
| **C15 AP matching** | EL1 + EL6 combinations with an unmatched invoice **and** an unmatched payment above €100. | None: risk of double payment. |
| **C16 AR matching** | EL1 + EL6 combinations on receivables with at least one unmatched credit. | Credits matched against open invoices. |
| **C17 Bank booking target date** | Bank statement booked on the next working day. Buckets: on time, within 4 days, after 4 days. | Average close to one day. |
| **C20 ERV booking** | Full-year ERV in Horizon (A) vs budget (B); YTD ERV (D), ERV reversal (E), TO rent only (F); control points C = A−B, I = G+D, J = H+D, K = D+E+F. | K differs only by agreed rent minus ERV. See [ERV and vacancy](erv-vacancy.md). |
| **C21 Bank booking without Crescendo** | Bookings on cash accounts (except 13332, 13312) outside Crescendo. | Move those bank accounts to Crescendo. |
| **C23 Capex reporting** | Lines on 11111 and 11340 with their capex id against the reporting hub. | Every line has a valid capex id. See [Capex](capex.md). |
| **C24 Loan overview** | Loan and interest accounts carry a loan code (element 7). | No line without loan code. |
| **C25 Bank booking after deadline** | Cash transactions booked after the bank booking deadline (3 WD after period end). | None, unless agreed with the cash manager. |
| **C26 Booking after closing deadline** | Bookings in MAN and FSM after the closing deadline. Now Reporting Hub control **99 Booking after Deadline**. | None, unless communicated to HQ accounting. |
| **C27 Valuation bookkeeping** | Movement on 11111 with code 054 equals the 4331X valuation accounts, per EL1 + EL2 + EL3. | Control column = 1 on every total line. |
| **C28 Document codes vs element 4** | Document code used on allowed accounts only; no pre-2020 codes used in 2020 or later. | No warnings. See [Document codes](document-codes.md). |
| **C29 Matching quality** | Matching on 13111 and 27310: one invoice to many bank lines or one bank line to many invoices of the same counterparty. Warns on multiple EL1, EL3 or EL6 in one match, matching date outside the period, or payment and matching in different periods. | No warnings. See [Matching](matching.md). |
| **C30 Employee costs** | Employee-cost accounts booked with an employee code (EL6) and the expected property code (EL2); dummy employee codes E9998 / E9999 only where a cost cannot be attributed. | See [Salary bookkeeping](salary-bookkeeping.md). |
| **C31 Result booking** | Result transferred from P&L to equity per EL1 and EL3 up to the refreshed period. | Done in every book. |
| **Statement reports (Info)** | 29 Standard P&L and 30 Balance Sheet in the Reporting Hub show the statements per group with row colouring, tabs and account drill-down. | No findings; used for the trial balance review. |

## Deadlines

[Milestone 11](closing-calendar.md): closing deadline ("99 Closing"). Refresh All, explain findings and submit before that day; the period closes at 23:59 Amsterdam.

## Open points

- **Replace the catalogue with the live Reporting Hub list.** Group Financial Controlling to provide the output of the query below (run in SSMS on `coda`); the page will then list every control with its Reporting Hub number, category (Control or Info) and description.

```sql
SELECT n.SortOrder, n.Label, r.StoredProcName, r.ReportCategory, r.[Description], n.IsActive
FROM   dbo.WEB_NavNode n
JOIN   dbo.WEB_Report  r ON r.NodeId = n.NodeId
WHERE  n.ParentNodeId = (SELECT TOP 1 NodeId FROM dbo.WEB_NavNode
                         WHERE ParentNodeId IS NULL AND Label = N'Accounting Control File')
ORDER  BY n.SortOrder;
```

## Change log

| Date | Change | Source |
|------|--------|--------|
| 2026-10-09 | Sign-off standard, single-deliverable rule and the Excel-to-Reporting-Hub history added from the closing instruction e-mails 2025 to 2026. | `sources/emails/*closing-instructions*`, `sources/inventory/batch-B.md`, `batch-C.md` |
| 2026-10-08 | Page rewritten around the online control file in the Multi Reporting Hub (control groups, Refresh All, findings and comments, submit with disclaimer, second-person approval and finding review, deadline close at 23:59 Amsterdam, status mails). Old Excel-era control descriptions kept as the catalogue pending the live list. | Multi Reporting Hub source (`202609MultiReportingHub`: Report.razor, sql/01, 13, 17, 22, 27, 37, 53, 54, DeadlineReportRunner), old wiki C01 to C31 |
| 2026-10-08 | Page created from the "Control file" page and the C01 to C31 pages; the two C11 pages merged. | `sources/wiki/pages/control-file.md`, `c*.md` |
