---
type: "Framework Learn Page"
framework: "Pydantic"
source_repo: "https://github.com/pydantic/pydantic"
source_branch: "main"
source_path: "docs/concepts/conversion_table.md"
source_commit: "4bc21c0fa28323c0f3e0be93c9ad114b705029c6"
source_commit_short: "4bc21c0"
source_commit_date: "2026-08-29T11:30:40+02:00"
generated_at: "2026-08-29T09:38:50.587727Z"
---
# Conversion_Table

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
