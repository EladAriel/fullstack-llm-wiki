---
type: "Framework Learn Page"
framework: "Sentry Python"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/python/enriching-events/attachments/index.mdx"
source_commit: "8b4e4a23b18ee70f5fdb05bcda48869c10be2f60"
source_commit_short: "8b4e4a2"
source_commit_date: "2026-08-28T22:17:56+00:00"
generated_at: "2026-08-29T09:40:09.044756Z"
---
# Index

---
title: Attachments
description: "Learn more about how Sentry can store additional files in the same request as event attachments."
---

Sentry can enrich your events for further investigation by storing additional files, such as config or log files, as attachments.

## Uploading Attachments

<PlatformContent includePath="enriching-events/add-attachment" />

<Alert>

Sentry allows at most 40MB for a compressed request, and at most 200MB of uncompressed attachments per event, including the crash report file (if applicable). Uploads exceeding this size are rejected with HTTP error `413 Payload Too Large` and the data is dropped immediately. To add larger or more files, consider secondary storage options.

</Alert>

Attachments are retained for 30 or 90 days, based on [your plan's data retention period](/security-legal-pii/security/data-retention-periods/#default-data-retention-by-plan); if your total storage included in your quota is exceeded, attachments will not be stored. You can delete attachments or their containing events at any time. Deleting an attachment does not affect your quota - Sentry counts an attachment toward your quota as soon as it is stored.

Learn more about how attachments impact your [quota](/pricing/quotas/).

## Add or Modify Attachments Before Sending

It's possible to add, remove, or modify attachments before an event is sent by way of
the <PlatformLink to="/configuration/options/#before-send"><PlatformIdentifier name="before-send" /></PlatformLink>
hook or an <PlatformLink to="/enriching-events/event-processors/">event processor</PlatformLink>.


```python
from sentry_sdk.scope import add_global_event_processor
from sentry_sdk.types import Event, Hint
from sentry_sdk.attachments import Attachment

@add_global_event_processor
def event_processor(event: Event, hint: Hint):
    hint["attachments"] = [Attachment(bytes=b"Hello World!", filename="attachment.txt")]
    return event
```

### Access to Attachments

To limit access to attachments, navigate to your organization's **General Settings**, then select the _Attachments Access_ dropdown to set appropriate access — any member of your organization, the organization billing owner, member, admin, manager, or owner.

<Include name="common-imgs/attachments-access" />

By default, access is granted to all members when storage is enabled. If a member does not have access to the project, the ability to download an attachment is not available; the button will be greyed out in Sentry. The member may only view that an attachment is stored.

## Viewing Attachments

Attachments display on the bottom of the **Issue Details** page for the event that is shown.

<Include name="common-imgs/attachments-access-denied" />

Alternately, attachments also appear in the _Attachments_ tab on the **Issue Details** page, where you can view the _Type_ of attachment, as well as associated events. Click the Event ID to open the **Issue Details** of that specific event.

<Include name="common-imgs/attachments-list-example" />
