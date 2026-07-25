---
type: "Framework Learn Page"
framework: "Model Context Protocol"
source_repo: "https://github.com/modelcontextprotocol/modelcontextprotocol"
source_branch: "main"
source_path: "docs/specification/2025-03-26/server/index.mdx"
source_commit: "7634684382c3d14cf7e9f14073fe40a2d8ace3fa"
source_commit_short: "76346843"
source_commit_date: "2026-07-23T16:49:30-07:00"
generated_at: "2026-07-25T11:50:39Z"
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
