---
type: "Framework Learn Page"
framework: "Sentry Python"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/python/tracing/instrumentation/automatic-instrumentation.mdx"
source_commit: "8b4e4a23b18ee70f5fdb05bcda48869c10be2f60"
source_commit_short: "8b4e4a2"
source_commit_date: "2026-08-28T22:17:56+00:00"
generated_at: "2026-08-29T09:40:09.046804Z"
---
# Automatic Instrumentation

---
title: Automatic Instrumentation
sidebar_order: 10
supported:
  - python
  - python.aiohttp
  - python.awslambda
  - python.asgi
  - python.celery
  - python.django
  - python.flask
  - python.pyramid
  - python.falcon
  - python.bottle
  - python.rq
  - python.wsgi
description: "Learn what instrumentation automatically captures transactions."
---

Many integrations for popular frameworks automatically capture transactions (or service spans in <PlatformLink to="/tracing/streamed-spans">stream mode</PlatformLink>). If you already have any of the following frameworks set up for Sentry error reporting, you will start to see traces immediately:

- All WSGI-based web frameworks (Django, Flask, Pyramid, Falcon, Bottle)
- Celery
- AIOHTTP web apps
- Redis Queue (RQ)

See the full [list of available integrations](/platforms/python/integrations/).

Spans are instrumented for the following operations within a transaction/service span:

- Database queries that use SQLAlchemy or the Django ORM
- HTTP requests made with HTTPX, requests, the stdlib, AIOHTTP, or pyreqwest
- Spawned subprocesses
- Redis operations

In transaction mode, spans are only created within an existing transaction. If you're not using any of the supported frameworks, you'll need to <PlatformLink to="/tracing/instrumentation/custom-instrumentation/">create transactions manually</PlatformLink>.

Stream mode removes this limitation. Since there are no transactions, any span started without a parent is automatically promoted to a service span (the equivalent of a transaction). You can also force any span to become a service span when starting it by setting its parent to `None`. See <PlatformLink to="/tracing/instrumentation/custom-instrumentation/">Custom Instrumentation</PlatformLink> to learn more.
