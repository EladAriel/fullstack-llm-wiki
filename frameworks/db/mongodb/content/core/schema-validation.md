---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/schema-validation.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=================

# Schema Validation

Schema validation lets you create validation rules for your fields, such as allowed data types and value ranges.

MongoDB uses a flexible schema model. By default, documents in a collection don't need the same fields or data types. After you establish an application schema, use schema validation to prevent unintended schema changes and data type errors.

## When to Use Schema Validation

.. include:: /includes/data-modeling/schema-validation-use-case.rst

## When MongoDB Checks Validation

After you add schema validation rules to a collection:

- All document inserts must match the rules.
- The validation level determines how rules apply to existing documents
and updates. To learn more, see `schema-specify-validation-level`.

To find documents in a collection that don't match the schema validation rules, see `use-json-schema-query-conditions-find-documents`.

## What Happens When a Document Fails Validation

By default, MongoDB rejects any insert or update operation that would produce an invalid document.

Alternatively, you can configure MongoDB to allow invalid documents and log a warning when a schema violation occurs.

To learn more, see `schema-validation-handle-invalid-docs`.

## Get Started

For schema validation tasks, see the following pages:

- `schema-validation-json`
- `schema-validation-polymorphic-collections`
- `schema-validation-query-expression`
- `schema-allowed-field-values`
- `schema-view-validation-rules`
- `schema-update-validation`
- `use-json-schema-query-conditions`
- `schema-bypass-document-validation`
## Learn More

To learn about MongoDB's flexible schema model, see `manual-data-modeling-intro`.

## Contents

- Specify JSON Validation </core/schema-validation/specify-json-schema>
- Specify Validation for Polymorphic Collections </core/schema-validation/specify-validation-polymorphic-collections>
- Specify Query Operators </core/schema-validation/specify-query-expression-rules>
- Specify Validation Level </core/schema-validation/specify-validation-level>
- Handle Invalid Documents </core/schema-validation/handle-invalid-documents>
- Bypass </core/schema-validation/bypass-document-validation>
- View Existing Rules </core/schema-validation/view-existing-validation-rules>
- Modify Rules </core/schema-validation/update-schema-validation>
- Query and Modify </core/schema-validation/use-json-schema-query-conditions>
