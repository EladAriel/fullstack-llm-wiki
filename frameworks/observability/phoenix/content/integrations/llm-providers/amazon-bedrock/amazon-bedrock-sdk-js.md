---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/integrations/llm-providers/amazon-bedrock/amazon-bedrock-sdk-js.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.852320Z"
---
# Amazon Bedrock Sdk Js

---
title: "Amazon Bedrock SDK for JavaScript"
description: Instrument and observe AWS Bedrock calls using the AWS SDK for JavaScript
---

This module provides automatic instrumentation for the [AWS SDK for JavaScript Bedrock Runtime Client](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_bedrock_code_examples.html), which may be used in conjunction with [@arizeai/phoenix-otel](https://www.npmjs.com/package/@arizeai/phoenix-otel).

## Install

```bash
npm install @arizeai/openinference-instrumentation-bedrock @aws-sdk/client-bedrock-runtime @arizeai/phoenix-otel
```

## Setup

To instrument your application, use the `register` function from `@arizeai/phoenix-otel` and manually instrument the Bedrock SDK.

Create the `instrumentation.ts` file:

```typescript expandable
import { register } from "@arizeai/phoenix-otel";
import { BedrockRuntimeClient } from "@aws-sdk/client-bedrock-runtime";
import { BedrockInstrumentation } from "@arizeai/openinference-instrumentation-bedrock";

// Initialize Phoenix tracing
const tracerProvider = register({
  projectName: "bedrock-app",
  // If Phoenix is running elsewhere:
  // url: "https://your-phoenix.example.com",
  // apiKey: process.env.PHOENIX_API_KEY,
  // If using self-hosted Phoenix:
  // url: "http://localhost:6006",
});

// Set up Bedrock instrumentation
const instrumentation = new BedrockInstrumentation();
instrumentation.manuallyInstrument(BedrockRuntimeClient);

console.log("Bedrock instrumentation registered");
```

## Run Bedrock

Import the `instrumentation.ts` file first, then use Bedrock as usual.

```typescript expandable
import "./instrumentation.js";
import { BedrockRuntimeClient, InvokeModelCommand } from "@aws-sdk/client-bedrock-runtime";

const client = new BedrockRuntimeClient({ region: "us-east-1" });

async function main() {
  const payload = {
    anthropic_version: "bedrock-2023-05-31",
    max_tokens: 1024,
    messages: [{ role: "user", content: "Write a haiku about clouds." }],
  };

  const command = new InvokeModelCommand({
    modelId: "anthropic.claude-3-sonnet-20240229-v1:0",
    contentType: "application/json",
    body: JSON.stringify(payload),
  });

  const response = await client.send(command);
  const responseBody = JSON.parse(new TextDecoder().decode(response.body));
  console.log(responseBody.content[0].text);
}

main();
```

## Observe

After setting up instrumentation and running your Bedrock application, traces will appear in the Phoenix UI for visualization and analysis.

## Resources

* [NPM Package](https://www.npmjs.com/package/@arizeai/openinference-instrumentation-bedrock)

* [AWS SDK for JavaScript Developer Guide](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_bedrock_code_examples.html)

* [OpenInference package for AWS Bedrock](https://github.com/Arize-ai/openinference/tree/main/js/packages/openinference-instrumentation-bedrock)
