---
type: "Framework Learn Page"
framework: "LangSmith"
source_repo: "https://github.com/langchain-ai/docs.git"
source_branch: "main"
source_path: "src/langsmith/smithdb-sdk-migration-runs.mdx"
source_commit: "a174f9cf7c91ee5eb14ee2382eb48bfe6e4956e9"
source_commit_short: "a174f9c"
source_commit_date: "2026-08-28T17:04:12-07:00"
generated_at: "2026-08-29T09:39:50.598825Z"
---
# Smithdb Sdk Migration Runs

---
title: Migrate run retrieval to SmithDB
sidebarTitle: Retrieve runs
description: Migrate the LangSmith SDK methods that retrieve a single run or build a run URL.
---

import SmithdbMigrationRunsRetrieve from '/snippets/langsmith/smithdb-migration/runs-retrieve.mdx';
import SmithdbMigrationRunsGetUrl from '/snippets/langsmith/smithdb-migration/runs-geturl.mdx';

These methods read a single run or build a link to one. To migrate run queries, see [Query runs](/langsmith/smithdb-sdk-migration-query-runs). For deprecation dates and minimum SDK versions, see [Migrate to SmithDB-backed SDK methods](/langsmith/smithdb-sdk-migration).

<SmithdbMigrationRunsRetrieve />

<SmithdbMigrationRunsGetUrl />

## See also

- [Query runs](/langsmith/smithdb-sdk-migration-query-runs)
- [Feedback and annotation queues](/langsmith/smithdb-sdk-migration-feedback)
- [Migration overview](/langsmith/smithdb-sdk-migration)
