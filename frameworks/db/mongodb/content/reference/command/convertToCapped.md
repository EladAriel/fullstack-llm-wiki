---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/convertToCapped.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================================

# convertToCapped (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

```javascript
db.runCommand(
   { 
     convertToCapped: <collection>,
     size: <capped size>,
     writeConcern: <document>,
     comment: <any>  
   }
)
```

### Command Fields

The command takes the following fields:

:dbcommand:`convertToCapped` takes an existing collection (`<collection>`) and transforms it into a capped collection with a maximum size in bytes, specified by the `size` argument (`<capped size>`).

During the conversion process, the :dbcommand:`convertToCapped` command exhibits the following behavior:

- MongoDB traverses the documents in the original collection in
`natural order` and loads the documents into a new capped collection.

- If the `capped size` specified for the capped collection is
smaller than the size of the original uncapped collection, then MongoDB will overwrite documents in the capped collection based on insertion order, or first in, first out order.

- Internally, to convert the collection, MongoDB uses the following
procedure

- :dbcommand:`cloneCollectionAsCapped` command creates the capped
collection and imports the data.

- MongoDB drops the original collection.
- :dbcommand:`renameCollection` renames the new capped collection
to the name of the original collection.

- .. include:: /includes/fact-database-lock.rst
> **Warning:** .. include:: /includes/fact-convertToCapped-indexes.rst

## Example

### Convert a Collection

The following example uses :method:`db.collection.insertOne()` to create an `events` collection, and :method:`db.collection.stats()` to obtain information about the collection:

```javascript
db.events.insertOne( { click: 'button-1', time: new Date() } )
db.events.stats()
```

MongoDB will return the following:

```javascript
{
        "ns" : "test.events",
        ...
        "capped" : false,
        ...
}
```

To convert the `events` collection into a capped collection and view the updated collection information, run the following commands:

```javascript
db.runCommand( { convertToCapped: 'events', size: 8192 } )
db.events.stats()
```

MongoDB will return the following:

```javascript
{
     "ns" : "test.events",
     ...
     "capped" : true,
     "max" : Long("9223372036854775807"),
     "maxSize" : 8192,
     ...
}
```

.. include:: /includes/fact-convertToCapped-indexes.rst

> **Seealso:** :dbcommand:`create`
