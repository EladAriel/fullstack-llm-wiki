---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-enforce-user-cluster-separation-parameter.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

If you set the `enforceUserClusterSeparation` parameter to `false`, the server doesn't distinguish between client certificates, which applications use to authenticate, and intra-cluster certificates, which have privileged access. This has no effect if your `clusterAuthMode` is `keyFile`. However, if your `clusterAuthMode` is `x509`, user certificates that use the allowed scheme are conflated with cluster certificates and granted privileged access.

Your existing certificates are granted internal privileges if you do the following:

1. Create a user, with a name allowed by this parameter.
#. Set the `enforceUserClusterSeparation` parameter to `false`. #. Set `clusterAuthMode` to `x509`.

You must not upgrade from `keyFile` to `x509` without validating that you've removed users with elevated privileges that the `enforceUserClusterSeparation` flag allowed you to create.
