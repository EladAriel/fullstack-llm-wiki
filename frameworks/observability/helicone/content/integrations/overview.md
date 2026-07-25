---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/integrations/overview.mdx"
source_commit: "67df07b8d807a960f2e53d9ec2a9c49513ca2379"
source_commit_short: "67df07b"
source_commit_date: "2026-07-21T05:35:38-07:00"
generated_at: "2026-07-25T19:08:22.191125Z"
---
# Overview

---
title: "Legacy Integrations"
sidebarTitle: "Overview"
description: "Legacy proxy-based integrations for existing codebases"
---

<Warning>
  These integration methods are maintained but no longer actively developed. For new projects and the best experience, use our [AI Gateway](/gateway/overview) with unified API access to 100+ models.
</Warning>

## What Are Legacy Integrations?

Legacy proxy-based integrations that add Helicone observability by changing your base URL:

- **OpenAI**: `api.openai.com` → `oai.helicone.ai`
- **Anthropic**: `api.anthropic.com` → `anthropic.helicone.ai`
- **Others**: Provider-specific proxy endpoints

You keep using your existing SDK and code — just point to our proxy URL and add a Helicone-Auth header.

## Why We Built the AI Gateway

These provider-specific proxies have limitations:

- **No automatic fallbacks** - If OpenAI goes down, your app goes down
- **Can't switch providers easily** - Each provider needs different code
- **Multiple endpoints to manage** - Different proxy for each provider
- **No unified routing** - Can't optimize for cost or latency across providers

The [AI Gateway](/gateway/overview) solves these problems with one unified API that routes to 100+ models with automatic fallbacks, intelligent routing, and zero markup.

## When to Use Legacy Integrations

Only use these if:

- **Existing production code** - You have a large codebase built with provider-specific SDKs and refactoring would be costly
- **Native SDK features** - You need specific features only available in the native SDK (rare)

Otherwise, use the [AI Gateway](/gateway/overview) for better reliability, flexibility, and features.

## How to Migrate to AI Gateway

Ready to switch to the unified API? It's simple:

```typescript
// Before: Provider-specific proxy
const client = new OpenAI({
  baseURL: "https://oai.helicone.ai/v1",
  apiKey: process.env.OPENAI_API_KEY,
  defaultHeaders: { "Helicone-Auth": `Bearer ${process.env.HELICONE_API_KEY}` }
});

// After: AI Gateway
const client = new OpenAI({
  baseURL: "https://ai-gateway.helicone.ai",
  apiKey: process.env.HELICONE_API_KEY, // Just your Helicone key
});

// Now access any model: gpt-4o, claude-sonnet-4, gemini-2.0-flash, etc.
```

See the [AI Gateway migration guide](/blog/migration-openrouter) for full details.

