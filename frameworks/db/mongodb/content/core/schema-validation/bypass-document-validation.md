---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/schema-validation/bypass-document-validation.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

========================

# Bypass Schema Validation

In some situations, you may need to bypass a collection's schema validation rules. For example, if you are restoring potentially invalid data from a backup to a collection that has validation rules. In this scenario, older documents may not meet new validation requirements.

## Context

Bypassing schema validation is done on a per-operation basis. If you bypass schema validation to insert an invalid document, any future updates to the invalid document must either:

- Also bypass schema validation
- Result in a valid document
## Supported Operations

You can use the following commands and methods to bypass validation on a per-operation basis:

- :dbcommand:`applyOps` command
- :dbcommand:`findAndModify` command and
:method:`db.collection.findAndModify()` method

- :dbcommand:`mapReduce` command and
:method:`db.collection.mapReduce()` method

- :dbcommand:`insert` command
- :dbcommand:`update` command
- :pipeline:`$out` and :pipeline:`$merge` stages for the
:dbcommand:`aggregate` command and :method:`db.collection.aggregate()` method

## Prerequisite

For deployments that have enabled access control, to bypass document validation, the authenticated user must have :authaction:`bypassDocumentValidation` action. The built-in roles :authrole:`dbAdmin` and :authrole:`restore` provide this action.

## Steps

The following example creates a collection with schema validation, and then inserts an invalid document by bypassing the validation rules.

## Results

To confirm that the document was successfully inserted, query the `students` collection:

```javascript
db.students.find()
```

MongoDB returns the inserted document:

```javascript
[
   {
      _id: ObjectId("62bcb4db3f7991ea4fc6830e"),
      name: 'Alice',
      year: 2016,
      major: 'History',
      gpa: 3,
      address: { city: 'NYC', street: '33rd Street' }
   }
]
```

## Learn More

- `use-json-schema-query-conditions`
- `schema-specify-validation-level`
