---
title: P&L accounts and BO codes
---

# P&L accounts and BO codes

<div class="page-meta" markdown>
**Applies to:** all entities · **Owner:** Group Finance / FAM · **Last reviewed:** 2026-10-08
</div>

Mapping of the P&L chart of accounts (element 4) to the BO reporting groups, as restructured per 2019. Old SCoA and element 8 are kept so that pre-2019 bookings can be read. Element 8 column: MSC = recoverable service charge, OPEX = non-recoverable asset cost, GEN = asset genex, OVH = service company overhead, ASSFIN / OTHFIN = financial items of asset / service companies, ASSET = asset company only.

| Group | BO code | BO name | SCoA | SCoA name | Old SCoA | Old EL8 |
|---|---|---|---|---|---|---|
| PA | PA | ERV | 41101 | Estimated rental value |  |  |
| PB | PB | Reversionary Potential | 41110 | Potential base rent |  |  |
| PB | PB | Reversionary Potential | 41111 | Estimated rental value reversal |  |  |
| PB | PB | Reversionary Potential | 41170 | Temporary in-line |  |  |
| PC | PC1 | Vacancy | 41130 | Vacancy |  |  |
| PC | PC2A | Structural discounts | 41412 | Structural discounts |  |  |
| PC | PC2 | Short term discounts | 41410 | Operational discounts |  |  |
| PC | PC2 | Short term discounts | 41411 | Stepped rents |  |  |
| PC | PC2 | Short term discounts | 41420 | Fit-out Phase |  |  |
| PC | PC2B | Rent free | 41415 | Rent Frees |  |  |
| PD | PD1 | Turnover Rent | 41140 | Turnover rent |  |  |
| PD | PD2 | Parking Rent | 41150 | Parking rent |  |  |
| PD | PD3 | Mall Income | 41160 | Mall income |  |  |
| PD | PD5 | Other Income | 41530 | Other asset income | 41510 |  |
| PD | PD5 | Other Income | 41530 | Other asset income | 41550 | ASSET |
| PE | PE1 | Service Charge Income | 46810 | Service income | 41840 | MSC |
| PE | PE1 | Service Charge Income | 46810 | Service income | 55830 | MSC |
| PE | PE2 | Marketing Income | 46820 | Marketing charges income | 41880 | MSC |
| PF | PF1 | Security and guarding | 46921 | Security and guarding | 42921 | MSC |
| PF | PF2 | Technical inspections | 46922 | Technical inspections | 42922 | MSC |
| PF | PF3 | Elevators and escalators | 46923 | Elevators and escalators | 42923 | MSC |
| PF | PF4 | Maintenance and Repair | 46924 | Maintenance and repair (recoverable) | 42924 | MSC |
| PF | PF5 | Cleaning | 46925 | recoverable Cleaning expenses | 42925 | MSC |
| PF | PF6 | Waste treatment and vermin extermina | 46926 | Waste treatment & vermin exterm. | 42926 | MSC |
| PF | PF7 | Utilities (water and electricity) | 46927 | Recoverable Utilities (water & electricity) | 42950 | MSC |
| PF | PF8 | Insurances | 46928 | Recoverable Insurance | 42110 | MSC |
| PF | PF9 | Taxes | 46929 | recoverable Real estate taxes | 42231 | MSC |
| PF | PF9 | Taxes | 46930 | Other recoverable taxes | 42233 | MSC |
| PF | PF10 | Advisors | 46931 | Other advisors (recoverable) | 42989 | MSC |
| PF | PF11 | Office costs (incl communication) | 46932 | Other recoverable office costs | 42790 | MSC |
| PF | PF12 | Staff costs | 46933 | Staff costs | 42955 | MSC |
| PF | PF13 | Property management fees | 46934 | Recoverable Property man. Fees | 45220 | MSC |
| PF | PF14 | Other service charges | 46935 | Other recoverable costs | 42960 | MSC |
| PF | PF15 | Recoverable marketing expenses | 46936 | Marketing expenses (recoverable) | 42400 | MSC |
| PF | PF16 | Asset management fee | 46937 | Asset management fees (recoverable) | 45210 | MSC |
| PG | PG1 | Collection Losses | 42593 | Doubtful debt provision (opex) | 44593 | OPEX |
| PG | PG2 | Landlord Marketing | 42530 | Marketing expenses (landlord) | 42400 | OPEX |
| PG | PG3 | Taxes | 42521 | Real estate taxes (landlord) | 42231 | OPEX |
| PG | PG3 | Taxes | 42522 | Other non-recoverable taxes | 42233 | OPEX |
| PG | PG4B | Insurances | 42520 | Insurance (landlord) | 42110 | OPEX |
| PG | PG4D | Property management fee | 42570 | Property management fees | 45220 | OPEX |
| PG | PG4E | Other non recoverable opex | 42590 | Other non-recoverable costs | 42960 | OPEX |
| PG | PG4A | Other Opex | 42540 | Maintenance and repair (opex) | 42924 | OPEX |
| PG | PG4F | Other Opex | 42550 | Utilities (water & electricity) non-recoverable | 42950 | OPEX |
| PG | PG4C | Other Opex | 42560 | Legal advisors (opex) | 42985 | OPEX |
| PG | PGH | Accrual releases | 42551 | Non recurring income | 41551 |  |
| PG | PGH | Accrual releases | 43000 | Accrual releases |  |  |
| PN | PN2A | Result from legacy files assets | 43241 | Legacy result assets |  |  |
| PH | PH1A | Advisors | 44550 | Auditors (genex) | 42981 | GEN |
| PH | PH1A | Advisors | 44560 | Other advisors (genex-asset) | 42989 | GEN |
| PH | PH1B | Appraisal costs | 44630 | Appraisers | 42987 | GEN |
| PH | PH4C | Leases | 44590 | Ground Leases | 44595 | GEN |
| PH | PH4B | Other Genex | 44581 | Other general expenses | 44599 | GEN |
| PH | PH4A | Other Genex | 44620 | Brokerage fees | 42600 | GEN |
| PH | PH5 | Asset management fees | 44570 | Asset management fees expense | 45210 | GEN |
| PH | PH5 | Asset management fees | 44580 | Statutory service fees expense | 45230 | GEN |
| PI | PI-A1 | Result from Sale Investment Property | 55800 | Result from sales Investment propert |  |  |
| PI | PI-A1 | Result from Sale Investment Property | 55801 | Result from sale participation IP |  |  |
| PI | PI1 | Interest costs group companies | 52330 | Interest expenses group | 51330 | ASSFIN |
| PI | PI2 | Interest costs banks | 52130 | Interest expense non-group | 51130 | ASSFIN |
| PI | PI3 | Interest costs other | 52820 | Other financial expenses | 51820 | ASSFIN |
| PI | PI4 | Bank fees and charges | 52821 | Bank costs (asset co.) | 51821 | ASSFIN |
| PJ | PJ1 | Interest income group companies | 52310 | Interest income group | 51310 | ASSFIN |
| PJ | PJ2 | Interest income banks | 52110 | Interest income non-group | 51110 | ASSFIN |
| PJ | PJ3 | Interest income other | 52810 | Other financial income | 51810 | ASSFIN |
| PK | PK1 | Market value changes | 43312 | Market value changes |  |  |
| PK | PK1 | Market value changes | 43313 | Impairment Capex |  |  |
| PK | PK1 | Market value changes | 43314 | Impairment Lease incentives |  |  |
| PK | PK1 | Market value changes | 43315 | Fair value adjustment IP |  |  |
| PK | PK2 | IFRS Rent-straightlining & other adjustments | 43400 | IFRS rent straightlining |  |  |
| PK | PK3 | Cost price adjustments | 43450 | Cost price adjustments |  |  |
| PL | PL | Result from participations IP | 55992 | Result non-group companies assets |  |  |
| PL | PL | Result from participations IP | 55994 | Result group companies assets |  |  |
| PM | PM1 | Currency differences | 52825 | FX results | 51825 | ASSFIN |
| PM | PM1 | Currency differences | 52825 | FX results | 55505 | ASSFIN |
| PM | PM2 | Depreciation | 53910 | Depreciation | 42910 | ASSET |
| PM | PM2 | Depreciation | 53910 | Depreciation | 42911 |  |
| PM | PM3 | Other income / expenses | 53810 | Extra-ordinary income | 55810 | ASSET |
| PM | PM3 | Other income / expenses | 54830 | Extra-ordinary expenses | 55830 | ASSET |
| PN | PN1 | Net result sale projects | 43210 | Sales projects |  |  |
| PN | PN1 | Net result sale projects | 43215 | Other project related income |  |  |
| PN | PN1 | Net result sale projects | 43250 | Value change due to reclassification |  |  |
| PN | PN2 | Direct project costs/Write-down inventories | 43220 | Cost of sales projects |  |  |
| PN | PN2 | Direct project costs/Write-down inventories | 43230 | Cost finished/cancelled projects |  |  |
| PN | PN2 | Direct project costs/Write-down inventories | 43240 | Impairment/provision projects |  |  |
| PN | PN2 | Direct project costs/Write-down inventories | 43540 | Acquisition costs projects | 44540 |  |
| PN | PN3 | Result from participations | 55991 | Result non-group companies non-asset |  |  |
| PN | PN3 | Result from participations | 55995 | Result group companies non-assets |  |  |
| PO | PO3 | Result from participations | 55996 | Result Sales group com/part int. |  |  |
| PP | PP1 | Asset Management Fee Income | 45810 | Asset management fee income |  |  |
| PP | PP1 | Asset Management Fee Income | 45811 | Asset Man Fee income 3rd |  |  |
| PP | PP2 | Property Management Fee Income | 45820 | Property management fee income |  |  |
| PP | PP2 | Property Management Fee Income | 45821 | Property Man. Fee Income 3rd |  |  |
| PP | PP3 | Statutory Services Fee Income | 45830 | Statutory service fee income |  |  |
| PP | PP3 | Statutory Services Fee Income | 45831 | Statutory service fee income 3rd |  |  |
| PP | PP4 | (Re-)Development Fee Income | 45880 | (Re-)Development fee income |  |  |
| PP | PP4 | (Re-)Development Fee Income | 45881 | Development management fee inc. 3rd |  |  |
| PQ | PQ1 | Salaries | 44111 | Wages and salaries |  |  |
| PQ | PQ1 | Salaries | 44122 | Holiday allowance |  |  |
| PQ | PQ1 | Salaries | 44123 | Leaving indemnity |  |  |
| PQ | PQ1 | Salaries | 44127 | Sickness benefits |  |  |
| PQ | PQ1 | Salaries | 44129 | Recharged salary costs | 44121 | OVH |
| PQ | PQ2 | Bonuses | 44124 | Bonus |  |  |
| PQ | PQ3 | External personnell (independent workers) | 44120 | Independent workers |  |  |
| PQ | PQ4 | Temporary personell | 44180 | Temporary staff |  |  |
| PQ | PQ5 | Reorganisation costs (staff) | 44125 | Redundancy |  |  |
| PQ | PQ5 | Reorganisation costs (staff) | 44126 | Staff cost (non-recurring) |  |  |
| PQ | PQ6 | Social security | 44112 | Health insurance |  |  |
| PQ | PQ6 | Social security | 44113 | Social security |  |  |
| PQ | PQ7 | Pension costs | 44115 | Pensions |  |  |
| PR | PR1 | Housing expenses | 44311 | Rent office and parking |  |  |
| PR | PR1 | Housing expenses | 44320 | Maintenance and repair (genex) | 42924 | OVH |
| PR | PR1 | Housing expenses | 44321 | Cleaning expenses | 42925 | OVH |
| PR | PR1 | Housing expenses | 44322 | Utilities (water & electricity) (genex) | 42950 | OVH |
| PR | PR1 | Housing expenses | 44380 | Other housing expenses |  |  |
| PR | PR1 | Housing expenses | 44390 | Other costs (genex) | 42960 | OVH |
| PR | PR2 | Office costs | 44310 | Repair and maintenance furniture | 42310 | OVH |
| PR | PR2 | Office costs | 44315 | Other housing / office costs | 42790 | OVH |
| PR | PR2 | Office costs | 44710 | Rent office equipment | 42710 |  |
| PR | PR2 | Office costs | 44720 | ICT costs | 42720 |  |
| PR | PR2 | Office costs | 44740 | Office supplies | 42740 |  |
| PR | PR2 | Office costs | 44750 | Printing | 42750 |  |
| PR | PR2 | Office costs | 44984 | ICT consultancy | 42984 |  |
| PR | PR3 | Telephone-, fax-, & postal exp. | 44760 | Telephone and postal costs | 42760 |  |
| PR | PR3 | Telephone-, fax-, & postal exp. | 44770 | Postal costs | 42770 |  |
| PR | PR4 | Contributions, insurance, subscriptions | 44110 | Insurance(genex) | 42110 | OVH |
| PR | PR4 | Contributions, insurance, subscriptions | 44780 | Contributions & subscriptions | 42780 |  |
| PR | PR5 | Advisory fees | 44573 | Service office/consultancy expense |  |  |
| PR | PR5 | Advisory fees | 44981 | Auditors (overhead) | 42981 | OVH |
| PR | PR5 | Advisory fees | 44982 | Other audit & administrative ass. fe | 42982 |  |
| PR | PR5 | Advisory fees | 44983 | Fiscal advisors | 42983 |  |
| PR | PR5 | Advisory fees | 44985 | Legal advisors | 42985 | OVH |
| PR | PR5 | Advisory fees | 44986 | Translation costs | 42986 |  |
| PR | PR5 | Advisory fees | 44989 | Other advisors (genex) | 42989 | OVH |
| PR | PR6 | Marketing expenses | 44410 | Public relations general | 42410 |  |
| PR | PR6 | Marketing expenses | 44430 | Sponsoring | 42430 |  |
| PR | PR6 | Marketing expenses | 44440 | Gifts to relations | 42440 |  |
| PR | PR6 | Marketing expenses | 44450 | Fairs and expositions | 42450 |  |
| PR | PR6 | Marketing expenses | 44460 | Advertising | 42460 |  |
| PR | PR6 | Marketing expenses | 44490 | Other marketing expenses | 42490 |  |
| PR | PR7 | Travel and entertainment | 44130 | Travel expenses |  |  |
| PR | PR7 | Travel and entertainment | 44131 | Flight expenses |  |  |
| PR | PR7 | Travel and entertainment | 44132 | Hotel expenses |  |  |
| PR | PR7 | Travel and entertainment | 44133 | Representation costs |  |  |
| PR | PR7 | Travel and entertainment | 44135 | Travel expense allowance |  |  |
| PR | PR8 | Car costs & -allowances | 44170 | Leasecost cars |  |  |
| PR | PR8 | Car costs & -allowances | 44171 | Fuel costs |  |  |
| PR | PR8 | Car costs & -allowances | 44172 | Other car expenses |  |  |
| PR | PR8 | Car costs & -allowances | 44173 | Withholding lease cars |  |  |
| PR | PR8 | Car costs & -allowances | 44174 | Mileage allowance |  |  |
| PR | PR9 | Other staff costs | 44140 | Training and education expenses |  |  |
| PR | PR9 | Other staff costs | 44150 | Employee party / entertainment |  |  |
| PR | PR9 | Other staff costs | 44160 | Recruitment costs |  |  |
| PR | PR9 | Other staff costs | 44190 | Other staff costs |  |  |
| PR | PR10 | Provision for bad debts | 44586 | Bad Debt provision (man.co.) | 44593 | OVH |
| PR | PR10 | Provision for bad debts | 44592 | Provision other receivables |  |  |
| PR | PR11 | Other general expenses | 44175 | Non-deductable VAT |  |  |
| PR | PR11 | Other general expenses | 44231 | Real estate taxes (genex) | 42231 | OVH |
| PR | PR11 | Other general expenses | 44233 | Other taxes | 42233 | OVH |
| PR | PR11 | Other general expenses | 44589 | Other general expenses (man.co.) | 44599 | OVH |
| PR | PR11 | Other general expenses | 44597 | Non Recoverable VAT |  |  |
| PR | PR12 | Reorganisation costs (general) | 44591 | Restructuring costs |  |  |
| PR | PR12 | Reorganisation costs (general) | 44594 | Advisory (non-recurring) |  |  |
| PR | PR12 | Reorganisation costs (general) | 44596 | Other non-recurring cost |  |  |
| PS | PS1 | Depreciation | 44910 | Depreciation (man.co.) | 42910 | OVH |
| PS | PS1 | Depreciation | 44910 | Depreciation (man.co.) | 42912 |  |
| PT | PT | Other operating income | 47510 | Other non-asset income | 41520 |  |
| PT | PT | Other operating income | 47520 | Other income (man.co.) | 41521 | OVH |
| PT | PT | Other operating income | 47520 | Other income (man.co.) | 41550 | OVH |
| PT | PT | Other operating income | 47610 | Extra-ordinary income (service comp) | 43810 | OVH |
| PT | PT | Other operating income | 47610 | Extra-ordinary income (service comp) | 55810 | OVH |
| PT | PT | Other operating income | 47620 | Extra-ordinary expenses (service comp) | 43830 | OVH |
| PT | PT | Other operating income | 47620 | Extra-ordinary expenses (service comp) | 55830 | OVH |
| PT | PT | Other operating income | 47700 | Administration fees non-group | 45930 |  |
| PT | PT | Other operating income | 47710 | Other administration fee | 45940 |  |
| PU | PU | Impairment goodwill | 47800 | Impairment goodwill | 44800 |  |
| PV | PV1 | Currency differences | 54825 | FX results (management comp) | 51825 | OTHFIN |
| PV | PV1 | Currency differences | 54825 | FX results (management comp) | 55505 | OTHFIN |
| PV | PV2 | Financing expenses | 54810 | Other financial income (man.co.) | 51810 | OTHFIN |
| PV | PV2 | Financing expenses | 54130 | Interest expense non-group (service comp) | 51130 | OTHFIN |
| PV | PV2 | Financing expenses | 54330 | Interest expenses group (service comp) | 51330 | OTHFIN |
| PV | PV2 | Financing expenses | 54820 | Other financial expenses (man.co.) | 51820 | OTHFIN |
| PV | PV2 | Financing expenses | 54821 | Bank costs (man.co.) | 51821 | OTHFIN |
| PV | PV3 | Financing income | 53110 | Interest income non-group (service comp) | 51110 | OTHFIN |
| PV | PV3 | Financing income | 53310 | Interest income group (service comp) | 51310 | OTHFIN |
| PW | PW | Recharged from/to group co. | 45910 | CAF income holding |  |  |
| PW | PW | Recharged from/to group co. | 45915 | CAF expense holding |  |  |
| PW | PW | Recharged from/to group co. | 45920 | CAF income group |  |  |
| PW | PW | Recharged from/to group co. | 45925 | CAF expense group |  |  |
| PX | PX | Income tax | 53100 | Current income tax |  |  |
| PX | PX | Income tax | 53300 | Deferred tax |  |  |
| PX | PX | Income tax | 53900 | Tax correction previous years |  |  |
| PY | PY | Non controlling interest | 55980 | Result non controlling interest |  |  |
| PZ | PZ | Transfer account result | 99998 | Transfer result current year |  |  |

## Change log

| Date | Change | Source |
|---|---|---|
| 2026-10-08 | Page generated from the old wiki "P&L Accounts" table. | `sources/wiki/pages/p-l-accounts.md` |
