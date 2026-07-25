---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/security-in-use-encryption.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=================

# In-Use Encryption

.. include:: /includes/in-use-encryption-intro.rst

## Choosing an In-Use Encryption Approach

You can use both {+qe+} and {+csfle+} in the same deployment, but they are incompatible with each other in the same collection. For a comparison of the two, including compatibility with MongoDB versions and points to consider when choosing one or the other, see `Choosing an In-Use Encryption Approach <about-qe-csfle>`.

## Encryption Keys and Key Vaults

Both {+qe+} and {+csfle+} use an `envelope encryption` approach to encrypt data, where an encrypted field in a document uses a unique `Data Encryption Key`, and those keys are encrypted using a `Customer Master Key`.

For details, see `<qe-reference-keys-key-vaults>`.

## {+qe+}

To learn how {+qe+} and its components work and how to implement it in your application, see `<qe-manual-feature-qe>`.

## {+csfle+}

To learn how {+csfle+} and its components work and how to implement it in your application, see `<manual-csfle-feature>`.

## Contents

- Comparing Approaches </core/queryable-encryption/about-qe-csfle>
- Compatibility </core/queryable-encryption/reference/compatibility>
- Cryptography </core/csfle/reference/cryptographic-primitives>
- Keys and Key Vaults </core/queryable-encryption/fundamentals/keys-key-vaults>
- Queryable Encryption </core/queryable-encryption>
- Client-Side Field Level Encryption </core/csfle>
