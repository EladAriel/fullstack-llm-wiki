---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/data-modeling/design-patterns/polymorphic-data/inheritance-schema-pattern.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================

# Use the Inheritance Pattern

Use the inheritance pattern when your documents are mostly similar and you want to keep them in the same collection so they can be read together. The inheritance pattern uses a parent entity with common fields to group child entities that have variable forms. The child entities can have unique fields, but are closely related to one another due to their common fields.

## About this Task

In this example, a book store uses the inheritance pattern to store different types of media. A `book` parent entity stores common fields like `title` and `author`, and multiple child entities inherit from the `book` entity. For example audio books, printed books, and ebooks have common fields, and also have unique fields specific to the media type.

The inheritance pattern stores these slightly different entities in the same collection, which improves performance for queries that need to access all books, regardless of type.

## Steps

## Learn More

- `polymorphic-schema-pattern`
- `schema-validation-overview`
- `create-indexes-to-support-queries`
