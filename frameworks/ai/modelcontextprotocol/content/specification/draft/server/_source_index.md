---
type: "Framework Learn Page"
framework: "Model Context Protocol"
source_repo: "https://github.com/modelcontextprotocol/modelcontextprotocol"
source_branch: "main"
source_path: "docs/specification/draft/server/index.mdx"
source_commit: "47501e4ced7823014b83be168916d4c9e63b594e"
source_commit_short: "47501e4c"
source_commit_date: "2026-06-22T09:16:44-07:00"
generated_at: "2026-06-23T14:04:43Z"
generated_filename: "_source_index.md"
---

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
    href="/specification/draft/server/prompts"
  />
  <Card
    title="Resources"
    icon="file-lines"
    href="/specification/draft/server/resources"
  />
  <Card title="Tools" icon="wrench" href="/specification/draft/server/tools" />
</CardGroup>
