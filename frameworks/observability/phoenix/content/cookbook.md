---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/cookbook.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.817728Z"
---
# Cookbook

---
title: "Cookbooks"
description: "Cookbooks & tutorials to help you build with Phoenix"
---
## Getting started with Phoenix

Not sure where to start? Try an end-to-end tutorial for a guided walkthrough of Phoenix's core features. These tutorials cover tracing, evaluation, and experimentation:

<Columns cols={2}>
  <Card 
    title="Python Walkthrough" 
    href="/docs/phoenix/cookbook/ai-engineering-workflows/iterative-evaluation-and-experimentation-workflow-python"
    img="https://storage.googleapis.com/arize-assets/dev-rel/Image%20Assets%20Public/python-logo.png"
  />
  <Card 
    title="TypeScript Walkthrough" 
    href="/docs/phoenix/cookbook/ai-engineering-workflows/iterative-evaluation-and-experimentation-workflow-typescript"
    img="https://storage.googleapis.com/arize-assets/dev-rel/Image%20Assets%20Public/ts-logo.png"
  />
</Columns>


## Featured AI Engineering Workflows

Discover workflows that illustrate how teams use Phoenix to build, evaluate, and scale AI systems.

<Columns cols={3}>
  <Card 
    title="Optimizing Coding Agent Prompts - Prompt Learning" 
    href="/docs/phoenix/cookbook/prompt-engineering/optimizing-coding-agent-prompts-prompt-learning"
    img="https://storage.googleapis.com/arize-phoenix-assets/assets/images/optimizing-coding-agent-prompt.png"
  />
  <Card 
    title="Aligning LLM Evals with Human Feedback" 
    href="/docs/phoenix/cookbook/human-in-the-loop-workflows-annotations/aligning-llm-evals-with-human-annotations-typescript"
    img="https://storage.googleapis.com/arize-phoenix-assets/assets/images/aligning-evals-with-feedback.png"
  />
  <Card 
    title="Write your First Custom LLM Eval" 
    href="/docs/phoenix/cookbook/evaluation/creating-a-custom-llm-evaluator-with-a-benchmark-dataset"
    img="https://storage.googleapis.com/arize-phoenix-assets/assets/images/build-custom-eval.png"
  />
</Columns>

## Agent Demos

These example agents are fully instrumented with OpenInference and utilize end-to-end tracing with Phoenix for comprehensive performance analysis. Enter your Phoenix and OpenAI keys to view traces.

<Columns cols={3}>
  <Card 
    title="Code Generation Agent" 
    href="https://phoenix-code-gen-agent.onrender.com/"
    img="https://storage.googleapis.com/arize-phoenix-assets/assets/images/agent-demos-code-gen.png"
  >
    Explore a Code Generator Copilot Agent designed to generate, optimize, and validate code.
  </Card>
  <Card 
    title="RAG Agent" 
    href="https://phoenix-rag-agent.onrender.com/"
    img="https://storage.googleapis.com/arize-phoenix-assets/assets/images/agent-demos-rag-agent.png"
  >
    Enter a source URL and collect traces in Phoenix to see how a RAG Agent can retrieve and generate accurate responses.
  </Card>
  <Card 
    title="Computer Use Agent" 
    href="https://github.com/Arize-ai/phoenix/tree/main/examples/computer_use_agent"
    img="https://storage.googleapis.com/arize-phoenix-assets/assets/images/agent-demos-computer-use.png"
  >
    Test out a Computer Use (Operator) Agent built to execute commands, edit files, and manage system operations.
  </Card>
</Columns>