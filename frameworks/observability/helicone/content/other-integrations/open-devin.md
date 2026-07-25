---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/other-integrations/open-devin.mdx"
source_commit: "67df07b8d807a960f2e53d9ec2a9c49513ca2379"
source_commit_short: "67df07b"
source_commit_date: "2026-07-21T05:35:38-07:00"
generated_at: "2026-07-25T19:08:22.199107Z"
---
# Open Devin

---
title: "Open Devin Integration"
sidebarTitle: "Open Devin"
description: "Integrate Helicone with Open Devin, an AI-powered platform for autonomous software engineering. Monitor interactions between AI agents and human developers in your projects."
"twitter:title": "Open Devin Integration - Helicone OSS LLM Observability"
---
import LegacyWarning from "/snippets/legacy-provider-warning.mdx";

<LegacyWarning />

## Introduction

Open Devin is a platform for AI-powered autonomous software engineering. It enables AI agents to collaborate with human developers to write code, fix bugs, and ship features. Integrating Helicone with Open Devin allows you to monitor and analyze these AI-human interactions throughout the development process.

## Integration Steps

<Steps>
  <Step title="Create an account + Generate an API Key">
    Log into [helicone](https://www.helicone.ai) or create an account. Once you have an account, you
    can generate an [API key](https://helicone.ai/developer).

    <Note>
      Make sure to generate a [write only API key](helicone-headers/helicone-auth).
    </Note>

  </Step>
  <Step title="Set OPENAI_API_BASE as an environment variable when running the container">

  <CodeGroup>

```bash example
export HELICONE_API_KEY=pk-<YOUR_API_KEY>

docker run -it \
    --pull=always \
    -e SANDBOX_USER_ID=$(id -u) \
    -e OPENAI_API_BASE="https://oai.helicone.ai/${HELICONE_API_KEY}/v1" \
    -e PERSIST_SANDBOX="true" \
    -e SSH_PASSWORD="make something up here" \
    -e WORKSPACE_MOUNT_PATH=$WORKSPACE_BASE \
    -v $WORKSPACE_BASE:/opt/workspace_base \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -p 3000:3000 \
    --add-host host.docker.internal:host-gateway \
    --name opendevin-app-$(date +%Y%m%d%H%M%S) \
    ghcr.io/opendevin/opendevin:0.6
```

</CodeGroup>

  </Step>

</Steps>

Check out the [Open Devin GitHub repository](https://github.com/OpenDevin/OpenDevin) for more information and examples.
