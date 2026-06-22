---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/databases-and-collections.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

====================================

# Databases and Collections in MongoDB

MongoDB stores data records as `documents <document>` (`BSON documents <bson-document-format>`) in `collections <collection>`. A `database <database>` holds one or more collections.

You can manage :atlas:`databases </atlas-ui/databases>` and :atlas:`collections </atlas-ui/collections>` using the Atlas UI, :binary:`~bin.mongosh`, or |compass|. This page covers Atlas UI procedures. For self-managed deployments, use :binary:`~bin.mongosh` or |compass|.

Select your client:

## Databases

### Create a Database

## Collections

MongoDB stores documents in collections. Collections are analogous to tables in relational databases.

.. include:: /images/crud-annotated-collection.rst

### Create a Collection

If a collection does not exist, MongoDB creates the collection when you first store data for that collection.

### Schema Validation

By default, documents in a collection do not share a schema. Fields and data types can vary across documents.

You can enforce `schema validation rules <schema-validation-overview>` during insert and update operations.

For {+atlas+} deployments, the `Performance Advisor <performance-advisor>` and the {+atlas+} UI detect common schema design issues and suggest modifications that follow MongoDB best practices. To learn more, see :atlas:`Schema Suggestions </performance-advisor/schema-suggestions/#schema-suggestions>`.

### Modifying Document Structure

To add, remove, or retype fields in a collection's documents, update the existing documents.

### Unique Identifiers

Collections are assigned an immutable :abbr:`UUID (Universally unique identifier)` that remains consistent across all replica set members and shards.

## Contents

- Views </core/views>
- On-Demand Materialized Views </core/materialized-views>
- Capped Collections </core/capped-collections>
- Clustered Collections </core/clustered-collections>
