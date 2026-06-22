---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/data-modeling/design-patterns/data-versioning/schema-versioning.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================================

# Maintain Different Schema Versions

Your application's schema requirements may change over time. For example, when new services become available, you may need to add new fields to your documents. MongoDB's flexible data model means that you can use a non-uniform document structure throughout your collection, and you can retain your older document structure alongside the updated schema.

The **Schema Versioning Pattern** lets you have different versions of your schema in the same collection, which avoids large-scale schema migrations when requirements change.

## About this Task

If you have a field that appears at different levels in your documents, the Schema Versioning Pattern may affect your indexes. For example, if you store the same field as both a top-level field and as an embedded field in different documents, you may need multiple indexes to support queries on that field.

## Before you Begin

In the following example, an online store uses a collection to track customer contact information. At first, the collection only contains home and work phone numbers. Over time, new contact methods are added and some older methods aren't needed.

Insert the sample document:

```javascript
db.contacts.insertOne(
   {
      _id: 1,
      name: "Taylor",
      home: "209-555-7788",
      work: "503-555-0110"
   }
)
```

## Steps

The following procedure sets the initial schema version for the collection, then inserts a new document with a different schema.

## Next Steps

After you implement the Schema Versioning Pattern, you need to modify how your application queries and updates data.

### Query the Collection

Now that there are two different schemas in the `contacts` collection, your query must check all possible locations for a field value depending on the document's schema version.

The following query searches based on the customer's `work` number. The query checks both possible locations for the `work` field:

```javascript
db.contacts.find(
   {
      $or: [
         {
            work: "503-555-0110"
         },
         {
            "contactInfo.work": "503-555-0110"
         }
      ]
   }
)
```

Output:

```javascript
{
   _id: 1,
   name: 'Taylor',
   home: '209-555-7788',
   work: '503-555-0110',
   schemaVersion: 1
}
```

### Update a Document in the Collection

Similar to inserting data, when you update a collection, your application must check all possible locations for the field to be updated. When you update data, you can use the `schemaVersion` field to determine the field to update.

To update the `work phone number for the user with id: 2`, run this command:

```javascript
db.contacts.updateOne(
   { _id: 2 },
   [
      {
         $set: {
            "work": {
               $cond: {
                  if: { $eq: [ "$schemaVersion", 1 ] },
                  then: "999-999-9999",
                  else: null
               }
            },
            "contactInfo.work": {
               $cond: {
                  if: { $eq: [ "$schemaVersion", 2 ] },
                  then: "999-999-9999",
                  else: null
               }
            }
         }
      }
   ]
)
```

In the previous example:

- If the matched document's `schemaVersion` is `1`, then the
`work` field is set to the updated value.

- If the matched document's `schemaVersion` is `2`, then the
`contactInfo.work` field is set to the updated value.

## Learn More

- `design-patterns-document-versioning`
- `schema-validation-overview`
- `data-modeling-schema-design`
