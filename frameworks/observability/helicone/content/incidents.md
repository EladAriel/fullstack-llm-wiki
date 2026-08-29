---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/incidents.mdx"
source_commit: "607c855f787d6cc66e83692874bf90f880a08d62"
source_commit_short: "607c855"
source_commit_date: "2026-08-25T19:59:29-04:00"
generated_at: "2026-08-29T09:39:42.264283Z"
---
# Incidents

### 🟡 [2024-05-27 1:00pm PST] - TLSv1 Alert Protocol Version

**Status** - _Active_

**Impact** - _Some users may be experiencing issues connecting to the platform._
Specifically users running Helicone locally within San Francisco.

**Description** - _We are currently investigating an issue with the TLSv1 Alert Protocol Version. We are working to resolve this issue as quickly as possible._

The issue seems to be with Cloudflare's SSL configuration for their workers, and we are working closely with them to get this resolved.

**Work Around** - If you are experiencing this issue you can revolve it by running a VPN or using our backup workers.

Here is a list of our backup workers:

- https://oai.helicone.ai
- https://oai.helicone.ai
- https://anthropic.helicone.ai
- https://api.helicone.ai
- https://openrouter.helicone.ai
- https://together.helicone.ai
- https://gateway.helicone.ai

To use this change the base URL from `oai.helicone.ai` -> `oai.helicone.ai`

#### Updates

**Update** - _2024-05-27 3:17pm PST_ - Cloudflare responded and is actively investigating the issue.
