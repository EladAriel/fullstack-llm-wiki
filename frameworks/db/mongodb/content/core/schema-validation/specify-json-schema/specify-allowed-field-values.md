---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/schema-validation/specify-json-schema/specify-allowed-field-values.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============================

# Specify Allowed Field Values

When you create a `JSON Schema <schema-validation-json>`, you can specify what values are allowed in a particular field. Use this functionality to ensure that your field values belong to an expected set of values, such as a list of countries. Similarly, you can use this functionality to prevent human error, such as typos, when inserting data into a collection.

## Context

To specify a list of allowed values, use the `enum` keyword in your JSON schema. The `enum` keyword means "enumerate", and is used to list possible values of a field.

## Steps

Consider a clothing company that only ships products to France, the United Kingdom, and the United States. In the validator, you can list the allowed country values and reject documents that specify a different country.
