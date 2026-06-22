---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/queryable-encryption/fundamentals/manage-keys.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=================================

# Rotate and Rewrap Encryption Keys

In this guide, you can learn how to manage your encryption keys with a {+kms-long+} ({+kms-abbr+}) in your application.

## Overview

This procedure shows you how to rotate encryption keys for {+qe+} using :binary:`~bin.mongosh`. Rotating DEKs consists of rewrapping them with a new {+cmk-long+}, so the terms "rotate" and "rewrap" are sometimes used interchangeably.

After completing this guide, you should be able to rotate your {+cmk-long+} ({+cmk-abbr+}) on your {+kms-long+}, and then rewrap existing DEKs in your {+key-vault-long+} with your new {+cmk-abbr+}.

> **Warning:** As you rotate keys, confirm that they aren't used to encrypt any keys
or data before deleting them. If you delete a {+dek-abbr+}, all
fields encrypted with that {+dek-abbr+} become permanently
unreadable. If you delete a {+cmk-abbr+}, all fields encrypted with a
{+dek-abbr+} using that {+cmk-abbr+} become permanently unreadable.

### Related Information

For a detailed explanation of the concepts included in this procedure, refer to the topics below.

To learn more about keys and key vaults, see `qe-reference-keys-key-vaults`. To view a list of supported {+kms-abbr+} providers, see the `qe-fundamentals-kms-providers` page.

For tutorials detailing how to set up a {+qe+} enabled application with each of the supported {+kms-abbr+} providers, see `Overview: Enable Queryable Encryption <qe-overview-enable-qe>`.

## Procedure

Your DEKs themselves are left unchanged after re-wrapping them with the new {+cmk-abbr+}. The key rotation process is seamless, and does not interrupt your application.
