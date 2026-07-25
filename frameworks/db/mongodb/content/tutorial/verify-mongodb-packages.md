---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/verify-mongodb-packages.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

:orphan:

====================================

# Verify Integrity of MongoDB Packages

.. include:: /includes/minor-release.rst

.. include:: /includes/unicode-checkmark.rst

The MongoDB release team digitally signs all software packages to certify that a particular MongoDB package is a valid and unaltered MongoDB release. Before installing MongoDB, you should validate the package using either the provided PGP signature or SHA-256 checksum.

PGP signatures provide the strongest guarantees by checking both the authenticity and integrity of a file to prevent tampering.

Cryptographic checksums only validate file integrity to prevent network transmission errors.

## Verify Linux/macOS Packages

### Use PGP/GPG

MongoDB signs each release branch with a different PGP key. The public key files for each release branch are available for download from the [key server](https://pgp.mongodb.com/) in both textual `.asc` and binary `.pub` formats.

.. include:: /includes/steps/install-verify-files-pgp.rst

### Use SHA-256

.. include:: /includes/steps/install-verify-files-sha.rst

## Verify Windows Packages

The following procedure verifies the MongoDB binary against its SHA256 key.

.. include:: /includes/steps/install-verify-files-windows.rst
