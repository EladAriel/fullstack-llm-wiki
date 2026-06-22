---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/load.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
---

LOAD

LOAD
7
SQL - Language Statements

LOAD
load a shared library file

```
LOAD 'filename'
```

## Description

This command loads a shared library file into the PostgreSQL server's address space. If the file has been loaded already, the command does nothing. Shared library files that contain C functions are automatically loaded whenever one of their functions is called. Therefore, an explicit `LOAD` is usually only needed to load a library that modifies the server's behavior through hooks rather than providing a set of functions.

The library file name is typically given as just a bare file name, which is sought in the server's library search path (set by `guc-dynamic-library-path`). Alternatively it can be given as a full path name. In either case the platform's standard shared library file name extension may be omitted. See `xfunc-c-dynload` for more information on this topic.

`$libdir/plugins`

Non-superusers can only apply `LOAD` to library files located in `$libdir/plugins/` -- the specified `filename` must begin with exactly that string. (It is the database administrator's responsibility to ensure that only safe libraries are installed there.)

## Compatibility

`LOAD` is a PostgreSQL extension.

## See Also

`sql-createfunction`
