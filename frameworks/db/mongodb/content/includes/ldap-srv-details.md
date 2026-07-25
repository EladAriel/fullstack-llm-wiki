---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/ldap-srv-details.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

If your connection string specifies `"srv:<DNS_NAME>"`, |ldap-binary| verifies that `"_ldap._tcp.gc._msdcs.<DNS_NAME>"` exists for SRV to support Active Directory. If not found, |ldap-binary| verifies that `"_ldap._tcp.<DNS_NAME>"` exists for SRV. If an SRV record cannot be found, |ldap-binary| warns you to use `"srv_raw:<DNS_NAME>"` instead.

If your connection string specifies `"srv_raw:<DNS_NAME>"`, |ldap-binary| performs an SRV record lookup for `"<DNS NAME>"`.
