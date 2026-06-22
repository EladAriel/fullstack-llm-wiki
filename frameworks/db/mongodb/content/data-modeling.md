---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/data-modeling.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

========================

# Data Modeling in MongoDB

Data modeling refers to the organization of data within a database and the links between related entities.

MongoDB has a **flexible data model** that allows you to store polymorphic data, meaning:

- `Documents <document>` within a single :term:`collection
<collection>` are not required to have the same set of fields.

- A field's data type can differ between documents within a collection.
A core principle of data modeling in MongoDB is that data that's accessed together should be stored together. You should structure your data model based on your application's data access patterns to optimize performance.

To learn more, see `data-modeling-best-practices`.

## Use Cases

Consider the following examples that take advantage of the document model's flexibility:

- Your company tracks which department each employee works in. You can
embed department information in the `employee` collection to return relevant information in a single query.

- Your e-commerce application shows the five most recent reviews on a product
page. You can store all reviews, including older ones, in a separate collection because they are not accessed as frequently.

- Your clothing store needs to create a single-page application for a
product catalog. Different products have different attributes and might have different document fields and field types. Despite these differences, you can store all of the products in the same collection.

## Get Started

To ensure that your data model has a logical structure and achieves optimal performance, plan your schema prior to using your database at a production scale. To determine and implement your data model, follow the `schema design process <data-modeling-schema-design>`.

## Details

### Developing with a Flexible Data Model

MongoDB's flexible schema lets you iteratively improve your data model as you develop your application.

By developing with MongoDB's flexible schema, you can:

- Map your data model directly to objects that exist in code.
- Add schema validation only to the sections and aspects of the documents that
need stricter control.

For an example of how you can iteratively modify your data model, see `data-modeling-schema-iteration-example`.

### Document Relationships

The value of a document field can include any of the BSON `data types <bson-types>`, including other documents, arrays, and arrays of documents. These objects can be used to represent different types of relationships in your data model, including:

- **One-to-one relationships**: Each document is associated with exactly one
other document. For example, a patient has exactly one medical record.

- **One-to-many relationships**: Each document is associated with multiple other
documents. For example, a web application user can have many posts or comments.

- **Many-to-many relationships**: Each document can be associated with multiple
other documents, and vice versa. For example, a student can be enrolled in multiple courses, and each course can have multiple students.

In MongoDB, you can model relationships by either `embedding <data-modeling-embedding>` or `referencing <data-modeling-referencing>` your data. By choosing the best data-linking method, you can optimize your data model for your application's specific access patterns.

To learn more about modeling relationships in MongoDB, see:

- `data-modeling-relationships`.
- `data-modeling-decisions`.
### Schema Design: Differences Between Relational and Document Databases

When you design a schema for a document database like MongoDB, consider the following important differences from relational databases:

## Learn More

- `data-modeling-best-practices`
- `compass-data-modeling`
## Contents

- Best Practices </data-modeling/best-practices>
- /data-modeling/schema-design-process
- /data-modeling/design-patterns
- /data-modeling/design-antipatterns
- Model Relationships </applications/data-models-relationships>
- Model Tree Structures </applications/data-models-tree-structures>
- Example Application Models </applications/data-models-applications>
