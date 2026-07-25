---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/ObjectId.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

===========================

# ObjectId() (mongosh method)

## Description

## Compatibility

.. include:: /includes/fact-compatibility.rst

## Syntax

:method:`ObjectId()` can accept one of the following inputs:

## Methods

:method:`ObjectId()` has the following methods:

## Behavior

.. include:: /includes/reference/fact-objectid-and-mongosh.rst

## Examples

### Generate a New ObjectId

To generate a new ObjectId, use :method:`ObjectId()` with no argument:

```javascript
newObjectId = ObjectId()
```

In this example, the value of `newObjectId` is:

```javascript
ObjectId("507f1f77bcf86cd799439011")
```

### Return a Hexadecimal String

To return the ObjectId as a hexadecimal string, use the `toString()` method.

```javascript
ObjectId("507f191e810c19729de860ea").toString()
```

The method returns:

```none
507f191e810c19729de860ea
```

### Specify a Date

You can use a custom `document-bson-type-date` to specify an ObjectId.

### Specify an Integer String

If you want to adjust the ObjectId timestamp, use an integer to generate a new ObjectId.

```javascript
newObjectId = ObjectId(32)
```

The ObjectId value resembles:

```javascript
ObjectId("00000020f51bb4362eee2a4d")
```

The example ObjectId consists of:

- A four byte time stamp, `00000020`
- A five byte random element, `f51bb4362e`
- A three byte counter, `ee2a4d`
The first four bytes of the ObjectId are the number of seconds since the :wikipedia:`Unix epoch`. In this example, the ObjectId timestamp is `00000020` which is `32` in hexadecimal.

### Specify a Hexadecimal String

If you want to use a hexadecimal string to specify an ObjectId, pass a unique, 24 character hexadecimal value when you call :method:`ObjectId()`:

```javascript
newObjectId = ObjectId("507f191e810c19729de860ea")
```

> **Seealso:** `ObjectId BSON Type <objectid>`
