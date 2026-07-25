---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/05-2025/05-05-2025-openinference-google-genai-instrumentation.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.901396Z"
---
# 05 05 2025 Openinference Google Genai Instrumentation

---
title: "05.05.2025: OpenInference Google GenAI instrumentation"
---

<Update label="05.05.2025">

## OpenInference Google GenAI Instrumentation

<Frame>
  <iframe
    src="https://cdn.iframe.ly/bdf8oY5"
    width={1000}
    height={400}
    allowFullScreen
    allow="encrypted-media *;"
  />
</Frame>

We've added a Python auto-instrumentation library for the Google GenAI SDK. This enables seamless tracing of GenAI workflows with full OpenTelemetry compatibility. Traces can be exported to any OpenTelemetry collector.

### Installation

```bash
pip install openinference-instrumentation-google-genai
```

For more details on how to set up the tracing integration seamlessly:
<Card title="openinference-instrumentation-google-genai" icon="box" href="https://pypi.org/project/openinference-instrumentation-google-genai/" horizontal>
  GitHub
</Card>

Additionally, the Google GenAI instrumentor is now supported and works seamlessly with **Span Replay** in Phoenix, enabling deep trace inspection and replay for more effective debugging and observability.

<Card title="Google GenAI | Phoenix" icon="book" href="/docs/phoenix/integrations/llm-providers/google-gen-ai" horizontal>
  GitHub
</Card>

### Acknowledgements

Big thanks to Harrison Chu for his contributions.

</Update>


