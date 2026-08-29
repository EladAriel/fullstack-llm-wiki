---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/integrations/ollama/javascript.mdx"
source_commit: "607c855f787d6cc66e83692874bf90f880a08d62"
source_commit_short: "607c855"
source_commit_date: "2026-08-25T19:59:29-04:00"
generated_at: "2026-08-29T09:39:42.355544Z"
---
---
title: "Ollama Javascript Integration"
sidebarTitle: "JavaScript"
description: "Use Helicone's JavaScript SDK to log your Ollama usage."
"twitter:title": "Anthropic JavaScript SDK Integration - Helicone OSS LLM Observability"
icon: "js"
iconType: "solid"
---

import LegacyWarning from "/snippets/legacy-provider-warning.mdx";

<LegacyWarning />

# Using the Helicone SDK (recommended)

## Walkthrough: logging chat completions

<Steps>
     <Step title="To get started, install the `@helicone/helpers` package">
     ```bash
     npm install @helicone/helpers
     ```
     </Step>
     <Step title="Setup the logger">
     ```typescript
       import { HeliconeManualLogger } from "@helicone/helpers";

       const logger = new HeliconeManualLogger({
         apiKey: process.env.HELICONE_API_KEY
       });
     ```
     </Step>
     <Step title="Call your LLM and log the request">
     ```typescript
     const reqBody = {
       model: "phi3:mini",
       messages: [{
          role: "user",
          content: "Why is the sky blue?"
       }],
       stream: false
     }

     const res = await logger.logRequest(reqBody, async (resultRecorder) => {
        const r = await fetch("http://localhost:11434/api/chat", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(reqBody)
        }) 
        
        const resBody = await r.json();
        resultRecorder.appendResult(resBody);
        return resBody;
     })
     ```
     </Step>
     {/* <Step title="Decode and send the logs!">
     ```typescript
       const res = await r.json();
       console.log(res);
       logger.sendLog(res);
     ```
     </Step> */}

     <Step title="Go to the Helicone Requests page and see your request!">
     </Step>

</Steps>

## Example: logging completion request

The above example uses `phi3:mini` model and the `Chat Completion` interface. The same can be done with a regular `completion` request:

```typescript
// ...
const reqBody = {
  model: "llama3.1",
  prompt: "Why is the sky blue?",
  stream: false,
};

const res = await logger.logRequest(reqBody, async (resultRecorder) => {
  const r = await fetch("http://localhost:11434/api/generate", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(reqBody)
  }) 
  
  const resBody = await r.json();
  resultRecorder.appendResult(resBody);
  return resBody;
})
```

# Resources

- See [Logging Custom Models](/getting-started/integration-method/custom) to learn how to log _any_ model.
- [Ollama API Reference](https://github.com/ollama/ollama/blob/main/docs/api.md)
