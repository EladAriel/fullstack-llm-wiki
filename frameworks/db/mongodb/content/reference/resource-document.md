---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/resource-document.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=============================================

# Resource Document on Self-Managed Deployments

The resource document specifies the resources upon which a privilege permits `actions`.

## Database and/or Collection Resource

To specify databases and/or collections, use the following syntax:

```javascript
{ db: <database>, collection: <collection> }
```

### Specify a Collection of a Database as Resource

If the resource document specifies both the `db` and `collection` fields as non-empty strings, the resource is the specified collection in the specified database. For example, the following document specifies a resource of the `inventory` collection in the `products` database:

```javascript
{ db: "products", collection: "inventory" }
```

.. include:: /includes/resource-document-facts.rst

### Specify a Database as Resource

If only the `collection` field is an empty string (`""`), the resource is the specified database, excluding the `system collections </reference/system-collections>`. For example, the following resource document specifies the resource of the `test` database, excluding the system collections:

```javascript
{ db: "test", collection: "" }
```

.. include:: /includes/resource-document-facts.rst

> **Note:** collections are excluded, unless you name them explicitly, as in the
following:
.. code-block:: javascript
   { db: "test", collection: "system.js" }
System collections include but are not limited to the following:
- `<database>.system.profile`
- `<database>.system.js`
- `/reference/system-users-collection` in the `admin` database
- `/reference/system-roles-collection` in the `admin` database

### Specify Collections Across Databases as Resource

If only the `db` field is an empty string (`""`), the resource is all collections with the specified name across all databases. For example, the following document specifies the resource of all the `accounts` collections across all the databases:

```javascript
{ db: "", collection: "accounts" }
```

.. include:: /includes/resource-document-facts.rst

### Specify All Non-System Collections in All Databases

If both the `db` and `collection` fields are empty strings (`""`), the resource is all collections, excluding the `system collections </reference/system-collections>`, in all the databases:

```javascript
{ db: "", collection: "" }
```

.. include:: /includes/resource-document-facts.rst

## Cluster Resource

To specify the cluster as the resource, use the following syntax:

```javascript
{ cluster : true }
```

Use the `cluster` resource for actions that affect the state of the system rather than act on specific set of databases or collections. Examples of such actions are `shutdown`, `replSetReconfig`, and `addShard`. For example, the following document grants the action `shutdown` on the `cluster`.

```javascript
{ resource: { cluster : true }, actions: [ "shutdown" ] }
```

.. include:: /includes/resource-document-facts.rst

## `anyResource`

The internal resource `anyResource` gives access to every resource in the system and is intended for internal use. **Do not** use this resource, other than in exceptional circumstances. The syntax for this resource is `{ anyResource: true }`.
