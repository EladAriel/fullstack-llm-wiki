---
type: "Framework Learn Page"
framework: "OpenTelemetry JS"
source_repo: "https://github.com/open-telemetry/opentelemetry.io.git"
source_branch: "main"
source_path: "content/en/docs/languages/js/_index.md"
source_commit: "8fd99e125e5510385b18b541d97c283e28f76ef2"
source_commit_short: "8fd99e1"
source_commit_date: "2026-07-25T10:22:15-04:00"
generated_at: "2026-07-25T19:07:58.990698Z"
---
# _Index

---
title: JavaScript
description: >-
  <img width="35" class="img-initial otel-icon"
  src="/img/logos/32x32/JS_SDK.svg" alt="JavaScript"> A language-specific
  implementation of OpenTelemetry in JavaScript (for Node.js & the browser).
aliases: [/js/metrics, /js/tracing, nodejs]
redirects:
  - { from: /js/*, to: ':splat' }
  - { from: /docs/js/*, to: ':splat' }
weight: 160
---

{{% docs/languages/index-intro js /%}}

{{% include browser-instrumentation-warning.md %}}

## Version Support

OpenTelemetry JavaScript supports all active or maintenance LTS versions of
Node.js. Previous versions of Node.js may work, but are not tested by
OpenTelemetry.

OpenTelemetry JavaScript has no official supported list of browsers. It is aimed
to work on currently supported versions of major browsers.

OpenTelemetry JavaScript follows DefinitelyTyped's support policy for TypeScript
which sets a support window of 2 years. Support for TypeScript versions older
than 2 years will be dropped in minor releases of OpenTelemetry JavaScript.

For more details on runtime support see
[this overview](https://github.com/open-telemetry/opentelemetry-js#supported-runtimes).

## Repositories

OpenTelemetry JavaScript consists of the following repositories:

- [opentelemetry-js](https://github.com/open-telemetry/opentelemetry-js), core
  repository containing the core distribution API and SDK.
- [opentelemetry-js-contrib](https://github.com/open-telemetry/opentelemetry-js-contrib),
  contributions that are not part of the core distribution of the API and SDK.

## Help or Feedback

If you have questions about OpenTelemetry JavaScript, please reach out via
[GitHub Discussions](https://github.com/open-telemetry/opentelemetry-js/discussions)
or the `#otel-js` channel on [CNCF Slack](https://slack.cncf.io/).

If you want to contribute to OpenTelemetry JavaScript, see the
[contributing instructions](https://github.com/open-telemetry/opentelemetry-js/blob/main/CONTRIBUTING.md)
