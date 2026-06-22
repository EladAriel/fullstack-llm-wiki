---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rc/changelog/2023/october-2023.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Redis Cloud changelog (October 2023)
alwaysopen: false
categories:
- docs
- operate
- rc
description: New features, enhancements, and other changes added to Redis Cloud during
  October 2023.
highlights: Cost report CSV download, SAML Account linking tokens
linktitle: October 2023
tags:
- changelog
weight: 76
aliases:
  - /operate/rc/changelog/october-2023
---

## New features

### Cost report CSV download

You can now download shard cost reports in CSV format from the [**Billing and Payments**]({{< relref "/operate/rc/billing-and-payments" >}}) and [**Usage Reports**]({{< relref "/operate/rc/logs-reports/usage-reports" >}}) pages.

{{< embed-md "rc-cost-report-csv.md" >}}
### SAML account linking tokens

The process for [linking new Redis accounts]({{< relref "/operate/rc/security/access-control/saml-sso#link-other-accounts" >}}) to your [SAML single sign-on]({{< relref "/operate/rc/security/access-control/saml-sso" >}}) configuration has changed to enhance security. Now, both accounts must use a token to ensure that the connection is legitimate.
