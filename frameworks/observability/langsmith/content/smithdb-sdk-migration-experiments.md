---
type: "Framework Learn Page"
framework: "LangSmith"
source_repo: "https://github.com/langchain-ai/docs.git"
source_branch: "main"
source_path: "src/langsmith/smithdb-sdk-migration-experiments.mdx"
source_commit: "a174f9cf7c91ee5eb14ee2382eb48bfe6e4956e9"
source_commit_short: "a174f9c"
source_commit_date: "2026-08-28T17:04:12-07:00"
generated_at: "2026-08-29T09:39:50.621730Z"
---
# Smithdb Sdk Migration Experiments

---
title: Migrate dataset experiment runs to SmithDB
sidebarTitle: Dataset experiment runs
description: Migrate the LangSmith SDK dataset experiment run methods to their SmithDB-backed equivalents.
---

import SmithdbMigrationExperimentRunsQuery from '/snippets/langsmith/smithdb-migration/experiment-runs-query.mdx';

These methods query the runs attached to a dataset experiment. For deprecation dates, minimum SDK versions, and the agent prompt that applies to every method, see [Migrate to SmithDB-backed SDK methods](/langsmith/smithdb-sdk-migration).

<SmithdbMigrationExperimentRunsQuery />

## See also

- [Threads](/langsmith/smithdb-sdk-migration-threads)
- [Feedback and annotation queues](/langsmith/smithdb-sdk-migration-feedback)
- [Migration overview](/langsmith/smithdb-sdk-migration)
