---
type: "Framework Learn Page"
framework: "Sentry Python"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/python/tracing/instrumentation/automatic-instrumentation.mdx"
source_commit: "8557ccbd46b02c43301ef74ff54516736ecf9d69"
source_commit_short: "8557ccb"
source_commit_date: "2026-07-24T13:12:02-04:00"
generated_at: "2026-07-25T19:08:13.534293Z"
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

Many integrations for popular frameworks automatically capture transactions. If you already have any of the following frameworks set up for Sentry error reporting, you will start to see traces immediately:

- All WSGI-based web frameworks (Django, Flask, Pyramid, Falcon, Bottle)
- Celery
- AIOHTTP web apps
- Redis Queue (RQ)

See the full [list of available integrations](/platforms/python/integrations/).

Spans are instrumented for the following operations within a transaction:

- Database queries that use SQLAlchemy or the Django ORM
- HTTP requests made with HTTPX, requests, the stdlib, AIOHTTP, or pyreqwest
- Spawned subprocesses
- Redis operations

Spans are only created within an existing transaction. If you're not using any of the supported frameworks, you'll need to <PlatformLink to="/tracing/instrumentation/custom-instrumentation/">create transactions manually</PlatformLink>.
