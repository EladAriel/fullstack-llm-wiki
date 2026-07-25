---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/csfle/reference/cryptographic-primitives.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

========================

# Cryptographic Primitives

MongoDB encrypts all fields in {+qe+} and {+csfle-abbrev+} with the [AEAD](https://en.wikipedia.org/wiki/Authenticated_encryption#Authenticated_encryption_with_associated_data)_ AES-256-CBC encryption algorithm.

- With {+qe+}, ciphertext is always non-deterministic.
- With {+csfle-abbrev+}, if you specify deterministic encryption for a field,
your application passes a deterministic initialization vector to AEAD.

- With {+csfle-abbrev+}, if you specify random encryption for a field, your
application passes a random initialization vector to AEAD.

> **Note:** MongoDB uses the  `encrypt-then-MAC
<https://en.wikipedia.org/wiki/Authenticated_encryption#Encrypt-then-MAC_(EtM)>`__
approach to perform authenticated encryption. Both {+qe+} and
{+csfle-abbrev+} use the HMAC-SHA-256 algorithm to generate your
MAC.
