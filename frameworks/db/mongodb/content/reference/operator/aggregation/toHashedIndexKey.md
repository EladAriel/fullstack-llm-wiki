---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/toHashedIndexKey.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=======================================

# $toHashedIndexKey (expression operator)

## Definition

## Syntax

`$toHashedIndexKey` has the following syntax:

```javascript
{ $toHashedIndexKey: <key or string to hash> }
```

## Example

You can use `$toHashedIndexKey` to compute the hashed value of a string in an aggregation pipeline. This example computes the hashed value of the string `"string to hash"`:

```javascript
db.aggregate(
   [ 
      { $documents: [ { val: "string to hash" } ] },
      { $addFields: { hashedVal: { $toHashedIndexKey: "$val" } } }
   ]
 )
```

Example output:

```javascript
[ { val: 'string to hash', hashedVal: Long("763543691661428748") } ]
```

## Learn More

For general-purpose hashing in an aggregation pipeline, see :expression:`$hash` and :expression:`$hexHash`. These operators differ from `$toHashedIndexKey` as follows:

- :expression:`$hash` and :expression:`$hexHash` are general-purpose
hashing expressions. The expressions return `null` when the input is `null` or missing.

- `$toHashedIndexKey` applies hashed index semantics. Unlike
`$hash` and `$hexHash`, it hashes `null` and missing values to a `Long` numeric value rather than returning `null`.

To learn more, see:

- :expression:`$hash`
- :expression:`$hexHash`
- :method:`convertShardKeyToHashed()`
