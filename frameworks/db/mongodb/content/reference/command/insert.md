---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/insert.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=========================

# insert (database command)

## Definition

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
      insert: <collection>,
      documents: [ <document>, <document>, <document>, ... ],
      ordered: <boolean>,
      maxTimeMS: <integer>,
      writeConcern: { <write concern> },
      bypassDocumentValidation: <boolean>,
      comment: <any>
   }
)
```

## Command Fields

The command takes the following fields:

## Behavior

### Size Limit

The total size of all `documents` array elements must not exceed the :limit:`maximum BSON document size <BSON Document Size>`.

The total number of documents in the `documents` array must not exceed the :limit:`maximum bulk size <Write Command Batch Limit Size>`.

### Schema Validation

.. include:: /includes/extracts/bypassDocumentValidation-insert.rst

### Transactions

.. include:: /includes/extracts/transactions-supported-operation.rst

.. include:: /includes/extracts/transactions-usage.rst

Collection Creation in Transactions ````````````````````````````````````

.. include:: /includes/extracts/transactions-insert-implicit-collection-creation.rst

Write Concerns and Transactions ````````````````````````````````

.. include:: /includes/extracts/transactions-operations-write-concern.rst

### Insert Inaccuracies

.. include:: /includes/fact-insert-inaccuracies.rst

## Examples

### Insert a Single Document

Insert a document into the `users` collection:

```javascript
db.runCommand(
   {
      insert: "users",
      documents: [ { _id: 1, user: "abc123", status: "A" } ]
   }
)
```

The operation returns the following document:

```javascript
{ "ok" : 1, "n" : 1 }
```

### Bulk Insert

Insert three documents into the `users` collection:

```javascript
db.runCommand(
   {
      insert: "users",
      documents: [
         { _id: 2, user: "ijk123", status: "A" },
         { _id: 3, user: "xyz123", status: "P" },
         { _id: 4, user: "mop123", status: "P" }
      ],
      ordered: false,
      writeConcern: { w: "majority", wtimeout: 5000 }
   }
)
```

The operation returns the following document:

```javascript
{ "ok" : 1, "n" : 3 }
```

### Using Insert with `bypassDocumentValidation`

If `schema validation <schema-validation-overview>` `validationActions` are set to `error`, the insert command returns an error for documents that fail validation. To insert documents that violate validation rules, set `bypassDocumentValidation: true`.

Create the `user` collection with a validation rule on the `status` fields.

The validation rule validates that the status must be "Unknown" or "Incomplete":

```javascript
db.createCollection("users", { 
   validator:
      { 
         status: {
            $in: [ "Unknown", "Incomplete" ]
         }
      }
})
```

Insert a document that violates the validation rule:

```javascript
db.runCommand({
      insert: "users",
      documents: [ {user: "123", status: "Active" } ]
})
```

The insert returns a write error message:

```javascript
{
   n: 0,
   writeErrors: [
      {
         index: 0,
         code: 121,
         errInfo: {
            failingDocumentId: ObjectId('6197a7f2d84e85d1cc90d270'),
            details: {
               operatorName: '$in',
               specifiedAs: { status: { '$in': [Array] } },
               reason: 'no matching value found in array',
               consideredValue: 'Active'
            }
         },
         errmsg: 'Document failed validation'
      }
   ],
   ok: 1
}
```

Set `bypassDocumentValidation: true` and rerun the insert:

```javascript
db.runCommand({
   insert: "users",
   documents: [ {user: "123", status: "Active" } ], 
   bypassDocumentValidation: true
})
```

The operation succeeds.

To check for documents that violate schema validation rules, use the :dbcommand:`validate` command.

## Output

The returned document contains a subset of the following fields:

The following shows an example output for a successful single-document insert:

```javascript
{ ok: 1, n: 1 }
```

The following shows an example output when one document inserts successfully and a second document fails:

```javascript
{
   "ok" : 1,
   "n" : 1,
   "writeErrors" : [
      {
         "index" : 1,
         "code" : 11000,
         "errmsg" : "insertDocument :: caused by :: 11000 E11000 duplicate key error index: test.users.$_id_  dup key: { : 1.0 }"
      }
   ]
}
```
