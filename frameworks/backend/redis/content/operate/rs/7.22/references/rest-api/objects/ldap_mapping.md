---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.22/references/rest-api/objects/ldap_mapping.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.381551Z"
---
# Ldap_Mapping

---
Title: LDAP mapping object
alwaysopen: false
categories:
- docs
- operate
- rs
description: An object that represents a mapping between an LDAP group and roles
linkTitle: ldap_mapping
weight: $weight
url: '/operate/rs/7.22/references/rest-api/objects/ldap_mapping/'
---

An API object that represents an [LDAP mapping]({{< relref "/operate/rs/7.22/security/access-control/ldap/map-ldap-groups-to-roles" >}}) between an LDAP group and [roles]({{< relref "/operate/rs/7.22/references/rest-api/objects/role" >}}).

| Name | Type/Value | Description |
|------|------------|-------------|
| uid | integer | LDAP mapping's unique ID |
| account_id | integer | SM account ID |
| action_uid | string | Action UID. If it exists, progress can be tracked by the `GET`&nbsp;`/actions/{uid}` API (read-only) |
| bdbs_email_alerts | complex object | UIDs of databases that associated email addresses will receive alerts for |
| cluster_email_alerts | boolean | Activate cluster email alerts for an associated email |
| dn | string | An LDAP group's distinguished name |
| email | string | Email address used for alerts (if set) |
| email_alerts | boolean (default:&nbsp;true) | Activate email alerts for an associated email |
| name | string | Role's name |
| role_uids | array of integers | List of role UIDs associated with the LDAP group |
