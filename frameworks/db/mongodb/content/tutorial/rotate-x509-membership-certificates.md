---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/rotate-x509-membership-certificates.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=======================================================

# Rotate Certificates on Clusters without clusterAuthX509

Members of a replica set or a sharded cluster can use `X.509 certificates <internal-auth-x509>` for membership authentication to identify other servers in the same deployment. This tutorial describes how to perform a rolling update to rotate X.509 certificates on a cluster that doesn't use the :setting:`net.tls.clusterAuthX509` settings to configure Distinguished Name (DN) attributes.

> **Note:** To perform a rolling update to rotate certificates on a cluster that uses
the :setting:`net.tls.clusterAuthX509` settings or on a cluster that will use
these settings after the update, see `x509-rotate-member-certs`.

When a server node receives a connection request, it compares the Distinguished Name (DN) attributes in the `subject` field of the presented certificates to the subject DN attributes of its own certificates. The certificates match if their subjects contain the same values for the Organization (`O`), Organizational Unit (`OU`), and Domain Component (`DC`) attributes. A server's configuration file can also specify alternative DN attributes to use for matching in the :parameter:`tlsX509ClusterAuthDNOverride` parameter. If the server's subject DN attributes or configured :parameter:`tlsX509ClusterAuthDNOverride` value match the subject DN attributes of the presented certificate, the server node treats the connection as a cluster member.

In some situations, you may need to update the member certificates to new certificates with new subject Distinguished Name (DN) attributes, such as if an organization changes its name. In a rolling update, member certificates are updated one at a time, and your deployment does not incur any downtime.

Clusters adopting new certificates can use the :parameter:`tlsX509ClusterAuthDNOverride` parameter to accept x.509 certificates with different subject DN attributes during the certificate rotation procedure. Once all members use certificates with the new value, remove the override to begin rejecting the now out of date certificates.

## About This Task

Consider a replica set where each member's X.509 certificates, set using the :setting:`~net.tls.clusterFile` and :setting:`~net.tls.certificateKeyFile` settings, have subject DN attributes of `"OU=10gen Server,O=10gen"`.

A member of this replica set has the following configuration file:

```yaml
net.tls.mode: requireTLS
net.tls.certificateKeyFile: "./mycerts/10gen-server1.pem"
net.tls.CAFile: "./mycerts/ca.pem"

security.clusterAuthMode: x509
net.tls.clusterFile:  "./mycerts/10gen-cluster1.pem"
net.tls.clusterCAFile: "./mycerts/ca.pem"
```

The following procedure updates each member's certificates to new certificates that have subject DN attributes of `"OU=MongoDB Server, O=MongoDB"`.

.. include:: /includes/x509-meets-requirements.rst

## Steps
