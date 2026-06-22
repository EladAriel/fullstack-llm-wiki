---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/queryable-encryption/install-library.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

================================================

# Install and Configure a Query Analysis Component

MongoDB uses the {+shared-library+} (recommended) or the `mongocryptd` executable process to translate queries into encrypted queries, and to encrypt or decrypt data.

## Before You Start

Follow the preceding tasks to `install a {+qe+} compatible driver and dependencies <qe-install>` before continuing.

## Choose a Query Analysis Component

### {+shared-library+}

The {+shared-library+} is a **dynamic library** that enables your client application to perform automatic encryption. A dynamic library is a set of functionality accessed by an application at runtime rather than compile time. The {+shared-library+} performs the following tasks:

- Reads the `{+enc-schema+} <qe-encryption-schema>` to determine which fields to encrypt or decrypt
- Prevents your application from executing unsupported operations on
encrypted fields

The {+shared-library+} does not do any of the following:

- Perform data encryption or decryption
- Access the encryption key material
- Listen for data over the network
The {+shared-library+} is a preferred alternative to `mongocryptd` and doesn't require you to start another process to perform automatic encryption.

### mongocryptd

> **Important:** If you are starting a new project, use the {+shared-library+}. The
{+shared-library+} replaces `mongocryptd` and does not require
you to start a new process.

`mongocryptd` is installed with [MongoDB Enterprise Server]({+enterprise-download-link+})_.

When you create a MongoDB client with {+in-use-encryption+}, the `mongocryptd` process starts automatically by default.

.. include:: /includes/queryable-encryption/qe-facts-mongocryptd-process.rst

## Procedure

## Next Steps

After installing a query analysis component, `create a {+cmk-long+} <qe-create-cmk>` in your {+kms-long+} of choice.
