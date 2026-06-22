---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/schema-validation/specify-validation-level.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================================

# Specify Validation Level for Existing Documents

For documents that already exist in your collection prior to adding validation, you can specify how MongoDB applies validation rules to these documents.

## Context

Your schema's `validationLevel` determines the documents for which MongoDB applies validation rules:

## Prerequisite

The examples on this page use a `contacts` collection with these documents:

```json
db.contacts.insertMany([
   { "_id": 1, "name": "Anne", "phone": "+1 555 123 456", "city": "London", "status": "Complete" },
   { "_id": 2, "name": "Ivan", "city": "Vancouver" }
])
```

## Steps: Use `strict` Validation

The following example adds a `strict` validation to the `contacts` collection and shows the results when attempting to update invalid documents.

## Steps: Use `moderate` Validation

The following example adds a `moderate` validation to the `contacts` collection and shows the results when attempting to update invalid documents.

> **Important:** The error output is intended for human consumption. It may change in
the future and should not be relied upon in scripts.

## Learn More

- `schema-validation-handle-invalid-docs`
- `schema-update-validation`
