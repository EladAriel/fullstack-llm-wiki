---
type: "Framework Learn Page"
framework: "Sentry Python"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/python/user-feedback/configuration/index.mdx"
source_commit: "8b4e4a23b18ee70f5fdb05bcda48869c10be2f60"
source_commit_short: "8b4e4a2"
source_commit_date: "2026-08-28T22:17:56+00:00"
generated_at: "2026-08-29T09:40:09.045419Z"
---
# Index

---
title: Configuration
description: "Learn about the general User Feedback configuration fields."
sidebar_order: 6100
---

## Crash-Report Modal

You can customize the Crash-Report modal to your organization's needs, for example, for localization purposes. All options can be passed through the `Sentry.showReportDialog` call.

| Param            | Default                                                                                           |
| ---------------- | ------------------------------------------------------------------------------------------------- |
| `eventId`        | Manually set the id of the event.                                                                 |
| `dsn`            | Manually set dsn to report to.                                                                    |
| `user`           | Manually set user data _[an object with keys listed below]_.                                      |
| `user.email`     | User's email address.                                                                             |
| `user.name`      | User's name.                                                                                      |
| `lang`           | _[automatic]_ – **override for Sentry’s language code**                                           |
| `title`          | It looks like we’re having issues.                                                                |
| `subtitle`       | Our team has been notified.                                                                       |
| `subtitle2`      | If you’d like to help, tell us what happened below. – **not visible on small screen resolutions** |
| `labelName`      | Name                                                                                              |
| `labelEmail`     | Email                                                                                             |
| `labelComments`  | What happened?                                                                                    |
| `labelClose`     | Close                                                                                             |
| `labelSubmit`    | Submit                                                                                            |
| `errorGeneric`   | An unknown error occurred while submitting your report. Please try again.                         |
| `errorFormEntry` | Some fields were invalid. Please correct the errors and try again.                                |
| `successMessage` | Your feedback has been sent. Thank you!                                                           |
| `onLoad`         | n/a - **an optional callback that will be invoked when the widget opens**                         |
| `onClose`        | n/a - **an optional callback that will be invoked when the widget closes**                        |

The optional callback `onLoad` will be called when users see the widget. You can use this to run custom logic, for example to log an analytics event:

<PlatformContent includePath="user-feedback/example-widget-onload" />

The optional callback `onClose` will be called when users close the widget. You can use this to run custom logic, for example to reload the page:

<PlatformContent includePath="user-feedback/example-widget-onclose" />
