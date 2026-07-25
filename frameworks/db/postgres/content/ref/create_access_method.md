---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/create_access_method.sgml"
source_commit: "38afc3dcb25c45b744d4025029ce0a6c90b7059f"
source_commit_short: "38afc3dc"
source_commit_date: "2026-07-25T19:08:27+09:00"
generated_at: "2026-07-25T11:50:59Z"
---

CREATE ACCESS METHOD

CREATE ACCESS METHOD
7
SQL - Language Statements

CREATE ACCESS METHOD
define a new access method

```
CREATE ACCESS METHOD name
    TYPE access_method_type
    HANDLER handler_function
```

## Description

`CREATE ACCESS METHOD` creates a new access method.

The access method name must be unique within the database.

Only superusers can define new access methods.

## Parameters

- The name of the access method to be created.
- This clause specifies the type of access method to define. Only `TABLE` and `INDEX` are supported at present.
- `handler_function` is the name (possibly schema-qualified) of a previously registered function that represents the access method. The handler function must be declared to take a single argument of type `internal`, and its return type depends on the type of access method; for `TABLE` access methods, it must be `table_am_handler` and for `INDEX` access methods, it must be `index_am_handler`. The C-level API that the handler function must implement varies depending on the type of access method. The table access method API is described in `tableam` and the index access method API is described in `indexam`.

## Examples

Create an index access method `heptree` with handler function `heptree_handler`:

```
CREATE ACCESS METHOD heptree TYPE INDEX HANDLER heptree_handler;
```

## Compatibility

`CREATE ACCESS METHOD` is a PostgreSQL extension.

## See Also
