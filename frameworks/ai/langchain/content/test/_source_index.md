---
type: "Framework Learn Page"
framework: "LangChain"
source_repo: "https://github.com/langchain-ai/docs"
source_branch: "main"
source_path: "src/oss/langchain/test/index.mdx"
source_commit: "d037cd23f3f298721837c403b2ffd289e31d56d0"
source_commit_short: "d037cd23"
source_commit_date: "2026-06-23T11:18:55+02:00"
generated_at: "2026-06-23T13:53:33Z"
generated_filename: "_source_index.md"
---

---
title: Test
sidebarTitle: Overview
description: Strategies for testing LangChain agents, including unit tests, integration tests, and trajectory evaluations.
---

Agentic applications let an LLM decide its own next steps to solve a problem. That flexibility is powerful, but the model's black-box nature makes it hard to predict how a tweak in one part of your agent will affect the whole. To build production-ready agents, thorough testing is essential.

There are a few approaches to testing your agents:

- **Unit tests** exercise small, deterministic pieces of your agent in isolation using in-memory fakes so you can assert exact behavior quickly and deterministically.
- **Integration tests** test the agent using real network calls to confirm that components work together, credentials and schemas line up, and latency is acceptable.
- **Evals** use evaluators to assess your agent's execution trajectory, either via deterministic matching or an LLM judge.

Agentic applications tend to lean more on integration because they chain multiple components together and must deal with flakiness due to the nondeterministic nature of LLMs.

<Tip>
Run evaluations at scale, track results over time, and compare experiments with [LangSmith](https://smith.langchain.com). See [Evaluate an LLM application](/langsmith/evaluate-llm-application) to get started.
</Tip>

<CardGroup cols={1}>
    <Card title="Unit testing" icon="flask" href="/oss/langchain/test/unit-testing" arrow>
        Mock chat models and use in-memory persistence to test agent logic without API calls.
    </Card>
    <Card title="Integration testing" icon="plug" href="/oss/langchain/test/integration-testing" arrow>
        Test your agent with real LLM APIs. Organize tests, manage keys, handle flakiness, and control costs.
    </Card>
    <Card title="Evals" icon="scale" href="/oss/langchain/test/evals" arrow>
        Evaluate agent trajectories with deterministic matching or LLM-as-judge evaluators.
    </Card>
</CardGroup>
