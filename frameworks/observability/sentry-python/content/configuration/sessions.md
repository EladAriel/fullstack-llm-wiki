---
type: "Framework Learn Page"
framework: "Sentry Python"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/python/configuration/sessions.mdx"
source_commit: "8b4e4a23b18ee70f5fdb05bcda48869c10be2f60"
source_commit_short: "8b4e4a2"
source_commit_date: "2026-08-28T22:17:56+00:00"
generated_at: "2026-08-29T09:40:09.037444Z"
---
# Sessions

---
title: Sessions
sidebar_order: 50
description: "Learn how to configure your SDK to tell Sentry about users sessions."
---

A session represents the interaction between the user and the application. Sessions contain a timestamp, a status (if the session was OK or if it crashed), and are always linked to a release. The SDK manages sessions automatically on <PlatformLink to="/integrations/#web-frameworks">supported web frameworks</PlatformLink>.

<PlatformContent includePath="configuration/auto-session-tracking" />

## Tracking Release Health With Sessions

Sessions are used to monitor the [health of releases](/product/releases/health/) by observing user adoption, usage of the application, percentage of [crashes](/product/releases/health/#crashes--unhandled), and [session data](/product/releases/health/#sessions). Release health will provide insight into the impact of crashes and bugs as it relates to user experience, and reveal trends with each new issue through the [Release Details](/product/releases/release-details/) graphs and filters.

In order to monitor release health, you need to set a <PlatformLink to="/configuration/releases/">release</PlatformLink>.
