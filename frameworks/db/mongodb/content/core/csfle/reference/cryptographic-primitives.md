---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/csfle/reference/cryptographic-primitives.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.812315Z"
---
.. _csfle-reference-cryptographic-primitives:
.. _qe-cryptographic-primitives:

# Cryptographic Primitives

**meta:** :description: Understand how MongoDB uses AEAD AES-256-CBC and HMAC-SHA-256 for field-level encryption.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 2
   :class: singlecol

MongoDB encrypts all fields in {+qe+} and {+csfle-abbrev+} with the `AEAD <https://en.wikipedia.org/wiki/Authenticated_encryption#Authenticated_encryption_with_associated_data>`__
AES-256-CBC encryption algorithm.

- With {+qe+}, ciphertext is always non-deterministic.

- With {+csfle-abbrev+}, if you specify deterministic encryption for a field,
  your application passes a deterministic initialization vector to AEAD.
  
- With {+csfle-abbrev+}, if you specify random encryption for a field, your
  application passes a random initialization vector to AEAD.

**note:** Authenticated Encryption

   MongoDB uses the  `encrypt-then-MAC
   <https://en.wikipedia.org/wiki/Authenticated_encryption#Encrypt-then-MAC_(EtM)>`__
   approach to perform authenticated encryption. Both {+qe+} and
   {+csfle-abbrev+} use the HMAC-SHA-256 algorithm to generate your
   MAC.