---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/rc-version-upgrade.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

Select **Version upgrade** to request to upgrade your subscription and databases if there is a later version available.

{{<image filename="images/rc/button-version-upgrade.png" width=150px alt="Version upgrade button." >}}

Select the version to upgrade your databases from the list and select **Upgrade** to submit the upgrade request.

{{<image filename="images/rc/version-upgrade-request.png" width=80% alt="Version upgrade request list with version 7.4 selected." >}}

The upgrade will start one week from your request, according to your subscription's [maintenance windows]({{< relref "/operate/rc/subscriptions/maintenance/set-maintenance-windows" >}}). 

Review the [7.2 breaking changes]({{< relref "/operate/rc/changelog/2023/june-2023#redis-72-breaking-changes" >}}) or [7.4 breaking changes]({{< relref "/operate/rc/changelog/2024/july-2024#redis-74-breaking-changes" >}}) before you request to upgrade.