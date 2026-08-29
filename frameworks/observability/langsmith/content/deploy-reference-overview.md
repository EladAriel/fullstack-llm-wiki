---
type: "Framework Learn Page"
framework: "LangSmith"
source_repo: "https://github.com/langchain-ai/docs.git"
source_branch: "main"
source_path: "src/langsmith/deploy-reference-overview.mdx"
source_commit: "a174f9cf7c91ee5eb14ee2382eb48bfe6e4956e9"
source_commit_short: "a174f9c"
source_commit_date: "2026-08-28T17:04:12-07:00"
generated_at: "2026-08-29T09:39:50.676406Z"
---
# Deploy Reference Overview

---
title: Reference
sidebarTitle: Overview
mode: "wide"
description: Reference for the LangSmith Deployment SDKs, CLI, and APIs for deploying and interacting with agents.
---

This section is a reference for the SDKs, CLI, and APIs you use to deploy and interact with agents on the [Agent Server](/langsmith/agent-server) runtime.

## SDKs and CLI

<CardGroup cols={1}>

<Card title="LangSmith Deployments SDK" icon="package" href="/langsmith/smith-deployments-sdk">
Management of LangSmith deployments and revisions using the LangGraph SDK.
</Card>

</CardGroup>

<CardGroup cols={2}>

<Card title="LangGraph CLI" icon="terminal" href="/langsmith/cli">
Build, deploy, and interact with agents from the command line.
</Card>

<Card title="RemoteGraph" icon="git-merge" href="/langsmith/remote-graph">
Client-side interface for calling deployed graphs as if they were local.
</Card>

</CardGroup>

## APIs

<CardGroup cols={2}>

<Card title="Agent Server API" icon="server" href="/langsmith/server-api-ref">
REST endpoints exposed by the Agent Server runtime: assistants, threads, runs, cron jobs, and the long-term memory store.
</Card>

<Card title="Control Plane API" icon="settings" href="/langsmith/api-ref-control-plane">
REST endpoints for managing deployments, revisions, and listeners.
</Card>

</CardGroup>

## Releases

<CardGroup cols={1}>

<Card title="Agent Server changelog" icon="versions" href="/langsmith/agent-server-changelog">
Version history and release notes for the Agent Server runtime.
</Card>

</CardGroup>
