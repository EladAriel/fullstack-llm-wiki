---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/UUID.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=======================

# UUID() (mongosh method)

## Definition

Generates a BSON :abbr:`UUID (Universally unique identifier)` object.

:method:`~UUID()` has the following syntax:

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Example

### Convert Character String to UUID

Create a 36 character string you wish to convert to a UUID:

```javascript
var myuuid = '3b241101-e2bb-4255-8caf-4136c566a962'
```

The following command outputs the `myuuid` variable as a BSON UUID object:

```javascript
UUID(myuuid)
```

This command generates the following output:

```javascript
UUID("3b241101-e2bb-4255-8caf-4136c566a962")
```

### Generate Random UUID

You can run the :method:`~UUID()` method without specifying an argument to generate a random UUID:

```javascript
UUID()
```

This command outputs a random UUID in the following form:

```javascript
UUID("dee11d4e-63c6-4d90-983c-5c9f1e79e96c")
```
