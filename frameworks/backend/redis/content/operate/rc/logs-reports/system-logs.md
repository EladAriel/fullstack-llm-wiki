---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rc/logs-reports/system-logs.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
Title: System logs
alwaysopen: false
categories:
- docs
- operate
- rc
description: You can view and export system logs to track any activity associated
  with your subscriptions and databases.
weight: 35
---
The **Logs** page contains events, alerts, and logs from the activities, databases, and subscriptions associated with your account.

{{<image filename="images/rc/system-logs.png" alt="Choose the Logs page from the Redis Cloud console menu to view your subscription system log." width="100%">}} 

You can:

* Sort the list by a specific field in descending or ascending order. Supported fields include *Time*, *Originator*, *Database name*, *API key name*, and *Activity*.

    {{<image filename="images/rc/icon-list-sort-asc.png#no-click" alt="Use the arrows in the list header to sort the list." class="inline">}}&nbsp;{{<image filename="images/rc/icon-list-sort-desc.png#no-click" alt="The direction of the arrow corresponds to the direction of the sort." class="inline">}}    
    
    Select the arrow icon to change the sort order.  You can only sort by one field at a time.

* Use the **Export all** button to export all logs as a comma-separated values (CSV) file for use in other systems and programs.

    {{<image filename="images/rc/system-logs-export.png" alt="Use the export all button in the top right to export all logs to a CSV file" width="130px">}} 

* Use the refresh button to refresh the system logs.

    {{<image filename="images/rc/system-logs-refresh.png" alt="Use the refresh button in the top right to refresh the system logs" width="30px">}}

* Use the search bar to search for specific entries. Supported fields include *Originator*, *Database name*, *API key name*, *Activity*, and *Description*.

## Get system logs using REST API

Use [`GET /logs`]({{< relref "/operate/rc/api/api-reference#tag/Account/operation/getAccountSystemLogs" >}}) to get the system logs using the REST API. See [Audit system logs]({{< relref "/operate/rc/api/examples/audit-system-logs" >}}) for more information.