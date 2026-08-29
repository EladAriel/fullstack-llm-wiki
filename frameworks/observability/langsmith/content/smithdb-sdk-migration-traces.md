---
type: "Framework Learn Page"
framework: "LangSmith"
source_repo: "https://github.com/langchain-ai/docs.git"
source_branch: "main"
source_path: "src/langsmith/smithdb-sdk-migration-traces.mdx"
source_commit: "a174f9cf7c91ee5eb14ee2382eb48bfe6e4956e9"
source_commit_short: "a174f9c"
source_commit_date: "2026-08-28T17:04:12-07:00"
generated_at: "2026-08-29T09:39:50.595841Z"
---
# Smithdb Sdk Migration Traces

---
title: Migrate trace methods to SmithDB
sidebarTitle: Traces
description: Migrate the LangSmith SDK trace methods to their SmithDB-backed equivalents.
---

import SmithdbMigrationTracesQuery from '/snippets/langsmith/smithdb-migration/traces-query.mdx';
import SmithdbMigrationTracesListRuns from '/snippets/langsmith/smithdb-migration/traces-list-runs.mdx';

These methods query traces and list the runs inside a trace. For deprecation dates, minimum SDK versions, and the agent prompt that applies to every method, see [Migrate to SmithDB-backed SDK methods](/langsmith/smithdb-sdk-migration).

<SmithdbMigrationTracesQuery />

<SmithdbMigrationTracesListRuns />

## See also

- [Query runs](/langsmith/smithdb-sdk-migration-query-runs)
- [Threads](/langsmith/smithdb-sdk-migration-threads)
- [Migration overview](/langsmith/smithdb-sdk-migration)
