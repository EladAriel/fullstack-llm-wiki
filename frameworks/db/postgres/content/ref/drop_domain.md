---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_domain.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
---

DROP DOMAIN

DROP DOMAIN
7
SQL - Language Statements

DROP DOMAIN
remove a domain

```
DROP DOMAIN [ IF EXISTS ] name [, ...] [ CASCADE | RESTRICT ]
```

## Description

`DROP DOMAIN` removes a domain. Only the owner of a domain can remove it.

## Parameters

- Do not throw an error if the domain does not exist. A notice is issued in this case.
- The name (optionally schema-qualified) of an existing domain.
- Automatically drop objects that depend on the domain (such as table columns), and in turn all objects that depend on those objects (see `ddl-depend`).
- Refuse to drop the domain if any objects depend on it. This is the default.

## Examples

To remove the domain `box`:

```
DROP DOMAIN box;
```

## Compatibility

This command conforms to the SQL standard, except for the `IF EXISTS` option, which is a PostgreSQL extension.

## See Also
