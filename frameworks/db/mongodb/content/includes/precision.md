---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/precision.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

MongoDB uses the IEEE 754 standard for floating point computations, and the behavior is consistent with that standard.

If you need a floating point number for an application that requires high precison, consider a `Decimal128` value. For details, see `bson-decimal128`.

If you need to store a currency value, consider an integer using the lowest currency denomination unit. For example, use an integer with cents or pennies instead of a floating point number.
