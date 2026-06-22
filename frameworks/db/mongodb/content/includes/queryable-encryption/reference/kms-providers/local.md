---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/queryable-encryption/reference/kms-providers/local.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Architecture ````````````

When you use a Local Key Provider for testing, your application retrieves your {+cmk-long+} from the computer it runs on. To use a Local Key Provider in production, use an approach that doesn't store the key on the file system. For example, you can inject the key into the client process via a sidecar.

The following diagram describes the architecture of a {+qe+}-enabled application using a Local Key Provider.

.. image:: /images/CSFLE_Data_Key_Local.png

kmsProviders Object ```````````````````

The following table presents the structure of a `kmsProviders` object for a Local Key Provider:

dataKeyOpts Object ``````````````````

When you use a Local Key Provider, you specify your {+cmk-long+} through your `kmsProviders` object.
