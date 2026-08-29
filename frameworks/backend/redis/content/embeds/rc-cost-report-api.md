---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/rc-cost-report-api.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.100393Z"
---
# Rc Cost Report Api

To get the cost report using the REST API:

1. Use [`POST /cost-report`]({{< relref "/operate/rc/api/api-reference#tag/Account/operation/createCostReport" >}}) to generate a cost report, with the request body containing the `startDate` and `endDate` for the report as well as any optional filters. Your account must have the **Owner**, **Viewer**, or **Billing admin** role to generate a cost report through this endpoint.

    The response includes a `taskId` that you can use to track the status of the report generation.

1. Use [`GET /tasks/{taskId}`]({{< relref "/operate/rc/api/api-reference#tag/Tasks/operation/getTaskById" >}}) to check report generation status. The report is ready when the `status` is `processing-completed` and the `response` field contains a `costReportId`.
1. Use [`GET /cost-report/{costReportId}`]({{< relref "/operate/rc/api/api-reference#tag/Account/operation/getCostReport" >}}) to download the generated cost report.