---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/csfle/reference/encryption-schemas.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

========================

# CSFLE Encryption Schemas

## Overview

.. include:: /includes/extracts/csfle-enterprise-atlas-only.rst

Encryption schemas contain user-specified rules that identify which fields must be encrypted and how to encrypt those fields. Applications must specify the automatic encryption rules using a strict subset of the [JSON Schema Draft 4 standard syntax](https://tools.ietf.org/html/draft-zyp-json-schema-04) and the following encryption-specific keywords:

- `Encrypt <csfle-reference-encryption-schemas-encrypt-keyword>`
specifies the encryption options to use when encrypting the current field.

- :ref:`Encrypt Metadata
<field-level-encryption-encryptMetadata-keyword>` specifies inheritable encryption options.

For the MongoDB shell, use the :method:`Mongo` constructor to create the database connection with the automatic encryption rules included as part of the {+csfle+} `configuration object <{+auto-encrypt-options+}>`. See `mongo-connection-automatic-client-side-encryption-enabled` for an example.

For the official MongoDB drivers, use the driver-specific database connection constructor (`MongoClient`) to create the database connection with the automatic encryption rules included as part of the {+csfle+} configuration object. To learn more about {+csfle-abbrev+}-specific `MongoClient` options, see the `mongo client <csfle-reference-mongo-client>` page.

> **Important:** Do  **not** specify schema validation keywords in the automatic
encryption rules. To define schema validation rules, configure
`schema validation<schema-validation-overview>`.

## Definition

## Examples

### Encryption Schema -  Multiple Fields

Consider a collection `MedCo.patients` where each document has the following structure:

```none
{
  "fname" : "<String>",
  "lname" : "<String>",
  "passportId" : "<String>",
  "bloodType" : "<String>",
  "medicalRecords" : [
    {<object>}
  ],
  "insurance" : {
    "policyNumber" : "<string>",
    "provider" : "<string>"
  }
}
```

The following fields contains personally identifiable information (PII) that may be queried:

- `passportId`
- `bloodType`
- `insurance.policyNumber`
- `insurance.provider`
The `deterministic <field-level-encryption-deterministic>` encryption algorithm guarantees that the encrypted output of a value remains static. This allows queries for a specific value to return meaningful results at the cost of increased susceptibility to frequency analysis recovery. The deterministic encryption algorithm therefore meets both the encryption and queryability requirements of the data.

The following fields contain legally protected personally identifiable information (PII) that may never be queried:

- `medicalRecords`
The `randomized <field-level-encryption-random>` encryption algorithm guarantees that the encrypted output of a value is always unique. This prevents queries for a specific field value from returning meaningful results while supporting the highest possible protection of the field contents. The randomized encryption algorithm therefore meets both the encryption and queryability requirements of the data.

The following schema specifies automatic encryption rules which meet the above requirements for the `MedCo.patients` collection:

```json
{
  "MedCo.patients" : {
    "bsonType" : "object",
    "properties" : {
      "passportId" : {
        "encrypt" : {
          "keyId" : [UUID("bffb361b-30d3-42c0-b7a4-d24a272b72e3")],
          "algorithm" : "AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic",
          "bsonType" : "string"
        }
      },
      "bloodType" : {
        "encrypt" : {
          "keyId" : [UUID("bffb361b-30d3-42c0-b7a4-d24a272b72e3")],
          "algorithm" : "AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic",
          "bsonType" : "string"
        }
      },
      "medicalRecords" : {
        "encrypt" : {
          "keyId" : [UUID("f3821212-e697-4d65-b740-4a6791697c6d")],
          "algorithm" : "AEAD_AES_256_CBC_HMAC_SHA_512-Random",
          "bsonType" : "array"
        }
      },
      "insurance" : {
        "bsonType" : "object",
        "properties" : {
          "policyNumber" : {
            "encrypt" : {
              "keyId" : [UUID("bffb361b-30d3-42c0-b7a4-d24a272b72e3")],
              "algorithm" : "AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic",
              "bsonType" : "string"
            }
          },
          "provider" : {
            "encrypt" : {
              "keyId" : [UUID("bffb361b-30d3-42c0-b7a4-d24a272b72e3")],
              "algorithm" : "AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic",
              "bsonType" : "string"
            }
          }
        }
      }
    }
  }
}
```

The above automatic encryption rules mark the `passportId`, `bloodType`, `insurance.policyNumber`, `insurance.provider`, and `medicalRecords` fields for encryption.

- The `passportId`, `bloodType`, `insurance.policyNumber`, and
`provider` fields require deterministic encryption using the specified key.

- The `medicalRecords` field requires randomized encryption using the
specified key.

.. include:: /includes/queryable-encryption/fact-csfle-compatibility-drivers.rst

### Encryption Schema -  Multiple Fields With Inheritance

Consider a collection `MedCo.patients` where each document has the following structure:

```none
{
  "fname" : "<String>",
  "lname" : "<String>",
  "passportId" : "<String>",
  "bloodType" : "<String>",
  "medicalRecords" : [
    {<object>}
  ],
  "insurance" : {
    "policyNumber" : "<string>",
    "provider" : "<string>"
  }
}
```

The following fields contain private data that may be queried:

- `passportId`
- `bloodType`
- `insurance.policyNumber`
- `insurance.provider`
The `deterministic <field-level-encryption-deterministic>` encryption algorithm guarantees that the encrypted output of a value remains static. This allows queries for a specific value to return meaningful results at the cost of increased susceptibility to frequency analysis recovery. The deterministic encryption algorithm therefore meets both the encryption and queryability requirements of the data.

The following fields contain private data that may never be queried:

- `medicalRecords`
The `randomized <field-level-encryption-random>` encryption algorithm guarantees that the encrypted output of a value is always unique. This prevents queries for a specific field value from returning meaningful results while supporting the highest possible protection of the field contents. The randomized encryption algorithm therefore meets both the encryption and queryability requirements of the data.

The following schema specifies automatic encryption rules which meet the encryption requirements for the `MedCo.patients` collection:

```json
{
  "MedCo.patients" : {
    "bsonType" : "object",
    "encryptMetadata" : {
      "keyId" : [UUID("6c512f5e-09bc-434f-b6db-c42eee30c6b1")],
      "algorithm" : "AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic"
    },
    "properties" : {
      "passportId" : {
        "encrypt" : {
          "bsonType" : "string"
        }
      },
      "bloodType" : {
        "encrypt" : {
          "bsonType" : "string"
        }
      },
      "medicalRecords" : {
        "encrypt" : {
          "keyId" : [UUID("6c512f5e-09bc-434f-b6db-c42eee30c6b1")],
          "algorithm" : "AEAD_AES_256_CBC_HMAC_SHA_512-Random",
          "bsonType" : "array"
        }
      },
      "insurance" : {
        "bsonType" : "object",
        "properties" : {
          "policyNumber" : {
            "encrypt" : {
              "bsonType" : "string"
            }
          },
          "provider" : {
            "encrypt" : {
              "bsonType" : "string"
            }
          }
        }
      }
    }
  }
}
```

The above automatic encryption rules mark the `passportId`, `bloodType`, `insurance.policyNumber`, `insurance.provider`, and `medicalRecords` fields for encryption.

- The `passportId`, `bloodType`, `insurance.policyNumber`, and
`provider` fields inherit their encryption settings from the parent `encryptMetadata` field. Specifically, these fields inherit the :autoencryptkeyword:`~encryptMetadata.algorithm` and :autoencryptkeyword:`~encryptMetadata.keyId` values specifying deterministic encryption with the specified {+dek-long+}.

- The `medicalRecords` field requires randomized encryption using the
specified key. The `encrypt` options override those specified in the parent `encryptMetadata` field.

.. include:: /includes/queryable-encryption/fact-csfle-compatibility-drivers.rst

To learn more about your CMK and {+key-vault-long+}, see the `key vaults <qe-reference-keys-key-vaults>` page.

To learn more about encryption algorithms, see the `Encryption algorithms <csfle-reference-encryption-algorithms>` page.

To learn more about {+csfle-abbrev+}-specific `MongoClient` options, see the `mongo client <csfle-reference-mongo-client>` page.

### Encryption Schema -  Encrypt with Pattern Properties

You can use the `patternProperties` keyword in your encryption schema to define encryption rules for all fields with names that match a regular expression.

Consider a collection `MedCo.patients` where each document has the following structure:

```none
{
  "fname" : "<string>",
  "lname" : "<string>",
  "passportId_PIIString" : "<string>",
  "bloodType_PIIString" : "<string>",
  "medicalRecords_PIIArray" : [
    {<object>}
  ],
  "insurance" : {
    "policyNumber_PIINumber" : "<number>",
    "provider_PIIString" : "<string>"
  }
}
```

The fields that contain private data are identified by a "_PII<type>" tag appended the end of the field name.

- `passportId_PIIString`
- `bloodType_PIIString`
- `medicalRecords_PIIArray`
- `insurance.policyNumber_PIINumber`
- `insurance.provider_PIIString`
You can use the `patternProperties` keyword to configure these fields for encryption, without identifying each field individually, and without using the full field name. Do this by using regular expressions that match all fields that end with the "_PII<type>" tag.

The following JSON schema uses `patternProperties` and regular expressions to specify which fields to encrypt.

```json
{
 "MedCo.patients": {
 "bsonType": "object",
 "patternProperties": {
   "_PIIString$": {
     "encrypt": {
       "keyId": [UUID("6c512f5e-09bc-434f-b6db-c42eee30c6b1")],
       "bsonType": "string",
       "algorithm": "AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic",
     },
   },
   "_PIIArray$": {
     "encrypt": {
       "keyId": [UUID("6c512f5e-09bc-434f-b6db-c42eee30c6b1")],
       "bsonType": "array",
       "algorithm": "AEAD_AES_256_CBC_HMAC_SHA_512-Random",
     },
   },
   "insurance": {
     "bsonType": "object",
     "patternProperties": {
       "_PIINumber$": {
         "encrypt": {
           "keyId": [UUID("6c512f5e-09bc-434f-b6db-c42eee30c6b1")],
           "bsonType": "int",
           "algorithm": "AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic",
         },
       },
       "_PIIString$": {
         "encrypt": {
           "keyId": [UUID("6c512f5e-09bc-434f-b6db-c42eee30c6b1")],
           "bsonType": "string",
           "algorithm": "AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic",
         },
       },
     },
   },
 },
 },
}
```

The above automatic encryption rules mark the `passportId_PIIString`, `bloodType_PIIString`, `medicalRecords_PIIArray`, `insurance.policyNumber_PIINumber`, `insurance.provider_PIIString` fields for encryption.

To Learn more about the `patternProperties` keyword, see `csfle-fundamentals-pattern-properties`.
