---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/model-embedded-one-to-many-relationships-between-documents.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=======================================================

# Model One-to-Many Relationships with Embedded Documents

Use `embedded <data-modeling-embedding>` documents for one-to-many relationships. Embedding connected data in a single document reduces the number of read operations required to retrieve data. Structure your schema so your application receives all required information in a single read operation. For example, use the embedded one-to-many model for the following relationships:

- Country to major cities
- Author to books
- Student to classes
## Example

The example schema contains three entities, with `address one` and `address two` belonging to the same `patron`:

```javascript
// patron document
{
   _id: "joe",
   name: "Joe Bookreader"
}

// address one
{
   street: "123 Fake Street",
   city: "Faketon",
   state: "MA",
   zip: "12345"
}

// address two
{
   street: "1 Some Other Street",
   city: "Boston",
   state: "MA",
   zip: "12345"
}
```

### Embedded Document Pattern

In this example the application needs to display information for the `patron` and both `address` objects on a single page. To retrieve all necessary information with a single query, embed the `address one` and `address two` information inside the `patron` document:

```javascript
{
   _id: "joe",
   name: "Joe Bookreader",
   addresses: [
      {
         street: "123 Fake Street",
         city: "Faketon",
         state: "MA",
         zip: "12345"
      },
      {
         street: "1 Some Other Street",
         city: "Boston",
         state: "MA",
         zip: "12345"
      }
   ]
 }
```

## Learn More

- `data-modeling-example-one-to-one`
- `data-modeling-publisher-and-books`
