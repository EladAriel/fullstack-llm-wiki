---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/func/func-statistics.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
---

## Statistics Information Functions

function
statistics

PostgreSQL provides a function to inspect complex statistics defined using the `CREATE STATISTICS` command.

## Inspecting MCV Lists

pg_mcv_list_items

```
pg_mcv_list_items ( pg_mcv_list ) setof record
```

`pg_mcv_list_items` returns a set of records describing all items stored in a multi-column MCV list. It returns the following columns: Name Type Description `index` `integer` index of the item in the MCV list `values` `text[]` values stored in the MCV item `nulls` `boolean[]` flags identifying `NULL` values `frequency` `double precision` frequency of this MCV item `base_frequency` `double precision` base frequency of this MCV item

The `pg_mcv_list_items` function can be used like this:

```
SELECT m.* FROM pg_statistic_ext join pg_statistic_ext_data on (oid = stxoid),
                pg_mcv_list_items(stxdmcv) m WHERE stxname = 'stts';
```

Values of the `pg_mcv_list` type can be obtained only from the `pg_statistic_ext_data`.`stxdmcv` column.
