---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/queryable-encryption/qe-create-encrypted-collection.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
