---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/security-internal-authentication.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================================

# Self-Managed Internal/Membership Authentication

You can require that members of `replica sets <replica set>` and `sharded clusters <sharded cluster>` authenticate to each other. For the internal authentication of the members, MongoDB can use either `keyfiles <internal-auth-keyfile>` or `X.509 <internal-auth-x509>` certificates.

The selected method is used for all internal communication. For example, when a client authenticates to a :binary:`~bin.mongos` using one of the supported `authentication mechanisms <security-authentication-mechanisms>`, the `mongos` then uses the configured internal authentication method to connect to the required :binary:`~bin.mongod` processes.

> **Note:** Enabling internal authentication also enables :doc:`client
authorization </core/authorization>`.

## Keyfiles

Keyfiles use `/core/security-scram` challenge and response authentication mechanism where the keyfiles contain the shared password for the members.

### Key Requirements

A key's length must be between 6 and 1024 characters and may only contain characters in the base64 set. MongoDB strips whitespace characters (e.g. `x0d`, `x09`, and `x20`) for cross-platform convenience. As a result, the following operations produce identical keys:

```bash
echo -e "mysecretkey" > key1
echo -e "my secret key" > key1
echo -e "my secret key\n" > key2
echo -e "my    secret    key" > key3
echo -e "my\r\nsecret\r\nkey\r\n" > key4
```

### Keyfile Format

.. include:: /includes/extracts/4.2-changes-keyfile-fmt.rst

For example,

The ability to specify multiple keys in a file allows for the rolling upgrade of the keys without downtime. See `/tutorial/rotate-key-replica-set` and `/tutorial/rotate-key-sharded-cluster`.

All :binary:`~bin.mongod` and :binary:`~bin.mongos` instances of a deployment must share at least one common key.

.. include:: /includes/extracts/keyfile-file-permission.rst

You must store the keyfile on each server hosting the member of the replica set or sharded clusters.

For `MongoDB's encrypted storage engine </core/security-encryption-at-rest>`, the `keyfile <encrypt-local-key-mgmt>` used for local key management can only contain a single key .

### MongoDB Configuration for Keyfile

To specify the keyfile, use the :setting:`security.keyFile` setting or `--keyFile` command line option.

For an example of keyfile internal authentication, see `/tutorial/enforce-keyfile-access-control-in-existing-replica-set`.

## X.509

Members of a replica set or sharded cluster can use X.509 certificates for internal authentication instead of using keyfiles. This is also known as Mutual TLS or mTLS. MongoDB supports X.509 certificate authentication for use with a secure TLS/SSL connection.

> **Note:** .. include:: /includes/fact-tls-1.0.rst

### Member Certificate Requirements

.. include:: /includes/extracts/x509-certificate-member.rst

### MongoDB Configuration

.. include:: /includes/extracts/x509-member-auth-configuration.rst

## Next Steps

For an example of X.509 internal authentication, see `x509-internal-authentication`.

To upgrade from keyfile internal authentication to X.509 internal authentication, see `upgrade-to-x509-internal-authentication`.

## Contents

- Deploy Replica Set </tutorial/deploy-replica-set-with-keyfile-access-control>
- Update Replica Set </tutorial/enforce-keyfile-access-control-in-existing-replica-set>
- Update Replica Set (No Downtime) </tutorial/enforce-keyfile-access-control-in-existing-replica-set-without-downtime>
- Deploy Sharded Cluster </tutorial/deploy-sharded-cluster-with-keyfile-access-control>
- Update Sharded Cluster </tutorial/enforce-keyfile-access-control-in-existing-sharded-cluster>
- Update Sharded Cluster (No Downtime) </tutorial/enforce-keyfile-access-control-in-existing-sharded-cluster-no-downtime>
- Rotate Replica Set Keys </tutorial/rotate-key-replica-set>
- Rotate Sharded Cluster Keys </tutorial/rotate-key-sharded-cluster>
- Use X.509 </tutorial/configure-x509-member-authentication>
- Upgrade to X.509 from Keyfile </tutorial/upgrade-keyfile-to-x509>
- Rotate X.509 with New DN </tutorial/rotate-x509-membership-certificates>
- Rotate X.509 with New clusterAuthX509 Attributes </tutorial/rotate-x509-member-cert>
- Rotate X.509 to Use Extension Values </tutorial/rotate-x509-to-extensionValue>
