---
type: "Framework Learn Page"
framework: "LangSmith"
source_repo: "https://github.com/langchain-ai/docs.git"
source_branch: "main"
source_path: "src/langsmith/trace-with-n8n.mdx"
source_commit: "a174f9cf7c91ee5eb14ee2382eb48bfe6e4956e9"
source_commit_short: "a174f9c"
source_commit_date: "2026-08-28T17:04:12-07:00"
generated_at: "2026-08-29T09:39:50.602457Z"
---
# Trace With N8N

---
title: Trace n8n workflows
sidebarTitle: n8n
description: Learn how to trace n8n AI workflows in LangSmith.
---

[n8n](https://n8n.io/) is a workflow automation platform that includes advanced AI capabilities built on LangChain. You can connect your n8n instance to LangSmith to record and monitor AI workflow runs.

<Note>
LangSmith tracing is available for **self-hosted n8n instances** only.
</Note>

## Prerequisites

- A [LangSmith account](https://smith.langchain.com) and [API key](/langsmith/create-account-api-key)
- A self-hosted n8n instance

## Set up tracing

1. Set the following environment variables in the environment where you host your n8n instance, in the same way as the rest of your [n8n configuration](https://docs.n8n.io/hosting/configuration/configuration-methods/).

   Required environment variables:
   - `LANGCHAIN_TRACING_V2`: Set to `true` to enable tracing.
   - `LANGCHAIN_API_KEY`: Your LangSmith API key.

   Optional environment variables:
   - `LANGCHAIN_ENDPOINT`: LangSmith API endpoint. Defaults to `https://api.smith.langchain.com`. Set this if using self-hosted LangSmith, GCP EU (`https://eu.api.smith.langchain.com`), GCP APAC (`https://apac.api.smith.langchain.com`), or AWS US (`https://aws.api.smith.langchain.com`).
   - `LANGCHAIN_PROJECT`: Project name for traces. Defaults to `"default"`.
   - `LANGCHAIN_CALLBACKS_BACKGROUND`: Set to `true` for asynchronous trace upload (default), or `false` for synchronous uploads. (default: `true`)

1. Restart your n8n instance for the environment variables to take effect.

## View traces in LangSmith

After running an AI workflow:

1. Open [LangSmith](https://smith.langchain.com).
1. Select your project. If you just created your account, the `"default"` project appears after the first trace is sent.
1. Locate the trace corresponding to your workflow execution.

## Additional resources

- [n8n LangSmith integration guide](https://docs.n8n.io/advanced-ai/langchain/langsmith/)
- [n8n Advanced AI documentation](https://docs.n8n.io/advanced-ai/)
