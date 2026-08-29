---
type: "Framework Learn Page"
framework: "Sentry Python"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/python/enriching-events/tags/index.mdx"
source_commit: "8b4e4a23b18ee70f5fdb05bcda48869c10be2f60"
source_commit_short: "8b4e4a2"
source_commit_date: "2026-08-28T22:17:56+00:00"
generated_at: "2026-08-29T09:40:09.043985Z"
---
# Index

---
title: Tags
description: "Tags power UI features such as filters and tag-distribution maps. Tags also help you quickly access related events and view the tag distribution for a set of events."
---

**Tags** are key/value string pairs that are both indexed and searchable. Tags power features in sentry.io such as filters and tag-distribution maps. Tags also help you quickly both access related events and view the tag distribution for a set of events. Common uses for tags include hostname, platform version, and user language.

We'll automatically index all tags for an event, as well as the frequency and the last time that Sentry has seen a tag. We also keep track of the number of distinct tags and can assist you in determining hotspots for various issues.

<Alert level="warning">

Tags are **not** applied to logs, metrics, or spans in stream mode. If you want to attach that data to logs, metrics, or spans in stream mode, use <PlatformLink to="/enriching-events/attributes/">Attributes</PlatformLink> instead.

</Alert>

_Tag keys_ have a maximum length of 200 characters and can contain only letters (`a-zA-Z`), numbers (`0-9`), underscores (`_`), periods (`.`), colons (`:`), and dashes (`-`).

_Tag values_ have a maximum length of 200 characters and they cannot contain the newline (`\n`) character.

Defining tags is easy, and will bind them to the [isolation scope](../scopes/) ensuring all future events within scope contain the same tags.

Tags can be set with the `set_tag` function:

<PlatformContent includePath="enriching-events/set-tag" />

<Alert>

Some tags are automatically set by Sentry. We strongly recommend against overwriting these [tags](/concepts/search/searchable-properties/#search-properties). Instead, name your tags with your organization's nomenclature. If you overwrite an automatically set tag, you must use [explicit tag syntax](/concepts/search/#explicit-tag-syntax) to search for it.

</Alert>

Once you've started sending tagged data, you'll see it when logged in to sentry.io. There, you can view the filters within the sidebar on the Project page, summarized within an event, and on the Tags page for an aggregated event.

<Include name="common-imgs/tags" />
