---
type: "Framework Learn Page"
framework: "Sentry Python"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/python/configuration/filtering/hints.mdx"
source_commit: "8b4e4a23b18ee70f5fdb05bcda48869c10be2f60"
source_commit_short: "8b4e4a2"
source_commit_date: "2026-08-28T22:17:56+00:00"
generated_at: "2026-08-29T09:40:09.045021Z"
---
# Hints

---
title: Hints
sidebar_order: 900
description: "Learn about the different kinds of Event and Breadcrumb `hints`."
---

Event and Breadcrumb `hints` are objects containing various information used to put together an event or a breadcrumb. These hints are passed as the `hint` parameter to `before_send` and `before_breadcrumb` (as well as event processors) as a dictionary. More than one hint can be supplied, but this is rare.

`exc_info`

If you set this hint, then it's an exc info tuple in the form `(exc_type, exc_value, tb)`. This can be used to extract additional information from the original error object.

`log_record`

This hint is passed to breadcrumbs and contains the log record that created it. It can be used to extract additional information from the original `logging` log record that is not extracted by default. Likewise, it can be useful to discard uninteresting breadcrumbs.

`httplib_request`

An `httplib` request object for breadcrumbs created from HTTP requests.
