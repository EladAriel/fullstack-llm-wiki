---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/hash.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

==============================

# $hash (aggregation expression)

## Definition

.. versionadded:: 8.3

## Syntax

`$hash` has the following syntax:

```javascript
{
   $hash: {
      input: <expression>,
      algorithm: <string>
   }
}
```

## Behavior

If `input` resolves to `null` or undefined, or refers to a missing field, `$hash` returns `null`.

If `input` resolves to a type other than a UTF-8 string or :bsontype:`BinData <Binary>`, `$hash` returns an error.

If `algorithm` is not one of the accepted values, `$hash` returns an error.

> **Important:** MD5 is not a cryptographically secure algorithm and is not
suitable for security-sensitive applications. If you are
hashing sensitive data, use `"sha256"` instead.
MD5 is also disabled in FIPS mode. If your deployment runs
with FIPS mode enabled, use `"sha256"` or `"xxh64"`
instead.

## Examples

The following examples use a collection named `files` with these documents:

### Hash a Field Value

The following example computes the SHA-256 hash of the `filename` field for each document:

### Hash a Literal String

The following example hashes a literal string value:

### Hash BinData

The following example computes the SHA-256 hash of a binary data field:

### Null or Missing Input

If `input` is `null` or refers to a missing field, `$hash` returns `null`:

## Learn More

- :expression:`$hexHash`
- :expression:`$toHashedIndexKey`
- :expression:`$convert`
