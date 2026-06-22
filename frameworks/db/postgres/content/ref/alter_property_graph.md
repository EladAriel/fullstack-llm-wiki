---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/alter_property_graph.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
---

ALTER PROPERTY GRAPH

ALTER PROPERTY GRAPH
7
SQL - Language Statements

ALTER PROPERTY GRAPH
change the definition of an SQL-property graph

```
ALTER PROPERTY GRAPH name ADD
    [ {VERTEX|NODE} TABLES ( vertex_table_definition [, ...] ) ]
    [ {EDGE|RELATIONSHIP} TABLES ( edge_table_definition [, ...] ) ]

ALTER PROPERTY GRAPH name DROP
    {VERTEX|NODE} TABLES ( vertex_table_alias [, ...] ) [ CASCADE | RESTRICT ]

ALTER PROPERTY GRAPH name DROP
    {EDGE|RELATIONSHIP} TABLES ( edge_table_alias [, ...] ) [ CASCADE | RESTRICT ]

ALTER PROPERTY GRAPH name ALTER
    {VERTEX|NODE|EDGE|RELATIONSHIP} TABLE element_table_alias
    { ADD LABEL label_name [ NO PROPERTIES | PROPERTIES ALL COLUMNS | PROPERTIES ( { expression [ AS property_name ] } [, ...] ) ] } [ ... ]

ALTER PROPERTY GRAPH name ALTER
    {VERTEX|NODE|EDGE|RELATIONSHIP} TABLE element_table_alias
    DROP LABEL label_name [ CASCADE | RESTRICT ]

ALTER PROPERTY GRAPH name ALTER
    {VERTEX|NODE|EDGE|RELATIONSHIP} TABLE element_table_alias
    ALTER LABEL label_name ADD PROPERTIES ( { expression [ AS property_name ] } [, ...] )

ALTER PROPERTY GRAPH name ALTER
    {VERTEX|NODE|EDGE|RELATIONSHIP} TABLE element_table_alias
    ALTER LABEL label_name DROP PROPERTIES ( property_name [, ...] ) [ CASCADE | RESTRICT ]

ALTER PROPERTY GRAPH name OWNER TO { new_owner | CURRENT_USER | SESSION_USER }
ALTER PROPERTY GRAPH name RENAME TO new_name
ALTER PROPERTY GRAPH [ IF EXISTS ] name SET SCHEMA new_schema
```

## Description

`ALTER PROPERTY GRAPH` changes the definition of an existing property graph. There are several subforms: - This form adds new vertex or edge tables to the property graph, using the same syntax as CREATE PROPERTY GRAPH. - This form removes vertex or edge tables from the property graph. (Only the association of the tables with the graph is removed. The tables themselves are not dropped.) - This form adds a new label to an existing vertex or edge table, using the same syntax as CREATE PROPERTY GRAPH. - This form removes a label from an existing vertex or edge table. - This form adds new properties to an existing label on an existing vertex or edge table. - This form removes properties from an existing label on an existing vertex or edge table. - This form changes the owner of the property graph to the specified user. - This form changes the name of a property graph. - This form moves the property graph into another schema.

You must own the property graph to use `ALTER PROPERTY GRAPH`. To change a property graph's schema, you must also have `CREATE` privilege on the new schema. To alter the owner, you must be able to `SET ROLE` to the new owning role, and that role must have `CREATE` privilege on the property graph's schema. (These restrictions enforce that altering the owner doesn't do anything you couldn't do by dropping and recreating the property graph. However, a superuser can alter ownership of any property graph anyway.)

## Parameters

- The name (optionally schema-qualified) of a property graph to be altered.
- Do not throw an error if the property graph does not exist. A notice is issued in this case.
- See CREATE PROPERTY GRAPH.
- The alias of an existing vertex or edge table to operate on. (Note that the alias is potentially different from the name of the underlying table, if the vertex or edge table was created with `AS alias`.)
- See CREATE PROPERTY GRAPH.
- The user name of the new owner of the property graph.
- The new name for the property graph.
- The new schema for the property graph.

## Notes

The consistency checks on a property graph described at `sql-create-property-graph-notes` must be maintained by `ALTER PROPERTY GRAPH` operations. In some cases, it might be necessary to make multiple alterations in a single command to satisfy the checks.

## Examples

```
ALTER PROPERTY GRAPH g1 ADD VERTEX TABLES (v2);

ALTER PROPERTY GRAPH g1 ALTER VERTEX TABLE v1 DROP LABEL foo;

ALTER PROPERTY GRAPH g1 RENAME TO g2;
```

## Compatibility

`ALTER PROPERTY GRAPH` conforms to ISO/IEC 9075-16 (SQL/PGQ).

## See Also
