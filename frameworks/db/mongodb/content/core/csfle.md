---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/csfle.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================================

# {+csfle+}

## Introduction

{+csfle+} ({+csfle-abbrev+}) enables you to encrypt data in your application before you send it over the network to MongoDB. With {+csfle-abbrev+} enabled, no MongoDB product has access to your data in an unencrypted form.

You can set up {+csfle-abbrev+} using the following mechanisms:

- Automatic Encryption: Enables you to perform encrypted read and
write operations without adding explicit calls to encrypt and decrypt fields.

- {+manual-enc-title+}: Enables you to perform encrypted read and write
operations through your MongoDB driver's encryption library. You must specify the logic for encryption with this library throughout your application.

## Considerations

When implementing an application that uses {+csfle+}, consider the points listed in `Security Considerations <qe-csfle-security-considerations>`.

For limitations, see `{+csfle-abbrev+} limitations <csfle-reference-encryption-limits>`.

### Compatibility

To learn which MongoDB server products and drivers support {+csfle-abbrev+}, see `csfle-compatibility-reference`.

## Features

To learn about the security benefits of {+csfle-abbrev+} for your applications, see the `<csfle-features>` page.

## Installation

To learn what you must install to use {+csfle-abbrev+}, see the `<csfle-install>` page.

## Quick Start

To start using {+csfle-abbrev+}, see the `<csfle-quick-start>`.

.. include:: /includes/fact-csfle-placeholder.rst

## Fundamentals

To learn how {+csfle-abbrev+} works and how to set it up, see the `<csfle-fundamentals>` section.

The fundamentals section contains the following pages:

- `csfle-fundamentals-automatic-encryption`
- `csfle-fundamentals-manual-encryption`
- `csfle-fundamentals-create-schema`
- `csfle-fundamentals-manage-keys`
- `csfle-reference-encryption-algorithms`
## Tutorials

To learn how to perform specific tasks with {+csfle-abbrev+}, see the `<csfle-tutorials>` section.

## Reference

To learn about encryption key management, see `qe-reference-keys-key-vaults`.

For reference on {+csfle-abbrev+}-enabled applications, see the `csfle-reference` section:

- `csfle-reference-encryption-schemas`
- `csfle-reference-server-side-schema`
- `csfle-reference-automatic-encryption-supported-operations`
- `csfle-reference-mongo-client`
- `csfle-reference-encryption-components`
- `csfle-reference-decryption`
- `csfle-reference-cryptographic-primitives`
- `csfle-reference-mongocryptd`
- `csfle-reference-libmongocrypt`
## Contents

- Features </core/csfle/features>
- Installation </core/csfle/install>
- Quick Start </core/csfle/quick-start>
- Fundamentals </core/csfle/fundamentals>
- Tutorials </core/csfle/tutorials>
- Reference </core/csfle/reference>
