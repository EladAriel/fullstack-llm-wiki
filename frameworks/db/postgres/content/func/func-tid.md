---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/func/func-tid.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
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
