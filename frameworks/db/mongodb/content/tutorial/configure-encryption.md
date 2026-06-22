---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/configure-encryption.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

====================

# Configure Encryption

## Overview

This page discusses server configuration to support encryption at rest. If you use [MongoDB Atlas](https://www.mongodb.com/atlas/database)_, your data is already encrypted. MongoDB manages Atlas encryption at the cloud provider level, but you can also use your own key management solution. See the Atlas [key management documentation](https://docs.atlas.mongodb.com/security-kms-encryption/)_ for details.

MongoDB Enterprise 3.2 introduces a native encryption option for the WiredTiger storage engine. Outside Atlas, encryption is only available for enterprise installations that use the WiredTiger Storage Engine.

Secure management of the encryption keys is a critical requirement for storage encryption. MongoDB uses a master key that is not stored with the MongoDB installation. Only the master key is externally managed, other keys can be stored with your MongoDB instance.

MongoDB's encrypted storage engine supports two key management options for the master key:

- Integration with a third party key management appliance via the Key
Management Interoperability Protocol (KMIP). **Recommended**

- Use of local key management via a keyfile.
> **Important:** MongoDB cannot encrypt existing data. When you enable encryption
with a new key, the MongoDB instance cannot have any pre-existing
data. If your MongoDB installation already has existing data, see
`encrypt-existing-data` for additional steps.

## Key Manager

MongoDB Enterprise supports secure transfer of keys with compatible key management appliances. Using a key manager allows for the keys to be stored in the key manager.

MongoDB Enterprise supports secure transfer of keys with Key Management Interoperability Protocol (KMIP) compliant key management appliances.

.. include:: /includes/partners-security.rst

> **Tip:** Using a key manager meets regulatory key management guidelines, such
as HIPAA, PCI-DSS, and FERPA, and is recommended over the local key
management.

### Prerequisites

- Your key manager must support the KMIP communication protocol.
.. include:: /includes/reference/fact-kmip-version.rst

- .. include:: /includes/fact-required-kmip-ops.rst
- To authenticate MongoDB to a KMIP server, you must have a valid
certificate issued by the key management appliance.

> **Note:** .. include:: /includes/fact-aes.rst

### Encrypt Using a New Key

To create a new key when you connect to the key manager, add an entry similar to the following to your configuration file. Replace the strings and port number with your values.

```yaml
security:
   enableEncryption: true
   kmip:
      serverName: "mdbhost.somecompany.com"
      port: 5696
      serverCAFile: "security/libs/trusted-ca.pem"
      clientCertificateFile: "security/libs/trusted-client.pem"
```

For more information on these options, see `encryption-key-management-conf-options`.

.. include:: /includes/reference/fact-add-v1-flag.rst

.. include:: /includes/extracts/default-bind-ip-security-additional-command-line.rst

.. include:: /includes/enable-KMIP-on-windows.rst

.. include:: /includes/reference/fact-connection-check.rst

To verify that the key creation and usage was successful, check the log file. If successful, the process will log the following messages:

```bash
[initandlisten] Created KMIP key with id: <UID>
[initandlisten] Encryption key manager initialized using master key with id: <UID>
```

> **Seealso:** `encryption-key-management-options`

### Encrypt Using an Existing Key

You can use an existing master key that your KMIP server already manages. To use an existing key, add an entry similar to the following to your configuration file before you start `mongod`. Replace the strings and port number with your values.

```yaml
security:
   enableEncryption: true
   kmip:
      keyIdentifier: "a29fba3-fd8327a2-74ba-43aa-bd3b-78a549a5295f"
      serverName: "mdbhost.somecompany.com"
      port: 5696
      serverCAFile: "security/libs/trusted-ca.pem"
      clientCertificateFile: "security/libs/trusted-client.pem"
```

For more information on these options, see `encryption-key-management-conf-options`.

.. include:: /includes/reference/fact-add-v1-flag.rst

.. include:: /includes/extracts/default-bind-ip-security-additional-command-line.rst

.. include:: /includes/reference/fact-connection-check.rst

> **Seealso:** `encryption-key-management-options`

## Local Key Management

Using the keyfile method does not meet most regulatory key management guidelines and requires users to securely manage their own keys.

The safe management of the keyfile is critical.

.. include:: /includes/admonition-local-key-mgmt-rotation.rst

To encrypt using a keyfile, you must have a base64 encoded keyfile that contains a single 16 or 32 character string. The keyfile must only be accessible by the owner of the :binary:`~bin.mongod` process.

#. Create the base64 encoded keyfile with the 16 or 32 character string. You can generate the encoded keyfile using any method you prefer. For example,

```bash
   openssl rand -base64 32 > mongodb-keyfile
```

#. Update the file permissions.

```bash
   chmod 600 mongodb-keyfile
```

#. To use the key file, start :binary:`~bin.mongod` with the following options:

- `--enableEncryption`,
- `--encryptionKeyFile <path to keyfile>`,
```bash
   mongod --enableEncryption --encryptionKeyFile  mongodb-keyfile

.. include:: /includes/extracts/default-bind-ip-security-additional-command-line.rst
```

#. Verify if the encryption key manager successfully initialized with the keyfile. If the operation was successful, the process will log the following message:

```bash
   [initandlisten] Encryption key manager initialized with key file: <path to keyfile>
```

> **Seealso:** `encryption-key-management-options`

## Encrypt Existing Data at Rest

MongoDB cannot encrypt existing data. When you enable encryption with a new key, the MongoDB instance cannot have any pre-existing data.

If you are using a replica set that does have existing data, use a rolling `initial sync <replica-set-initial-sync>` to encrypt the data.

For example, consider a replica set with three members. The replica set is in use and holds data that you want to encrypt. These are the steps you would take to encrypt the data at rest:

.. include:: /includes/steps/encrypt-with-rolling-sync.rst
