---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/audit-message.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================

# System Event Audit Messages

> **Note:** System Event Audit Messages are available in
`MongoDB Enterprise <install-mdb-enterprise>`
and :atlas:`{+atlas+} </>`.
To learn more about this feature in {+atlas+}, see
the Atlas documentation for `<set-up-database-auditing>`
and `<mongodb-logs>`.

When the MongoDB auditing facility captures events, you can specify the schema that MongoDB uses for log message output:

- The `mongo` schema writes logs in a format designed by MongoDB. This
is the default log output schema.

- The `OCSF` schema writes logs in {+ocsf+} format. This option
provides logs in a more widely-used standardized format compatible with log processors.

To set the schema used for log messages, use the :setting:`auditLog.schema` configuration file option.

For examples and details on the messages returned in each schema, see these pages:

- `event-audit-messages-mongo`
- `event-audit-messages-ocsf`
## Contents

- mongo Schema </reference/audit-message/mongo>
- OSCF Schema </reference/audit-message/ocsf>
