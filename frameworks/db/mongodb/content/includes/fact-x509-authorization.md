---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-x509-authorization.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

When the server authenticates connections from members, it analyzes the X.509 certificate to determine whether it belongs to a cluster member. If the server uses the :setting:`~net.tls.clusterAuthX509.attributes` setting or the `attributes` field on the :parameter:`tlsClusterAuthX509Override` parameter, it checks the Distinguished Name (DN) values of the certificate. If the :setting:`~net.tls.clusterAuthX509.extensionValue` setting or the `extensionValue` field of the :parameter:`tlsClusterAuthX509Override` parameter is set, it checks the extension values of the certificate.  If it finds a match, it authorizes the connection as a peer.
