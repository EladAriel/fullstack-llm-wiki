---
type: "Framework Learn Page"
framework: "Langfuse"
source_repo: "https://github.com/langfuse/langfuse-docs"
source_branch: "main"
source_path: "content/docs/evaluation/agentic-access.mdx"
source_commit: "ba26344559edee69ba55c5d3aa80e632f56c1626"
source_commit_short: "ba26344"
source_commit_date: "2026-08-29T02:57:18+00:00"
generated_at: "2026-08-29T09:38:37.747886Z"
---
---
title: Agentic access
sidebarTitle: Agent Access
description: Let AI agents work with scores, datasets, experiments, evaluators, and annotation queues through the Agent Skill, CLI, or MCP server.
---

# Agentic access to evaluation

AI agents can help investigate quality issues and operate evaluation workflows in Langfuse. There are different ways for agents to access your data:

import AgenticAccessMethods from "@/components-mdx/agentic-access-methods.mdx";
import { ManualGuideList } from "@/components/academy/ManualGuideList";

<AgenticAccessMethods />

## Example workflows

Ask your agent to:

- Find low-scoring observations and add representative examples to a dataset
- Create or update score configurations and record scores
- Review experiment results and identify regressions
- Set up evaluators and evaluation rules
- Create and manage annotation queues for human review

## Work across Langfuse

Agents can also [investigate production behavior](/docs/observability/features/agentic-access) and [manage prompts](/docs/prompt-management/features/agentic-access) in Langfuse.

<ManualGuideList
  title="Related guides and blog posts"
  guides={[
    {
      href: "/guides/llm-as-a-judge-calibration-skill",
      topic: "Calibrate LLM-as-a-judge with the Langfuse skill",
      lede: "Use an agent-guided workflow to compare an evaluator with human labels and improve its prompt.",
    },
    {
      href: "/blog/2026-02-26-evaluate-ai-agent-skills",
      topic: "Evaluating AI Agent Skills",
      lede: "See how Langfuse datasets, tracing, and an agent SDK can be used to iteratively evaluate and improve a skill.",
    },
    {
      href: "/guides/videos/headless-langfuse",
      topic: "Headless Langfuse from your coding agent",
      lede: "Analyze production traces, build a dataset, and configure evaluations without leaving your coding agent.",
    },
  ]}
/>
