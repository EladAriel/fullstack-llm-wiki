---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/redis8-breaking-changes-rqe.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.102770Z"
---
# Redis8 Breaking Changes Rqe

The following changes affect behavior and validation in Redis Search:
- Enforces validation for `LIMIT` arguments (offset must be 0 if limit is 0).
- Enforces parsing rules for `FT.CURSOR READ` and `FT.ALIASADD`.
- Parentheses are now required for exponentiation precedence in `APPLY` expressions.
- Invalid input now returns errors instead of empty results.
- Default values revisited for reducers like `AVG`, `COUNT`, `SUM`, `STDDEV`, `QUANTILE`, and others.
- Updates to scoring (`BM25` is now the default instead of `TF-IDF`).
- Improved handling of expired records, memory constraints, and malformed fields.

For a full list of Redis Search-related changes, see the [release notes](https://github.com/redis/redis/releases).