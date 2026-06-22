---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/cursor.forEach.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=================================

# cursor.forEach() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The method has the following syntax:

```javascript
db.collection.find().forEach( <function> )
```

## Method Fields

The method accepts the following field:

## Examples

Create the `users` collection:

```none
db.users.insertMany( [
   { name: "John" },
   { name: "Jane" }
] )
```

The following example uses `forEach()` with the :method:`~db.collection.find()` method to print the user names that are read from the `users` collection. `myDoc` stores the current document.

```none
db.users.find().forEach( function( myDoc ) {
   print( "User name: " + myDoc.name )
} )
```

Example output:

```none
User name: John
User name: Jane
```

Starting in :binary:`~bin.mongosh` 2.1.0, you can also use `for-of` loops. The following example returns the same results as the previous example:

```none
for ( const myDoc of db.users.find() ) {
   print( "User name: " + myDoc.name )
}
```

## Learn More

For a method that has similar functionality, see :method:`cursor.map()`.
