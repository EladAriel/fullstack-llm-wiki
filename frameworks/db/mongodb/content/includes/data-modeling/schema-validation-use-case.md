---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/data-modeling/schema-validation-use-case.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Your schema validation needs depend on how your application organizes data. Schema validation is most useful for an established application with a defined data structure.

> **Note:** Schema validation rules are also flexible, so they don't need to cover every
field in a document, unless your application requires that they do.

You can use schema validation in the following scenarios:

- For an `events` collection, ensure that the `start_date` field
stores only a date, not a string. Consistent types prevent unexpected values in connecting applications.

- For a `store` collection, ensure that the `accepted_credit_cards`
field contains only accepted card types, such as `["Visa", "MasterCard", "American Express"]`. This rule prevents users from entering unsupported values.

- For a `students` collection, ensure that the `gpa` field is
always a positive floating-point number. This rule prevents data entry errors.
