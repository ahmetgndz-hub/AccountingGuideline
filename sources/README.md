# Sources

Raw source material for the guideline. Files here are **never edited** after intake, except for the
`status` / `superseded_by` fields in the front matter.

## emails/

One file per guideline e-mail, named `YYYY-MM-DD_<short-subject>.md`:

```markdown
---
date: 2026-09-02
subject: September 2026 closing instructions
from: Ahmet Gündüz
to: Finance teams
status: current          # current | superseded | obsolete
superseded_by:           # file name of the newer e-mail, if any
topics: [closing-calendar, accruals]
---

<e-mail body, verbatim>
```

- `current`: the instruction is in force and reflected in the guideline.
- `superseded`: a newer e-mail replaced it; kept for history only.
- `obsolete`: withdrawn without replacement; not in the guideline.

## wiki/

Copies of the old SharePoint Multi Wiki page, dated, for comparison. Not maintained.
