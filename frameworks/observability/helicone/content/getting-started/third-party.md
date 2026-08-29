---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/getting-started/third-party.mdx"
source_commit: "607c855f787d6cc66e83692874bf90f880a08d62"
source_commit_short: "607c855"
source_commit_date: "2026-08-25T19:59:29-04:00"
generated_at: "2026-08-29T09:39:42.267239Z"
---
# Third Party

---
title: "3rd party integrations"
---

<Tabs>

<Tab title="LangChain">

Integrating with Langchain is super easy! Just change the base_url

```ini
export OPENAI_API_BASE="https://oai.helicone.ai/v1"
python3 you_lang_chain_program.py
```

</Tab>

<Tab title="gpt_index">

Since GPT Index uses lang chain under the hood, you can use the same technique
to integrate as well

```ini
export OPENAI_API_BASE="https://oai.helicone.ai/v1"
python3 you_lang_chain_program.py
```

</Tab>

<Tab title="Fabius">

[Fabius](https://github.com/fabiustech/openai) now supports Helicone

```go
package main

import "github.com/fabiustech/openai"

func main() {
	var client = openai.NewClient("your token")
	client.SetBaseURL("https://oai.helicone.ai/v1")

	// Your code goes here!
}
```

</Tab>

</Tabs>
