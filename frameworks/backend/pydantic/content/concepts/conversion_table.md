---
type: "Framework Learn Page"
framework: "pydantic"
source_repo: "https://github.com/pydantic/pydantic"
source_branch: "main"
source_path: "docs/concepts/conversion_table.md"
source_commit: "a2a6577d4c329dd574a45dbb01a8feaa16b1ad3d"
source_commit_short: "a2a6577d"
source_commit_date: "2026-07-23T15:38:17Z"
generated_at: "2026-07-25T11:50:12Z"
---

The following table provides details on how Pydantic converts data during validation in both strict and lax modes.

The "Strict" column contains checkmarks for type conversions that are allowed when validating in
[Strict Mode](strict_mode.md).

=== "All"
{{ conversion_table_all }}

=== "JSON"
{{ conversion_table_json }}

=== "JSON - Strict"
{{ conversion_table_json_strict }}

=== "Python"
{{ conversion_table_python }}

=== "Python - Strict"
{{ conversion_table_python_strict }}
