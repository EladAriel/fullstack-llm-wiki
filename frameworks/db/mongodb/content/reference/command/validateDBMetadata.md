---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/validateDBMetadata.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=====================================

# validateDBMetadata (database command)

## Definition

.. versionadded:: 5.0

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

```javascript
db.runCommand( 
   { 
     validateDBMetadata: 1,
     apiParameters: {
       version: <string>,
       strict: <boolean>,
       deprecationErrors: <boolean>
      },
     db: <string>,
     collection: <string>,
   } 
)
```

## Command Fields

The command takes the following fields:

## Behavior

- Validate all collections in all databases, reporting
`APIStrictError <api-strict-resp>` and `APIVersionError <api-vers-resp>` error responses.

```javascript
  db.runCommand( { 
    validateDBMetadata: 1, 
    apiParameters: { 
      version: "1", 
      strict: true, 
      deprecationErrors: true 
    }, 
  })
```

- Validate all collections in `inventory`:
```javascript
  db.runCommand( { 
    validateDBMetadata: 1, 
    apiParameters: { 
      version: "1", 
      strict: true, 
      deprecationErrors: true 
    }, 
    db: "inventory",
  })
```

- Validate the `sales` collection in the `inventory` database:
```javascript
  db.runCommand( { 
    validateDBMetadata: 1, 
    apiParameters: { 
      version: "1", 
      strict: true, 
      deprecationErrors: true 
    }, 
    db: "inventory",
    collection: "sales",
  })
```

- Validate any and all `sales` collections across all databases:
```javascript
  db.runCommand( { 
    validateDBMetadata: 1, 
    apiParameters: { 
      version: "1", 
      strict: true, 
      deprecationErrors: true 
    }, 
    collection: "sales",
  })
```

> **Note:** Your user must have the :authaction:`validate` privilege action on
all collections you want to validate.

## Output

```javascript
{
   apiVersionErrors: [
     {
       ns: <string>,
       code: <int>,
       codeName: <string>,
       errmsg: <string>
     }
   ],
   ok: <int>,
   hasMoreErrors: <boolean>,
}
```

## Example

Use the sample Query API code to create a `sales` collection in :binary:`~bin.mongosh`:

```javascript
db.sales.insertMany([
    { "_id" : 1, "item" : "shoes", "price" : 10, "quantity" : 2, "date" : ISODate("2021-01-01T08:00:00Z") },
    { "_id" : 2, "item" : "hat", "price" : 20, "quantity" : 1, "date" : ISODate("2021-02-03T09:00:00Z") },
    { "_id" : 3, "item" : "gloves", "price" : 5, "quantity" : 5, "date" : ISODate("2021-02-03T09:05:00Z") },
    { "_id" : 4, "item" : "pants", "price" : 10, "quantity" : 10, "date" : ISODate("2021-02-15T08:00:00Z") },
    { "_id" : 5, "item" : "socks", "price" : 5, "quantity" : 10, "date" : ISODate("2021-02-15T09:05:00Z") },
    { "_id" : 6, "item" : "shirt", "price" : 5, "quantity" : 5, "date" : ISODate("2021-02-15T12:05:10Z") },
    { "_id" : 7, "item" : "belt", "price" : 5, "quantity" : 10, "date" : ISODate("2021-02-15T14:12:12Z") },
    { "_id" : 8, "item" : "blouse", "price" : 10, "quantity" : 5, "date" : ISODate("2021-03-16T20:20:13Z") }
])
```

Add a `text index <index-type-text>` on the `item` field.

```javascript
db.sales.createIndex( { item: "text" } )
```

Validate the `sales` collection for strict compliance with API version 1 and include `deprecationErrors` in the output.

```javascript
  db.runCommand( { 
    validateDBMetadata: 1, 
    apiParameters: { 
      version: "1", 
      strict: true, 
      deprecationErrors: true 
    }, 
    collection: "sales",
  })
```

:dbcommand:`validateDBMetadata` reports an `APIStrictError` on the `item_text` index.

```javascript
{
   apiVersionErrors: [
     {
       ns: 'test.sales',
       code: 323,
       codeName: 'APIStrictError',
       errmsg: 'The index with name item_text is not allowed in API version 1.'
     }
   ],
   ok: 1,
   hasMoreErrors: false,
}
```
