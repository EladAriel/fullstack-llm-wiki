---
type: "Framework Learn Page"
framework: "Sentry Python"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/python/tracing/distributed-tracing/dealing-with-cors-issues/index.mdx"
source_commit: "8b4e4a23b18ee70f5fdb05bcda48869c10be2f60"
source_commit_short: "8b4e4a2"
source_commit_date: "2026-08-28T22:17:56+00:00"
generated_at: "2026-08-29T09:40:09.049528Z"
---
# Index

---
title: Dealing with CORS Issues
sidebar_order: 80
---

If your frontend and backend are hosted on different domains (for example, your frontend is on `https://example.com` and your backend is on `https://api.example.com`), and the frontend does XHR/fetch requests to your backend, you'll need to configure your backend [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Headers) headers to ensure requests aren't blocked.

Configure your backend CORS to allow the `sentry-trace` and `baggage` headers.

Your server's response header configuration might look like: `"Access-Control-Allow-Headers: sentry-trace, baggage"`. Your configuration will be specific to your setup.
