---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/qe-connection-boilerplate.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

a. Start mongosh

Start the `mongosh` client.

```bash
   mongosh --nodb
```

#. Generate Your Key

To configure Queryable Encryption for a locally managed key, generate a base64-encoded 96-byte string with no line breaks.

```javascript
   const TEST_LOCAL_KEY = require("crypto").randomBytes(96).toString("base64")
```

#. Create the Queryable Encryption Options

Create the Queryable Encryption options using the generated local key string:

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

#. Create Your Encrypted Client

Use the :method:`Mongo()` constructor with the queryable encryption options configured to create a database connection. Replace the `mongodb://myMongo.example.net` URI with the `connection string URI <mongodb-uri>` of the target cluster.

```javascript
   encryptedClient = Mongo( 
      "mongodb://myMongo.example.net:27017/?replSetName=myMongo", 
      autoEncryptionOpts
   )
```
