---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/8.0/references/rest-api/objects/sso.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.669528Z"
---
# Sso

---
Title: SSO object
alwaysopen: false
categories:
- docs
- operate
- rs
description: An object for single sign-on (SSO) configuration
linkTitle: sso
weight: $weight
url: '/operate/rs/8.0/references/rest-api/objects/sso/'
---

An API object that represents single sign-on (SSO) configuration in the cluster.

| Name | Type/Value | Description |
|------|------------|-------------|
| control_plane | boolean (default: false) | If `true`, enables single sign-on (SSO) for the control plane. |
| enforce_control_plane | boolean (default: false) | If `true`, enforce SSO login for the control plane for non-admin users. If `false`, all users can still login using their local username and password if SSO is down. |
| protocol | "saml2" | SSO protocol to use. |
| issuer | complex object	 | Issuer related configuration.<br>Contains the following fields:<br>**id**: Unique ID of the issuer side (example: "urn:sso:example:idp")<br>**login_url**: SSO login URL (example: "https://idp.example.com/sso/saml")<br>**logout_url**: SSO logout URL (example: "https://idp.example.com/sso/slo")<br />**metadata**: Base64 encoded IdP metadata (read-only) |
| service | complex object	 | Service related configuration.<br />For SAML2 service configuration:<br />{{<code>}}{
  "address": "string",
  "saml2": {
    "entity_id": "string",
    "acs_url": "string",
    "slo_url": "string"
  }
}{{</code>}}<br>**address**: External service address used for SSO. By default, the cluster name with the Cluster Manager port is used.<br />**acs_url**: Assertion Consumer Service URL (read-only)<br>**slo_url**: Single Logout URL (read-only)<br>**entity_id**: Service entity ID (read-only) |
