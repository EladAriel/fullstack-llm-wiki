---
type: "Framework Learn Page"
framework: "Sentry Python"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/python/enriching-events/identify-user/index.mdx"
source_commit: "8b4e4a23b18ee70f5fdb05bcda48869c10be2f60"
source_commit_short: "8b4e4a2"
source_commit_date: "2026-08-28T22:17:56+00:00"
generated_at: "2026-08-29T09:40:09.043429Z"
---
# Index

---
title: Users
description: "Learn how to configure the SDK to capture the user and gain critical pieces of information that construct a unique identity in Sentry."
---

Users consist of a few critical pieces of information that construct a unique identity in Sentry. Each of these is optional, but one **must** be present for the Sentry SDK to capture the user:

<DefinitionList>

### `id`

Your internal identifier for the user.

### `username`

The username. Typically used as a better label than the internal id.

### `email`

An alternative, or addition, to the username. Sentry is aware of email addresses and can display things such as Gravatars and unlock messaging capabilities.

### `ip_address`

The user's IP address. If the user is unauthenticated, Sentry uses the IP address as a unique identifier for the user.
The SDK will attempt to pull the IP address from the HTTP request data on incoming requests (`request.env.REMOTE_ADDR` field in JSON), if available. That requires <PlatformIdentifier name="send-default-pii" /> set to `true` in the SDK options.

If the user's `ip_address` is set to `"{{auto}}"`, Sentry will infer the IP address from the connection between your app and Sentry's server. If the field is omitted, the default value is `None`.

To opt out of storing users' IP addresses in your event data, users with project admin permissions (Org Owner, Org Manager, Team Admin, or Org Admin) can go to your project settings, click on "Security & Privacy", and enable "Prevent Storing of IP Addresses". Alternatively, use Sentry's [server-side data](/security-legal-pii/scrubbing/) scrubbing to remove `$user.ip_address`. Adding such a rule ultimately overrules any other logic.

</DefinitionList>

Additionally, you can provide arbitrary key/value pairs beyond the reserved names, and the Sentry SDK will store those with the user.

To identify the user:

<PlatformContent includePath="enriching-events/set-user" />

You can also clear the currently set user:

<PlatformContent includePath="enriching-events/unset-user" />
