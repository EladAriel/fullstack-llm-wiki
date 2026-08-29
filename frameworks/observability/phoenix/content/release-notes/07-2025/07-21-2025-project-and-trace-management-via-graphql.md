---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/07-2025/07-21-2025-project-and-trace-management-via-graphql.mdx"
source_commit: "c48e50e9906fcc56c1c103ebd93ef3c95ed6b6e7"
source_commit_short: "c48e50e"
source_commit_date: "2026-08-29T01:45:20-06:00"
generated_at: "2026-08-29T09:39:58.848200Z"
---
# 07 21 2025 Project And Trace Management Via Graphql

---
title: "07.21.2025: Project and trace management via GraphQL"
description: Available in Phoenix 11.9+
---

<Update label="07.21.2025">

## Project and Trace Management via GraphQL

**New Features:**

* Added `transferTracesToProject` GraphQL mutation to **move traces between projects**, preserving **annotations and cost calculations** for seamless reorganization.

* Added `createProject` GraphQL mutation to **create new projects programmatically** via the API.

<Card title="feat(traces): Implement trace project transfer API by mikeldking · Pull Request #8645 · Arize-ai/phoenix" icon="github" href="https://github.com/Arize-ai/phoenix/pull/8645" horizontal>
GitHub
</Card>

<Card title="feat: createProject GraphQL mutation by mikeldking · Pull Request #8660 · Arize-ai/phoenix" icon="github" href="https://github.com/Arize-ai/phoenix/pull/8660" horizontal>
GitHub
</Card>
</Update>