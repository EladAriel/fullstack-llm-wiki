---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/mql/update.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

================

# Update Operators

The following modifiers are available for use in update operations such as :method:`db.collection.updateMany()` and :method:`db.collection.findAndModify()`.

## Syntax

Specify update operators in the following form:

```javascript
{
   <operator1>: { <field1>: <value1>, ... },
   <operator2>: { <field2>: <value2>, ... },
   ...
}
```

## Update Operators

### Behavior

Starting in MongoDB 5.0, update operators process document fields with string-based names in lexicographic order. Fields with numeric names are processed in numeric order.

Consider this example :update:`$set` command:

```javascript
{ $set: { "a.2": <new value>, "a.10": <new value>, } }
```

In MongoDB 5.0 and later, `"a.2"` is processed before `"a.10"` because `2` comes before `10` in numeric order.

### Fields

### Array

Operators `````````

Modifiers `````````

### Bitwise

## Contents

- Arrays </reference/operator/update-array>
- Bitwise </reference/operator/update-bitwise>
- Fields </reference/operator/update-field>

## Updates with Aggregation Pipeline

To create expressive update statements, such as conditional updates based on current field values or single-field updates that use the value of another field, you can perform updates with an aggregation pipeline.

For syntax and examples, see `updates-agg-pipeline`.
