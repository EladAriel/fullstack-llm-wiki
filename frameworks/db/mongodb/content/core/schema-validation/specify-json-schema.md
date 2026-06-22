---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/schema-validation/specify-json-schema.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================

# Specify JSON Schema Validation

JSON Schema is a vocabulary that lets you annotate and validate JSON documents. Use JSON Schema to specify validation rules for your fields in a human-readable format.

## Context

.. include:: /includes/schema-validation/json-schema-intro.rst

## Restrictions

You can't specify schema validation for:

- Collections in the `admin`, `local`, and `config` databases
- `System collections <metadata-system-collections>`
.. include:: /includes/queryable-encryption/qe-csfle-schema-validation.rst

## Steps

In this example, you create a `students` collection with validation rules and observe the results after you attempt to insert an invalid document.

## Additional Information

You can combine JSON Schema validation with `query operator validation <schema-validation-query-expression>`.

.. include:: /includes/schema-validation-combine-validation-types.rst

## Learn More

- For a complete list of allowed JSON Schema keywords, see
`jsonSchema-keywords`.

- To restrict what values a certain field can contain, see
`schema-allowed-field-values`.

- To avoid issues with JSON Schema validation, see
`json-schema-tips`.

## Contents

- Specify Field Values </core/schema-validation/specify-json-schema/specify-allowed-field-values>
- Best Practices </core/schema-validation/specify-json-schema/json-schema-tips>
