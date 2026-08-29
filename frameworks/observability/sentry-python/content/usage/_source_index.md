---
type: "Framework Learn Page"
framework: "Sentry Python"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/python/usage/index.mdx"
source_commit: "8b4e4a23b18ee70f5fdb05bcda48869c10be2f60"
source_commit_short: "8b4e4a2"
source_commit_date: "2026-08-28T22:17:56+00:00"
generated_at: "2026-08-29T09:40:09.039133Z"
---
# Index

---
title: Capturing Errors
description: "Learn how to use the SDK to manually capture errors and other events."
sidebar_order: 2
sidebar_section: features
---

Sentry's SDK hooks into your runtime environment and automatically reports errors, uncaught exceptions, and unhandled rejections as well as other types of errors depending on the platform.

<Alert>

Key terms:

- An _event_ is one instance of sending data to Sentry. Generally, this data is an error or exception.
- An _issue_ is a grouping of similar events.
- The reporting of an event is called _capturing_.
  When an event is captured, it's sent to Sentry.

</Alert>

The most common form of capturing is to capture errors. What can be captured as an error varies by platform. In general, if you have something that looks like an exception, it can be captured. For some SDKs, you can also omit the argument to <PlatformIdentifier name="capture-exception" /> and Sentry will attempt to capture the current exception. It is also useful for manual reporting of errors or messages to Sentry.

While capturing an event, you can also record the breadcrumbs that lead up to that event. Breadcrumbs are different from events: they will not create an event in Sentry, but will be buffered until the next event is sent. Learn more about breadcrumbs in our <PlatformLink to="/enriching-events/breadcrumbs/">Breadcrumbs documentation</PlatformLink>.

## Capturing Errors

<PlatformContent includePath="capture-error" />

See the [API documentation](https://getsentry.github.io/sentry-python/api.html#sentry_sdk.api.capture_exception) for details on the `capture_exception` function.

## Capturing Messages

Another common operation is to capture a bare message. A message is textual information that should be sent to Sentry. Typically, our SDKs don't automatically capture messages, but you can capture them manually.

Messages show up as issues on your issue stream, with the message as the issue name.

<PlatformContent includePath="capture-message" />

See the [API documentation](https://getsentry.github.io/sentry-python/api.html#sentry_sdk.api.capture_message) for details on the `capture_message` function.
