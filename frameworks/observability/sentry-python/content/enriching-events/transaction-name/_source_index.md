---
type: "Framework Learn Page"
framework: "Sentry Python"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/python/enriching-events/transaction-name/index.mdx"
source_commit: "8b4e4a23b18ee70f5fdb05bcda48869c10be2f60"
source_commit_short: "8b4e4a2"
source_commit_date: "2026-08-28T22:17:56+00:00"
generated_at: "2026-08-29T09:40:09.043241Z"
---
# Index

---
title: Transaction Name
description: "Learn how to set or override the transaction name to capture the user and gain critical pieces of information that construct a unique identity in Sentry."
---

The current transaction name is used to group transactions in our
[pre-built Sentry Dashboards](/product/dashboards/sentry-dashboards/) product, as well as annotate error events with their point of failure.

The transaction name can reference the current web app route, or the current
task being executed. For example:

- `GET /api/{version}/users/`
- `UserListView`
- `myapp.tasks.renew_all_subscriptions`

Ideally, the transaction name does not contain variable values such as user
IDs but has rather low cardinality while still uniquely identifying a piece of
code you care about.

A lot of our framework integrations already set a transaction name, though you can set one yourself.

To override the name of the currently running transaction:

<PlatformContent includePath="enriching-events/set-transaction-name" />

Please refer to [the tracing documentation](../../tracing/) for how to start and stop transactions.
