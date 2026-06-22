---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/aggregation-variables.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

====================================

# Variables in Aggregation Expressions

`Aggregation expressions <aggregation-expressions>` can use both user-defined and system variables.

Variables can hold any `BSON type data <bson-types>`. To access the value of the variable, prefix the variable name with double dollar signs (`$$`); i.e. `"$$<variable>"`.

If the variable references an object, to access a specific field in the object, use the dot notation; i.e. `"$$<variable>.<field>"`.

## User Variables

User variable names can contain the ascii characters `[_a-zA-Z0-9]` and any non-ascii character.

User variable names must begin with a lowercase ascii letter `[a-z]` or a non-ascii character.

## System Variables

MongoDB offers the following system variables:

> **Seealso:** - :expression:`$let`
- :pipeline:`$redact`
- :expression:`$map`
- :expression:`$filter`
- :expression:`$reduce`
