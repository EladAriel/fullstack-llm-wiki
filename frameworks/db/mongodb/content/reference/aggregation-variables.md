---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/aggregation-variables.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
