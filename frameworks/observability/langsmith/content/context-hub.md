---
type: "Framework Learn Page"
framework: "LangSmith"
source_repo: "https://github.com/langchain-ai/docs.git"
source_branch: "main"
source_path: "src/langsmith/context-hub.mdx"
source_commit: "2aae1dfc98ee953a9a5185fb6fcdd9efb3f4d878"
source_commit_short: "2aae1df"
source_commit_date: "2026-07-25T00:27:23+00:00"
generated_at: "2026-07-25T19:08:33.358568Z"
---
# Context Hub

---
title: Context Hub
sidebarTitle: Overview
description: Manage the instructions and tools your agents use with version control and environment promotion in the LangSmith Context Hub.
icon: "book"
mode: wide
---

The Context Hub gives your team version-controlled, environment-aware management of the instructions and tools your agents use in production. A _context_ is a versioned bundle of agent instructions and tools, either a skill or a full agent, that you manage in LangSmith and promote to an environment so your agents can pull it.

<CardGroup cols={2}>
  <Card title="Concepts" icon="bulb" href="/langsmith/context-engineering-concepts" arrow="true">
    Learn the core concepts of context engineering: skills, agents, versioning, and sharing.
  </Card>
  <Card title="Use the Context Hub" icon="pointer" href="/langsmith/use-the-context-hub" arrow="true">
    Create a context, view its files and history, and promote it to an environment.
  </Card>
  <Card title="Manage contexts with the SDK" icon="code" href="/langsmith/manage-contexts-sdk" arrow="true">
    Push, pull, list, and delete agent and skill repos in the Context Hub programmatically.
  </Card>
  <Card title="Configure commit webhooks" icon="webhook" href="/langsmith/context-hub-webhooks" arrow="true">
    Send every agent and skill commit in your workspace to an external HTTPS endpoint.
  </Card>
</CardGroup>
