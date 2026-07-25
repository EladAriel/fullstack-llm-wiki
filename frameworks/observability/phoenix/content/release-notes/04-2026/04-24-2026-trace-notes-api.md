---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/04-2026/04-24-2026-trace-notes-api.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.880749Z"
---
---
title: "04.24.2026 Trace Notes API"
description: "Add trace notes via REST endpoint, TypeScript client, or CLI; reserve the note annotation name for note-specific APIs."
---

## Trace Notes API

**Available in arize-phoenix 14.13.0+ (server), @arizeai/phoenix-client 6.8.0+ (TypeScript), @arizeai/phoenix-cli 1.3.0+ (CLI)**

Phoenix now supports creating trace notes through a dedicated REST endpoint, TypeScript client function, and CLI command. Notes are stored separately from annotations — each trace can hold multiple notes, and `--include-notes` keeps them out of the annotations view.

To keep note behavior consistent, the reserved annotation name `note` is no longer accepted on the generic annotation endpoints. Use the dedicated note endpoints instead:

- `POST /v1/trace_notes` for trace notes
- `POST /v1/span_notes` for span notes

## TypeScript

```typescript
import { addTraceNote } from "@arizeai/phoenix-client/traces";

const result = await addTraceNote({
  traceNote: {
    traceId: "abc123def456",
    note: "Needs follow-up review.",
  },
});
console.log(result.id); // note annotation ID
```

## CLI

```bash
# Add a note to a trace
px trace add-note <trace-id> --text "Needs follow-up review."

# Fetch a trace with its notes
px trace get <trace-id> --include-notes

# List traces with notes
px trace list --include-notes
```

Notes appear under `notes[]` on the trace object (distinct from `annotations[]`) when you pass `--include-notes`.
