---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/model-embedded-one-to-one-relationships-between-documents.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================================================

# Model One-to-One Relationships with Embedded Documents

Create a data model that uses `embedded <data-modeling-embedding>` documents to describe a one-to-one relationship between connected data. Embedding connected data in a single document can reduce the number of read operations required to obtain data. In general, structure your schema so your application receives all of its required information in a single read operation. For example, you can use the the embedded one-to-one model to describe the following relationships:

- Country to capital city
- User account to email address
- Building to address
## Example

The example schema contains two entities, a `patron` and an `address`:

```javascript
// patron document
{
   _id: "joe",
   name: "Joe Bookreader"
}
// address document
{
   street: "123 Fake Street",
   city: "Faketon",
   state: "MA",
   zip: "12345"
}
```

### Embedded Document Pattern

The `address` data is frequently retrieved with the `patron` information. To allow your application to retreive all necessary information with a single query, embed the `address` information inside of the `patron` document:

```javascript
{
   _id: "joe",
   name: "Joe Bookreader", 
   address: {
              street: "123 Fake Street",
              city: "Faketon",
              state: "MA",
              zip: "12345"
            }
}
```

## Learn More

- `data-modeling-example-one-to-many`
- `data-modeling-publisher-and-books`
