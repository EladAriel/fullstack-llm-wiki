---
type: "Framework Learn Page"
framework: "Sentry Python"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/python/configuration/environments.mdx"
source_commit: "8b4e4a23b18ee70f5fdb05bcda48869c10be2f60"
source_commit_short: "8b4e4a2"
source_commit_date: "2026-08-28T22:17:56+00:00"
generated_at: "2026-08-29T09:40:09.038212Z"
---
# Environments

---
title: Environments
sidebar_order: 30
description: "Learn how to configure your SDK to tell Sentry about your environments."
---

Environments tell you where an error occurred, whether that's in your production system, your staging server, or elsewhere.

Environments are case-sensitive. The environment name can't contain newlines, spaces or forward slashes, can't be the string "None", or exceed 64 characters. You can't delete environments, but you can [hide](/concepts/key-terms/environments/#hidden-environments) them.

<PlatformContent includePath="set-environment" />

If you do not set `environment` in `init()`, the Sentry SDK will check for the environment variable, `SENTRY_ENVIRONMENT`. If this is not set, `environment` will default to `production`.

Environments help you better filter issues, releases, and user feedback in the Issue Details page of sentry.io, which you learn more about in our [documentation that covers using environments](/concepts/key-terms/environments/).
