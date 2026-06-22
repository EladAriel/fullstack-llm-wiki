---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/schema-validation/update-schema-validation.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

========================

# Modify Schema Validation

After you add schema validation to a collection, you can modify validation rules at any time. For example, you may decide:

- That documents in a `users` collection no longer require an email
address.

- To increase the minimum length for a `password` field from 8
characters to 12.

To modify a collection's schema validation, use the :dbcommand:`collMod` command and specify the updated validation in the `validator` object.

## About This Task

You can modify all components of a schema validation, including its rules, validation level, and validation action.

If you update a collection's validation rules, documents inserted prior to the validation change may no longer be valid. How MongoDB handles these invalid documents depends on your `validationLevel`. By default, MongoDB applies validation checks to all documents, regardless of when they were inserted.

## Steps

The following procedure creates a collection with validation rules and then modifies those rules.

> **Tip:** You can also use the `collMod` command to add validation to an existing
collection that was not created with validation.

## Results

The following sections show the results of the updated validation in these scenarios:

- When you insert an invalid document.
- When you insert a valid document.
- When a previously valid document becomes invalid because of the
validation rule changes.

### Insert an Invalid Document

The following operation attempts to insert an invalid document. The document is invalid because the `password` field is 10 characters long when the minimum length is 12:

```javascript
db.users.insertOne(
   {
      "username": "salesAdmin01",
      "password": "kT9$j4wg#M"
   }
)
```

MongoDB returns the following error:

```javascript
MongoServerError: Document failed validation
Additional information: {
  failingDocumentId: ObjectId("62be0adb73c105dde9231299"),
  details: {
    operatorName: '$jsonSchema',
    schemaRulesNotSatisfied: [
      {
        operatorName: 'properties',
        propertiesNotSatisfied: [
          {
            propertyName: 'password',
            description: 'must be a string of at least 8 characters, and is required',
            details: [
              {
                operatorName: 'minLength',
                specifiedAs: { minLength: 12 },
                reason: 'specified string length was not satisfied',
                consideredValue: 'kT9$j4wg#M'
              }
            ]
          }
        ]
      }
    ]
  }
}
```

### Insert a Valid Document

The following operation inserts a valid document, where the `password` field is at least 12 characters long:

```javascript
db.users.insertOne(
   {
      "username": "salesAdmin01",
      "password": "8p&SQd7T90$KKx"
   }
)
```

### Handle a Previously Valid Document That Is No Longer Valid

Consider the following document that is valid for the first version of the schema validation, but not the second:

```javascript
db.users.insertOne(
   {
      "username": "salesAdmin02",
      "password": "i8U60*VyL8"
   }
)
```

The document's `password` field is 10 characters. The first version of the schema validation required a minimum of 8 characters, meaning this document was valid. However, after updating the validation to require the `password` to be a minimum of 12 characters, the document is no longer valid.

When a change in schema validation causes previously valid documents to become invalid, the newly invalid documents remain in the collection.

The way MongoDB handles newly invalid documents depends on the schema's `validationLevel`. The schema validation in this example uses the default `validationLevel` of `strict`, meaning the document must match the new validation rules. MongoDB checks the validation each time the document is updated.

If the updated schema validation had a `validationLevel` of `moderate`, this document would not need to match the new validation rules.

## Learn More

- `schema-specify-validation-level`
- `schema-validation-handle-invalid-docs`
