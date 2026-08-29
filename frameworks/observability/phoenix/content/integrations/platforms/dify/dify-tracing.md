---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/integrations/platforms/dify/dify-tracing.mdx"
source_commit: "c48e50e9906fcc56c1c103ebd93ef3c95ed6b6e7"
source_commit_short: "c48e50e"
source_commit_date: "2026-08-29T01:45:20-06:00"
generated_at: "2026-08-29T09:39:58.940641Z"
---
# Dify Tracing

---
title: "Dify Tracing"
description: Configure your Dify application to view traces in Phoenix
---

import StartPhoenix from "../../../../snippets/start-phoenix.mdx";
import PhoenixAuthNote from "../../../../snippets/phoenix-auth-note.mdx";

## Launch Phoenix

<StartPhoenix />

Dify connects to Phoenix over the network, so it needs the endpoint you just started — and an API key if the instance requires one.

<PhoenixAuthNote />

## Connect Dify and Phoenix

To configure Phoenix tracing in your Dify application:

1. Open the Dify application you want to monitor.

2. In the left sidebar, navigate to **Monitoring**.

3. On the Monitoring page, select Phoenix in the Tracing drop down to begin setup.

4. Enter your Phoenix credentials and save. You can verify the monitoring status on the current page.

<Frame>
  <iframe src="https://cdn.iframe.ly/JC08HhsU" allowFullScreen className="aspect-video"></iframe>
</Frame>

## Observe

View Dify traces in Phoenix. Get rich details into tool calls, session data, workflow steps, and more.

<Frame>
![](https://storage.googleapis.com/arize-phoenix-assets/assets/images/phoenix-dify-traces.png)
</Frame>

## Resources

* Learn more details about the tracing data captured in the [Dify documentation](https://docs.dify.ai/en/guides/monitoring/integrate-external-ops-tools/integrate-phoenix)


