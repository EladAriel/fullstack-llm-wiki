---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/Mongo.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

========================

# Mongo() (mongosh method)

## Description

> **Seealso:** :method:`Mongo.getDB()` and :method:`db.getMongo()`

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-onprem-only.rst

## `{+title-auto-encrypt-options+}`

The `{+auto-encrypt-options+}` document specifies configuration options for `security-in-use-encryption`. If your database connection has an existing in-use encryption configuration, `{+auto-encrypt-options+}` overrides that configuration. MongoDB provides two approaches to In-Use Encryption: `manual-csfle-feature` and `qe-manual-feature-qe`.

For example, starting :binary:`~bin.mongosh` with client-side field level encryption command-line options enables client-side encryption for that connection. New database connections created using :method:`Mongo()` inherit the encryption settings unless :method:`Mongo()` includes `{+auto-encrypt-options+}`.

The `{+auto-encrypt-options+}` document has the following syntax:

```none
{
  "keyVaultClient" : <object>,
  "keyVaultNamespace" : "<string>",
  "kmsProviders" : <object>,
  "schemaMap" : <object>,
  "bypassAutoEncryption" : <boolean>,
  "tlsOptions": <object>,
  "encryptedFieldsMap": <object>
}
```

The `{+auto-encrypt-options+}` document takes the following parameters:

## `api`

The `api` parameter specifies configuration options for the `Stable API <stable-api>`. You can enable or disable optional behavior using the following options:

.. include:: /includes/stable-api-options.rst

The `api` parameter has the following syntax:

```javascript
{ api: { version: <string>, strict: <boolean>, deprecationErrors: <boolean> } }
```

## Examples

### Connect to a MongoDB Cluster

The following operation creates a new connection object from within a :binary:`~bin.mongosh` session:

```javascript
cluster = Mongo("mongodb://mymongo.example.net:27017/?replicaSet=myMongoCluster")
```

Issue operations against the `cluster` object to interact with the `mymongo.example.net:27017` cluster:

```javascript
myDB = cluster.getDB("myDB"); //returns the database object
myColl = myDB.getCollection("myColl"); // returns the collection object
```

### Connect to a Cluster with Client-Side Encryption Enabled

.. include:: /includes/csfle-connection-boilerplate-example.rst

Issue operations against the `cluster` object to interact with the `mymongo.example.net:27017` cluster and perform explicit encryption:

```javascript
// returns the database object
myDB = cluster.getDB("myDB");

// returns the collection object
myColl = myDB.getCollection("myColl");

// returns object for managing data encryption keys
keyVault = cluster.getKeyVault();

// returns object for explicit encryption/decryption
clientEncryption = cluster.getClientEncryption();
```

See `in-use-encryption-methods` for a complete list of client-side field level encryption methods.

### Connect to a Cluster with Automatic Client-Side Encryption Enabled

To configure client-side field level encryption for a locally managed key:

- generate a base64-encoded 96-byte string with no line breaks
- use :binary:`mongosh` to load the key
```bash
export TEST_LOCAL_KEY=$(echo "$(head -c 96 /dev/urandom | base64 | tr -d '\n')")

mongosh --nodb
```

The following operation creates a new connection object from within a :binary:`~bin.mongosh` session. The `{+auto-encrypt-options+}` option specifies the required options for enabling `automatic client-side encryption <field-level-encryption-automatic>` on the `hr.employees` collection:

```javascript
var autoEncryptionOpts = {
  "keyVaultNamespace" : "encryption.__dataKeys",
  "kmsProviders" : {
    "local" : {
      "key" : BinData(0, process.env["TEST_LOCAL_KEY"])
    }
  },
  schemaMap : {
    "hr.employees" : {
      "bsonType": "object",
      "properties" : {
        "taxid" : {
          "encrypt" : {
            "keyId" : [UUID("bffb361b-30d3-42c0-b7a4-d24a272b72e3")],
            "bsonType" : "string",
            "algorithm" : "AEAD_AES_256_CBC_HMAC_SHA_512-Random"
          }
        },
        "taxid-short": {
          "encrypt": {
            "keyId": [UUID("33408ee9-e499-43f9-89fe-5f8533870617")],
            "algorithm": "AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic",
            "bsonType": "string"
          }
        }
      }
    }
  }
}

cluster = Mongo(
  "mongodb://mymongo.example.net:27017/?replicaSet=myMongoCluster",
  autoEncryptionOpts
)
```

Issue operations against the `cluster` object to interact with the `mymongo.example.net:27017` cluster and utilize automatic encryption:

```javascript
// returns the database object
myDB = cluster.getDB("myDB");

// returns the collection object
myColl = myDB.getCollection("myColl");

myColl.insertOne(
  {
    "name" : "J Doe",
    "taxid" : "123-45-6789",
    "taxid-short" : "6789"
  }
)
```

The specified automatic encryption rules encrypt the `taxid` and `taxid-short` fields using the specified data encryption key and algorithm. Only clients configured for the correct KMS and access to the specified data encryption key can decrypt the field.

The following operation creates a new connection object from within a :binary:`~bin.mongosh` session. The `mongo.tlsOptions` option enables a connection using KMIP as the KMS provider:

```javascript
var csfleConnection = {
  keyVaultNamespace: "encryption.__keyVault",
  kmsProviders: { kmip: { endpoint: "kmip.example.com:123" } },
  tlsOptions: { kmip: { tlsCertificateKeyFile: "/path/to/client/cert-and-key-bundle.pem" } }
}

cluster = Mongo(
  "mongodb://mymongo.example.net:27017/?replicaSet=myMongoCluster",
  csfleConnection
);
```

See `in-use-encryption-methods` for a complete list of client-side field level encryption methods.

### Connect to a Cluster with the Stable API Enabled

The following operation creates a new connection object from within a :binary:`~bin.mongosh` session. The `mongo-api-options` option enables Stable API V1 and specifies that you cannot run deprecated command or commands outside of the Stable API.

```javascript
cluster = Mongo(
  "mongodb://mymongo.example.net:27017/?replicaSet=myMongoCluster", 
   null, 
   { api: { version: "1", strict: true, deprecationErrors: true } }
)
```

To interact with the `mymongo.example.net:27017` cluster, issue operations against the `cluster` object. For a full list of Stable API commands, see `<api-v1-command-list>`.
