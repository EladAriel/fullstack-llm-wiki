---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/unset.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

==========================

# $unset (aggregation stage)

## Definition

> **Note:** The following page refers to the aggregation stage
:pipeline:`$unset`. For the update operator :update:`$unset`, see
:update:`$unset`.

## Syntax

The :pipeline:`$unset` stage has the following syntax:

- To remove a single field, the :pipeline:`$unset` takes a string that
specifies the field to remove:

```javascript
  { $unset: "<field>" }
```

- To remove multiple fields, the :pipeline:`$unset` takes an array of
fields to remove.

```javascript
 { $unset: [ "<field1>", "<field2>", ... ] }
```

## Considerations

### `$unset` and `$project`

The :pipeline:`$unset` is an alias for the :pipeline:`$project` stage that removes/excludes fields:

```javascript
{ $project: { "<field1>": 0, "<field2>": 0, ... } }
```

### Embedded Fields

To remove/exclude a field or fields within an embedded document, you can use the `dot notation`, as in:

```javascript
{ $unset: "<field.nestedfield>" }
```

or

```javascript
{ $unset: [ "<field1.nestedfield>", ...] }
```

## Examples
