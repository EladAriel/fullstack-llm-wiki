---
type: "Framework Learn Page"
framework: "Sentry JavaScript (React)"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/javascript/guides/react/features/react-router/index.mdx"
source_commit: "8b4e4a23b18ee70f5fdb05bcda48869c10be2f60"
source_commit_short: "8b4e4a2"
source_commit_date: "2026-08-28T22:17:56+00:00"
generated_at: "2026-08-29T09:40:04.522955Z"
---
# Index

---
title: React Router
description: "Learn about Sentry's React Router integration."
---

_(Available in version 5.21.0 and above)_

React Router support is included in the `@sentry/react` package since version `5.21.0`.

<Alert title="Note">

The React Router integration is designed to work with Sentry Tracing. Please see [Set Up Tracing with React](/platforms/javascript/guides/react/tracing/) for more details on how to set up and install the SDK.

</Alert>

The React Router instrumentation uses the React Router library to create `pageload/navigation` transactions to ensure you collect meaningful performance data about the health of your page loads and associated requests.

We support integrations for React Router 3, 4, 5, 6, 7, and 8.



<PageGrid />
