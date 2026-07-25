---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rc/changelog/december-2025.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
Title: Redis Cloud changelog (December 2025)
alwaysopen: false
categories:
- docs
- operate
- rc
description: New features, enhancements, and other changes added to Redis Cloud during
  December 2025.
highlights: FOCUS-compliant cost reports with REST API
linktitle: December 2025
weight: 55
tags:
- changelog
---

## New features

### FOCUS-compliant cost reports with REST API

Select users can now generate and download [cost reports]({{< relref "/operate/rc/billing-and-payments/cost-report" >}}) in a [FinOps Open Cost and Usage Specification (FOCUS)](https://focus.finops.org/) compliant format using the Redis Cloud REST API. You can use this cost report with any FOCUS-compatible cost reporting tool to analyze and visualize your costs.

[Contact support](https://redis.io/support/) to request access to the cost report endpoint.

See [Generate FOCUS-compliant cost report with REST API]({{< relref "/operate/rc/api/examples/generate-cost-report" >}}) for examples.