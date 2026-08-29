---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/guides/cookbooks/environment-tracking.mdx"
source_commit: "607c855f787d6cc66e83692874bf90f880a08d62"
source_commit_short: "607c855"
source_commit_date: "2026-08-25T19:59:29-04:00"
generated_at: "2026-08-29T09:39:42.333255Z"
---
# Environment Tracking

---
title: "Environment Tracking"
sidebarTitle: "Environment Tracking"
description: "Effortlessly track and manage your development, staging, and production environments with Helicone."
"twitter:title": "Environment Tracking - Helicone OSS LLM Observability"
---

Many organizations operate across multiple environments, such as development, staging, and production. To differentiate these environments, you can establish a `Helicone-Property-Environment` property. In the example below, we assign the "development" property to the environment:

```python
client.chat.completions.create(
    # ...
    extra_headers={
        "Helicone-Property-Environment": "development",
    }
)
```

If you are utilizing any other libraries or packages, please refer to our [Custom Properties](/features/advanced-usage/custom-properties) documentation for guidance.

### Viewing Environments

On the [request page](https://www.helicone.ai/requests), you can conveniently view all the environments that your organization has employed.

<Frame>
  <img
    src="/images/environment-cp/1.png"
    alt="View environments tracked by Helicone on the Requests page."
  />
</Frame>

Additionally, you can filter by environment to view all the requests made within that specific environment.

<Frame>
  <img
    src="/images/environment-cp/2.png"
    alt="Filter requests by specific environments on the Requests page."
  />
</Frame>

Efficiently add filters to your requests to view all the requests made in a particular environment.

<Frame>
  <img
    src="/images/environment-cp/3.png"
    alt="Add filters to specify environment within Helicone."
  />
</Frame>

Helicone also offers a dedicated page to view all the environments that your organization has utilized. You can also view the number of requests made in each environment.

Visit the [properties page](https://www.helicone.ai/properties) to view all the environments that your organization has employed.

<Frame>
  <img
    src="/images/environment-cp/4.png"
    alt="View cost, usage and latency associated with a custom property on the Properties page."
  />
</Frame>
