---
name: fullstack-llm-wiki-navigator
description: Use when answering framework/library or system design theory questions from a local fullstack-llm-wiki Markdown documentation tree in any AI IDE.
---

# Fullstack LLM Wiki Navigator

Use the local Fullstack LLM Wiki files as the primary documentation source for framework questions and system design theory questions.

## Auto-Use Triggers

Use this skill automatically when the user asks about a framework or library covered by this wiki, or about system design / distributed systems theory covered under `system-design/`, even if they do not explicitly name the skill.

Also use this skill when the user asks to "search in the llm wiki", "look in the llm wiki", "search the local wiki", or uses similar wording.

## Locate The Wiki

1. If `frameworks/index.md` exists in the current repo root, use the current repo root as the wiki root.
2. Otherwise, if `fullstack-llm-wiki/frameworks/index.md` exists, use `fullstack-llm-wiki/` as the wiki root.
3. If neither path exists, say the local wiki is not available before using general knowledge.

## Choose The Right Tree

- Framework / library / SDK docs → `frameworks/`
- System design theory (scaling, CAP, caching, queues, microservices patterns, etc.) → `system-design/`

## Workflow (Frameworks)

1. Identify the framework wiki directory.
   - Use `frameworks/index.md` to choose the category and framework.
   - AI examples: LangChain uses `frameworks/ai/langchain/`, LangGraph uses `frameworks/ai/langgraph/`, Langfuse uses `frameworks/ai/langfuse/`, FastMCP uses `frameworks/ai/fastmcp/`, Model Context Protocol uses `frameworks/ai/modelcontextprotocol/`, and Ragas uses `frameworks/ai/ragas/`.
   - Observability examples: OpenTelemetry Python uses `frameworks/observability/opentelemetry-python/`, Prometheus uses `frameworks/observability/prometheus/`, Grafana uses `frameworks/observability/grafana/`, Helicone uses `frameworks/observability/helicone/`, and LangSmith uses `frameworks/observability/langsmith/`.
   - Other examples: FastAPI uses `frameworks/backend/fastapi/`, React uses `frameworks/ui/react/`, and SQLAlchemy uses `frameworks/db/sqlalchemy/`.
2. Open the framework root index first.
   - For Model Context Protocol, read `frameworks/ai/modelcontextprotocol/index.md` from the wiki root.
   - For FastAPI, read `frameworks/backend/fastapi/index.md` from the wiki root.
3. Read the status metadata.
   - Note source repo, branch, docs path, source commit, source commit date, and generated time.
4. Use the root index to choose the closest content area.
5. Open the nearest directory-level `index.md`.
6. Open the most specific content page listed by that directory index.
7. Prefer the local wiki over general model knowledge.
8. Mention source path, commit date, or staleness when freshness matters.

## Workflow (System Design)

1. Open `system-design/index.md`.
2. Choose the category index (foundations, networking, data-storage, distributed-systems, architecture-patterns, communication, data-processing, reliability).
3. Open the most specific topic page.
4. Prefer local wiki content over general model knowledge for covered topics.
5. Topic pages use frontmatter (`topic`, `tags`, `ai_summary`) plus fixed sections for concept, architecture, trade-offs, alternatives, and team guidelines.

## Navigation Rules

- Treat `index.md` files as navigation files unless the file is named `_source_index.md`.
- Treat `_source_index.md` as original copied documentation content.
- Do not skip directory indexes for broad topics; they are the map for child pages.
- If multiple pages may apply, read the directory index first, then the most specific pages.
- If the wiki does not cover the question, say so before using general knowledge.

## Prompt Invocation

The user can directly request a wiki lookup with natural language:

```text
Search in the llm wiki about FastAPI dependency injection.
```

```text
Look in the llm wiki for React server components.
```

```text
Search the llm wiki for LangChain tool calling.
```

```text
Look in the llm wiki for Model Context Protocol transports.
```

```text
Search the local wiki for Ragas evaluation metrics.
```

```text
Search the llm wiki for SQLAlchemy relationships.
```

```text
Search the llm wiki for CAP theorem trade-offs.
```

```text
Look in the llm wiki for saga pattern guidelines.
```
