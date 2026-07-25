---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-bindata-endian.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

The `endianness` of your system depends on the architecture of your machine. Numbers in BSON data are always stored as `little-endian`, if your system is `big-endian` this means that numeric data is converted between big and little endian.

In the context of the bit-test match expression operators:

- :query:`$bitsAnySet`
- :query:`$bitsAnyClear`
- :query:`$bitsAllSet`
- :query:`$bitsAllClear`
:bsontype:`BinData <Binary>` values act as [bitmasks](https://en.wikipedia.org/wiki/Mask_(computing))_ and are interpreted as though they are arbitrary-length unsigned little-endian numbers. The lowest-addressable byte is always interpreted as the least significant byte. Similarly, the highest-addressable byte in the `BinData` is always interpreted as the most significant byte.
