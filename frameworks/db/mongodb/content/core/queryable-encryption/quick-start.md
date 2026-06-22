---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/queryable-encryption/quick-start.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

================================

# {+qe+} Quick Start

## Overview

This guide shows you how to build an application that implements the MongoDB {+qe+} feature to automatically encrypt and decrypt document fields.

Select your driver language in the dropdown menu on the right to learn how to create an application that automatically encrypts and decrypts document fields.

> **Note:** MongoDB Community Edition `doesn't support <qe-csfle-compatibility>`
{+qe+} with Automatic Encryption. You must use MongoDB Atlas or MongoDB
Enterprise Advanced to implement this sample application.

.. include:: /includes/queryable-encryption/quick-start/production-warning.rst

## Before You Get Started

> **Warning:** Version 8.2.0 of `mongocryptd` might not run on Windows.
This bug affects `In-Use Encryption <security-in-use-encryption>`
with the MongoDB .NET/C# driver and might affect other drivers based
on your `mongocryptd` spawn arguments.
To learn more about this issue and how to resolve it, see `8.2-known-issues`
in the MongoDB 8.2 Release Notes.

.. include:: /includes/queryable-encryption/set-up-section.rst

### Full Application Code

To see the complete code for the sample application, select your programming language in the language selector.

## Procedure

## Learn More

To view a tutorial on production-ready {+qe+} with a remote KMS, see `<qe-tutorial-automatic-encryption>`.

To learn how {+qe+} works, see `<qe-fundamentals>`.

To learn more about the topics mentioned in this guide, see the following links:

- Learn more about {+qe+} components on the `Reference <qe-reference>` page.
- Learn how {+cmk-long+}s and {+dek-long+}s work on the `<qe-reference-keys-key-vaults>` page.
- See how KMS Providers manage your {+qe+} keys on the `<qe-fundamentals-kms-providers>` page.
