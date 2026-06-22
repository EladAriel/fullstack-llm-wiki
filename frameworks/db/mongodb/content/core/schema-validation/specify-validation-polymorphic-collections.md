---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/schema-validation/specify-validation-polymorphic-collections.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================================

# Specify Validation for Polymorphic Collections

You can specify schema validation for a collection that stores `polymorphic data<polymorphic-data>`, or documents with varying structures or schemas.

To create schema validation for multiple schemas within a single collection, you can set the schemas in your validation rules and ensure that documents conform to one of your collection's schemas.

## About this Task

Consider a collection, `accounts`, that stores data on customers of a bank and their account details. The collection contains both `customer` documents and `account` documents.

The following code inserts two `customer` documents into the `accounts` collection to store the details of customers Andrew and Anne, respectively. It also inserts two `account` documents to represent each of their individual savings accounts and a third `account` document to represent their shared checking account. You can run the code for this tutorial in the :mongosh:`MongoDB Shell (mongosh) </>`.

```javascript
db.accounts.insertMany( [
   {
      "customerId": "CUST-123456789",
      "docType": "customer",
      "name": {
         "title": "Mr",
         "first": "Andrew",
         "middle": "James",
         "last": "Morgan"
      },
      "address": {
         "street1": "240 Blackfriars Rd",
         "city": "London",
         "postCode": "SE1 8NW",
         "country": "UK"
      },
      "customerSince": ISODate("2005-05-20")
   },
   {
      "customerId": "CUST-987654321",
      "docType": "customer",
      "name": {
         "title": "Mrs",
         "first": "Anne",
         "last": "Morgan"
      },
      "address": {
         "street1": "240 Blackfriars Rd",
         "city": "London",
         "postCode": "SE1 8NW",
         "country": "UK"
      },
      "customerSince": ISODate("2003-12-01")
   },
   {
      "accountNumber": "ACC1000000654",
      "docType": "account",
      "accountType": "checking",
      "customerId": [
         "CUST-123456789",
         "CUST-987654321"
      ],
      "dateOpened": ISODate("2003-12-01"),
      "balance": Decimal128("5067.65")
   },
   {
      "accountNumber": "ACC1000000432",
      "docType": "account",
      "accountType": "savings",
      "customerId": [
         "CUST-123456789"
      ],
      "dateOpened": ISODate("2005-10-28"),
      "balance": Decimal128("10341.21")
   },
   {
      "accountNumber": "ACC1000000890",
      "docType": "account",
      "accountType": "savings",
      "customerId": [
         "CUST-987654321"
      ],
      "dateOpened": ISODate("2003-12-15"),
      "balance": Decimal128("10341.89")
   }
] );
```

To only allow documents that adhere to the `customer` or `account` schemas into the `accounts` collection, set up schema validation using the following procedure.

## Steps
