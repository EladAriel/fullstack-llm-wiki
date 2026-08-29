---
type: "Framework Learn Page"
framework: "Sentry Python"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/python/enriching-events/event-processors/index.mdx"
source_commit: "8b4e4a23b18ee70f5fdb05bcda48869c10be2f60"
source_commit_short: "8b4e4a2"
source_commit_date: "2026-08-28T22:17:56+00:00"
generated_at: "2026-08-29T09:40:09.044367Z"
---
# Index

---
title: Event Processors
description: "Learn more about how you can add your own event processors globally or to the current scope."
---

You can enrich events with additional data by adding your own event processors, either on the scope level or globally. Though event processors are similar to <PlatformIdentifier name="before-send" /> and <PlatformIdentifier name="before-send-transaction" />, there are two key differences:

- Event processors added with either <PlatformIdentifier name="add-global-event-processor" /> or <PlatformIdentifier name="scope.add-event-processor" /> run in an undetermined order, which means changes to the event may still be made after the event processor runs. <PlatformIdentifier name="before-send" /> and <PlatformIdentifier name="before-send-transaction" /> are guaranteed to be run last, after all other event processors, (which means they get the final version of the event right before it's sent, hence the name).
- While <PlatformIdentifier name="before-send" />, <PlatformIdentifier name="before-send-transaction" />, and processors added with <PlatformIdentifier name="add-global-event-processor" /> run globally, regardless of scope, processors added with <PlatformIdentifier name="scope.add-event-processor" /> only run on events captured while that scope is active.

Like <PlatformIdentifier name="before-send" /> and <PlatformIdentifier name="before-send-transaction" />, event processors are passed two arguments, the event itself and <PlatformLink to="/configuration/filtering/#using-hints">a `hint` object</PlatformLink> containing extra metadata.

<PlatformContent includePath="enriching-events/event-processors" />
