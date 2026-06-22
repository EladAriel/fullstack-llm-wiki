---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/list-cluster-x509-requirements.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

- Cluster member configuration must specify a non-empty value for
at least one of the attributes used for authentication. By default, MongoDB accepts:

- the Organization (`O`)
- the Organizational Unit (`OU`)
- the Domain Component (`DC`)
MongoDB verifies that entries match exactly across all member certificates. If you list multiple `OU` values, all certificates must use an identical list.

You can specify alternative attributes to use for authentication by setting :setting:`net.tls.clusterAuthX509.extensionValue`.

- Cluster member configuration must include the same
:setting:`net.tls.clusterAuthX509.attributes` and use matching values. Attribute order doesn't matter. The following example sets `O` and `OU`, but not `DC`:

```yaml
   net:
     tls:
       clusterAuthX509:
         attributes: O=MongoDB, OU=MongoDB Server
```
