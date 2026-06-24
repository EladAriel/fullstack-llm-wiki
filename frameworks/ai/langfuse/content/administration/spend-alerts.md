---
type: "Framework Learn Page"
framework: "Langfuse"
source_repo: "https://github.com/langfuse/langfuse-docs"
source_branch: "main"
source_path: "content/docs/administration/spend-alerts.mdx"
source_commit: "4a702ece53852a6af86b3883f434adf3f5cae421"
source_commit_short: "4a702ece"
source_commit_date: "2026-06-23T13:41:14Z"
generated_at: "2026-06-23T13:55:15Z"
---

---
title: Spend Alerts
sidebarTitle: Spend Alerts
description: Get notified when your organization's spend exceeds predefined monetary thresholds to better manage your Langfuse Cloud costs.
---

# Spend Alerts

<AvailabilityBanner
  availability={{
    hobby: "not-available",
    core: "full",
    pro: "full",
    enterprise: "full",
    selfHosted: "not-available",
  }}
/>

Configure spend alerts to receive email notifications when your **Langfuse Cloud** bill exceeds a predefined monetary threshold. These alerts cover what you pay Langfuse for using Langfuse Cloud — not LLM or model costs you track in Langfuse observability. This helps you monitor your Langfuse bill and take action before unexpected charges occur.

Navigate to your organization settings and the **Billing** tab to configure spend alerts.

<Frame className="my-10" fullWidth>
  ![Configure spend alerts in Langfuse](/images/docs/spend-alerts.png)
</Frame>

## How it works

Spend alerts monitor your organization's total Langfuse Cloud subscription spend. You can set custom thresholds in your organization's billing currency and receive email notifications when spending crosses these limits.

**Threshold calculation:** Spend is evaluated against the total expected invoice, including base fees, usage-based fees, discounts, and taxes.

**Monitoring frequency:** We check each organization's usage every 60-90 minutes to ensure timely notifications.

**Notifications:** Email alerts are sent to all organization members with **Owner** or **Admin** roles. Each configured alert triggers at most once per billing cycle to avoid notification fatigue.
