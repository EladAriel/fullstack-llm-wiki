---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/rotate-x509-to-extensionValue.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=================================================

# Rotate X.509 Certificates to Use Extension Values

.. versionadded:: 7.0

Cluster members can use `X.509 certificates <internal-auth-x509>` for membership authentication to identify other servers in the same deployment. This tutorial describes how to perform a rolling update to migrate from using certificate Distinguished Name (DN) attributes to using extension values to identify members of a cluster.

When a server configured with the :setting:`net.tls.clusterAuthX509.extensionValue` setting receives a connection request, it compares the the extension value string of the presented certificates to the configured values of the :setting:`~net.tls.clusterAuthX509.extensionValue` setting and :parameter:`tlsClusterAuthX509Override` parameter. If the values match, it treats the connection as a cluster member.

Clusters adopting new certificates can use the :parameter:`tlsClusterAuthX509Override` parameter to accept X.509 certificates with different DN attributes during the certificate rotation procedure. Once all members use certificates with the new value, remove the override to begin rejecting the now out of date certificates.

## About This Task

Consider a replica set where member certificates, set using the :setting:`~net.tls.clusterFile` and :setting:`~net.tls.certificateKeyFile` settings, have Distinguished Name (DN) attributes that use the `MongoDB` organization and `MongoDB Server` organizational unit. These DN attributes are set using the :setting:`net.tls.clusterAuthX509.attributes` setting.

```yaml
security:
  clusterAuthMode:      x509
net:
  tls:
    mode:               requireTLS
    certificateKeyFile: /etc/mycerts/10gen-server1.pem
    CAFile:             /etc/mycerts/ca.pem
    clusterFile:        /etc/mycerts/10gen-cluster1.pem
    clusterCAFile:      /etc/mycerts/ca.pem
    clusterAuthX509:
       attributes:      O=MongoDB, OU=MongoDB Server
```

.. include:: /includes/x509-meets-requirements.rst

## Steps

These steps update member certificates to use new X.509 certificates on a cluster configured with the :setting:`~net.tls.clusterAuthX509.attributes` setting.

Initially, the clusters identify members using DN values. With the new certificates, the servers instead identify members using the `mongodb://example.mongodb.net` extension value and ignore certificate attributes.

## Learn More

- `security-auth-x509`
- `x509-internal-authentication`
- `upgrade-to-x509-internal-authentication`
- `x509-rotate-member-certs`
