---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/profile.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========================

# profile (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

```javascript
db.runCommand(
  {
    profile: <level>,
    slowms: <threshold>,
    sampleRate: <rate>,
    filter: <filter expression>
  }
)
```

## Command Fields

The command takes the following fields:

The :method:`db.getProfilingStatus()` and :method:`db.setProfilingLevel()` `shell methods <js-administrative-methods>` provide wrappers around the :dbcommand:`profile` command.

## Behavior

The :dbcommand:`profile` command obtains a write lock on the affected database while enabling or disabling the profiler. This is typically a short operation. The lock blocks other operations until the :dbcommand:`profile` command has completed.

When connected to a sharded cluster through :binary:`~bin.mongos`, you can run the :dbcommand:`profile` command against any database.

> **Seealso:** `Database Profiling <database-profiling>`

## Example

### Enable Filtering

To enable profiling and filter the logged data:

```javascript
db.runCommand( 
   {
     profile: 1,
     filter:
        {
           $or:
           [
              { millis: { $gte: 100 } },
              { user: "testuser@admin" }
           ]
        }
   }
)
```

The `filter <profile-filter-def>` only selects operations that are:

- at least `100` milliseconds long, or
- submitted by the `testuser`.
### Unset a Filter

To clear a profile filter, run `profile` with the `filter: "unset"` option.

```javascript
db.runCommand(
   { 
      profile: 1,
      filter: "unset" 
   }
)
```

.. include:: /includes/reference/return-set-profile.rst
