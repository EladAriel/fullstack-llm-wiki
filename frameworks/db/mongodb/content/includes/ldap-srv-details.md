---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/ldap-srv-details.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

If your connection string specifies `"srv:<DNS_NAME>"`, |ldap-binary| verifies that `"_ldap._tcp.gc._msdcs.<DNS_NAME>"` exists for SRV to support Active Directory. If not found, |ldap-binary| verifies that `"_ldap._tcp.<DNS_NAME>"` exists for SRV. If an SRV record cannot be found, |ldap-binary| warns you to use `"srv_raw:<DNS_NAME>"` instead.

If your connection string specifies `"srv_raw:<DNS_NAME>"`, |ldap-binary| performs an SRV record lookup for `"<DNS NAME>"`.
