---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/datasets-and-experiments/how-to-datasets/exporting-datasets.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.876357Z"
---
# Exporting Datasets

---
title: "Exporting Datasets"
---

## Exporting to CSV

Want to just use the contents of your dataset in another context? Simply click on the export to CSV button on the dataset page and you are good to go!

## Exporting for Fine-Tuning

Fine-tuning lets you get more out of the models available by providing:

* Higher quality results than prompting

* Ability to train on more examples than can fit in a prompt

* Token savings due to shorter prompts

* Lower latency requests

Fine-tuning improves on few-shot learning by training on many more examples than can fit in the prompt, letting you achieve better results on a wide number of tasks. **Once a model has been fine-tuned, you won't need to provide as many examples in the prompt.** This saves costs and enables lower-latency requests. Phoenix natively exports OpenAI Fine-Tuning JSONL as long as the dataset contains compatible inputs and outputs.

## Exporting OpenAI Evals

Evals provide a framework for evaluating large language models (LLMs) or systems built using LLMs. OpenAI Evals offer an existing registry of evals to test different dimensions of OpenAI models and the ability to write your own custom evals for use cases you care about. You can also use your data to build private evals. Phoenix can natively export the OpenAI Evals format as JSONL so you can use it with OpenAI Evals. See [https://github.com/openai/evals](https://github.com/openai/evals) for details.

## Exporting via CLI

The [Phoenix CLI](/docs/phoenix/sdk-api-reference/typescript/arizeai-phoenix-cli) (`@arizeai/phoenix-cli`) provides command-line access to datasets and experiments:

```bash
npx @arizeai/phoenix-cli dataset get my-dataset --file dataset.json
npx @arizeai/phoenix-cli experiment list --dataset my-dataset ./experiments/
```

The CLI integrates with AI coding assistants like [Claude Code](https://claude.com/product/claude-code), [Cursor](https://cursor.sh), and [Windsurf](https://codeium.com/windsurf)—ask them to fetch and analyze your Phoenix data directly.

<CardGroup cols={2}>
  <Card title="Phoenix CLI Reference" icon="terminal" href="/docs/phoenix/sdk-api-reference/typescript/arizeai-phoenix-cli">
    Complete CLI documentation with all commands and options
  </Card>
  <Card title="TypeScript Client" icon="code" href="/docs/phoenix/sdk-api-reference/typescript/arizeai-phoenix-client">
    Programmatic access via the TypeScript SDK
  </Card>
</CardGroup>
