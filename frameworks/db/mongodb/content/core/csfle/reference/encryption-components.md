---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/csfle/reference/encryption-components.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.813050Z"
---
.. _csfle-reference-encryption-components:
.. _csfle-encryption-components:

# CSFLE Encryption Components

**meta:** :description: Discover CSFLE encryption components in MongoDB: ``libmongocrypt``, ``mongocryptd``, Key Vault collection, and Key Management System for data protection.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 2
   :class: singlecol

## Diagram

The following diagram illustrates the relationships between a MongoDB
driver or :binary:`~bin.mongosh` and each component of {+csfle+}
({+csfle-abbrev+}):

**figure:** /images/client-side-field-level-encryption-diagram.svg
   :alt: Diagram of relationships between driver and encryption components
   :figwidth: 600px

## Components

The following sections discuss the individual components of the preceding
diagram.

### libmongocrypt

``libmongocrypt`` is the `Apache-licensed open-source
<https://github.com/mongodb/libmongocrypt>`__ core cryptography
library used by the official MongoDB drivers and :binary:`~bin.mongosh` to 
power {+csfle+}. Some drivers may require specific integration steps to install 
or link the library.

To view steps for installing ``libmongocrypt``,
see the :ref:`libmongocrypt reference page <csfle-reference-libmongocrypt>`.

### mongocryptd

``mongocryptd`` supports automatic encryption and is only available
with MongoDB Enterprise. ``mongocryptd`` does not perform
cryptographic functions.

To learn more about ``mongocryptd``, see
:ref:`csfle-reference-mongocryptd`.

### {+key-vault-long+}

The {+key-vault-long+} is a standard MongoDB collection
that stores all {+dek-long+}s used to encrypt application data.
{+dek-long+}s are themselves encrypted using a {+cmk-long+}
({+cmk-abbr+}) prior to storage in the {+key-vault-long+}. You can host
your {+key-vault-long+} on a different MongoDB cluster than
the cluster storing your encrypted application data.

To learn more about the {+key-vault-long+}, see
:ref:`qe-reference-keys-key-vaults`.

### {+kms-long+}

The {+kms-long+} ({+kms-abbr+}) stores the
{+cmk-long+} ({+cmk-abbr+}) used to encrypt {+dek-long+}s.

To view a list of all {+kms-abbr+} providers MongoDB supports,
see :ref:`qe-fundamentals-kms-providers`.

### MongoDB Cluster

The MongoDB cluster which stores the encrypted data may also enforce
{+csfle+}. For more information on server-side schema enforcement,
see :ref:`csfle-reference-server-side-schema`.