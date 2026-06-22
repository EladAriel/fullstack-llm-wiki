---
type: "Framework Learn Page"
framework: "pydantic"
source_repo: "https://github.com/pydantic/pydantic"
source_branch: "main"
source_path: "docs/integrations/llms.md"
source_commit: "363728fe0b353db1a1fcb44aac5c38fd96a8cc20"
source_commit_short: "363728fe"
source_commit_date: "2026-06-20T11:20:58+01:00"
generated_at: "2026-06-21T11:37:01Z"
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
