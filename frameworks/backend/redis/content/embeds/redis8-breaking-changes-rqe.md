---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/redis8-breaking-changes-rqe.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

The following changes affect behavior and validation in Redis Search:
- Enforces validation for `LIMIT` arguments (offset must be 0 if limit is 0).
- Enforces parsing rules for `FT.CURSOR READ` and `FT.ALIASADD`.
- Parentheses are now required for exponentiation precedence in `APPLY` expressions.
- Invalid input now returns errors instead of empty results.
- Default values revisited for reducers like `AVG`, `COUNT`, `SUM`, `STDDEV`, `QUANTILE`, and others.
- Updates to scoring (`BM25` is now the default instead of `TF-IDF`).
- Improved handling of expired records, memory constraints, and malformed fields.

For a full list of Redis Search-related changes, see the [release notes](https://github.com/redis/redis/releases).