---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/cursor.comment.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=================================

# cursor.comment() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Behavior

:method:`~cursor.comment()` associates a comment string with the find operation. This can make it easier to track a particular query in the following diagnostic outputs:

- The `system.profile <<database>.system.profile>`
- The `QUERY` `log <log-messages-ref>` component
- :method:`db.currentOp()`
See `configure log verbosity <log-messages-configure-verbosity>` for the :binary:`~bin.mongod` log, the `Database Profiler tutorial <database-profiler>`, or the :method:`db.currentOp()` command.

## Example

The following operation attaches a comment to a query on the `restaurants` collection:

```javascript
db.restaurants.find(
   { "borough" : "Manhattan" }
).comment( "Find all Manhattan restaurants" )
```

## Output Examples

### `system.profile <<database>.system.profile>`

The following is an excerpt from the `system.profile <<database>.system.profile>`:

```javascript
{
   "op" : "query",
   "ns" : "guidebook.restaurant",
   "query" : {
      "find" : "restaurant",
      "filter" : {
         "borough" : "Manhattan"
      },
      "comment" : "Find all Manhattan restaurants"
   },
   ...
}
```

### :binary:`~bin.mongod` `log <log-messages-ref>`

The following is an excerpt from the :binary:`~bin.mongod` log. It has been formatted for readability.

> **Important:** The verbosity level for `QUERY` must be greater than `0`.
See `log-messages-configure-verbosity`

```javascript
2015-11-23T13:09:16.202-05:00 I COMMAND  [conn1]
   command guidebook.restaurant command: find {
      find: "restaurant",
      filter: { "borough" : "Manhattan" },
      comment: "Find all Manhattan restaurants"
   }
   ...
```

### :method:`db.currentOp()`

Suppose the following operation is currently running on a :binary:`~bin.mongod` instance:

```javascript
db.restaurants.find(
   { "borough" : "Manhattan" }
).comment("Find all Manhattan restaurants")
```

Running the :method:`db.currentOp()` command returns the following:

```javascript
{
   "inprog" : [
      {
         "host" : "198.51.100.1:27017",
         "desc" : "conn3",
         "connectionId" : 3,
         ...

         "op" : "query",
         "ns" : "test.$cmd",
         "command" : {
            "find" : "restaurants",
            "filter" : {
               "borough" : "Manhattan"
            },
            "comment" : "Find all Manhattan restaurants",
            "$db" : "test"
         },
         "numYields" : 0,
         ...
      }
   ],
   "ok" : 1
}
```
