---
type: "Framework Learn Page"
framework: "Sentry Python"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/python/tracing/instrumentation/opentelemetry.mdx"
source_commit: "8b4e4a23b18ee70f5fdb05bcda48869c10be2f60"
source_commit_short: "8b4e4a2"
source_commit_date: "2026-08-28T22:17:56+00:00"
generated_at: "2026-08-29T09:40:09.046643Z"
---
# Opentelemetry

---
title: OpenTelemetry Integration Support (Deprecated)
description: "Using OpenTelemetry with Sentry Performance."
sidebar_order: 20
---

<Alert level="warning" title="Deprecated">

The `OpenTelemetryIntegration` is deprecated in favor of the <PlatformLink to="/integrations/otlp/">OTLPIntegration</PlatformLink>, which sends OpenTelemetry traces directly to Sentry over OTLP. Migrate to the new integration for a simpler setup.

</Alert>

You can configure your [OpenTelemetry SDK](https://opentelemetry.io/) to send traces and spans to Sentry.

## Install

<PlatformContent includePath="performance/opentelemetry-install" />

## Usage

<PlatformContent includePath="performance/opentelemetry-setup" />

## OpenTelemetry and Sentry

With Sentry’s OpenTelemetry SDK, an OpenTelemetry `Span` becomes a Sentry `Transaction` or `Span`. The first `Span` sent through the Sentry `SpanProcessor` is a `Transaction`, and any child `Span` gets attached to the first `Transaction` upon checking the parent `Span` context. This is true for the OpenTelemetry root `Span` and any top level `Span` in the system. For example, a request sent from frontend to backend will create an OpenTelemetry root `Span` with a corresponding Sentry `Transaction`. The backend request will create a new Sentry `Transaction` for the OpenTelemetry `Span`. The Sentry `Transaction` and `Span` are linked as a trace for navigation and error tracking purposes.

## Additional Configuration

If you need more fine-grained control over Sentry, take a look at the <PlatformLink to="/configuration/">Configuration page</PlatformLink>. In case you'd like to apply client-side sampling or filter out transactions before sending them to Sentry (to get rid of health checks, for example), you may find the <PlatformLink to="/configuration/filtering/#filtering-transactions-and-spans">Filtering page</PlatformLink> helpful.
