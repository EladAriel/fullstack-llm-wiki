---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.validate.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=========================================

# db.collection.validate() (mongosh method)

.. include:: includes/wayfinding/mongosh-method-validate.rst

## Description

.. versionchanged:: 6.2

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The :method:`db.collection.validate()` method has the following syntax:

```javascript
db.collection.validate( { 
   full: <boolean>,  // Optional
   repair: <boolean>,  // Optional, added in MongoDB 5.0
   checkBSONConformance: <boolean>  // Optional, added in MongoDB 6.2
} )
```

### Parameters

The :method:`db.collection.validate()` method can take the following optional document parameter with the fields:

## Behavior

### Performance

The :method:`db.collection.validate()` method is potentially resource intensive and may impact the performance of your MongoDB instance, particularly on larger data sets.

The :method:`db.collection.validate()` method obtains an exclusive lock on the collection. This will block all reads and writes on the collection until the operation finishes. When run on a secondary, the operation can block all other operations on that secondary until it finishes.

> **Warning:** Validation has exclusive lock requirements that affect performance
on primaries and on secondaries that are servicing reads. Consider
only running :method:`db.collection.validate()` on nodes that are
not servicing reads or writes.
To minimize impact on the primary, the majority of the data-bearing
(non-arbiter), voting members in the cluster must be available and
must not have significant replication lag.
To minimize the impact of the validation operation on client
applications, run :method:`db.collection.validate()` on a secondary
node that is not servicing read requests. You can convert the
current primary node to a secondary node, by running the
:method:`rs.stepDown()` method.
To completely isolate the :method:`db.collection.validate()`
operation from client traffic, choose one of the following options:
- Isolate a replica set member by following the :ref:`rolling
  maintenance procedure <perform-maint-on-replica-set>` to
  temporarily remove it from the cluster.
- :ref:`Convert a secondary node
  <configure-hidden-replica-set-member>` to a replica set
  `hidden member <replica-set-hidden-members>` and perform the
  validation on the hidden node.

### Data Throughput Metrics

.. include:: /includes/extracts/4.4-validate-data-throughput.rst

### Collection Validation Improvements

.. include:: /includes/validate-improvements-introduction.rst

## Examples

- To validate a collection `myCollection` using the default validation
setting (specifically, `full: false <method-validate-full>`):

```javascript
  db.myCollection.validate()

  db.myCollection.validate({ })

  db.myCollection.validate( { full: false } )
```

- To perform a full validation of collection `myCollection`, specify
`full: true <method-validate-full>`:

```javascript
  db.myCollection.validate( { full: true } )
```

- To repair collection `myCollection`, specify
`repair: true <method-validate-repair>`:

```javascript
  db.myCollection.validate( { repair: true } )
```

- To perform additional BSON conformance checks in `myCollection`,
specify `checkBSONConformance: true <method-validate-checkBSONConformance>`:

```javascript
 db.myCollection.validate( { checkBSONConformance: true } )
```

For details of the output, see `validate-output`.
