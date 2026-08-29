---
type: "Framework Learn Page"
framework: "Sentry JavaScript (React)"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/javascript/guides/react/features/tanstack-router.mdx"
source_commit: "8b4e4a23b18ee70f5fdb05bcda48869c10be2f60"
source_commit_short: "8b4e4a2"
source_commit_date: "2026-08-28T22:17:56+00:00"
generated_at: "2026-08-29T09:40:04.521620Z"
---
# Tanstack Router

---
title: TanStack Router
description: "Learn about Sentry's TanStack Router integration."
---

The TanStack Router integration is included in the `@sentry/react` package and is compatible with version `1.64.0` of `@tanstack/react-router` and above.

<Alert title="Note">

The TanStack Router integration is designed to work with Sentry Tracing. Please see <PlatformLink to="/tracing/#enable-tracing">Getting Started with React Performance</PlatformLink> for more details on how to set up and install the SDK.

</Alert>

The TanStack Router instrumentation uses your TanStack Router routes to create `pageload/navigation` transactions to ensure you collect meaningful performance data about the health of your page loads and associated requests.

## Usage

To use the TanStack Router integration, pass the `Sentry.tanstackRouterBrowserTracingIntegration` inside your `integrations` option:

```javascript
import * as Sentry from "@sentry/react";
import { createRouter } from "@tanstack/react-router";

const router = createRouter({
  // Your router options...
});

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [Sentry.tanstackRouterBrowserTracingIntegration(router)],

  // Setting a sample rate is required for sending performance data.
  // We recommend adjusting this value in production, or using tracesSampler
  // for finer control.
  tracesSampleRate: 1.0,
});
```

## Next Steps:

- [Return to **Getting Started**](../../)
- [Return to the main integrations page](../)
