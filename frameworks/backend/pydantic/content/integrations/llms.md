---
type: "Framework Learn Page"
framework: "pydantic"
source_repo: "https://github.com/pydantic/pydantic"
source_branch: "main"
source_path: "docs/integrations/llms.md"
source_commit: "a2a6577d4c329dd574a45dbb01a8feaa16b1ad3d"
source_commit_short: "a2a6577d"
source_commit_date: "2026-07-23T15:38:17Z"
generated_at: "2026-07-25T11:50:12Z"
---

The Pydantic documentation is available in the [llms.txt](https://llmstxt.org/) format.
This format is defined in Markdown and suited for large language models.

Two formats are available:

* [llms.txt](https://pydantic.dev/docs/validation/latest/llms.txt): a file containing a brief description
  of the project, along with links to the different sections of the documentation. The structure
  of this file is described in details in the [format documentation](https://llmstxt.org/#format).
* [llms-full.txt](https://pydantic.dev/docs/validation/latest/llms-full.txt): Similar to the `llms.txt` file,
  but every link content is included. Note that this file may be too large for some LLMs.

As of today, these files *cannot* be natively leveraged by LLM frameworks or IDEs. Alternatively,
a [MCP server](https://modelcontextprotocol.io/) can be implemented to properly parse the `llms.txt`
file.

Where `llms.txt` gives an AI tool the Pydantic *documentation*, the
[Logfire MCP server](https://pydantic.dev/docs/logfire/guides/mcp-server/) gives it your
application's *runtime data*: an agent can query the traces, metrics, and recorded validations from your
own service and, for example, pull up the input behind a [`ValidationError`][pydantic_core.ValidationError]
while it's helping you fix it.
