---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/HexData.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========================

# HexData() (mongosh method)

## Definition

Creates a binary data object from hexadecimal data.

## Syntax

`HexData()` has the following syntax:

## Command Fields

The command takes these fields:

> **Note:** `mongosh` silently stops parsing at the first non-hex character, unlike the
legacy shell which rejects invalid hex characters. To determine if your
`HexData()` output is valid, you can use the `.toString('hex')` method on the
`HexData()` output and compare that string against the original input string
using a case-insensitive comparison.

## Examples

## Learn More

- :method:`BinData()`
- :method:`Binary.createFromBase64()`
