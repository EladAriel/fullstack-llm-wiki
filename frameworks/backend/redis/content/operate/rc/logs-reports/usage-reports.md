---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rc/logs-reports/usage-reports.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Usage reports
alwaysopen: false
categories:
- docs
- operate
- rc
description: You can view usage reports to track the memory usage and shard usage
  of all your databases.
weight: 70
---

The **Usage Report** shows the daily memory usage and shard usage of all databases from the subscriptions associated with your account.

{{< image filename="/images/rc/usage-report-memory-usage.png" >}}

To filter the data, you can:
* Select a month and year from the **View Statement For** list to view the daily memory usage during a specific month.
* Select a subscription from the **Subscription** list to view the daily memory usage of a specific subscription associated with your account.
* Select a database from the **Database** list to view the daily memory usage of a specific database.

You can also hold the pointer over each bar in the graph to view the precise memory usage on that day.

## Download cost report

{{< embed-md "rc-cost-report-csv.md" >}}

See [Cost report]({{< relref "/operate/rc/billing-and-payments/cost-report" >}}) and [How to download and visualize the cost report](https://support.redislabs.com/hc/en-us/articles/30042563097874-How-to-Download-and-Visualize-Redis-Cloud-Cost-Report) for more information.