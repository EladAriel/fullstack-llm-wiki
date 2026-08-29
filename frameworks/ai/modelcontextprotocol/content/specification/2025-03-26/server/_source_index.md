---
type: "Framework Learn Page"
framework: "Model Context Protocol"
source_repo: "https://github.com/modelcontextprotocol/modelcontextprotocol"
source_branch: "main"
source_path: "docs/specification/2025-03-26/server/index.mdx"
source_commit: "ca4ab3027f7c844cd3039c956438d72e8253f7f5"
source_commit_short: "ca4ab30"
source_commit_date: "2026-08-28T21:24:44-07:00"
generated_at: "2026-08-29T09:38:48.094076Z"
---
# Index

---
title: Overview
---

Servers provide the fundamental building blocks for adding context to language models via
MCP. These primitives enable rich interactions between clients, servers, and language
models:

- **Prompts**: Pre-defined templates or instructions that guide language model
  interactions
- **Resources**: Structured data or content that provides additional context to the model
- **Tools**: Executable functions that allow models to perform actions or retrieve
  information

Each primitive can be summarized in the following control hierarchy:

| Primitive | Control                | Description                                        | Example                         |
| --------- | ---------------------- | -------------------------------------------------- | ------------------------------- |
| Prompts   | User-controlled        | Interactive templates invoked by user choice       | Slash commands, menu options    |
| Resources | Application-controlled | Contextual data attached and managed by the client | File contents, git history      |
| Tools     | Model-controlled       | Functions exposed to the LLM to take actions       | API POST requests, file writing |

Explore these key primitives in more detail below:

<CardGroup cols={3}>
  <Card
    title="Prompts"
    icon="message"
    href="/specification/2025-03-26/server/prompts"
  />
  <Card
    title="Resources"
    icon="file-lines"
    href="/specification/2025-03-26/server/resources"
  />
  <Card
    title="Tools"
    icon="wrench"
    href="/specification/2025-03-26/server/tools"
  />
</CardGroup>
