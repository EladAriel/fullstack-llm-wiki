---
type: "Framework Learn Page"
framework: "LangSmith"
source_repo: "https://github.com/langchain-ai/docs.git"
source_branch: "main"
source_path: "src/langsmith/components.mdx"
source_commit: "a174f9cf7c91ee5eb14ee2382eb48bfe6e4956e9"
source_commit_short: "a174f9c"
source_commit_date: "2026-08-28T17:04:12-07:00"
generated_at: "2026-08-29T09:39:50.658799Z"
---
# Components

---
title: LangSmith Deployment components
sidebarTitle: Overview
mode: wide
description: Overview of Agent Server, LangGraph CLI, Studio, SDKs, RemoteGraph, control plane, and data plane components.
---

A [LangSmith Deployment](/langsmith/deployment) installation includes several key components. Together these tools and services provide a complete solution for building, deploying, and managing graphs (including agentic applications), whether on [Cloud](/langsmith/cloud) or in your own [self-hosted](/langsmith/self-hosted) infrastructure:

```mermaid
flowchart
    subgraph LangSmith Deployment
        A[LangGraph CLI] -->|creates| B(Agent Server deployment)
        B <--> D[Studio]
        B <--> E[SDKs]
        B <--> F[RemoteGraph]
    end

    classDef process fill:#E5F4FF,stroke:#006DDD,stroke-width:2px,color:#030710

    class A,B,D,E,F process
```

- [Agent Server](/langsmith/agent-server): Defines an opinionated API and runtime for deploying graphs and agents. Handles execution, state management, and persistence so you can focus on building logic rather than server infrastructure.
- [LangGraph CLI](/langsmith/cli): A command-line interface to build, package, and interact with graphs locally and prepare them for deployment.
- [Studio](/langsmith/studio): A specialized IDE for visualization, interaction, and debugging. Connects to a local Agent Server for developing and testing your graph.
- [Python/JS SDK](/langsmith/reference): The Python/JS SDK provides a programmatic way to interact with deployed graphs and agents from your applications.
- [RemoteGraph](/langsmith/use-remote-graph): Allows you to interact with a deployed graph as though it were running locally.
- [Control Plane](/langsmith/control-plane): The UI and APIs for creating, updating, and managing Agent Server deployments.
- [Data plane](/langsmith/data-plane): The runtime layer that executes your graphs, including Agent Servers, their backing services (PostgreSQL, Redis, etc.), and the listener that reconciles state from the control plane.
