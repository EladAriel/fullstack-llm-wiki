---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_event_trigger.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
---

DROP EVENT TRIGGER

DROP EVENT TRIGGER
7
SQL - Language Statements

DROP EVENT TRIGGER
remove an event trigger

```
DROP EVENT TRIGGER [ IF EXISTS ] name [ CASCADE | RESTRICT ]
```

## Description

`DROP EVENT TRIGGER` removes an existing event trigger. To execute this command, the current user must be the owner of the event trigger.

## Parameters

- Do not throw an error if the event trigger does not exist. A notice is issued in this case.
- The name of the event trigger to remove.
- Automatically drop objects that depend on the trigger, and in turn all objects that depend on those objects (see `ddl-depend`).
- Refuse to drop the trigger if any objects depend on it. This is the default.

## Examples

Destroy the trigger `snitch`:

```
DROP EVENT TRIGGER snitch;
```

## Compatibility

There is no `DROP EVENT TRIGGER` statement in the SQL standard.

## See Also
