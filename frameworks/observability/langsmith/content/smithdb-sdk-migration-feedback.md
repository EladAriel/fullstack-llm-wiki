---
type: "Framework Learn Page"
framework: "LangSmith"
source_repo: "https://github.com/langchain-ai/docs.git"
source_branch: "main"
source_path: "src/langsmith/smithdb-sdk-migration-feedback.mdx"
source_commit: "a174f9cf7c91ee5eb14ee2382eb48bfe6e4956e9"
source_commit_short: "a174f9c"
source_commit_date: "2026-08-28T17:04:12-07:00"
generated_at: "2026-08-29T09:39:50.654084Z"
---
# Smithdb Sdk Migration Feedback

---
title: Migrate feedback and sharing methods to SmithDB
sidebarTitle: Feedback and sharing
description: Migrate the LangSmith SDK feedback, annotation queue, and public run methods to their SmithDB-backed equivalents.
---

import SmithdbMigrationRunsAddToAnnotationQueue from '/snippets/langsmith/smithdb-migration/runs-add-to-annotation-queue.mdx';
import SmithdbMigrationPublicRuns from '/snippets/langsmith/smithdb-migration/public-runs.mdx';
import SmithdbMigrationFeedbackCreate from '/snippets/langsmith/smithdb-migration/feedback-create.mdx';

These methods add runs to annotation queues, share runs publicly, and create feedback. For deprecation dates, minimum SDK versions, and the agent prompt that applies to every method, see [Migrate to SmithDB-backed SDK methods](/langsmith/smithdb-sdk-migration).

<SmithdbMigrationRunsAddToAnnotationQueue />

<SmithdbMigrationPublicRuns />

<SmithdbMigrationFeedbackCreate />

## See also

- [Retrieve runs](/langsmith/smithdb-sdk-migration-runs)
- [Dataset experiment runs](/langsmith/smithdb-sdk-migration-experiments)
- [Migration overview](/langsmith/smithdb-sdk-migration)
