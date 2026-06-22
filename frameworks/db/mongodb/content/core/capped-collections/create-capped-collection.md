---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/capped-collections/create-capped-collection.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========================

# Create a Capped Collection

To create a `capped collection <manual-capped-collection>`, specify the `capped` option to either the :method:`db.createCollection()` method or the :dbcommand:`create` command.

You must create capped collections explicitly. You cannot create a capped collection implicitly by inserting data into a non-existing collection.

When you create a capped collection you must specify the maximum size of the collection. MongoDB pre-allocates the specified storage for the collection. The size of the capped collection includes a small amount of space for internal overhead.

You can optionally specify a maximum number of documents for the collection. MongoDB removes older documents if the collection reaches the maximum size limit before it reaches the maximum document count.

## About this Task

.. include:: /includes/capped-collections/use-ttl-index.rst

## Steps

The following examples show you how to:

- `create-capped-collection-max-size`
- `create-capped-collection-max-docs`
### Create a Capped Collection with a Maximum Size

Create a capped collection called `log` that has a maximum size of 100,000 bytes:

```javascript
db.createCollection( "log", { capped: true, size: 100000 } )
```

> **Note:** The value that you provide for the `size` field
must be greater than `0` and less than or equal to
`1024^5` (1 {+pb+}). MongoDB rounds the `size` of all capped
collections up to the nearest integer multiple of 256, in bytes.

### Create a Capped Collection with a Maximum Number of Documents

Create a capped collection called `log2` that has a maximum size of 5,242,880 bytes and can store a maximum of 5,000 documents:

```javascript
db.createCollection(
   "log2",
   { 
      capped: true,
      size: 5242880,
      max: 5000
   }
)
```

> **Important:** The `size` field is always required, even when you specify the
`max` number of documents.

## Learn More

- :method:`db.createCollection()`
- `capped-collections-query`
- `capped-collections-check`
