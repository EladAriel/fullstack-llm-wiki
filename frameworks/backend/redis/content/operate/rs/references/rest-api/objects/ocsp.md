---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/references/rest-api/objects/ocsp.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: OCSP object
alwaysopen: false
categories:
- docs
- operate
- rs
description: An object that represents the cluster's OCSP configuration
linkTitle: ocsp
weight: $weight
---

An API object that represents the cluster's OCSP configuration.

| Name | Type/Value | Description |
|------|------------|-------------|
| ocsp_functionality | boolean (default:&nbsp;false) | Enables or turns off OCSP for the cluster |
| query_frequency | integer <nobr>(range: 60-86400)</nobr> (default:&nbsp;3600) | The time interval in seconds between OCSP queries to check the certificate’s status |
| recovery_frequency | integer <nobr>(range: 60-86400)</nobr> (default:&nbsp;60) | The time interval in seconds between retries after the OCSP responder returns an invalid status for the certificate |
| recovery_max_tries | integer <nobr>(range: 1-100)</nobr> (default:&nbsp;5) | The number of retries before the validation query fails and invalidates the certificate |
| responder_url | string | The OCSP server URL embedded in the proxy certificate (if available) (read-only) |
| response_timeout | integer <nobr>(range: 1-60)</nobr> (default:&nbsp;1) | The time interval in seconds to wait for a response before timing out |
