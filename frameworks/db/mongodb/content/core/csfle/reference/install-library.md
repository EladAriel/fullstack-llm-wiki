---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/csfle/reference/install-library.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================================================

# Install and Configure a CSFLE Query Analysis Component

MongoDB uses the {+shared-library+} (recommended) or the `mongocryptd` executable process to translate queries into encrypted queries, and to encrypt or decrypt data.

## Before You Begin

To use CSFLE with automatic encryption, you must first choose the query analysis component you want MongoDB to use to encrypt the fields.

- `crypt_shared <csfle-reference-install-shared-lib>`, the
recommended CSFLE library.

- :ref:`mongocryptd
<csfle-reference-install-mongocryptd>`, which is included in MongoDB Enterprise Server installations.

The `libmongocrypt` library and MongoDB drivers require the {+shared-library+} or `mongocryptd` to interpret encrypted queries. For more information, see `csfle-reference-libmongocrypt`.

### {+shared-library+}

The {+shared-library+} is a **dynamic library** that enables your client application to perform automatic encryption. A dynamic library is a set of functionality accessed by an application at runtime rather than compile time. The {+shared-library+} performs the following tasks:

- Reads the encryption schema to determine which fields to
encrypt or decrypt

- Prevents your application from executing unsupported
operations on encrypted fields

The {+shared-library+} does not do any of the following:

- Perform data encryption or decryption
- Access the encryption key material
- Listen for data over the network
The {+shared-library+} is a preferred alternative to `mongocryptd` and does not require you to spawn another process to perform automatic encryption.

> **Note:** While we recommend using the {+shared-library+}, `mongocryptd` is still supported.

To learn more about automatic encryption, see `<csfle-features>`.

### mongocryptd

`mongocryptd` is installed with [MongoDB Enterprise Server]({+enterprise-download-link+})_.

When you create a CSFLE-enabled MongoDB client, the `mongocryptd` process starts automatically by default.

.. include:: /includes/queryable-encryption/qe-facts-mongocryptd-process.rst

The official MongoDB drivers require access to the `mongocryptd` process on the client host machine. These clients search for the `mongocryptd` process in the system `PATH` by default.

## Steps

Select the query analysis component you want to use and follow the steps to install and configure a CSFLE query analysis component.
