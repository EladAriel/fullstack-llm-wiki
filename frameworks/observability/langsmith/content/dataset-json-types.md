---
type: "Framework Learn Page"
framework: "LangSmith"
source_repo: "https://github.com/langchain-ai/docs.git"
source_branch: "main"
source_path: "src/langsmith/dataset-json-types.mdx"
source_commit: "2aae1dfc98ee953a9a5185fb6fcdd9efb3f4d878"
source_commit_short: "2aae1df"
source_commit_date: "2026-07-25T00:27:23+00:00"
generated_at: "2026-07-25T19:08:33.404100Z"
---
# Dataset Json Types

---
title: Dataset prebuilt JSON schema types
sidebarTitle: Dataset prebuilt JSON schema types
---

LangSmith recommends that you set a schema on the inputs and outputs of your dataset schemas to ensure data consistency and that your examples are in the right format for downstream processing, like running evals.

In order to better support LLM workflows, LangSmith has support for a few different predefined prebuilt types. These schemas are hosted publicly by the LangSmith API, and can be defined in your dataset schemas using [JSON Schema references](https://json-schema.org/understanding-json-schema/structuring#dollarref). The table of available schemas can be seen below

| Type    | JSON Schema Reference Link                                                                                                       | Usage                                                                                                                     |
| ------- | -------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| Message | [https://api.smith.langchain.com/public/schemas/v1/message.json](https://api.smith.langchain.com/public/schemas/v1/message.json) | Represents messages sent to a chat model, following the OpenAI standard format.                                           |
| Tool    | [https://api.smith.langchain.com/public/schemas/v1/tooldef.json](https://api.smith.langchain.com/public/schemas/v1/tooldef.json) | Tool definitions available to chat models for function calling, defined in OpenAI's JSON Schema inspired function format. |

LangSmith lets you define a series of transformations that collect the above prebuilt types from your traces and add them to your dataset. For more info on available transformations, see our [reference](/langsmith/dataset-transformations)
