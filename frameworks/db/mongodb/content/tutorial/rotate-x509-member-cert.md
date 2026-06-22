---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/rotate-x509-member-cert.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

====================================================

# Rotate Certificates on Clusters with clusterAuthX509

.. versionadded:: 7.0

Cluster members can use `X.509 certificates <internal-auth-x509>` for membership authentication to identify other servers in the same deployment. This tutorial describes how to perform a rolling update to rotate X.509 certificates on a cluster that uses the :setting:`net.tls.clusterAuthX509.attributes` settings to configure the cluster members' Distinguished Name (DN) attributes.

> **Note:** To perform a rolling update to rotate certificates on a cluster that doesn't
use the :setting:`net.tls.clusterAuthX509` settings and won't after the update,
see `x509-rolling-update`.

When a server configured with the :setting:`net.tls.clusterAuthX509.attributes` setting receives a connection request, it compares the Distinguished Name (DN) attributes in the `subject` field of the presented certificates to the configured values of the :setting:`~net.tls.clusterAuthX509.attributes` setting and :parameter:`tlsClusterAuthX509Override` parameter. If the values match, it treats the connection as a cluster member.

In some situations, you may need to update the member certificates to new certificates with a new Distinguished Name (DN), such as if an organization changes its name. In a rolling update, member certificates are updated one at a time, and your deployment does not incur any downtime.

Clusters adopting new certificates can use the :parameter:`tlsClusterAuthX509Override` parameter to accept X.509 certificates with different subject DN attributes during the certificate rotation procedure. Once all members use certificates with the new value, remove the override to begin rejecting the now out of date certificates.

## About This Task

Consider a replica set where member certificates, set using the :setting:`~net.tls.clusterFile` and :setting:`~net.tls.certificateKeyFile` settings, have Distinguished Name (DN) attributes that use the `10gen` organization and `10gen Server` organizational unit. These DN attributes are set using the :setting:`net.tls.clusterAuthX509.attributes` setting.

A member of this replica set has the following configuration file:

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
       attributes:      O=10gen, OU=10gen Server
```

The following procedure updates each replica set member's X.509 certificates to new certificates that have DN attributes that use the `MongoDB` organization and `MongoDB Server` organizational unit.

.. include:: /includes/x509-meets-requirements.rst

## Steps

These steps update member certificates to use new X.509 certificates on a cluster configured with the :setting:`net.tls.clusterAuthX509.attributes` setting.

The new certificates have Distinguished Names (DN) that change the Organization (O) attributes from `10gen` to `MongoDB` and the Organizational Unit (OU) attribute from `10gen Server` to `MongoDB Server`.

## Learn More

- `security-auth-x509`
- `x509-internal-authentication`
- `upgrade-to-x509-internal-authentication`
- `x509-rotate-member-to-extensionValue`
