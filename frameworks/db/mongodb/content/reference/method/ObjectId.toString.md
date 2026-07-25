---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/ObjectId.toString.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

====================================

# ObjectId.toString() (mongosh method)

## Compatibility

.. include:: /includes/fact-compatibility.rst

## Example

The following example:

- Generates a new :method:`ObjectId()` and stores it in the
variable `myObjectId`.

- Creates a string representation of `myObjectId` using
the :method:`toString()<ObjectId.toString()>` method.

- Stores the string representation in the variable `myObjectIdString`.
Run the following commands in :binary:`mongosh`:

```javascript
myObjectId = ObjectId("507c7f79bcf86cd7994f6c0e")
myObjectIdString = myObjectId.toString()
```

The operation returns the following string:

```javascript
507c7f79bcf86cd7994f6c0e
```

To confirm the type of `myObjectIdString`, use the `typeof` JavaScript operator:

```javascript
typeof myObjectIdString
```

The operation returns the following:

```javascript
string
```
