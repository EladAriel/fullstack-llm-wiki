---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/12-2025/12-09-2025-span-notes-api.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.909025Z"
---
# 12 09 2025 Span Notes Api

---
title: "12.09.2025: Span Notes API"
description: Available in Phoenix 12.21+
---


## Span Notes API

New dedicated endpoints for span notes enable open coding and seamless annotation integrations. Add notes to spans programmatically using the Phoenix client in both Python and TypeScript.

**Python Client:**

```python
from phoenix.client import Client

client = Client()
client.spans.add_span_note(
    span_id="your-span-id",
    note="This span shows unexpected latency"
)
```

**TypeScript Client:**

```typescript
import { addSpanNote } from "@arizeai/phoenix-client/spans";

await addSpanNote({
  spanNote: {
    spanId: "your-span-id",
    note: "This span shows unexpected latency"
  }
});
```

**Use Cases:**

* Add contextual notes during debugging sessions
* Annotate spans with human feedback
* Build custom annotation pipelines and integrations
* Document issues or observations for team collaboration

#### API Reference:

<CardGroup cols={2}>
  <Card title="Python Client" icon="python" href="https://arize-phoenix.readthedocs.io/projects/client/api/spans.html#client.resources.spans.Spans.add_span_note" horizontal>
    spans.add_span_note()
  </Card>
  <Card title="TypeScript Client" icon="js" href="https://arize-ai.github.io/phoenix/functions/_arizeai_phoenix-client.spans_addSpanNote.addSpanNote.html" horizontal>
    addSpanNote()
  </Card>
</CardGroup>


