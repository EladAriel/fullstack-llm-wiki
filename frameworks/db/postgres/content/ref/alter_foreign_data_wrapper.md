---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/alter_foreign_data_wrapper.sgml"
source_commit: "38afc3dcb25c45b744d4025029ce0a6c90b7059f"
source_commit_short: "38afc3dc"
source_commit_date: "2026-07-25T19:08:27+09:00"
generated_at: "2026-07-25T11:50:59Z"
---

ALTER FOREIGN DATA WRAPPER

ALTER FOREIGN DATA WRAPPER
7
SQL - Language Statements

ALTER FOREIGN DATA WRAPPER
change the definition of a foreign-data wrapper

```
ALTER FOREIGN DATA WRAPPER name
    [ HANDLER handler_function | NO HANDLER ]
    [ VALIDATOR validator_function | NO VALIDATOR ]
    [ CONNECTION connection_function | NO CONNECTION ]
    [ OPTIONS ( [ ADD | SET | DROP ] option ['value'] [, ... ]) ]
ALTER FOREIGN DATA WRAPPER name OWNER TO { new_owner | CURRENT_ROLE | CURRENT_USER | SESSION_USER }
ALTER FOREIGN DATA WRAPPER name RENAME TO new_name
```

## Description

`ALTER FOREIGN DATA WRAPPER` changes the definition of a foreign-data wrapper. The first form of the command changes the support functions or the generic options of the foreign-data wrapper (at least one clause is required). The second form changes the owner of the foreign-data wrapper.

Only superusers can alter foreign-data wrappers. Additionally, only superusers can own foreign-data wrappers.

## Parameters

- The name of an existing foreign-data wrapper.
- Specifies a new handler function for the foreign-data wrapper.
- This is used to specify that the foreign-data wrapper should no longer have a handler function. Note that foreign tables that use a foreign-data wrapper with no handler cannot be accessed.
- Specifies a new validator function for the foreign-data wrapper. Note that it is possible that pre-existing options of the foreign-data wrapper, or of dependent servers, user mappings, or foreign tables, are invalid according to the new validator. PostgreSQL does not check for this. It is up to the user to make sure that these options are correct before using the modified foreign-data wrapper. However, any options specified in this `ALTER FOREIGN DATA WRAPPER` command will be checked using the new validator.
- This is used to specify that the foreign-data wrapper should no longer have a validator function.
- Specifies a new connection function for the foreign-data wrapper.
- This is used to specify that the foreign-data wrapper should no longer have a connection function.
- Change options for the foreign-data wrapper. `ADD`, `SET`, and `DROP` specify the action to be performed. `ADD` is assumed if no operation is explicitly specified. Option names must be unique; names and values are also validated using the foreign data wrapper's validator function, if any.
- The user name of the new owner of the foreign-data wrapper.
- The new name for the foreign-data wrapper.

## Examples

Change a foreign-data wrapper `dbi`, add option `foo`, drop `bar`:

```
ALTER FOREIGN DATA WRAPPER dbi OPTIONS (ADD foo '1', DROP bar);
```

Change the foreign-data wrapper `dbi` validator to `bob.myvalidator`:

```
ALTER FOREIGN DATA WRAPPER dbi VALIDATOR bob.myvalidator;
```

## Compatibility

`ALTER FOREIGN DATA WRAPPER` conforms to ISO/IEC 9075-9 (SQL/MED), except that the `HANDLER`, `VALIDATOR`, `OWNER TO`, and `RENAME` clauses are extensions.

## See Also
