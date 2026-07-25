---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/queryable-encryption/qe-create-encrypted-collection.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

===================================================

# Create an Encrypted Collection and Insert Documents

## Overview

This guide shows you how to create a {+qe+}-enabled collection and insert a document with encrypted fields.

After you complete the steps in this guide, you should be able to create an encrypted collection and insert a document with fields that are encrypted with your {+cmk-long+}.

## Before You Start

`Create your {+qe+}-enabled application <qe-create-application>` before creating an encrypted collection.

If you are using `{+manual-enc+} <qe-fundamentals-manual-encryption>`, you must also create a unique {+dek-long+} for each encrypted field in advance. For more information, see `qe-reference-keys-key-vaults`.

## Procedure

## Next Steps

After creating a {+qe+}-enabled collection, you can `query the encrypted fields <qe-query-encrypted-document>`.
