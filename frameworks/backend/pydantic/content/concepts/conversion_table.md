---
type: "Framework Learn Page"
framework: "pydantic"
source_repo: "https://github.com/pydantic/pydantic"
source_branch: "main"
source_path: "docs/concepts/conversion_table.md"
source_commit: "363728fe0b353db1a1fcb44aac5c38fd96a8cc20"
source_commit_short: "363728fe"
source_commit_date: "2026-06-20T11:20:58+01:00"
generated_at: "2026-06-21T11:37:01Z"
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
