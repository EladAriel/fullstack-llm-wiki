---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/rotate-key-replica-set.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=========================================

# Rotate Keys for Self-Managed Replica Sets

Replica set members can use `keyfiles <internal-auth-keyfile>` to authenticate each other as members of the same deployment.

.. include:: /includes/fact-keyfile-common-key.rst

The following tutorial steps through the process to update the key for a replica set without downtime. [#exclude-encryption-keyfile]_

> **Warning:** The example keys in this tutorial are for illustrative purposes
only. Do :red:`NOT` use for your deployment. Instead, generate a
keyfile using any method you choose (for example, ``openssl rand -base64
756``, etc.).

Consider a replica set where each member's keyfile contains the following key:

.. figure:: /images/example-key1.png

The following procedure updates the replica set members to use a new key:

.. figure:: /images/example-key2.png

This tutorial is not applicable to the `keyfile <encrypt-local-key-mgmt>` used for the `MongoDB's encrypted storage engine </core/security-encryption-at-rest>` local key management. That `keyfile <encrypt-local-key-mgmt>` can only contain a single key.

## Procedure

### 1. Modify the Keyfile to Include Old and New Keys

Modify each member's keyfile to include both the old and new keys. You can specify multiple keys either as strings enclosed in quotes or as a sequence of keys.

> **Warning:** The example keys in this tutorial are for illustrative purposes
only. Do :red:`NOT` use for your deployment. Instead, generate a
keyfile using any method you choose (e.g. ``openssl rand -base64
756``, etc.).

You can specify multiple key strings as a sequence of key strings (optionally enclosed in single or double quotes).

.. figure:: /images/example-multiple-keys2.png

### 2. Restart Each Member

Once all the keyfiles contain both the old and new keys, restart each member one at a time.

**For each secondary member**, connect :binary:`~bin.mongosh` to the member and:

a. Use the :method:`db.shutdownServer()` method to shut down the member:

```javascript
      use admin
      db.shutdownServer()
```

b.   Restart the member.

**For the primary**, connect :binary:`~bin.mongosh` to the member and

a. Use :method:`rs.stepDown()` to step down the member:

```javascript
   rs.stepDown()
```

#. Use the :method:`db.shutdownServer()` method to shut down the member:

```javascript
   use admin
   db.shutdownServer()
```

#. Restart the member.

Since the keyfiles contains both the old and new keys, all members can now accept either keys for membership authentication.

### 3. Update Keyfile Content to the New Key Only

> **Warning:** The example keys in this tutorial are for illustrative purposes
only. Do :red:`NOT` use for your deployment. Instead, generate a
keyfile using any method you choose (e.g. ``openssl rand -base64
756``, etc.).

Modify each member's keyfile to include only the new password.

.. figure:: /images/example-key2.png

### 4. Restart Each Member

Once all the keyfiles contain the new key only, restart each member one at a time.

**For each secondary member**, connect :binary:`~bin.mongosh` to the member and:

a. Use the :method:`db.shutdownServer()` method to shut down the member:

```javascript
   use admin
   db.shutdownServer()
```

b.   Restart the member.

**For the primary**, connect :binary:`~bin.mongosh` to the member and

a. Use :method:`rs.stepDown()` to step down the member:

```javascript
   rs.stepDown()
```

#. Use the :method:`db.shutdownServer()` method to shut down the member:

```javascript
   use admin
   db.shutdownServer()
```

#. Restart the member.

All members now accept only the new key for membership authentication.
