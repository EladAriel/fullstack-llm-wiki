---
type: "Framework Learn Page"
framework: "Sentry Python"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/python/integrations/gql/index.mdx"
source_commit: "8b4e4a23b18ee70f5fdb05bcda48869c10be2f60"
source_commit_short: "8b4e4a2"
source_commit_date: "2026-08-28T22:17:56+00:00"
generated_at: "2026-08-29T09:40:09.050051Z"
---
# Index

---
title: GQL
description: GQL GraphQL client integration
---

The [GQL](https://gql.readthedocs.io/en/stable/) integration allows you to monitor all GraphQL requests that your Python application makes using the `gql` library. Specifically, this integration reports every [`TransportQueryError`](https://gql.readthedocs.io/en/latest/modules/transport_exceptions.html#gql.transport.exceptions.TransportQueryError) to Sentry and provides additional context including:

- The URL the request was made to
- The GraphQL query which caused the error
- The `errors` information that the GraphQL server returns

## Install

Make sure you have the latest version of the Sentry SDK installed:

```bash {tabTitle:pip}
pip install "sentry-sdk"
```
```bash {tabTitle:uv}
uv add "sentry-sdk"
```

## Configure

If you have the `gql` package in your dependencies, the GQL integration will be enabled automatically when you initialize the Sentry SDK.

<PlatformContent includePath="getting-started-config" />

## Data Privacy and the GQL Integration

To ensure data privacy, the SDK avoids sending any information that may potentially contain personally identifiable information (PII) by default. See the docs for the [`send_default_pii` flag](/platforms/python/configuration/options/#send-default-pii) for more information.

For the GQL integration, this policy means that the SDK **doesn't send** the GraphQL queries and the `errors` information that the GraphQL server returns, unless you override the default configuration via the `send_default_pii` flag.

<Alert level="warning">

Before enabling the `send_default_pii` flag, ensure you've configured Sentry's [sensitive data scrubbing](/platforms/python/data-management/sensitive-data/) tools to scrub all PII.

</Alert>

To have Sentry record the GraphQL queries and the `errors` information returned by the GraphQL server, add the following to your SDK init:

```python
sentry_sdk.init(
    # ...
    # Add data like request headers and IP for users, if applicable;
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
)
```
