---
type: "Framework Learn Page"
framework: "Sentry Python"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/python/tracing/index.mdx"
source_commit: "8b4e4a23b18ee70f5fdb05bcda48869c10be2f60"
source_commit_short: "8b4e4a2"
source_commit_date: "2026-08-28T22:17:56+00:00"
generated_at: "2026-08-29T09:40:09.039340Z"
---
# Index

---
title: Set Up Tracing
sidebar_title: Tracing
description: "With Tracing, Sentry tracks your software performance, measuring metrics like throughput and latency, and displays the impact of errors across multiple systems."
sidebar_order: 6
sidebar_section: features
---

<AgentSetupCallout skill="sentry-python-sdk" platformName="Python" />

## Prerequisites

* You have the <PlatformLink to="/">Python SDK installed</PlatformLink> (version 0.11.2 or higher)

## Configure

To enable tracing in your application, adjust the `traces_sample_rate` based on the number of trace samples you want to send to Sentry by adding the highlighted code snippet below. (Setting a value of `1.0` will send 100% of your traces.)


```python {diff}
import sentry_sdk

sentry_sdk.init(
    dsn="___PUBLIC_DSN___",
    # Add data like request headers and IP for users, if applicable;
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for tracing.
+   traces_sample_rate=1.0,
)
```

If you’re adopting Tracing in a high-throughput environment, we recommend testing prior to deployment to ensure that your service’s performance characteristics maintain expectations.

Learn more about tracing <PlatformLink to="/configuration/options/#tracing-options">options</PlatformLink>, how to use the <PlatformLink to="/configuration/sampling/#setting-a-sampling-function">traces_sampler</PlatformLink> function, or how to <PlatformLink to="/configuration/sampling/#sampling-transaction-events">sample transactions</PlatformLink>.

## Agent Tracing

If you're building with agents or LLMs, you can extend your tracing setup to capture agent workflows, model calls, tool executions, and token usage. With tracing already enabled, the Python SDK automatically instruments supported libraries like OpenAI, Anthropic, LangChain, and others.

<PlatformLink to="/agent-tracing/">Set up Agent Tracing</PlatformLink> to get started.

## Next Steps

<PageGrid />
