---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/func/func-tid.sgml"
source_commit: "38afc3dcb25c45b744d4025029ce0a6c90b7059f"
source_commit_short: "38afc3dc"
source_commit_date: "2026-07-25T19:08:27+09:00"
generated_at: "2026-07-25T11:50:59Z"
---

## TID Functions

TID
functions

tid_block

tid_offset

`functions-tid-table` lists functions for the `tid` data type (tuple identifier).

## TID Functions

Function

Description

Example(s)

`tid_block` ( `tid` ) bigint

Extracts the block number from a tuple identifier.

`tid_block('(42,7)'::tid)` 42

`tid_offset` ( `tid` ) integer

Extracts the tuple offset within the block from a tuple identifier.

`tid_offset('(42,7)'::tid)` 7
