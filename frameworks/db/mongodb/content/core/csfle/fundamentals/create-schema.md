---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/csfle/fundamentals/create-schema.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================

# Encryption Schemas

## Overview

On this page, you can learn how to create an encryption schema for automatic {+csfle+} ({+csfle-abbrev+}) as well as see an example detailing how to create the encryption schema used in the {+csfle-abbrev+} `Quick Start <csfle-quick-start>`.

## Encryption Schemas

An encryption schema is a JSON object which uses a strict subset of [JSON Schema Draft 4 standard syntax](https://tools.ietf.org/html/draft-zyp-json-schema-04) along with the keywords `encrypt` and `encryptMetadata` to define the **encryption rules** that specify how your {+csfle-abbrev+}-enabled client should encrypt your documents.

Encryption rules are JSON key-value pairs that define how your client application encrypts your fields. You must specify or inherit the following information in an encryption rule:

- The algorithm used to encrypt your field
- Which {+dek-long+} (DEK) your client uses to encrypt your field
- The [BSON](https://bsonspec.org/)_ type of your field
Encryption rules must contain either the `encrypt` or `encryptMetadata` keyword.

To learn more about the encryption algorithms you can define in your encryption schema, see `<csfle-reference-encryption-algorithms>`.

To learn more about {+dek-long+}s, see `qe-reference-keys-key-vaults`.

### encrypt Keyword

The `encrypt` keyword defines an encryption rule for a single field in a BSON document. Encryption rules containing the `encrypt` keyword have the following structure:

### encryptMetadata Keyword

The `encryptMetadata` keyword defines encryption rules which child elements of the sibling `properties` tag inherit. Encryption rules containing `encryptMetadata` have the following structure:

### patternProperties Keyword

You can use the `patternProperties` keyword in your encryption schema to define encryption rules for all fields with names that match a regular expression. This allows you to specify multiple fields for encryption based on a single regular expression, or to specify them by only using a part of the field name. The `patternProperties` keyword replaces `properties` in your encryption schema.

Specify encryption rules with `patternProperties` using the following structure:

To see an example of how to use `patternProperties` see `field-level-encryption-auto-encrypt-with-pattern-properties`

## Example

This example explains how to generate the encryption schema used in the `Create an Encryption Schema For Your Documents <csfle-quickstart-encryption-schema>` step of the {+csfle-abbrev+} Quick Start.

In the Quick Start, you insert documents with the following structure into the `patients` collection of the `medicalRecords` database:

### Specify the Namespace

At the root of your encryption schema, specify the namespace to which your encryption schema applies. Specify the following to encrypt and decrypt documents in the `patients` collection of the `medicalRecords` database:

### Specify the {+dek-long+}

In the Quick Start, you encrypt all fields of your document with a single {+dek-long+} (DEK). To configure all fields in your documents to use a single DEK for encryption and decryption, specify the `_id` of your DEK with the `encryptMetadata` keyword at the root of your encryption schema as follows:

### Choose Encryption Rules

You decide to encrypt the following fields with the following encryption algorithms:

You choose to encrypt the `ssn` and `insurance.policyNumber` fields with deterministic encryption for the following reasons:

- You want to be able to query on these fields.
- The values in these fields have a high cardinality, so
this data is not susceptible to a frequency analysis attack.

You choose to encrypt the `bloodType` field with random encryption for the following reasons:

- You do not plan to query on this field.
- The values in this field have low cardinality, making
them susceptible to a frequency analysis attack if you encrypted them deterministically.

that only automatic encryption did not support deterministic enryption of BSON arrays, however after testing it seems both manual and automatic encryption DO NOT support deterministic encryption of BSON arrays. Updated phrasing from "automatic encryption does not support deterministic..." to "CSFLE does not support deterministic...", let us know if this is incorrect!

You must encrypt the `medicalRecords` field with random encryption as {+csfle-abbrev+} does not support deterministic encryption of fields of type `array`.

> **Tip:** To learn more about supported and unsupported automatic encryption
operations, see `csfle-reference-automatic-encryption-supported-operations`.

### Specify Encryption Rules

To encrypt the `ssn` field with deterministic encryption, specify the following in your encryption schema:

To encrypt the `bloodType` field with random encryption, specify the following in your encryption schema:

To encrypt the `medicalRecords` field with random encryption, specify the following in your encryption schema:

To encrypt the `insurance.policyNumber` field with deterministic encryption, specify the following in your encryption schema:

### View the Complete Schema

The complete encryption schema for the Quick Start is as follows:

## Learn More

To learn more about encryption schemas, see `csfle-reference-encryption-schemas`

To learn more about automatic encryption, see `csfle-fundamentals-automatic-encryption`.

To view the Quick Start, see `csfle-quick-start`.
