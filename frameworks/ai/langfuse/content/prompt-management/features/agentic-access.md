---
type: "Framework Learn Page"
framework: "Langfuse"
source_repo: "https://github.com/langfuse/langfuse-docs"
source_branch: "main"
source_path: "content/docs/prompt-management/features/agentic-access.mdx"
source_commit: "ba26344559edee69ba55c5d3aa80e632f56c1626"
source_commit_short: "ba26344"
source_commit_date: "2026-08-29T02:57:18+00:00"
generated_at: "2026-08-29T09:38:37.761656Z"
---
---
title: Agentic Prompt Management
sidebarTitle: Agent Access
description: Let AI agents retrieve, create, migrate, and update Langfuse prompts through the Agent Skill, CLI, or MCP server.
---

# Agentic Prompt Management

AI agents can work with your Langfuse prompt library while they edit application code. There are different ways for agents to access your data:

import AgenticAccessMethods from "@/components-mdx/agentic-access-methods.mdx";
import { ManualGuideList } from "@/components/academy/ManualGuideList";

<AgenticAccessMethods />

## Example workflows

Ask your agent to:

- Migrate hardcoded prompts from a codebase to Langfuse
- Retrieve a prompt and compare its latest versions
- Create a new text or chat prompt version
- Promote a tested prompt version by updating its deployment labels

## Work across Langfuse

Agents can also [investigate production behavior](/docs/observability/features/agentic-access) and [run evaluation workflows](/docs/evaluation/agentic-access) in Langfuse.

<ManualGuideList
  title="Related guides and blog posts"
  guides={[
    {
      href: "/blog/2026-02-16-prompt-improvement-claude-skills",
      topic: "Automatically improve prompts with Agent Skills",
      lede: "Use the Langfuse skill to analyze trace feedback and iteratively improve your prompts.",
    },
    {
      href: "/guides/videos/headless-langfuse",
      topic: "Headless Langfuse from your coding agent",
      lede: "Instrument an application, analyze traces, build a dataset, and run evaluations without leaving your coding agent.",
    },
  ]}
/>
