---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/iterate-a-cursor.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================

# Iterate a Cursor in `mongosh`

This tutorial demonstrates how to access documents in a `cursor`.

## About This Task

To access documents in a cursor, you can manually iterate the cursor or use the :method:`~cursor.toArray()` method.

This tutorial overviews how to:

- Save a cursor as a variable using the `let` keyword.
- Use the :method:`next() <cursor.next()>`, :method:`hasNext()
<cursor.hasNext()>`, and :method:`forEach() <cursor.forEach()>` methods to access documents in a cursor.

- Return and access the cursor documents as an array with the
:method:`~cursor.toArray()` method.

## Before You Begin

- Install `mongosh <mdb-shell-install>`.
- Connect to a `deployment <mdb-shell-connect>`.
### Insert Documents Into a New Collection

Use :binary:`~bin.mongosh` to insert documents into a new collection using the default `test` database:

```javascript
db.users.insertMany( [ 
   { _id: 0, type: "admin", email: "admin@example.com", name: "Admin User" }, 
   { _id: 1, type: "user", email: "user1@example.com", name: "Test User 1" }, 
   { _id: 2, type: "user", email: "user2@example.com", name: "Test User 2" }
] )
```

## Examples

### Save a Cursor with `let`

In :binary:`~bin.mongosh`, the cursor does not automatically iterate when you assign it to a variable using the `let` keyword.

```javascript
let myCursor = db.users.find( { type: "user" } )
```

You can call the cursor variable in the shell to iterate up to 20 times [#set-shell-batch-size]_ and print the matching documents.

If the returned cursor is not assigned to a variable using the `let` keyword, then the cursor is automatically iterated up to the batch size [#set-shell-batch-size]_, printing the first batch of results.

### Access Documents in a Cursor with :method:`next() <cursor.next()>`

You can also use the cursor method :method:`next() <cursor.next()>` to access the documents. :method:`next() <cursor.next()>` returns the document the cursor currently points and then moves the cursor forward to the next document.

### Access Documents in a Cursor with :method:`hasNext() <cursor.hasNext()>`

The cursor method :method:`hasNext() <cursor.hasNext()>` returns `true` or `false` to indicate if there are more documents to be returned from the cursor.

You can use the :method:`hasNext() <cursor.hasNext()>` and :method:`next() <cursor.next()>` methods to print all remaining documents from the cursor using the `printjson()` helper.

### Access Documents in a Cursor with :method:`forEach() <cursor.forEach()>`

Similarly, you can use the cursor method :method:`forEach() <cursor.forEach()>` to apply a helper, such as `printjson()`, to each document in the cursor.

Starting in :binary:`~bin.mongosh` 2.1.0, you can also use `for-of` loops to iterate the cursor. The following example returns the same results as the previous example.

See `JavaScript cursor methods <js-query-cursor-methods>` and your :driver:`driver </>` documentation for more information on cursor methods.

### Access Documents in a Cursor with :method:`toArray() <cursor.toArray()>`

In :binary:`~bin.mongosh`, use the :method:`~cursor.toArray()` method to iterate the cursor and return the documents in an array.

You can access the resulting document array as a traditional array.

The :method:`~cursor.toArray()` method loads all documents returned by the cursor into RAM and exhausts the cursor.

Some :driver:`Drivers </>` provide access to the documents by using an index on the cursor (i.e. `cursor[index]`). This is a shortcut for first calling the :method:`~cursor.toArray()` method and then using an index on the resulting array.

.. include:: /includes/footnote-set-shell-batch-size.rst
