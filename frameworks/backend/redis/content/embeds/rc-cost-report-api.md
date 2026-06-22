---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/rc-cost-report-api.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

To get the cost report using the REST API:

1. Use [`POST /cost-report`]({{< relref "/operate/rc/api/api-reference#tag/Account/operation/createCostReport" >}}) to generate a cost report, with the request body containing the `startDate` and `endDate` for the report as well as any optional filters. Your account must have the **Owner**, **Viewer**, or **Billing admin** role to generate a cost report through this endpoint.

    The response includes a `taskId` that you can use to track the status of the report generation.

1. Use [`GET /tasks/{taskId}`]({{< relref "/operate/rc/api/api-reference#tag/Tasks/operation/getTaskById" >}}) to check report generation status. The report is ready when the `status` is `processing-completed` and the `response` field contains a `costReportId`.
1. Use [`GET /cost-report/{costReportId}`]({{< relref "/operate/rc/api/api-reference#tag/Account/operation/getCostReport" >}}) to download the generated cost report.