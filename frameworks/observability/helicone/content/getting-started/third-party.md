---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/getting-started/third-party.mdx"
source_commit: "67df07b8d807a960f2e53d9ec2a9c49513ca2379"
source_commit_short: "67df07b"
source_commit_date: "2026-07-21T05:35:38-07:00"
generated_at: "2026-07-25T19:08:22.200882Z"
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
