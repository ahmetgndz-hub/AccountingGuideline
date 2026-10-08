---
title: "C30 Employee costs"
source_file: "C30 Employee costs.aspx"
sharepoint: "https://multieu.sharepoint.com/sites/Wiki/Paginas/C30 Employee costs.aspx"
contact: "Dennis Pieterson"
categories: ""
converted: 2026-10-08
status: old-wiki
---

# C30 Employee costs

# C30 Employee costs

To keep track of employee costs all the employee related costs are booked on an employee code (Element 6 per employee / for example E4016).
This employee code needs to be created for all internal, external en temporary employees. 
If an employee works for a specific asset, the costs for this employee should also be booked on this property code (element 2)

An employee code can be requested via the FAM mailbox.

The following checks are done in this control:

- Costs booked on SCoA's relating to employee costs (see below overview for all related SCoA's) are booked with an employee code;
- Check with the combination of used employee code (Element 6) and property code (Element 2) is as expected.
- If a dummy employee code (E9998/E9999) is used, only acceptable if costs can't be properly defined to an employee.

Below an overview with all BO-groups with SCoA's that expect the use of an employee code on Element 6.

- PQ1 Salaries

  - 44111 Wages and salaries
  - 44122 Holiday allowance
  - 44123 Leaving indemnity
  - 44127 Sickness benefits
  - 44128 Vacation days accrual
  - 44198 CAF IGS recharge salary

- PQ2 Bonuses

  - 44124 Bonus

- PQ3 External personnel (independent workers)

  - 44120 Independent workers

- PQ4 Temporary personnel

  - 44180 Temporary staff

- PQ6 Social security

  - 44112 Health insurance
  - 44113 Social security

- PQ7 Pension costs

  - 44115 Pensions

- PR7 Travel and entertainment

  - 44130 Travel expenses
  - 44131 Flight expenses
  - 44132 Hotel expenses
  - 44133 Representation expenses
  - 44135 Travel expenses allowance

- PR8 Car costs & allowances

  - 44170 Lease costs cars
  - 44171 Fuel costs
  - 44172 Other car expenses
  - 44173 Withholding lease cars
  - 44174 Mileage allowance

- PR9 Other staff costs

  - 44140 Training and education expenses
  - 44150 Employee party / entertainment
  - 44160 Recruitment costs
  - 44190 Other staff costs

Example overview of the control:

![Employeecosts.JPG](/sites/Wiki/SiteCollectionImages/Paginas/C30%20Employee%20costs/Employeecosts.JPG)
 

| **[Control file](/sites/Wiki/Paginas/Control%20file.aspx) ** | **[Accounting Manual](/sites/Wiki/Paginas/Accounting%20Manual.aspx)** | **[Multi Wiki](/sites/Wiki/Paginas/Multi%20Wiki.aspx)** |
|---|---|---|
