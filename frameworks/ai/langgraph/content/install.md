---
type: "Framework Learn Page"
framework: "LangGraph"
source_repo: "https://github.com/langchain-ai/docs"
source_branch: "main"
source_path: "src/oss/langgraph/install.mdx"
source_commit: "2aae1dfc98ee953a9a5185fb6fcdd9efb3f4d878"
source_commit_short: "2aae1dfc"
source_commit_date: "2026-07-25T00:27:23Z"
generated_at: "2026-07-25T11:51:08Z"
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
