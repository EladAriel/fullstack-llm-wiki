---
type: "Framework Learn Page"
framework: "Sentry Python"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/python/user-feedback/index.mdx"
source_commit: "8b4e4a23b18ee70f5fdb05bcda48869c10be2f60"
source_commit_short: "8b4e4a2"
source_commit_date: "2026-08-28T22:17:56+00:00"
generated_at: "2026-08-29T09:40:09.038948Z"
---
# Index

---
title: Set Up User Feedback
sidebar_title: User Feedback
description: "Learn more about collecting user feedback when an event occurs. Sentry pairs the feedback with the original event, giving you additional insight into issues."
sidebar_order: 10
sidebar_section: features
---

When a user experiences an error, Sentry provides the ability to collect additional feedback. You can collect feedback according to the method supported by the SDK.

## Crash-Report Modal

Our embeddable, JavaScript-based, Crash-Report modal is useful when you would typically render a plain error page (the classic `500.html`) on your website.

To collect feedback, the Crash-Report modal requests and collects the user's name, email address, and a description of what occurred. When feedback is provided, Sentry pairs the feedback with the original event, giving you additional insights into issues.

The screenshot below provides an example of the Crash-Report modal, though yours may differ depending on your customization:

<Include name="common-imgs/user_feedback_widget" />

### Integration

The modal authenticates with your public DSN, then passes in the Event ID that was generated on your backend.

<PlatformContent includePath="user-feedback/example-widget/" />
