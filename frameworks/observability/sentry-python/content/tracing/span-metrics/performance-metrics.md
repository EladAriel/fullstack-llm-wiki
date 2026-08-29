---
type: "Framework Learn Page"
framework: "Sentry Python"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/python/tracing/span-metrics/performance-metrics.mdx"
source_commit: "8b4e4a23b18ee70f5fdb05bcda48869c10be2f60"
source_commit_short: "8b4e4a2"
source_commit_date: "2026-08-28T22:17:56+00:00"
generated_at: "2026-08-29T09:40:09.047740Z"
---
# Performance Metrics

---
title: Sending Performance Metrics
description: "Learn how to attach performance metrics to your Sentry transactions."
sidebar_order: 20
notSupported:
  - javascript.cordova
---

The SDK supports sending performance metrics data to Sentry. These are numeric values attached to transactions that are aggregated and displayed in Sentry.

## Custom Measurements

In addition to automatic performance metrics, the SDK supports custom performance measurements on transactions. <Include name="custom-measurements-blurb.mdx" />

To set a performance measurement, you need to supply the following:

- name (`string`)
- value (any numeric type - `float`, `integer`, etc.)
- unit (`string`, defaults to the string `none` if omitted)

Sentry supports adding arbitrary custom units, but we recommend using one of the [supported units listed below](./#supported-measurement-units).

<PlatformContent includePath="performance/custom-performance-metrics" />

<Include name="custom-measurements-units-disclaimer.mdx" />

## Supported Measurement Units

Units augment measurement values by giving meaning to what otherwise might be abstract numbers. Adding units also allows Sentry to offer controls - unit conversions, filters, and so on - based on those units. For values that are unitless, you can supply an empty string or `none`.

### Duration Units

- `nanosecond`
- `microsecond`
- `millisecond`
- `second`
- `minute`
- `hour`
- `day`
- `week`

### Information Units

- `bit`
- `byte`
- `kilobyte`
- `kibibyte`
- `megabyte`
- `mebibyte`
- `gigabyte`
- `gibibyte`
- `terabyte`
- `tebibyte`
- `petabyte`
- `pebibyte`
- `exabyte`
- `exbibyte`

### Fraction Units

- `ratio`
- `percent`

If you want to explore further, you can find details about supported units in our [event ingestion documentation](https://getsentry.github.io/relay/relay_metrics/enum.MetricUnit.html).
