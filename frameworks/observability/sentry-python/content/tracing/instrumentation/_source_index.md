---
type: "Framework Learn Page"
framework: "Sentry Python"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/python/tracing/instrumentation/index.mdx"
source_commit: "8b4e4a23b18ee70f5fdb05bcda48869c10be2f60"
source_commit_short: "8b4e4a2"
source_commit_date: "2026-08-28T22:17:56+00:00"
generated_at: "2026-08-29T09:40:09.046976Z"
---
# Index

---
title: Instrumentation
description: "Learn what Sentry instruments automatically, and how to configure spans to capture tracing data on any action in your app."
sidebar_order: 50
---

<Alert>

To capture transactions and spans customized to your organization's needs, you must first <PlatformLink to="/tracing/">set up tracing</PlatformLink>.

</Alert>

There are two ways that instrumentation is applied to your application:

## Automatic Instrumentation

Many integrations for popular frameworks automatically capture transactions and spans that can be sent to Sentry. Read more about automatic instrumentation [here](/platforms/python/tracing/instrumentation/automatic-instrumentation/).

## Custom Instrumentation

To add custom performance data to your application, you need to add custom instrumentation in the form of [spans](/concepts/key-terms/tracing/distributed-tracing/#traces-transactions-and-spans). Spans are a way to measure the time it takes for a specific action to occur. For example, you can create a span to measure the time it takes for a function to execute. Learn more about span lifecycles [here](/platforms/python/tracing/span-lifecycle/).
