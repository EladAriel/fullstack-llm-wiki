---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/schema-validation/view-existing-validation-rules.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

==============================

# View Existing Validation Rules

You can view a collection's validation rules to determine what restrictions are imposed on documents and how MongoDB handles invalid documents when they occur.

To view a collection's validation rules, use the :method:`db.getCollectionInfos()` method or :dbcommand:`listCollections` database command.

Both commands return the same information, but the output format differs between each command.

## Prerequisite

To run the examples on this page, create a `students` collection with validation rules. For more information, see `schema-validation-json`.

## Example: `db.getCollectionInfos()` Syntax

The following command uses :method:`db.getCollectionInfos()` to return the validation rules for the `students` collection:

```javascript
db.getCollectionInfos( { name: "students" } )[0].options.validator
```

The output resembles the following validation object:

```javascript
{
  '$jsonSchema': {
    bsonType: 'object',
    required: [ 'name', 'year', 'major', 'address' ],
    properties: {
      name: {
        bsonType: 'string',
        description: 'must be a string and is required'
      },
      year: {
        bsonType: 'int',
        minimum: 2017,
        maximum: 3017,
        description: 'must be an integer in [ 2017, 3017 ] and is required'
      },
      gpa: {
        bsonType: [ 'double' ],
        description: 'must be a double if the field exists'
      }
    }
  }
}
```

> **Note:** If `validationAction` and `validationLevel` are not explicitly
set, :method:`db.getCollectionInfos()` does not include those fields
in its output.

## Example: `listCollections` Syntax

The following command uses :dbcommand:`listCollections` to return the validation rules for the `students` collection:

```javascript
db.runCommand ( { listCollections: 1, filter: { name: "students" } } )
```

The output resembles the following object:

```javascript
{
  cursor: {
    id: Long("0"),
    ns: 'test.$cmd.listCollections',
    firstBatch: [
      {
        name: 'students',
        type: 'collection',
        options: {
          validator: {
            '$jsonSchema': {
              bsonType: 'object',
              required: [ 'name', 'year', 'major', 'address' ],
              properties: {
                name: {
                  bsonType: 'string',
                  description: 'must be a string and is required'
                },
                gpa: {
                  bsonType: [ 'double' ],
                  description: 'must be a double if the field exists'
                }
              }
            },
            validationAction: 'warn'
          }
        },
        info: {
          readOnly: false,
          uuid: UUID("bf560865-5879-4ec1-b389-f77a03abbc5a")
        },
        idIndex: { v: 2, key: { _id: 1 }, name: '_id_' }
      }
    ]
  },
  ok: 1
}
```

## Learn More

- `use-json-schema-query-conditions`
- `schema-validation-handle-invalid-docs`
