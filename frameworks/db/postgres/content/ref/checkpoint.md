---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/checkpoint.sgml"
source_commit: "38afc3dcb25c45b744d4025029ce0a6c90b7059f"
source_commit_short: "38afc3dc"
source_commit_date: "2026-07-25T19:08:27+09:00"
generated_at: "2026-07-25T11:50:59Z"
---

CHECKPOINT

CHECKPOINT
7
SQL - Language Statements

CHECKPOINT
force a write-ahead log checkpoint

```
CHECKPOINT [ ( option [, ...] ) ]

where option can be one of:

    FLUSH_UNLOGGED [ boolean ]
    MODE { FAST | SPREAD }
```

## Description

A checkpoint is a point in the write-ahead log sequence at which all data files for permanent relations have been updated to reflect the information in the log. All data for permanent relation files will be flushed to disk. Dirty buffers of unlogged relations are not flushed unless `FLUSH_UNLOGGED` is specified. Refer to `wal-configuration` for more details about what happens during a checkpoint.

By default, the `CHECKPOINT` command forces a fast checkpoint when the command is issued, without waiting for a regular checkpoint scheduled by the system (controlled by the settings in `runtime-config-wal-checkpoints`). To request the checkpoint be spread over a longer interval, set the `MODE` option to `SPREAD`. `CHECKPOINT` is not intended for use during normal operation.

The server may consolidate concurrently requested checkpoints. Such consolidated requests will contain a combined set of options. For example, if one session requests a fast checkpoint and another requests a spread checkpoint, the server may combine those requests and perform one fast checkpoint.

If executed during recovery, the `CHECKPOINT` command will force a restartpoint (see `wal-configuration`) rather than writing a new checkpoint.

Only superusers or users with the privileges of the `predefined-role-pg-checkpoint` role can call `CHECKPOINT`.

## Parameters

- Normally, `CHECKPOINT` does not flush dirty buffers of unlogged relations. This option, which is disabled by default, enables flushing unlogged relations to disk.
- When set to `FAST`, which is the default, the requested checkpoint will be completed as fast as possible, which may result in a significantly higher rate of I/O during the checkpoint. `MODE` can also be set to `SPREAD` to request the checkpoint be spread over a longer interval (controlled via the settings in `runtime-config-wal-checkpoints`), like a regular checkpoint scheduled by the system. This can reduce the rate of I/O during the checkpoint.
- Specifies whether the selected option should be turned on or off. You can write `TRUE`, `ON`, or `1` to enable the option, and `FALSE`, `OFF`, or `0` to disable it. The `boolean` value can also be omitted, in which case `TRUE` is assumed.

## Compatibility

The `CHECKPOINT` command is a PostgreSQL language extension.
