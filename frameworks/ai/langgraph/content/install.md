---
type: "Framework Learn Page"
framework: "LangGraph"
source_repo: "https://github.com/langchain-ai/docs"
source_branch: "main"
source_path: "src/oss/langgraph/install.mdx"
source_commit: "a174f9cf7c91ee5eb14ee2382eb48bfe6e4956e9"
source_commit_short: "a174f9c"
source_commit_date: "2026-08-28T17:04:12-07:00"
generated_at: "2026-08-29T09:38:45.965036Z"
---
---
title: Install LangGraph
sidebarTitle: Install
---


To install the base LangGraph package:

:::python
<CodeGroup>
```bash pip
pip install -U langgraph
```

```bash uv
uv add langgraph
```
</CodeGroup>
:::

:::js
<CodeGroup>
```bash npm
npm install @langchain/langgraph @langchain/core
```

```bash pnpm
pnpm add @langchain/langgraph @langchain/core
```

```bash yarn
yarn add @langchain/langgraph @langchain/core
```

```bash bun
bun add @langchain/langgraph @langchain/core
```
</CodeGroup>
:::

To use LangGraph you will usually want to access LLMs and define tools.
You can do this however you see fit.

One way to do this (which we will use in the docs) is to use [LangChain](/oss/langchain/overview).

Install LangChain with:

:::python
<CodeGroup>
```bash pip
pip install -U langchain
# Requires Python 3.10+
```

```bash uv
uv add langchain
# Requires Python 3.10+
```
</CodeGroup>
:::

:::js
<CodeGroup>
```bash npm
npm install langchain
```

```bash pnpm
pnpm add langchain
```

```bash yarn
yarn add langchain
```

```bash bun
bun add langchain
```
</CodeGroup>
:::

To work with specific LLM provider packages, you will need install them separately.

Refer to the [integrations](/oss/integrations/providers/overview) page for provider-specific installation instructions.
