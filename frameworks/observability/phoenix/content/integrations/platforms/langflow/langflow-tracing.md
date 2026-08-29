---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/integrations/platforms/langflow/langflow-tracing.mdx"
source_commit: "c48e50e9906fcc56c1c103ebd93ef3c95ed6b6e7"
source_commit_short: "c48e50e"
source_commit_date: "2026-08-29T01:45:20-06:00"
generated_at: "2026-08-29T09:39:58.940426Z"
---
---
title: "LangFlow Tracing"
---

## Pull Langflow Repo

Navigate to the Langflow GitHub repo and pull the project down

<Card horizontal icon="github" href="https://github.com/langflow-ai/langflow" title="Not found" description="LangFlow GitHub repository"/>

## Create .env file

Navigate to the repo and create a `.env` file with all the Arize Phoenix variables.

You can use the `.env.example` as a template to create the `.env` file

Add the following environment variable to the `.env` file

```python
# Arize Phoenix Env Variables
PHOENIX_API_KEY="YOUR_PHOENIX_KEY_HERE"
```

## Start Docker Desktop

Start Docker Desktop, build the images, and run the container (this will take around 10 minutes the first time) Go into your terminal into the Langflow directory and run the following commands

```bash highlight={1}
docker compose -f docker/dev.docker-compose.yml down || true
docker compose -f docker/dev.docker-compose.yml up --remove-orphans
```

## Go to Hosted Langflow UI

<Card horizontal href="http://localhost:3000/" >
  http://localhost:3000/
</Card>

## Create a Flow

In this example, we'll use Simple Agent for this tutorial

Add your OpenAI Key to the Agent component in Langflow

Go into the Playground and run the Agent

## Go to Arize Phoenix

Open Phoenix and navigate to your project (its name should match your Langflow Agent name).

## Inspect Traces

AgentExecutor Trace is Arize Phoenix instrumentation to capture what's happening with the LangChain being ran during the Langflow components

The other UUID trace is the native Langflow tracing.


