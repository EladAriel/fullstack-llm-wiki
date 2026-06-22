---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/warning-hashed-index-floating-point.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

> **Warning:** MongoDB `hashed` indexes truncate floating point numbers to 64-bit integers
before hashing. For example, a `hashed` index would store the same
value for a field that held a value of `2.3`, `2.2`, and `2.9`.
To prevent collisions, do not use a `hashed` index for floating
point numbers that cannot be reliably converted to 64-bit
integers (and then back to floating point). MongoDB `hashed` indexes do
not support floating point values larger than 2\ :sup:`53`.
To see what the hashed value would be for a key, see
:method:`convertShardKeyToHashed()`.
