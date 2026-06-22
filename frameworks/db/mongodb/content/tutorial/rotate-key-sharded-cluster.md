---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/rotate-key-sharded-cluster.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=============================================

# Rotate Keys for Self-Managed Sharded Clusters

Sharded cluster members can use `keyfiles <internal-auth-keyfile>` to authenticate each other as memers of the same deployment.

.. include:: /includes/fact-keyfile-common-key.rst

The following tutorial steps through the process to update, without any downtime, the key for a sharded cluster. [#exclude-encryption-keyfile]_

> **Warning:** The example keys in this tutorial are for illustrative purposes
only. Do :red:`NOT` use for your deployment. Instead, generate a
keyfile using any method you choose (e.g. ``openssl rand -base64
756``, etc.).

Consider a sharded cluster where each member's keyfile contains the following key:

.. figure:: /images/example-key1.png

The following procedure updates the sharded cluster members to use a new key:

.. figure:: /images/example-key2.png

This tutorial is not applicable to the `keyfile <encrypt-local-key-mgmt>` used for the `MongoDB's encrypted storage engine </core/security-encryption-at-rest>` local key management. That `keyfile <encrypt-local-key-mgmt>` can only contain a single key.

## Before You Begin

.. include:: /includes/dSO-role-intro.rst

.. include:: /includes/dSO-warning.rst

## Procedure

### 1. Modify the Keyfile to Include Old and New Keys

Modify each member's keyfile to include both the old and new keys.

> **Warning:** The example keys in this tutorial are for illustrative purposes
only. Do :red:`NOT` use for your deployment. Instead, generate a
keyfile using any method you choose (e.g. ``openssl rand -base64
756``, etc.).

You can specify multiple key strings as a sequence of key strings (optionally enclosed in quotes):

.. figure:: /images/example-multiple-keys2.png

### 1. Restart Each Member

Once all the keyfiles contain both the old and new keys, restart each member one at a time.

Config Servers ``````````````

**For each secondary of the config server replica set (CSRS)**, connect :binary:`~bin.mongosh` to the member and:

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

Shard Replica Sets ``````````````````

**For each secondary member of the shard replica sets**, connect :binary:`~bin.mongosh` to the member and:

a. Use the :method:`db.shutdownServer()` method to shut down the member:

```javascript
   use admin
   db.shutdownServer()
```

b.   Restart the member.

**For the primary of each shard replica set**, connect :binary:`~bin.mongosh` to the member and

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

`mongos` Routers ``````````````````

**For each mongos/router instance**, connect :binary:`~bin.mongosh` to the :binary:`~bin.mongos` instance and:

a. Use the :method:`db.shutdownServer()` method to shut down the member:

```javascript
   use admin
   db.shutdownServer()
```

b.   Restart the member.

Once all members have been restarted, the members now accept either the old or new key for membership authentication.

### 3. Update Keyfile Content to the New Key Only

> **Warning:** The example keys in this tutorial are for illustrative purposes
only. Do :red:`NOT` use for your deployment. Instead, generate a
keyfile using any method you choose (e.g. ``openssl rand -base64
756``, etc.).

Modify each member's keyfile to include only the new password.

.. figure:: /images/example-key2.png

### 4. Restart Each Member

Once all the keyfiles contain the new key only, restart each member one at a time.

Config Servers ``````````````

**For each secondary of the config server replica set (CSRS)**, connect :binary:`~bin.mongosh` to the member and:

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

Shard Replica Sets ``````````````````

**For each secondary member of the shard replica sets**, connect :binary:`~bin.mongosh` to the member and:

a. Use the :method:`db.shutdownServer()` method to shut down the member:

```javascript
   use admin
   db.shutdownServer()
```

b.   Restart the member.

**For the primary of each shard replica set**, connect :binary:`~bin.mongosh` to the member and

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

`mongos` Routers ``````````````````

**For each mongos/router instance**, connect :binary:`~bin.mongosh` to the :binary:`~bin.mongos` instance and:

a. Use the :method:`db.shutdownServer()` method to shut down the member:

```javascript
   use admin
   db.shutdownServer()
```

b.   Restart the member.

Once all members have been restarted, the members now accept only the new key for membership authentication.
