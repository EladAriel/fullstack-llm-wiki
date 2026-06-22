---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/queryable-encryption.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

====================

# {+qe+}

## Introduction

{+qe+} lets you perform the following tasks:

- Encrypt sensitive data fields from the client-side.
- Store sensitive data fields as fully randomized encrypted data on the database
server-side.

- Run expressive queries on the encrypted data.
The server has no knowledge of the data it processes.

Sensitive data is encrypted throughout its lifecycle: in-transit, at-rest, in-use, in logs, and in backups. Data is decrypted only on the client-side, since only you have access to the encryption keys.

{+qe+} introduces an industry-first, fast, searchable encryption scheme developed by the pioneers in encrypted search. The feature supports equality and range searches, with additional query types such as prefix, suffix, and substring available in Public Preview.

You can set up {+qe+} using the following mechanisms:

- Automatic Encryption: Enables you to perform encrypted read and
write operations without adding explicit calls to encrypt and decrypt fields.

- {+manual-enc-title+}: Enables you to perform encrypted read and write
operations through your MongoDB driver's encryption library. You must specify the logic for encryption with this library throughout your application.

## Considerations

When implementing an application that uses {+qe+}, consider the points listed in `Security Considerations <qe-csfle-security-considerations>`.

For limitations, see `{+qe+} limitations <qe-reference-encryption-limits>`.

### Compatibility

To learn which MongoDB server products and drivers support {+qe+}, see `qe-compatibility-reference`.

### MongoDB Support Limitations

.. include:: /includes/queryable-encryption/qe-supportability.rst

For details, see `qe-redaction`.

## Features

To learn about the security benefits of {+qe+} for your applications, see the `<qe-features>` page.

## Installation

To learn what you must install to use {+qe+}, see the `<qe-install>` and `<qe-csfle-install-library>` pages.

## Quick Start

To start using {+qe+}, see the `<qe-quick-start>`.

## Fundamentals

To learn about encryption key management, see `qe-reference-keys-key-vaults`.

To learn how {+qe+} works, see the `<qe-fundamentals>` section, which contains the following pages:

- `qe-fundamentals-encrypt-query`
- `qe-create-encryption-schema`
- `qe-fundamentals-collection-management`
- `qe-fundamentals-manual-encryption`
- `qe-fundamentals-manage-keys`
## Tutorials

To learn how to perform specific tasks with {+qe+}, see the `<qe-tutorials>` section.

## Reference

For reference, see the `qe-reference` section.

The reference section contains the following pages:

- `qe-reference-automatic-encryption-supported-operations`
- `qe-reference-mongo-client`
## Contents

- Features </core/queryable-encryption/features>
- Quick Start </core/queryable-encryption/quick-start>
- Fundamentals </core/queryable-encryption/fundamentals>
- Tutorials </core/queryable-encryption/tutorials>
- Reference </core/queryable-encryption/reference>
