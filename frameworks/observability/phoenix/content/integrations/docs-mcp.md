---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/integrations/docs-mcp.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.821847Z"
---
# Docs Mcp

---
title: "Phoenix Docs MCP"
description: "Let AI assistants search and retrieve the Phoenix documentation in real time over MCP."
---

The Phoenix Docs MCP server lets AI assistants search and retrieve Phoenix documentation in real time. It's complementary to the [Remote MCP Server](/docs/phoenix/integrations/remote-mcp) — run it alongside a data server so your assistant can answer questions from the docs as well as your Phoenix instance.

**Server URL:**

```
https://arizeai-433a7140.mintlify.app/mcp
```

Point your client at the server URL above. No authentication is required.

<AccordionGroup>
  <Accordion title="Claude Code">
    <Steps>
      <Step title="Add the Phoenix Docs MCP server">
        ```bash
        claude mcp add --transport http phoenix-docs https://arizeai-433a7140.mintlify.app/mcp
        ```

        Add `--scope user` to make it available in all projects instead of the current directory only.
      </Step>
    </Steps>
  </Accordion>

  <Accordion title="Claude Desktop">
    <Steps>
      <Step title="Add a custom connector">
        Go to **Settings → Connectors → Add custom connector** and enter:

        - **Name**: `Phoenix Docs`
        - **URL**: `https://arizeai-433a7140.mintlify.app/mcp`
      </Step>
    </Steps>
  </Accordion>

  <Accordion title="Cursor">
    <Steps>
      <Step title="Add the Phoenix Docs MCP server">
        Add to `~/.cursor/mcp.json` (or project `.cursor/mcp.json`):

        ```json
        {
          "mcpServers": {
            "phoenix-docs": {
              "url": "https://arizeai-433a7140.mintlify.app/mcp"
            }
          }
        }
        ```
      </Step>
    </Steps>
  </Accordion>

  <Accordion title="VS Code">
    <Steps>
      <Step title="Add the Phoenix Docs MCP server">
        Run `MCP: Add Server` from the Command Palette, or add to `.vscode/mcp.json`:

        ```json
        {
          "servers": {
            "phoenix-docs": {
              "type": "http",
              "url": "https://arizeai-433a7140.mintlify.app/mcp"
            }
          }
        }
        ```
      </Step>
    </Steps>
  </Accordion>

  <Accordion title="Other clients">
    Any client that supports streamable HTTP works. Configure the URL as `https://arizeai-433a7140.mintlify.app/mcp` — no authentication is required.
  </Accordion>
</AccordionGroup>

## Related

<CardGroup cols={2}>
  <Card title="Remote MCP Server" icon="database" href="/docs/phoenix/integrations/remote-mcp">
    Connect assistants to your Phoenix data — traces, datasets, experiments, and prompts.
  </Card>
  <Card title="MCP Overview" icon="plug" href="/docs/phoenix/integrations/mcp">
    Compare the Phoenix MCP servers and pick the right one.
  </Card>
</CardGroup>
