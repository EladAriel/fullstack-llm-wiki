---
type: "Framework Learn Page"
framework: "LangSmith"
source_repo: "https://github.com/langchain-ai/docs.git"
source_branch: "main"
source_path: "src/langsmith/smithdb-sdk-migration-query-runs.mdx"
source_commit: "a174f9cf7c91ee5eb14ee2382eb48bfe6e4956e9"
source_commit_short: "a174f9c"
source_commit_date: "2026-08-28T17:04:12-07:00"
generated_at: "2026-08-29T09:39:50.679387Z"
---
# Smithdb Sdk Migration Query Runs

---
title: Migrate run queries to SmithDB
sidebarTitle: Query runs
description: Migrate the LangSmith SDK run query methods to their SmithDB-backed equivalents.
---

import SmithdbMigrationRunsQuery from '/snippets/langsmith/smithdb-migration/runs-query.mdx';

Run queries are the largest surface area in the migration, so they have their own page. For deprecation dates, minimum SDK versions, and the agent prompt that applies to every method, see [Migrate to SmithDB-backed SDK methods](/langsmith/smithdb-sdk-migration).

<SmithdbMigrationRunsQuery />

## See also

- [Retrieve runs](/langsmith/smithdb-sdk-migration-runs)
- [Traces](/langsmith/smithdb-sdk-migration-traces)
- [Migration overview](/langsmith/smithdb-sdk-migration)
