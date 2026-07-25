---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/getting-started/how-to-integrate.mdx"
source_commit: "67df07b8d807a960f2e53d9ec2a9c49513ca2379"
source_commit_short: "67df07b"
source_commit_date: "2026-07-21T05:35:38-07:00"
generated_at: "2026-07-25T19:08:22.201755Z"
---
# How To Integrate

---
title: "How to integrate"
description: "Integrate Helicone today with one line of code"
---

<Tabs>

<Tab title="Curl" >

Replace the OpenAI base url

```bash
POST https://api.openai.com/v1
```

with Helicone's

```
POST https://oai.helicone.ai/v1
```

</Tab>

<Tab title="Python" >

Change the default base API url to Helicone's

```py
import openai

openai.api_base = "https://oai.helicone.ai/v1"
```

</Tab>

<Tab title="Node.js" >

Add a `basePath` to the `Configuration:`

Before:

```js
import { Configuration, OpenAIApi } from "openai";

const configuration = new Configuration({
  apiKey: process.env.OPENAI_API_KEY,
});

const openai = new OpenAIApi(configuration);
```

After:

```js
import { Configuration, OpenAIApi } from "openai";

const configuration = new Configuration({
  apiKey: process.env.OPENAI_API_KEY,
  basePath: "https://oai.helicone.ai/v1",
});

const openai = new OpenAIApi(configuration);
```

</Tab>

</Tabs>

By using our API, you agree to our
[Privacy Policy](https://www.helicone.ai/privacy) and
[Terms of Services](https://www.helicone.ai/terms) agreements.

Once you've integrated,
[**head on to onboarding**](https://www.helicone.ai/onboarding) to get into your
dashboard 🏡
