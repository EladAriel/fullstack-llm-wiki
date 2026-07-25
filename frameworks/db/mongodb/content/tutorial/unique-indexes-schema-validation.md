---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/unique-indexes-schema-validation.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

====================================

# Unique Indexes and Schema Validation

To ensure your database adheres to your application design, you can strategically create indexes to combine index properties with schema validation.

## About this Task

Consider an application that summarizes a user’s finances. The main page of the application displays the user’s ID and the balances on all of their banking accounts synced with the application.

The application stores its user information in a collection called `users`. The `users` collection contains documents with the following schema:

```javascript
db.users.insertOne( {
   _id: 1,
   name: { first: "john", last: "smith" },
   accounts: [
      { balance: 500, bank: "abc", number: "123" },
      { balance: 2500, bank: "universal bank", number: "9029481" }
   ]
} )
```

The application requires the following rules:

- A user can register in the application and not sync a bank account.
- A user identifies an account by its `bank` and `number` fields.
- A user cannot register the same account for two different users.
- A user cannot register the same account multiple times for the same user.
To design your database so that it confines its documents to the application’s rules, combine a unique index and schema validation on your database using the following procedure.

## Steps
