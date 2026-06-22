---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/queryable-encryption/reference/kms-providers/kmip.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Architecture ````````````

The following diagram describes the architecture of a {+qe+} enabled application using a {+kmip-kms+}.

.. image:: /images/CSFLE_Data_Key_KMIP.png

> **Important:** When your {+qe+} enabled application uses
a {+kmip-kms+} without specifying the `delegated` option, your application
directly accesses your {+cmk-long+}. To avoid directly accessing your
{+cmk-abbr+}, you can set the `delegated` option to `true` in your
`dataKeyOpts object <qe-fundamentals-kms-providers-kmip-datakeyopts>`.

kmsProviders Object ```````````````````

The following table presents the structure of a `kmsProviders` object for a KMIP compliant {+kms-long+}:

> **Note:** Your {+qe+} enabled application authenticates through
:abbr:`TLS/SSL (Transport Layer Security/Secure Sockets Layer)`
when using KMIP.

dataKeyOpts Object ``````````````````

The following table presents the structure of a `dataKeyOpts` object for a KMIP compliant {+kms-long+}:
