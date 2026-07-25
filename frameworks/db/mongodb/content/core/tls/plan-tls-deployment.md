---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/tls/plan-tls-deployment.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

========================================================

# Plan Your TLS Configuration for Self-Managed Deployments

|tls| encrypts connections between clients and your MongoDB deployment, and between nodes in a replica set. Before you configure TLS, use this page to decide on the configuration that matches your security requirements.

.. include:: /includes/tls/note-self-managed-only.rst

## Before You Begin

Before you plan your TLS configuration, ensure that you have the following resources and information:

- A self-managed MongoDB replica set to configure with TLS.
- The type of certificate authority available to you, such as a
public or private :abbr:`CA (Certificate Authority)`.

- Your security requirements, such as whether you need
`X.509 authentication <security-auth-x509>`.

The type of CA you have access to determines which TLS configurations are available to you:

## Choose Your Configuration

The following sections help you decide how to configure TLS encryption and authentication between nodes in a replica set, and between clients and the server.

.. figure:: /images/tls-config-tls-x509.svg

### Encryption Between Nodes

All TLS-enabled deployments encrypt connections between nodes. You can also enable intra-cluster :abbr:`mTLS (Mutual TLS)`, which requires nodes to present certificates to authenticate as clients during the TLS handshake. When a node accepts an incoming connection, it presents its server certificate so that the connecting party can verify its identity. When a node makes an outbound connection to another node, its behavior depends on whether you enable intra-cluster mTLS.

Use the following table to determine what you need for each encryption mode:

Without intra-cluster mTLS, nodes do not present a certificate to authenticate as a client on outbound connections. The connecting node verifies the receiving node's server certificate, but the receiving node does not verify the connecting node's identity through the TLS handshake. Use this configuration if you can only obtain certificates with a `serverAuth` :abbr:`EKU (Extended Key Usage)`, such as through a public CA. You cannot enable X.509 authentication between nodes with this configuration.

With intra-cluster mTLS, each node also presents a certificate on outbound connections to other nodes, providing mutual identity verification. Intra-cluster mTLS is required to use X.509 node authentication. However, because it requires certificates with the `clientAuth` EKU, you must have access to a private CA.

### Authentication Between Nodes

Replica set members authenticate to each other to confirm that only authorized members participate in replication. By default, authorization-enabled replica sets use keyfile authentication between nodes. However, if you enable intra-cluster mTLS, you can use X.509 certificate authentication instead.

Use the following table to determine what you need for each authentication mode:

If you use keyfile authentication, all replica set members share a single secret stored in a keyfile. Each node proves its membership by presenting the shared secret when it connects to other nodes in the set. Because all nodes share the same key, if you want to revoke an individual node's access you must replace the keyfile across all nodes.

X.509 authentication uses each node's cluster certificate to verify membership. Because the certificate exchange occurs during the TLS handshake, X.509 node authentication requires intra-cluster mTLS so nodes have mutual verification of identity. Each node's unique certificate identity allows you to revoke an individual node's access by revoking its certificate, without affecting other nodes. Additionally, authentication and encryption are established together in a single handshake.

Cluster member certificates must include X.509 attributes that distinguish them from regular client certificates. To learn about the required certificate attributes, see `x509-member-certificate`.

### Encryption Between Client and Server

When a client such as {+mongosh+} or a driver connects to a TLS-enabled `mongod` instance, the server presents its certificate to prove its identity, and the client verifies the certificate against a trusted CA certificate. The client also confirms that the server's hostname matches the certificate's hostname. If verification succeeds, TLS encrypts the connection between server and client.

Use the following table to determine what you need for each encryption mode:

You can set :setting:`~net.tls.allowConnectionsWithoutCertificates` to `true` to enable the client to connect without sending a certificate. Enabling this prevents users from connecting with incorrect certificates, such as those that only include the `serverAuth` EKU. The server encrypts the connection and proves its own identity to the client, but the server cannot verify the client's identity through the TLS handshake. The client must authenticate through a method like SCRAM.

If the client presents its own certificate during the handshake, the server can verify the client certificate against a trusted CA. This establishes mutual TLS between server and client. The client must present a certificate to enable X.509 client authentication between client and server.

### Authentication Between Client and Server

After you establish the TLS connection, clients must authenticate to access the deployment. Clients can authenticate in `many ways <authentication>`, but this quickstart covers SCRAM and X.509 authentication.

Use the following table to determine what you need for each authentication mode:

MongoDB uses SCRAM as the default client authentication mechanism. The client provides a username, password, and the authentication database, and MongoDB verifies the credentials against users in the specified database. SCRAM does not require the client to present a certificate during the TLS handshake.

X.509 client authentication uses the certificate that the client presents during connection. Once mutual TLS is established, the client authenticates to the `$external` database using the `MONGODB-X509` mechanism. MongoDB maps the subject field in the certificate to a user in the `$external` database.

## Next Steps

After you determine your configuration using this page, continue to `tls-certificate-tutorial`.
