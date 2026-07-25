---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/04-2025/04-18-2025-tracing-for-mcp-client-server-applications.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.899488Z"
---
# 04 18 2025 Tracing For Mcp Client Server Applications

---
title: "04.18.2025: Tracing for MCP client server applications"
description: Available in Phoenix 8.26+
---

<Update label="04.18.2025">

## Tracing For MCP Client Server Applications

<Frame>
  <iframe 
    src="https://cdn.iframe.ly/Yqc5Yah" 
    width={1000} 
    height={400}
    allowFullScreen
  />
</Frame>

We're excited to announce a powerful capability in the [**OpenInference**](https://github.com/Arize-ai/openinference) OSS library **`openinference-instrumentation-mcp` —** seamless OTEL context propagation for MCP clients and servers.

### **What's New?**

This release introduces automatic distributed tracing for **Anthropic's Model Context Protocol (MCP)**. Using OpenTelemetry, you can now:

* **Propagate context** across MCP client-server boundaries
* Generate **end-to-end traces** of your AI system across services and languages
* Gain full visibility into how models access and use external context

The `openinference-instrumentation-mcp` package handles this for you by:

* Creating spans for MCP client operations
* Injecting trace context into MCP requests
* Extracting and continuing the trace context on the server
* Associating the context with OTEL spans on the server side

### **Set up**

1. Instrument both MCP client and server with OpenTelemetry.
2. Add the `openinference-instrumentation-mcp` package.
3. Spans will propagate across services, appearing as a **single connected trace** in Phoenix.

<Card title="phoenix/tutorials/mcp/tracing_between_mcp_client_and_server at main · Arize-ai/phoenix" icon="github" href="https://github.com/Arize-ai/phoenix/tree/main/tutorials/mcp/tracing_between_mcp_client_and_server" horizontal>
  GitHub
</Card>

### **Walkthrough Video**

<Frame>
  <iframe 
    src="https://www.youtube.com/embed/dhK2pWQdGjk" 
    width={1000} 
    height={400}
    allowFullScreen
  />
</Frame>

### **Acknowledgments**

Big thanks to Adrian Cole and Anuraag Agrawal for their contributions to this feature.

</Update>