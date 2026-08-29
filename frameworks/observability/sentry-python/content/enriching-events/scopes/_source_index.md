---
type: "Framework Learn Page"
framework: "Sentry Python"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/python/enriching-events/scopes/index.mdx"
source_commit: "8b4e4a23b18ee70f5fdb05bcda48869c10be2f60"
source_commit_short: "8b4e4a2"
source_commit_date: "2026-08-28T22:17:56+00:00"
generated_at: "2026-08-29T09:40:09.043795Z"
---
# Index

---
title: Scopes
description: "The SDK will in most cases automatically manage the scopes for you in the framework integrations. Learn what a scope is and how you can use it to your advantage."
---

Scopes store extra data that the SDK adds to your event when sending the event to Sentry. While the SDKs typically manage the scope automatically, understanding how scopes work and how you can manage them manually can be helpful.

## What is a Scope?

A scope manages an event's data. For instance, the SDK stores [contexts](../context/) and [breadcrumbs](../breadcrumbs/) on the scope.

There are three types of scopes. Exactly one scope of each type will be active at a specific point in time.

- *Global scope*: A single globally-shared scope storing data relevant for the whole app (such as the release).
- *Isolation scope*: Thread-local scope created for each request-response lifecycle to store data relevant to the request.
- *Current scope*: Thread-local scope created for each span to store data relevant to the span.

The SDK and the SDK's built-in integrations automatically manage the scopes. For example, web framework integrations create an isolation scope for each request handled. When you call a top-level API function, such as <PlatformIdentifier name="set-tag" />, the SDK determines the correct scope on which to operate.

When sending an event to Sentry, the final data applied to the event is the result of merging the three scopes, applying data from each in turn. The global scope is applied first, followed by the isolation scope, and then the current scope.

## Changing the Scope

We generally recommend using the top-level API to manage your scopes, since the SDK's automatic scope management handles most use cases.

However, if your use case requires direct access to the scope object, you can use the <PlatformIdentifier name="new-scope" /> context manager. <PlatformIdentifier name="new-scope" /> forks the current scope, allows you to modify the new scope while the context manager is active, and restores the original scope afterwards. Using <PlatformIdentifier name="new-scope" /> allows you to send data for only one specific event, such as [modifying the context](../context/). It is roughly equivalent to the <PlatformIdentifier name="push-scope" /> context manager in earlier (1.x) versions of the SDK.

<Alert>

Avoid calling top-level APIs inside the <PlatformIdentifier name="new-scope" /> context manager. The top-level API might interact with a different scope from what <PlatformIdentifier name="new-scope" /> yields, causing unintended results. While within the <PlatformIdentifier name="new-scope" /> context manager, please call methods directly on the scope that <PlatformIdentifier name="new-scope" /> yields!

</Alert>

Using <PlatformIdentifier name="new-scope" /> allows you to attach additional information, such as adding custom tags.

<PlatformContent includePath="enriching-events/scopes/configure-scope" />

To learn what useful information can be associated with scopes see
[the context documentation](../context/).
