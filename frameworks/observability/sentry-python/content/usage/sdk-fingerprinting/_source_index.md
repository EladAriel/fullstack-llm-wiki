---
type: "Framework Learn Page"
framework: "Sentry Python"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/python/usage/sdk-fingerprinting/index.mdx"
source_commit: "8b4e4a23b18ee70f5fdb05bcda48869c10be2f60"
source_commit_short: "8b4e4a2"
source_commit_date: "2026-08-28T22:17:56+00:00"
generated_at: "2026-08-29T09:40:09.045625Z"
---
# Index

---
title: "SDK Fingerprinting"
description: "Learn about overriding default fingerprinting in your SDK."
sidebar_order: 30
---

All events have a fingerprint. Events with the same fingerprint are grouped together into an issue.

By default, Sentry will run one of our built-in grouping algorithms to generate a fingerprint based on information available within the event such as `stacktrace`, `exception`, and `message`. To extend the default grouping behavior or change it completely, you can use a combination of the following options:

1. In your SDK, using SDK Fingerprinting, as documented below
2. In your project, using [Fingerprint Rules](/concepts/data-management/event-grouping/fingerprint-rules/) or [Stack Trace Rules](/concepts/data-management/event-grouping/stack-trace-rules/)

You can override Sentry's default grouping that passes the fingerprint attribute as an array of strings. The length of a fingerprint's array is not restricted. This works similarly to the [fingerprint rules functionality](/concepts/data-management/event-grouping/fingerprint-rules/), which can achieve similar results.

## Basic Example

In the most basic case, values are passed directly:

<PlatformContent includePath="set-fingerprint/basic" />

You can use variable substitution to fill dynamic values into the fingerprint generally computed on the server. For instance, the value `{{ default }}` can be added to add the entire normally generated grouping hash into the fingerprint. These values are the same as for server-side fingerprinting. See [Variables](/concepts/data-management/event-grouping/fingerprint-rules/#variables) for more information.

## Group Errors With Greater Granularity

In some scenarios, you'll want to group errors more granularly.

For example, if your application queries a Remote Procedure Call Model (RPC) interface or external Application Programming Interface (API) service, the stack trace is generally the same, even if the outgoing request is very different.

The following example will split up the default group Sentry would create (represented by `{{ default }}`) further, taking some attributes on the error object into account:

<PlatformContent includePath="set-fingerprint/rpc" />

## Group Errors More Aggressively

You can also overwrite Sentry's grouping entirely.

For example, if a generic error, such as a database connection error, has many different stack traces and never groups them together, you can overwrite Sentry's grouping by omitting `{{ default }}` from the array:

<PlatformContent includePath="set-fingerprint/database-connection" />
