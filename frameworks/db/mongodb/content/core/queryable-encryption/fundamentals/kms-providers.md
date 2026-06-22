---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/queryable-encryption/fundamentals/kms-providers.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=============

# KMS Providers

## Overview

Learn about the {+kms-long+} ({+kms-abbr+}) providers {+in-use-encryption+} supports.

## Reasons to Use a Remote {+kms-long+}

Using a remote {+kms-long+} to manage your {+cmk-long+} has the following advantages over using your local filesystem to host it:

- Secure storage of the key with access auditing
- Reduced risk of access permission issues
- Availability and distribution of the key to remote clients
- Automated key backup and recovery
- Centralized encryption key lifecycle management
Additionally, for the following {+kms-abbr+} providers, your {+kms-abbr+} remotely encrypts and decrypts your {+dek-long+}, ensuring your {+cmk-long+} is never exposed to your {+qe+} or {+csfle-abbrev+} enabled application:

- {+aws-long+} KMS
- {+azure-kv+}
- {+gcp-kms-abbr+}
## {+kms-long+} Tasks

In {+in-use-encryption+}, your {+kms-long+}:

- Creates and encrypts the {+cmk-long+}
- Encrypts the {+dek-long+}s created by your application
- Decrypts {+dek-long+}s
To learn more about {+cmk-long+}s and {+dek-long+}s, see `qe-reference-keys-key-vaults`.

### Create and Store your {+cmk-long+}

To create a {+cmk-long+}, configure your {+kms-long+} to generate your {+cmk-long+} as follows:

.. image:: /images/CSFLE_Master_Key_KMS.png

To view a tutorial that demonstrates how to create and store a {+cmk-abbr+} in your preferred {+kms-abbr+}, see the `{+qe+} Automatic Encryption Tutorial <qe-tutorial-automatic-encryption>` or `{+csfle-abbrev+} Automatic Encryption Tutorial <csfle-tutorial-automatic-encryption>`.

### Create and Encrypt a {+dek-long+}

To create a {+dek-long+}:

- Instantiate a `ClientEncryption` instance in your
{+qe+} or {+csfle-abbrev+} enabled application:

- Provide a `kmsProviders` object that specifies the credentials
your application uses to authenticate with your {+kms-abbr+} provider.

- Create a {+dek-long+} with the `CreateDataKey` method of the
`ClientEncryption` object in your application.

- Provide a `dataKeyOpts` object that specifies with which key
your {+kms-abbr+} should encrypt your new {+dek-long+}.

To view a tutorial demonstrating how to create and encrypt a {+dek-long+}, see the following resources:

- `{+qe+} Quick Start <qe-quick-start>`
- :ref:`{+qe+} Automatic Encryption Tutorial
<qe-tutorial-automatic-encryption>`

- `{+csfle-abbrev+} Quick Start <csfle-quick-start>`
- `{+csfle-abbrev+} Automatic Encryption Tutorial <csfle-tutorial-automatic-encryption>`
To view the structure of `kmsProviders` and `dataKeyOpts` objects for all supported {+kms-abbr+} providers, see `qe-fundamentals-kms-providers-supported-kms`.

## Supported Key Management Services

The following sections of this page present the following information for all {+kms-long+} providers:

- Architecture of {+in-use-encryption+} enabled client
- Structure of `kmsProviders` objects
- Structure of `dataKeyOpts` objects
Both {+qe+} and {+csfle-abbrev+} support the following {+kms-long+} providers:

- `qe-fundamentals-kms-providers-aws`
- `qe-fundamentals-kms-providers-azure`
- `qe-fundamentals-kms-providers-gcp`
- `qe-fundamentals-kms-providers-kmip`
- `qe-fundamentals-kms-providers-local`
### Amazon Web Services KMS

This section provides information related to using [AWS Key Management Service](https://aws.amazon.com/kms/) in your {+qe+} or {+csfle-abbrev+} enabled application.

To view a tutorial demonstrating how to use AWS KMS in your application, see `Overview: Enable Queryable Encryption <qe-overview-enable-qe>` or `csfle-tutorial-automatic-aws`.

.. include:: /includes/queryable-encryption/reference/kms-providers/aws.rst

### Azure Key Vault

This section provides information related to using [Azure Key Vault](https://azure.microsoft.com/en-us/services/key-vault/) in your {+qe+} or {+csfle-abbrev+} enabled application.

To view a tutorial demonstrating how to use Azure Key Vault in your application, see `Overview: Enable Queryable Encryption <qe-overview-enable-qe>` or `csfle-tutorial-automatic-azure`.

.. include:: /includes/queryable-encryption/reference/kms-providers/azure.rst

### Google Cloud Platform KMS

This section provides information related to using [Google Cloud Key Management](https://cloud.google.com/security-key-management) in your {+qe+} or {+csfle-abbrev+} enabled application.

To view a tutorial demonstrating how to use GCP KMS in your application, see `Overview: Enable Queryable Encryption <qe-overview-enable-qe>` or `csfle-tutorial-automatic-gcp`.

.. include:: /includes/queryable-encryption/reference/kms-providers/gcp.rst

### KMIP

This section provides information related to using a [KMIP](https://docs.oasis-open.org/kmip/spec/v1.0/os/kmip-spec-1.0-os.html) compliant {+kms-long+} in your {+qe+} or {+csfle-abbrev+} enabled application.

To learn how to set up KMIP with HashiCorp Vault, see [Manage client encryption keys with Vault as a KMIP server](https://developer.hashicorp.com/vault/tutorials/enterprise/kmip-engine)_ in the HashiCorp Vault documentation.

.. include:: /includes/queryable-encryption/reference/kms-providers/kmip.rst

### Local Key Provider

This section provides information related to using a Local Key Provider in your {+qe+} or {+csfle-abbrev+} enabled application.

.. include:: /includes/queryable-encryption/qe-warning-local-keys.rst

To view a tutorial demonstrating how to use a Local Key Provider for testing {+qe+}, see the `{+qe+} Quick Start <qe-quick-start>` or `{+csfle-abbrev+} Quick Start <csfle-quick-start>`.

.. include:: /includes/queryable-encryption/reference/kms-providers/local.rst
