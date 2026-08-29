---
type: "Framework Learn Page"
framework: "Sentry Python"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/python/configuration/releases.mdx"
source_commit: "8b4e4a23b18ee70f5fdb05bcda48869c10be2f60"
source_commit_short: "8b4e4a2"
source_commit_date: "2026-08-28T22:17:56+00:00"
generated_at: "2026-08-29T09:40:09.038042Z"
---
# Releases

---
title: Releases
sidebar_order: 40
description: "Learn how to configure your SDK to tell Sentry about your releases."
---

A `release` is a version of your code that is deployed to an <PlatformLink to="/configuration/environments/">environment</PlatformLink>. When you give Sentry information about your releases, you can:

- Determine issues and regressions introduced in a new release
- Predict which commit caused an issue and who is likely responsible
- Resolve issues by including the issue number in your commit message
- Receive email notifications when your code gets deployed


Include the `release` when you initialize the SDK. The release name cannot:

- contain newlines, tabulator characters, forward slashes(`/`) or back slashes(`\`)
- be (in their entirety) period (`.`), double period (`..`), or space ( )
- exceed 200 characters

The value can be arbitrary, but we recommend [Semantic Versioning](https://semver.org/), [Calendar Versioning](https://calver.org/), or the Git commit SHA.

We recommend that your release is prefixed with a project-specific package identifier (such as `"mypackage@1.0.0"`).


The behavior of a few features depends on whether a project is using semantic or time-based versioning including the `"mypackage@"` prefix:

- Regression detection
- Data filtering by `release:latest`

We automatically detect whether a project is using semantic or time-based versioning.

## Setting a Release

<PlatformContent includePath="set-release" notateUnsupported />

How you make the `release` available to your code is up to you. For example, you could use an environment variable that is set during the build process or during initial start-up.

If you do not set `release` in `init()`, the Sentry SDK will try to guess it. The SDK will first check for the environment variable, `SENTRY_RELEASE`. If this environment variable is not set, the SDK will then check if a Git repository is present and, if so, will take the Git SHA from the latest commit. If this doesn't work, the SDK will check for environment variables used by hosting providers like `HEROKU_SLUG_COMMIT`, `SOURCE_VERSION`, `CODEBUILD_RESOLVED_SOURCE_VERSION`, `CIRCLE_SHA1`, and `GAE_DEPLOYMENT_ID`.

## Unlocking More Release Features

We recommend that you tell Sentry about a new release before sending events with that release name, as this will unlock a few more features like identifying regressions and associating commits to releases. Learn more in our [Releases](/product/releases/) documentation.

After configuring your SDK, you can install a repository integration or manually supply Sentry with your own commit metadata. Read our documentation about [setting up releases](/product/releases/setup/) for further information about integrations, associating commits, and telling Sentry when deploying releases.

## Release Health

Monitor the [health of releases](/product/releases/health/) by observing user adoption, usage of the application, percentage of [crashes](/product/releases/health/#crashes--unhandled), and [session data](/product/releases/health/#sessions). Release health will provide insight into the impact of crashes and bugs as it relates to user experience, and reveal trends with each new issue through the [Release Details](/product/releases/release-details/) graphs and filters.

In order to monitor release health, the SDK sends <PlatformLink to="/configuration/sessions/">sessions</PlatformLink>.
