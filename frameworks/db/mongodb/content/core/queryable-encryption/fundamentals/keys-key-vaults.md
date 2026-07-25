---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/queryable-encryption/fundamentals/keys-key-vaults.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

==============================

# Encryption Keys and Key Vaults

## Overview

In this guide, you can learn details about the following components of {+in-use-encryption+}:

- {+dek-long+}s ({+dek-abbr+})s
- {+cmk-long+}s ({+cmk-abbr+})s
- {+key-vault-long+}s
- {+kms-long+} ({+kms-abbr+})
To view step by step guides demonstrating how to use the preceding components to set up a {+qe+} or {+csfle+} enabled client, see the following resources:

- `{+qe+} Quick Start <qe-quick-start>`
- :ref:`{+qe+} Automatic Encryption Tutorial
<qe-tutorial-automatic-encryption>`

- `{+csfle-abbrev+} Quick Start <csfle-quick-start>`
- `{+csfle-abbrev+} Automatic Encryption Tutorial <csfle-tutorial-automatic-encryption>`
## Data Encryption Keys and the Customer Master Key

.. include:: /includes/queryable-encryption/qe-csfle-about-dek-cmk-keys.rst

.. include:: /includes/queryable-encryption/qe-csfle-warning-remote-kms.rst

### Key Rotation

.. include:: /includes/queryable-encryption/qe-csfle-key-rotation.rst

For details on rotating keys, see `Rotate Encryption Keys <qe-fundamentals-manage-keys>`.

## {+key-vault-long-title+}s

.. include:: /includes/queryable-encryption/qe-csfle-about-key-vault-collections.rst

To view diagrams detailing how your {+dek-abbr+}, {+cmk-abbr+}, and {+key-vault-long+} interact in all supported {+kms-abbr+} provider architectures, see `qe-fundamentals-kms-providers`.

### {+key-vault-long+} Name

.. include:: /includes/fact-csfle-qe-keyvault-name.rst

### Permissions

.. include:: /includes/queryable-encryption/qe-csfle-key-vault-permissions.rst

To learn how to grant your application access to your {+cmk-long+}, see the `{+qe+} Automatic Encryption Tutorial <qe-tutorial-automatic-encryption>` or `{+csfle-abbrev+} Automatic Encryption Tutorial <csfle-tutorial-automatic-encryption>`.

### Key Vault Cluster

.. include:: /includes/queryable-encryption/qe-csfle-key-vault-cluster.rst

To specify the cluster that hosts your {+key-vault-long+}, use the `keyVaultClient` field of your client's `MongoClient` object. To learn more about the specific configuration options in your client's `MongoClient` object, see the `MongoClient Options for {+qe+} <qe-reference-mongo-client>` or `MongoClient Options for {+csfle-abbrev+} <csfle-reference-mongo-client>`.

### Update a {+key-vault-long-title+}

.. include:: /includes/in-use-encryption/update-a-key.rst

To view a tutorial that shows how to create a {+dek-long+}, see the `{+qe+} Quick Start <qe-quick-start>` or the `{+csfle-abbrev+} Quick Start <csfle-local-create-dek>`.

## Contents

- KMS Providers </core/queryable-encryption/fundamentals/kms-providers>
