---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/indexes/index-types/index-hashed.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============

# Hashed Indexes

Hashed indexes collect and store hashes of the values of the indexed field.

Hashed indexes support `sharding <sharding-background>` using hashed shard keys. `Hashed based sharding <sharding-hashed-sharding>` uses a hashed index of a field as the shard key to partition data across your sharded cluster.

## Use Cases

.. include:: /includes/indexes/hashed-sharding-use-cases.rst

## Behavior

### Floating-Point Numbers

Hashed indexes truncate floating-point numbers to 64-bit integers before hashing. For example, a hashed index uses the same hash to store the values `2.3`, `2.2`, and `2.9`. This is a **collision**, where multiple values are assigned to a single hash key. Collisions may negatively impact query performance.

To prevent collisions, do not use a hashed index for floating-point numbers that cannot be reliably converted to 64-bit integers and then back to floating point.

Hashed indexes do not support floating-point numbers larger than 2\ :sup:`53`.

### Limitations

Hashed indexes have limitations for array fields and the unique property.

Array Fields ````````````

The hashing function does not support `multikey indexes <index-type-multikey>`:

- You cannot create a hashed index on a field that contains an array
or insert an array into a hashed indexed field.

- If any field in a compound index is an array, no field in that
index can use a hashed index. This includes non-array fields.

- You cannot use hashed indexes in a compound index that becomes a
multikey index.

Covered Queries ```````````````

.. include:: /includes/fact-hashed-index-covered-query.rst

Unique Constraint `````````````````

You cannot specify a `unique constraint <index-type-unique>` on a hashed index. Instead, you can create an additional non-hashed index with the unique constraint. MongoDB can use that non-hashed index to enforce uniqueness on the chosen field.

## Get Started

To create a hashed index, see `hashed-index-create`.

## Details

This section describes technical details for hashed indexes.

### Hashing Function

> **Important:** When MongoDB uses a hashed index to resolve a query, it uses a
hashing function to automatically compute the hash values.
Applications do **not** need to compute hashes.

To see what the hashed value would be for a key, use the :method:`convertShardKeyToHashed()` method. This method uses the same hashing function as the hashed index.

### Embedded Documents

The hashing function collapses embedded documents and computes the hash for the entire value.

## Learn More

- `sharding-background`
- `sharding-hashed-sharding`
- `hashed-versus-ranged-sharding`
## Contents

- Create </core/indexes/index-types/index-hashed/create>
