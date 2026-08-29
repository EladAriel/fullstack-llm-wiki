---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rc/changelog/2024/november-2024.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.310908Z"
---
# November 2024

---
Title: Redis Cloud changelog (November 2024)
aliases:
- /operate/rc/changelog/november-2024/
alwaysopen: false
categories:
- docs
- operate
- rc
description: New features, enhancements, and other changes added to Redis Cloud during
  November 2024.
highlights: Pro subscription version upgrade
linktitle: November 2024
tags:
- changelog
weight: 40
---

## New Features

### Pro subscription version upgrade

You can now upgrade all databases in your Pro subscription from your [subscription page]({{< relref "/operate/rc/subscriptions/view-pro-subscription" >}}). 

Select **Version upgrade** to request to upgrade your subscription and databases if there is a later version available.

{{<image filename="images/rc/button-version-upgrade.png" width=150px alt="Version upgrade button." >}}

Select the version to upgrade your databases from the list and select **Upgrade** to submit the upgrade request.

{{<image filename="images/rc/version-upgrade-request.png" width=80% alt="Version upgrade request list with version 7.4 selected." >}}

The upgrade will start one week from your request, according to your subscription's [maintenance windows]({{< relref "/operate/rc/subscriptions/maintenance/set-maintenance-windows" >}}). 

Review the [7.2 breaking changes]({{< relref "/operate/rc/changelog/2023/june-2023#redis-72-breaking-changes" >}}) or [7.4 breaking changes]({{< relref "/operate/rc/changelog/2024/july-2024#redis-74-breaking-changes" >}}) before you request to upgrade.