---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/indexes/wildcard-restrictions-compound.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

`Compound wildcard indexes <wildcard-index-compound>` have the following restrictions:

- A compound wildcard index can only have one wildcard term.
For example, you cannot specify the following index:

```javascript
  { userID: 1, "object1.$**": 1, "object2.$**": 1 }
```

- The non-wildcard terms in a compound wildcard index must be single key
terms. `Multikey <index-type-multikey>` index terms are not permitted.

- You can only specify the `wildcardProjection` option when the
wildcard field is `$**`. You cannot use `wildcardProjection` when you specify a field path for the wildcard index term.

This is a valid definition:

```javascript
  {
     key: { "$**": 1 },
     name: "index_all_with_projection",
     wildcardProjection: {
        "someFields.name": 1,
        "otherFields.values": 1
     }
  }

This is an invalid definition: 

.. code-block:: javascript
  :copyable: false

  {
     key: { "someFields.$**": 1 },
     name: "invalid_index",
     wildcardProjection: {
        "someFields.name": 1,
        "otherFields.values": 1
     }
  }
```

- The `_id field is omitted by default. If you need the id`
field:

- Specify a wildcard index as `$**`.
- Include the `_id` field in the `wildcardProjection` with ``_id:
1``.

```javascript
  db.studentGrades.createIndex(
     {
        "$**": 1,
     },
     { 
        wildcardProjection: {
           _id: 1,
           exams: 1, 
           extraCredit: 1
        }
     }
  )
```

- You cannot include the same field in the wildcard fields and the
regular fields. To exclude fields from the wildcard pattern, use a `wildcardProjection` with exclusion rules.

```javascript
  db.studentGrades.createIndex(
     {
        exams: 1,
        "$**": 1,
        homeworks: 1
     },
     { 
        wildcardProjection: {
           exams: 0, 
           homeworks: 0
        }
     }
  )
```

### wildcardProjection Validation Rules

Starting in MongoDB 8.3 (and 8.2.4, 8.0.18, 7.0.29), stricter validation rules apply to `wildcardProjection` in compound wildcard indexes to prevent invalid configurations.

Existing indexes that do not meet the new validation requirements continue to function, but you cannot create new indexes that don't meet these requirements.

When using `wildcardProjection` with compound wildcard indexes, the following rules apply:
