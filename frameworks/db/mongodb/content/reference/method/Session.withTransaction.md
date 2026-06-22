---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/Session.withTransaction.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========================================

# Session.withTransaction() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Behavior

The Node.js driver has a version of `Session.withTransaction()` that is known as the [Callback API](https://www.mongodb.com/docs/drivers/node/current/fundamentals/transactions/#callback-api)_. The `Callback API` also accepts an callback, however the return type for the Node.js method must be a Promise. The `mongosh` `Session.withTransaction()` method does not require a Promise.

## Example

The following example creates the `balances` collection and uses a transaction to transfer money between two customers.

Create the `balances` collection:

```javascript
use accounts
db.balances.insertMany( [
  { customer: "Pat", balance: Decimal128( "35.88" ) },
  { customer: "Sasha", balance: Decimal128( "5.23" ) }
] )
```

Initialize some variables that are used in the transaction:

```javascript
var fromAccount = "Pat"
var toAccount = "Sasha"
var transferAmount = 1

var dbName = "accounts"
var collectionName = "balances"
```

Start a session, then run a transaction to update the accounts:

```javascript
var session = db.getMongo().startSession( { readPreference: { mode: "primary" } } );
session.withTransaction( async() => {  

   const sessionCollection = session.getDatabase(dbName).getCollection(collectionName);

   // Check needed values
   var checkFromAccount = sessionCollection.findOne(
      {
         "customer": fromAccount,
         "balance": { $gte: transferAmount }
      }
   )
   if( checkFromAccount === null ){
      throw new Error( "Problem with sender account" )
   } 

   var checkToAccount = sessionCollection.findOne(
      { "customer": toAccount }
   )
   if( checkToAccount === null ){
      throw new Error( "Problem with receiver account" )
   } 

   // Transfer the funds
   sessionCollection.updateOne(
      { "customer": toAccount },
      { $inc: { "balance": transferAmount } }
   )
   sessionCollection.updateOne(
      { "customer": fromAccount },
      { $inc: { "balance": -1 * transferAmount } }
   )

 } )
```

The lambda function includes initial checks to validate the operation before updating the `balances` collection.

MongoDB automatically completes the transaction.

- If both `updateOne()` operations succeed,
`Session.withTransaction()` commits the transaction when the callback returns.

- If an exception is thrown inside the callback,
`Session.withTransaction()` ends the transaction and rolls back any uncommitted changes.

> **Note:** By default, MongoDB ends transactions that run for more than 60
seconds. If you want to extend the default timeout to experiment with
transactions in :binary:`mongosh`, see `transaction-limit`.
