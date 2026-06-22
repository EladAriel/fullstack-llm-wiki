---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/csfle-connection-boilerplate-example-2.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

a. Start mongosh

Run:

```bash
   mongosh --nodb

``--nodb`` means don't connect to a database.
```

#. Generate a Key String

Generate a base 64 96-byte string:

```javascript
   const TEST_LOCAL_KEY = require("crypto").randomBytes(96).toString("base64")
```

#. Create an Encryption Options Object

To create a client-side field level encryption options object, use the `TEST_LOCAL_KEY` string from the previous step:

```javascript
      var autoEncryptionOpts = {
         "keyVaultNamespace" : "encryption.__dataKeys",
         "kmsProviders" : {
            "local" : {
               "key" : BinData(0, TEST_LOCAL_KEY)
            }
         }
      }
```

#. Create an Encrypted Client Object

To create an encrypted client object, use the :method:`Mongo()` constructor. Replace the `mongodb://myMongo.example.net` URI with the `connection string URI <mongodb-uri>` for the target cluster. For example:

```javascript
   encryptedClient = Mongo( 
      "mongodb://myMongo.example.net:27017/?replSetName=myMongo", 
      autoEncryptionOpts
   )
```
