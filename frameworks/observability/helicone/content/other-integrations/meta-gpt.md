---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/other-integrations/meta-gpt.mdx"
source_commit: "67df07b8d807a960f2e53d9ec2a9c49513ca2379"
source_commit_short: "67df07b"
source_commit_date: "2026-07-21T05:35:38-07:00"
generated_at: "2026-07-25T19:08:22.198383Z"
---
# Meta Gpt

---
title: "MetaGPT Integration"
sidebarTitle: "MetaGPT"
description: "Integrate Helicone with MetaGPT, a multi-agent framework that simulates a software company workflow. Monitor AI-driven software development processes and agent interactions."
"twitter:title": "MetaGPT Integration - Helicone OSS LLM Observability"
---
import LegacyWarning from "/snippets/legacy-provider-warning.mdx";

<LegacyWarning />

## Introduction

MetaGPT is an open-source framework that simulates a software company workflow using multiple AI agents. It transforms one-line requirements into comprehensive software development outputs, including user stories, APIs, and documentation.

Integrating Helicone with MetaGPT allows you to monitor agent interactions and track performance across your AI-driven development process.

## Integration Steps

<Steps>
  <Step title="Create an account + Generate an API Key">
    Log into [helicone](https://www.helicone.ai) or create an account. Once you have an account, you
    can generate an [API key](https://helicone.ai/developer).

    <Note>
      Make sure to generate a [write only API key](helicone-headers/helicone-auth).
    </Note>

  </Step>
  <Step title="Set base_url in the your config file">
You can configure your metagpt `config.yaml` and change the base_url to the following
  <CodeGroup>

```yaml config.yaml
llm:
  api_type: "openai"
  model: "gpt-4-turbo" # or gpt-4o-mini
  base_url: "https://oai.helicone.ai/{HELICONE_API_KEY}/v1"
  api_key: "YOUR_API_KEY"
```

</CodeGroup>

  </Step>

</Steps>

Check out the [MetaGPT](https://github.com/geekan/MetaGPT) GitHub repository for more information and examples.
