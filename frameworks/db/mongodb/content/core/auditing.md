---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/auditing.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

========

# Auditing

> **Note:** {+atlas+} supports auditing for `M10` and larger clusters.
To learn more, see `<set-up-database-auditing>` in the {+atlas+}
documentation.

MongoDB Enterprise includes an auditing facility for :binary:`~bin.mongod` and :binary:`~bin.mongos` instances. The facility allows administrators and users to track system activity for deployments with multiple users and applications.

## Enable and Configure Audit Output

The auditing facility can write audit events to the console, the `syslog`, a JSON file, or a BSON file. To enable auditing in MongoDB Enterprise, set an audit output destination with :option:`--auditDestination <mongod --auditDestination>`. For details, see `/tutorial/configure-auditing`.

For information on the audit log messages, see `/reference/audit-message`.

## Audit Events and Filter

Once enabled, the auditing system can record the following operations [#transactions]_:

- schema (DDL),
- replica set and sharded cluster,
- authentication and authorization, and
- CRUD operations (requires :parameter:`auditAuthorizationSuccess` set to `true`).
> **Note:** Starting in MongoDB 5.0, `secondaries <secondary>` do not log
DDL audit events for replicated changes. DDL audit events are still
logged for DDL operations that modify the :ref:`local database
<replica-set-local-database>` and the :data:`system.profile
<<database>.system.profile>` collection.

For details on audited actions, see `audit-message-format`.

Use `filters <audit-filter>` to restrict captured events. See `Configure Audit Filters <audit-filter>` for details.

Operations in an aborted transaction still generate audit events. However, there is no audit event that indicates that the transaction aborted.

## Audit Guarantee

The auditing system writes every audit event [#filter]_ to an in-memory buffer. MongoDB writes this buffer to disk periodically.

Events from a single connection are ordered: if MongoDB writes one event to disk, it has written all prior events for that connection.

If an audit event corresponds to an operation that affects the durable state of the database, such as a modification to data, MongoDB writes the audit event to disk before writing to the `journal` for that entry. Before adding an operation to the journal, MongoDB writes all audit events on that connection, up to and including the entry for that operation.

> **Warning:** MongoDB may lose events **if** the server terminates before it
commits the events to the audit log. The client may receive
confirmation of the event before MongoDB commits to the audit log.
For example, while auditing an aggregation operation, the server
might terminate after returning the result but before the audit log
flushes.
In addition, if the server cannot write to the audit log at the
:option:`audit destination <mongod --auditDestination>`, the server
terminates.

<audit-filter>` to limit events to audit.

## Contents

- Configure </tutorial/configure-auditing>
- Configure Filters </tutorial/configure-audit-filters>
- Audit Messages </reference/audit-message>
