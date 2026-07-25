---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/subtype.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

==============================

# $subtype (expression operator)

## Definition

.. versionadded:: 8.3

## Syntax

:expression:`$subtype` has the following syntax:

```javascript
{ $subtype: <expression> }
```

The `<expression>` can be any valid `expression <aggregation-expressions>` that contains a subtype.

> **Note:** In MongoDB 8.3, the only expression that contains a subtype is a
:bsontype:`BinData <data_binary>` expression.

## Behavior

### Null or Missing Values

`$subtype` operations on null or missing values return `null`.

### Unaccepted Expressions

`$subtype` operations on expressions that do not have a subtype return an error.

### BinData Output

`$subtype` operations on  :bsontype:`BinData <data_binary>` expressions return the binary subtype of the expression. For more information, see `binData-subtype`.

## Example

Use the :method:`BinData()` constructor to create a `bdata` variable.

```javascript
var bdata = BinData(0, "gf1UcxdHTJ2HQ/EGQrO7mQ==")
```

The following operation outputs the subtype of the bdata object:

```javascript
{ $subtype: bdata }
```

The expression returns `0`.

## Learn More

- `server-binData-method`
- `Binary.createFromBase64`
