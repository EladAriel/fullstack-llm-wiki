---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/hexHash.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=================================

# $hexHash (aggregation expression)

## Definition

.. versionadded:: 8.3

## Syntax

`$hexHash` has the following syntax:

```javascript
{
   $hexHash: {
      input: <expression>,
      algorithm: <string>
   }
}
```

## Behavior

`$hexHash` returns an uppercase hexadecimal string. The length of the output depends on the algorithm:

If `input` resolves to `null` or undefined, or refers to a missing field, `$hexHash` returns `null`.

If `input` resolves to a type other than a UTF-8 string or :bsontype:`BinData <Binary>`, `$hexHash` returns an error.

If `algorithm` is not one of the accepted values, `$hexHash` returns an error.

> **Important:** MD5 is not a cryptographically secure algorithm and is not
suitable for security-sensitive applications. If you are
hashing sensitive data, use `"sha256"` instead.
MD5 is also disabled in FIPS mode. If your deployment runs
with FIPS mode enabled, use `"sha256"` or `"xxh64"`
instead.

## Examples

The following examples use a collection named `files` with this document:

### Hash a Field Value

The following example computes the SHA-256 hexadecimal hash of the `filename` field:

The `hexHash` field contains the SHA-256 hash as a 64-character uppercase hexadecimal string. To use a different algorithm, change the `algorithm` value. For example, `"xxh64"` produces a 16-character string.

### Null or Missing Input

If `input` is `null`, or `input` refers to a missing field, `$hexHash` returns `null`:

## Learn More

- :expression:`$hash`
- :expression:`$toHashedIndexKey`
- :expression:`$convert`
