---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/csfle/fundamentals/encryption-algorithms.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================

# Fields and Encryption Types

This page describes the types of encryption used by MongoDB to perform {+csfle+} ({+csfle-abbrev+}). To perform {+csfle-abbrev+}, MongoDB uses the following types of encryption algorithms:

- `Deterministic Encryption <csfle-deterministic-encryption>`
- `Randomized Encryption <csfle-random-encryption>`
## Deterministic Encryption

The deterministic encryption algorithm ensures that a given input value always encrypts to the same output value each time the algorithm is executed. While deterministic encryption provides greater support for read operations, encrypted data with low cardinality is susceptible to frequency analysis recovery.

For sensitive fields that are not used in read operations, applications may use `randomized encryption <csfle-random-encryption>` for improved protection from frequency analysis recovery.

> **Important:** Encrypting entire objects and arrays is not supported with
deterministic encryption. To learn more and see an example, see
`csfle-encrypting-objects-support`.

### Query for Documents on a Deterministically Encrypted Field

You can query deterministically encrypted fields using standard MongoDB driver and :binary:`mongosh` methods.

To view the complete list of all supported query operators on deterministically encrypted fields, see `csfle-reference-automatic-encryption-supported-operations`.

To learn more about reads on encrypted data, see `encrypted-reads-diagram`.

> **Note:** When you query on an encrypted field using a client that is not
configured to use {+csfle+} ({+csfle-abbrev+}), the query returns a
null value. A client without {+csfle-abbrev+} configured cannot query
on an encrypted field.

## Randomized Encryption

The randomized encryption algorithm ensures that a given input value always encrypts to a different output value each time the algorithm is executed. While randomized encryption provides the strongest guarantees of data confidentiality, it also prevents support for any read operations which must operate on the encrypted field to evaluate the query.

For sensitive fields that are used in read operations, applications must use `deterministic encryption <csfle-deterministic-encryption>` for improved read support on encrypted fields.

### Support for Encrypting Objects and Arrays

Encrypting entire objects or arrays is only supported with `randomized encryption <csfle-random-encryption>`.

For example, consider the following document:

```json
{
   "personal_information" : {
      "ssn" : "123-45-6789",
      "credit_score" : 750,
      "credit_cards" : [ "1234-5678-9012-3456", "9876-5432-1098-7654"]
   },
   "phone_numbers" : [ "(212) 555-0153" ]
}
```

Encrypting the `personal_information` and `phone_numbers` fields using the randomized encryption algorithm encrypts the entire object. While this protects all fields nested under those fields, it also prevents querying against those nested fields.

To learn more about supported operations for encryption, see `csfle-reference-automatic-encryption-supported-operations`.

### Query for Documents on a Randomly Encrypted Field

You cannot directly query for documents on a randomly encrypted field. However, you can use another field to find the document that contains an approximation of the randomly encrypted field data.

For example, consider the following document where the `ssn` field is randomly encrypted:

```json
{
   "_id": "5d6ecdce70401f03b27448fc",
   "name": "Jon Doe",
   "ssn": 241014209,
   "bloodType": "AB+",
   "medicalRecords": [
       {
           "weight": 180,
           "bloodPressure": "120/80"
       }
   ],
   "insurance": {
       "provider": "MaestCare",
       "policyNumber": 123142
   }
}
```

Instead of querying the `ssn` field, you can add another plain-text field called `last4ssn` that contains the last 4 digits of the `ssn` field. You can then query on the `last4ssn` field as a proxy for `ssn`:

```json
{
   "_id": "5d6ecdce70401f03b27448fc",
   "name": "Jon Doe",
   "ssn": 241014209,
   "last4ssn": 4209,
   "bloodType": "AB+",
   "medicalRecords": [
      {
            "weight": 180,
            "bloodPressure": "120/80"
      }
   ],
   "insurance": {
      "provider": "MaestCare",
      "policyNumber": 123142
   }
}
```
