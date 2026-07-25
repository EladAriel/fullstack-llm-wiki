---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/05-2026/05-15-2026-otel-semconv-conversion.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.907060Z"
---
# 05 15 2026 Otel Semconv Conversion

---
title: "05.15.2026: OTel GenAI Semantic Convention Auto-Conversion"
description: "Phoenix now automatically converts OpenTelemetry GenAI semantic convention attributes to OpenInference, so traces from OTel-native instrumentations render with full message I/O, tool calls, and token counts."
---

**Available in arize-phoenix 15.10.0+**

Phoenix now automatically converts [OpenTelemetry GenAI semantic convention](https://opentelemetry.io/docs/specs/semconv/gen-ai/) attributes (`gen_ai.*`) to OpenInference format when spans arrive. Traces produced by OTel-native instrumentations — such as the OpenAI, Anthropic, and Google GenAI contrib packages — now render in Phoenix with full message I/O, tool definitions, retrieval documents, and token counts without any code changes.

## What gets converted

| OTel GenAI attribute | OpenInference output |
|---|---|
| `gen_ai.input.messages` | `llm.input_messages.*` (role, content, tool calls) |
| `gen_ai.output.message` | `llm.output_messages.*` |
| `gen_ai.system_instructions` | Synthetic `system` message prepended to inputs |
| Tool definitions and call results | `llm.tools.*`, `tool.*` |
| Retrieval documents | `retrieval.documents.*` |
| `gen_ai.usage.*` | `llm.token_count.prompt`, `llm.token_count.completion` |
| `gen_ai.system` / `gen_ai.request.model` | `llm.provider`, `llm.model_name` |
| `gen_ai.operation.name` | `llm.invocation_parameters` |

If a span already has OpenInference attributes (e.g., from `openinference-instrumentation-*`), those values take precedence — conversion only fills in what's missing.

## No code changes required

Send OTel-native traces directly to Phoenix and the conversion happens at ingest time. Install any OTel GenAI contrib package, point it at Phoenix's OTLP endpoint, and spans appear with the full Phoenix trace detail view.

```python
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace.export import SimpleSpanProcessor
from openai.contrib.instrumentation import OpenAIInstrumentor  # example

provider = TracerProvider()
provider.add_span_processor(
    SimpleSpanProcessor(
        OTLPSpanExporter(endpoint="http://localhost:6006/v1/traces")
    )
)
OpenAIInstrumentor().instrument(tracer_provider=provider)
```

Spans emitted this way now show message I/O, tool calls, and token counts in the Phoenix UI exactly as they would from OpenInference-native instrumentation.
