---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.getCollectionInfos.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

========================================

# db.getCollectionInfos() (mongosh method)

## Definition

## Syntax

The `db.getCollectionInfos()` method has the following parameters:

### Options

You can specify the following options in the `options` document of a `db.getCollectionInfos()` command:

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Required Access

.. include:: /includes/extracts/listCollections-auth-required-access.rst

### `show collections`

.. include:: /includes/extracts/listCollections-auth-show-collections.rst

## Behavior

### Client Disconnection

.. include:: /includes/extracts/4.2-changes-disconnect.rst

### Replica Set Member State Restriction

.. include:: /includes/extracts/4.4-changes-repl-state-restrictions-operation.rst

## Examples

### Return Information for All Collections in a Database

The following returns information for all collections in the `example` database:

### Return Only Collection Names

To return only the names of collections in the current database, specify the `nameOnly: true` option. For example:

### Return Information for a Specific Collection

To request collection information for a specific collection, specify the collection name in the filter document. The following example returns an array with a single document that details the collection information for the `employees` collection in the `example` database.

### Return Information for Read-Only Collections

You can specify a filter on any of the fields returned by `db.getCollectionInfos()`.

For example, the following command returns information for all collections in the `example` database where `info.readOnly` is `true`:
