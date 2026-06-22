---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/queryable-encryption/tutorials/automatic/named-kms-note-local.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

You can also provide a custom name for your KMS provider by passing in a string that includes the name of the KMS provider, followed by a colon and the custom name. Providing a unique name for a KMS provider allows you to specify multiple KMS providers of the same type.

The following example shows an object that sets a the KMS provider name to "my_kms_provider":

```json
{
    "local:my_kms_provider": {
       { "key" : "<local CMK>" }
    },
}
```
