---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/natural-language-to-mongodb.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===================================

# Natural Language to MongoDB Queries

This page provides guidance on how to generate MongoDB queries for your data from natural language using a large language model (LLM).

For example, consider the following natural language query to generated query in :binary:`mongosh` for the Atlas :atlas:`sample_mflix </sample-data/sample-mflix/>` database:

## Available Methods

In addition to using LLMs out of the box, you can use the following tools built by MongoDB to generate MongoDB queries from natural language:

- `Compass Natural Language Querying <compass-query-natural-language>`
- [MongoDB MCP Server](https://www.mongodb.com/docs/mcp-server/)_
- [MongoDB Extension for Github Copilot](https://www.mongodb.com/docs/mongodb-vscode/copilot/)_
- :atlas:`LangChain MongoDB Integration </ai-integrations/langchain/natural-language-to-mql/>`
## Selecting a Model

Models that perform well on general tasks typically also perform well at MongoDB query generation. When selecting an LLM to generate MongoDB queries, refer to popular benchmarks like [MMLU-Pro](https://huggingface.co/spaces/TIGER-Lab/MMLU-Pro)_ and [Chatbot Arena ELO](https://openlm.ai/chatbot-arena/)_ to evaluate performance between models.

## Effective Prompting

This section outlines effective strategies for prompting an LLM to generate MongoDB queries.

> **Note:** The following prompting strategies are based on benchmarks created by MongoDB.
To learn more, see our public benchmark of natural language to :binary:`mongosh` code
on [Hugging Face](https://huggingface.co/datasets/mongodb-eai/natural-language-to-mongosh)_.

### Base Prompt

Your base prompt, also called the system prompt, should provide a clear overview of your task, including:

- The type of query to generate.
- Information about the expected output structure, such as
the driver language or tool that executes the query.

The following base prompt example demonstrates how to generate a MongoDB read operation or aggregation for :binary:`mongosh`:

General Guidance ````````````````

To improve query quality, add the following guidance to your base prompt to provide the model with common tips for generating effective MongoDB queries:

Chain of Thought ````````````````

You can prompt the model to "think out loud" before generating the response to improve response quality. This technique, called [chain of thought](https://www.promptingguide.ai/techniques/cot)_ prompting, improves performance but increases generation time and costs.

To encourage the model to think step-by-step before generating the query, add the following text to your base prompt:

### Include Sample Documents

To significantly improve query quality, include a few representative sample documents from your collection. Two to three representative documents typically provide the model with sufficient context about the data structure.

When providing sample documents, follow these guidelines:

- Use the `BSON.EJSON.serialize() <mongosh-ejson>` function to convert BSON documents to EJSON strings
for the prompt.

- Truncate long fields or deeply nested objects.
- Exclude long string values.
- For large arrays, like vector embeddings, include only a few elements.
### Best Practices

Apply the following prompting best practices for specific use cases when generating MongoDB queries from natural language.

Include Index Information `````````````````````````

Include collection indexes in your prompt to encourage the LLM to generate more performant queries. MongoDB drivers and :binary:`mongosh` provide methods to get index information. For example, the Node.js driver provides the :driver:`listIndexes() </node/current/indexes/>` method to get indexes for your prompt.

Time-Based Queries ``````````````````

Most LLM tools include the date in their system prompt. However, if you're using an LLM out of the box, the model does not know the current date or time. Therefore, when working with base models or building your own natural language to MongoDB tools, include the latest date in your prompt. Use the method for your programming language to get the current date as a string such as JavaScript's `new Date().toString()` or Python's `str(datetime.now())`.

Annotated Database Schemas ``````````````````````````

Include annotated schemas of relevant database collections in your prompt. While no single representation method works best for all LLMs, some approaches are more effective than others.

We recommend representing collections using programming language-native types that describe data shape, such as TypeScript Types, Python Pydantic models, or Go structs. If you use MongoDB from these languages, you likely have the data shape defined already. To guide the LLM and reduce ambiguity, add comments to your prompt to describe each field.

The following example shows a TypeScript type for the `sample_mflix.movies` collection:

## Prompt Template

The following example demonstrates a complete prompt using the strategies described on this page for generating :binary:`mongosh` code from natural language.

### Base Prompt Example

Use the following system prompt example as a template for your MongoDB query generation tasks. The sample prompt includes the following components:

- Task overview and expected output format
- General MongoDB query authoring `guidance <natural-language-general-guidance>`
> **Note:** You might also add the `chain-of-thought prompt <natural-language-cot>`
to encourage step-by-step thinking before code generation.

### User Message Template

Then, use the following user message template to provide the model with the necessary context about your database and your desired query:
