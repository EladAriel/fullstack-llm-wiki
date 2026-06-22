---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/rs.add.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=========================

# rs.add() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-onprem-only.rst

## IP Binding

.. include:: /includes/fact-default-bind-ip.rst

.. include:: /includes/important-hostnames.rst

## Behavior

:method:`rs.add()` can, in some cases, trigger an election for primary which will disconnect the shell (such as adding a new member with a higher priority than the current primary). In such cases, :binary:`~bin.mongosh` may display an error even if the operation succeeds.

> **Warning:** .. include:: /includes/tip-repl-set-add-members.rst

## Example

### Add a Secondary to a New Replica Set

To add a new secondary member with default vote and priority settings to a new replica set, you can call the :method:`rs.add()` method with:

- Member Configuration Document
```javascript
  rs.add( { host: "mongodbd4.example.net:27017" } )
```

- Host name
```javascript
  rs.add( "mongodbd4.example.net:27017" )
```

### Add a Secondary to an Existing Replica Set

Add a new secondary member with default vote and priority settings to an existing replica set:

```javascript
  rs.add( { host: "mongodbd4.example.net:27017" } )
```

> **Warning:** .. include:: /includes/tip-repl-set-add-members.rst

### Add a Priority 0 Member to a Replica Set

The following operation adds a :binary:`~bin.mongod` instance, running on the host `mongodb4.example.net` and accessible on the default port `27017`, as a `priority 0 <replica-set-secondary-only-members>` secondary member:

```javascript
rs.add( { host: "mongodbd4.example.net:27017", priority: 0 } )
```

You must specify the :rsconf:`members[n].host` field in the member configuration document.

See the :rsconf:`members` for the available replica set member configuration settings.

### Add an Arbiter to a Replica Set

The following operation adds a :binary:`~bin.mongod` instance, running on the host `mongodb3.example.net` and accessible on the default port `27017` as an arbiter:

- Member Configuration Document
```javascript
  rs.add( { host: "mongodb3.example.net:27017", arbiterOnly: true } )
```

- Host name
```javascript
  rs.add("mongodb3.example.net:27017", true)
```

See also:

- `/tutorial/expand-replica-set`
- `/tutorial/add-replica-set-arbiter`
- `/tutorial/replace-replica-set-member`
- `/tutorial/remove-replica-set-member`
