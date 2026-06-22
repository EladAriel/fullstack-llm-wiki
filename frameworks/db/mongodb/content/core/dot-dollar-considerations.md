---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/dot-dollar-considerations.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=========================================

# Field Names with Periods and Dollar Signs

MongoDB allows field names that contain dollar signs (`$`) or periods (`.`). However, use of these characters within field names is discouraged, because MongoDB does not support some features with these fields.

In most cases data that has been stored using field names like these is not directly accessible. You need to use helper methods like :expression:`$getField`, :expression:`$setField`, and :expression:`$literal` in queries that access those fields.

The field name validation rules are not the same for all types of storage operations.

## General Restrictions

There are some general restrictions on using dollar (`$`) prefixed field names or field names that contain a period (`.`). These fields cannot:

- Be indexed
- Be used as part of a shard key
- Be validated using :query:`$jsonSchema`
- Be modified with an escape sequence
- Be used with
:driver:`Field Level Encryption </security/client-side-field-level-encryption-guide>`

- Be used as a subfield in an `_id` document
- Have more than 255 words separated by periods in field names
- (`$`-prefix only) Be used as part of the `timeField` in
a `time series collection <manual-timeseries-collection>`

.. include:: /includes/warning-possible-data-loss.rst

.. include:: /includes/warning-dot-dollar-import-export.rst

## Learn More

For examples of how to handle field names that contain periods and dollar signs, see these pages:

- `dollar-prefix-field-names`
- `period-field-names`
## Contents

- Dollar Signs </core/dot-dollar-considerations/dollar-prefix>
- Periods </core/dot-dollar-considerations/periods>
