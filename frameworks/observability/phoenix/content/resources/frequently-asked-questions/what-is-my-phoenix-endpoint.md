---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/resources/frequently-asked-questions/what-is-my-phoenix-endpoint.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.879426Z"
---
# What Is My Phoenix Endpoint

---
title: "What is my Phoenix Endpoint?"
---


There are two endpoints that matter in Phoenix:

1. **Application Endpoint:** The endpoint your Phoenix instance is running on
2. **OTEL Tracing Endpoint:** The endpoint through which your Phoenix instance receives OpenTelemetry traces

### **Application Endpoint**

You choose this endpoint when you set up the app. For a local `phoenix serve` the default is `http://localhost:6006`. For a remote deployment, it's available under the `Hostname` field of the **Settings** page.

To set this endpoint, use the `PHOENIX_COLLECTOR_ENDPOINT` environment variable. This is used by the Phoenix client package to query traces, log annotations, and retrieve prompts.

### **OTEL Tracing Endpoint**

You choose this endpoint when you set up the app. For a remote deployment, it's available under the `Hostname` field of the **Settings** page. For a local `phoenix serve` the defaults are:

* Using the GRPC protocol: `http://localhost:4317`
* Using the HTTP protocol: `http://localhost:6006/v1/traces`

To set this endpoint, use the `register(endpoint=YOUR ENDPOINT)` function. This endpoint can also be set using environment variables. For more on the register function and other configuration options, [see here](https://github.com/Arize-ai/phoenix/tree/main/packages/phoenix-otel#configuring-the-collector-endpoint).
