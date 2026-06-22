---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=================

# Database Commands

All command documentation outlined below describes a command and its available parameters and provides a document template or prototype for each command. Some command documentation also includes the relevant :binary:`~bin.mongosh` helpers.

To run a command against the current database, use :method:`db.runCommand()`:

```javascript
db.runCommand( { <command> } )
```

To run an administrative command against the `admin` database, use :method:`db.adminCommand()`:

```javascript
db.adminCommand( { <command> } )
```

.. include:: /includes/extracts/commands-toc-explanation.rst

## Command Syntax

When you run a database command, you specify the command as a document to :method:`db.runCommand()`. The document's key is the command to run, and the value is typically supplied as `1`. The value does not affect the output of the command for example:

```javascript
db.runCommand( { hello: 1 } )
```

## User Commands

### Aggregation Commands

### Query and Write Operation Commands

### Query Plan Cache Commands

## Contents

- Query Plan Cache </reference/command/nav-plan-cache>

## Database Operations

### Authentication Commands

## Contents

- Authentication </reference/command/nav-authentication>

### User Management Commands

## Contents

- User Management </reference/command/nav-user-management>

### Role Management Commands

## Contents

- Role Management </reference/command/nav-role-management>

### Replication Commands

## Contents

- Replication </reference/command/nav-replication>

> **Seealso:** `/replication` for more information regarding
replication.

### Sharding Commands

## Contents

- Sharding </reference/command/nav-sharding>

> **Seealso:** `/sharding` for more information about MongoDB's
sharding functionality.

### Session Commands

.. include:: /includes/table-sessions-commands.rst

## Contents

- Sessions </reference/command/nav-sessions>

### Administration Commands

## Contents

- Administration </reference/command/nav-administration>

### Diagnostic Commands

## Contents

- Diagnostics </reference/command/nav-diagnostic>

### Auditing Commands

## Contents

- Auditing </reference/command/nav-auditing>

## {+fts+} Commands

.. versionadded:: 7.0 (Also available starting in 6.0.7)

.. include:: /includes/atlas-search-commands/atlas-search-command-table.rst

## Contents

- {+fts+} </reference/command/nav-atlas-search>
