---
type: "Framework Learn Page"
framework: "Sentry Python"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/python/integrations/google-genai/index.mdx"
source_commit: "8b4e4a23b18ee70f5fdb05bcda48869c10be2f60"
source_commit_short: "8b4e4a2"
source_commit_date: "2026-08-28T22:17:56+00:00"
generated_at: "2026-08-29T09:40:09.059521Z"
---
# Index

---
title: Google Gen AI
description: "Learn about using Sentry for Google Gen AI."
---

This integration connects Sentry with the [Google Gen AI Python SDK](https://github.com/googleapis/python-genai).

Once you've installed this SDK, you can use the Sentry Agents Tracing, a Sentry dashboard that helps you understand what's going on with your AI requests.

Sentry AI Observability will automatically collect information about prompts, tools, tokens, and models. Learn more about the [Agents Dashboard](/product/agents/dashboards/).

<Include name="python-stream-mode-general-callout.mdx" />

## Install

Install `sentry-sdk` from PyPI:

```bash {tabTitle:pip}
pip install sentry-sdk
```

```bash {tabTitle:uv}
uv add sentry-sdk
```

## Configure

Add `GoogleGenAIIntegration()` to your `integrations` list:

```python
import sentry_sdk
from sentry_sdk.integrations.google_genai import GoogleGenAIIntegration

sentry_sdk.init(
    dsn="___PUBLIC_DSN___",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for tracing.
    traces_sample_rate=1.0,
    # Add data like inputs and responses;
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
    integrations=[
        GoogleGenAIIntegration(),
    ],
)
```

## Verify

Verify that the integration works by making a chat request to Google Gen AI.

```python
import sentry_sdk
from sentry_sdk.integrations.google_genai import GoogleGenAIIntegration
from google.genai import Client

sentry_sdk.init(...)  # same as above

client = Client(api_key="(your Google API key)")

def my_llm_stuff():
    # or sentry_sdk.traces.start_span(name="The result of the AI inference", parent_span=None) in stream mode
    with sentry_sdk.start_transaction(name="The result of the AI inference"):
        response = client.models.generate_content(
            model="gemini-2.0-flash-exp",
            contents="say hello"
        )
        print(response.text)
```

After running this script, the resulting data should show up in the `"AI Spans"` tab on the `"Explore" > "Traces"` page on Sentry.io.

If you manually created an <PlatformLink to="/agent-tracing/manual-instrumentation/#invoke-agent-span">Invoke Agent Span</PlatformLink> (not done in the example above) the data will also show up in the [Agents Dashboard](/product/agents/dashboards/).

It may take a couple of moments for the data to appear in [sentry.io](https://sentry.io).

## Behavior

- The Google Gen AI integration will connect Sentry with the supported Google Gen AI methods automatically.

- The supported function is currently `models.generate_content` (both sync and async).

- Sentry considers LLM inputs/outputs as PII (Personally identifiable information) and doesn't include PII data by default. If you want to include the data, set `send_default_pii=True` in the `sentry_sdk.init()` call. To explicitly exclude prompts and outputs despite `send_default_pii=True`, configure the integration with `include_prompts=False` as shown in the [Options section](#options) below.

## Options

You can set options for `GoogleGenAIIntegration` to change its behavior:

```python
import sentry_sdk
from sentry_sdk.integrations.google_genai import GoogleGenAIIntegration

sentry_sdk.init(
    # ...
    # Add data like inputs and responses;
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
    integrations=[
        GoogleGenAIIntegration(
            include_prompts=False,  # LLM inputs/outputs will be not sent to Sentry, despite send_default_pii=True
        ),
    ],
)
```

You can pass the following keyword arguments to `GoogleGenAIIntegration()`:

- `include_prompts`:

  Whether LLM inputs and outputs should be sent to Sentry. Sentry considers this data personal identifiable data (PII) by default. If you want to include the data, set `send_default_pii=True` in the `sentry_sdk.init()` call. To explicitly exclude prompts and outputs despite `send_default_pii=True`, configure the integration with `include_prompts=False`.

  The default is `True`.

## Supported Versions

- google-genai: 1.29.0+
- Python: 3.9+
