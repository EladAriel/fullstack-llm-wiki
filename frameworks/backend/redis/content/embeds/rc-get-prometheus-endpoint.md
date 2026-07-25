---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/rc-get-prometheus-endpoint.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

In the **Metrics** tab of your database, select **Connect to Prometheus > Copy Prometheus endpoint** to save your Prometheus endpoint to the clipboard.

{{<image filename="images/rc/database-metrics-connect-prometheus.png" width="250px" alt="Use the Connect to Prometheus button to get the Prometheus endpoint.">}}

You can also get the Prometheus endpoint by calling [`GET /subscriptions/{subscriptionId}`]({{< relref "/operate/rc/api/api-reference#tag/Subscriptions-Pro/operation/getSubscriptionById" >}}) and getting the `prometheusEndpoint` from the response.
