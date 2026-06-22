---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/queryable-encryption/qe-create-encryption-schema.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

========================================================================

# Create an {+enc-schema-title+}

## About this Task

To make encrypted fields queryable, create an `{+enc-schema+}`. This schema defines which fields are queryable, and which query types are permitted. For more information, see `qe-fundamentals-encrypt-query`.

> **Important:** {+qe+} supports equality and range queries. You can configure a
field for only one query type.

## Before you Begin

When you make encrypted fields queryable, consider performance and security. For details on how each configuration option affects these, see `qe-field-configuration`.

To use the Public Preview prefix, suffix, or substring queries with :binary:`mongosh`, you must separately download the :manual:`{+shared-library+} </core/queryable-encryption/install-library>` 8.2 or higher, then specify the library path to `mongosh` using the :mongosh:`--cryptSharedLibPath </reference/options>` option.

## Field Reference

You can configure encryption for each field in the `fields` array of your `encryptedFieldsObject`. The following table describes the available subfields:

## Steps

## Example

This example shows how to create an {+enc-schema+} for hospital data.

Consider the following document that contains personally identifiable information (PII), credit card information, and sensitive medical information:

```json
{
   "firstName": "Jon",
   "lastName": "Snow",
   "patientId": 12345187,
   "address": "123 Cherry Ave",
   "medications": [
      "Adderall",
      "Lipitor"
   ],
   "patientInfo": {
      "ssn": "921-12-1234",
      "billing": {
            "type": "visa",
            "number": "1234-1234-1234-1234"
      }
   }
}
```

To ensure the PII and sensitive medical information stays secure, this {+enc-schema+} adds the relevant fields:

```javascript
const encryptedFieldsObject = {
   fields: [
      {
         path: "patientId",
         bsonType: "int"
      },
      {
         path: "patientInfo.ssn",
         bsonType: "string"
      },
      {
         path: "medications",
         bsonType: "array"
      },
      {
         path: "patientInfo.billing",
         bsonType: "object"
      }
   ]
}
```

Adding the `queries` property makes the `patientId` and `patientInfo.ssn` fields queryable. This example enables equality queries:

```javascript
const encryptedFieldsObject = {
   fields: [
      {
         path: "patientId",
         bsonType: "int",
         queries: { queryType: "equality" }
      },
      {
         path: "patientInfo.ssn",
         bsonType: "string",
         queries: { queryType: "equality" }
      },
      {
         path: "medications",
         bsonType: "array"
      },
      {
         path: "patientInfo.billing",
         bsonType: "object"
      },
   ]
}
```
