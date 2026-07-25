---
type: "Framework Learn Page"
framework: "Langfuse"
source_repo: "https://github.com/langfuse/langfuse-docs"
source_branch: "main"
source_path: "content/docs/prompt-management/features/n8n-node.mdx"
source_commit: "fcd1eca34a924867563c3c4e801254c4e66c0021"
source_commit_short: "fcd1eca3"
source_commit_date: "2026-07-25T00:45:45Z"
generated_at: "2026-07-25T11:51:12Z"
---

---
title: n8n Node
sidebarTitle: n8n Node
description: Community-maintained n8n node that enables seamless integration of Langfuse prompt management capabilities into n8n workflows.
---

# n8n Node for Langfuse Prompt Management

The Langfuse n8n node enables seamless integration of [Langfuse's Prompt Management](/docs/prompts/get-started) with n8n workflows. This community-maintained node allows you to fetch and use prompts directly from your Langfuse project within n8n workflows.

> **What is n8n?** [n8n](https://github.com/n8n-io/n8n) is an open‑source, node‑based workflow automation platform that lets you visually connect and orchestrate APIs, apps, and data without writing full code.

**Langfuse Node in example n8n workflow:**

<Frame fullWidth>
  ![n8n node for
  langfuse](/images/docs/prompt-management-node-in-n8n-workflow.png)
</Frame>

<Callout type="info">

Interested in tracing of n8n workflows? Check out the [n8n/langfuse integration page](/integrations/no-code/n8n).

</Callout>

## Installation

Self-hosted n8n: Install via **Settings** > **Community Nodes** using package name: [`@langfuse/n8n-nodes-langfuse`](https://www.npmjs.com/package/@langfuse/n8n-nodes-langfuse)

n8n Cloud: Use the node directly in your workflows by searching for `Langfuse`.

## GitHub Readme

<div className="p-6 mt-6 border bg-card rounded-md">
  <FetchReadme url="https://raw.githubusercontent.com/langfuse/n8n-nodes-langfuse/refs/heads/master/README.md" />
</div>

Source: [langfuse/n8n-nodes-langfuse](https://github.com/langfuse/n8n-nodes-langfuse)
