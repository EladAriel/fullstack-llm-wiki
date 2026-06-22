---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/rc-get-prometheus-endpoint.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

In the **Metrics** tab of your database, select **Connect to Prometheus > Copy Prometheus endpoint** to save your Prometheus endpoint to the clipboard.

{{<image filename="images/rc/database-metrics-connect-prometheus.png" width="250px" alt="Use the Connect to Prometheus button to get the Prometheus endpoint.">}}

You can also get the Prometheus endpoint by calling [`GET /subscriptions/{subscriptionId}`]({{< relref "/operate/rc/api/api-reference#tag/Subscriptions-Pro/operation/getSubscriptionById" >}}) and getting the `prometheusEndpoint` from the response.
