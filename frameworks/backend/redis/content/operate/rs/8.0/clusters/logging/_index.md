---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/8.0/clusters/logging/_index.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
Title: Logging events
alwaysopen: false
categories:
- docs
- operate
- rs
description: Management actions performed with Redis Software are logged to make
  sure system management tasks are appropriately performed or monitored by administrators
  and for compliance with regulatory standards.
hideListLinks: true
linkTitle: Logging
weight: 95
url: '/operate/rs/8.0/clusters/logging/'
---
Management actions performed with Redis Software are logged to make sure system management tasks are appropriately performed or monitored by administrators and for compliance with regulatory standards.

Log entries contain the
following information:

1. Who performed the action?
1. What exactly was the performed action?
1. When was the action performed?
1. Did the action succeed or not?

To get the list of logged events, you can use the REST API or
the **Logs** screen in the UI. The **Logs** screen displays the system and user
events regarding alerts, notifications, and configuration.

{{<image filename="images/rs/screenshots/cluster/cluster-logs.png" alt="Logs screen in the new Cluster Manager UI.">}}

You can use the **Logs** screen to review what actions a user has performed, such as editing a database's configuration.

- [Redis slow
    log]({{< relref "/operate/rs/8.0/clusters/logging/redis-slow-log.md" >}})
- [rsyslog logging]({{< relref "/operate/rs/8.0/clusters/logging/rsyslog-logging/" >}})

## View logs in the UI

Redis Software provides log files for auditing cluster management actions and troubleshooting. You can view these logs in the UI and on the host operating system.

To view event logs in the new Cluster Manager UI, go to **Cluster > Logs**.

## View logs on the server

Server logs can be found by default in the directory `/var/opt/redislabs/log/`.

These log files are used by the Redis support team to troubleshoot issues. The logs you will most frequently interact with is 'event_log.log'. This log file is where logs of configuration actions within Redis are stored and is useful to determine events that occur within Redis Software.

## Configure log timestamps

Redis Software allows you to configure log timestamps. To configure log timestamps in the new Cluster Manager UI:

1. Go to **Cluster > Configuration > General**.

1. Change the **Time zone** for the logs based on your location.
