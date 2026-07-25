---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/replSetStepDown.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

==================================

# replSetStepDown (database command)

## Description

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-onprem-only.rst

.. include:: /includes/fact-environments-no-atlas-support.rst

## Syntax

The command has the following syntax:

```javascript
db.adminCommand( 
   { 
     replSetStepDown: <seconds>,
     secondaryCatchUpPeriodSecs: <seconds>,
     force: <true|false>
   } 
)
```

## Command Fields

The command takes the following fields:

## Behavior

### Concurrent Operations

.. include:: /includes/extracts/rs-stepdown-concurrent-ops.rst

### Availability of Eligible Secondaries

.. include:: /includes/extracts/rs-stepdown-eligible-secondaries.rst

### Client Connections

.. include:: /includes/extracts/rs-stepdown-client-connections.rst

### Writes During Stepdown

.. include:: /includes/extracts/rs-stepdown-write-fail.rst

### Election Handoff

.. include:: /includes/extracts/rs-stepdown-election-handoff.rst

## Examples

### Step Down with Default Options

The following example, run on the current primary, attempts to step down the member for `120` seconds.

The operation waits up to the default `10` seconds for a secondary to catch up. If no suitable secondary exists, the primary does not step down and the command errors.

.. include:: /includes/extracts/rs-stepdown-write-fail.rst

```javascript
db.adminCommand( { replSetStepDown: 120 } )
```

### Specify Wait Time for Secondary Catch Up

The following example, run on the current primary, attempts to step down the member for `120` seconds, waiting up to `15` seconds for an electable secondary to catch up. If no suitable secondary exists, the primary does not step down and the command errors.

.. include:: /includes/extracts/rs-stepdown-write-fail.rst

```javascript
db.adminCommand( { replSetStepDown: 120, secondaryCatchUpPeriodSecs: 15 } )
```

### Specify Secondary Catch Up with Force Step Down

The following example, run on the current primary, attempts to step down the member for `120` seconds, waiting up to `15` seconds for an electable secondary to catch up. Because of the `force: true` option, the primary steps down even if no suitable secondary exists.

.. include:: /includes/extracts/rs-stepdown-write-fail.rst

```javascript
db.adminCommand( { replSetStepDown: 120, secondaryCatchUpPeriodSecs: 15, force: true } )
```

> **Seealso:** :method:`rs.stepDown()`
