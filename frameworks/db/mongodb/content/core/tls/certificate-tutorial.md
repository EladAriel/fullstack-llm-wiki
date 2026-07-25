---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/tls/certificate-tutorial.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

==============================

# Obtain TLS Server Certificates

Obtain server certificates to enable |tls| encryption for your self-managed MongoDB replica set deployments.

.. include:: /includes/tls/note-self-managed-only.rst

## Before you Begin

Before you start, ensure you have the following information and resources:

- You have a self-managed MongoDB replica set deployment that you want to
secure with TLS.

- You have at least one admin user enabled on your deployment
to verify TLS connections in later tutorials. If you want to enable X.509 client authentication, the admin user must have at least the :authrole:`userAdmin` role to create and modify users in the `$external` database.

- You have a hostname for each node in your deployment, such as `mongo0.example.com`,
`mongo1.example.com`, and `mongo2.example.com`. If you are using a public :abbr:`CA (Certificate Authority)`, you must have a registered domain name that corresponds to these hostnames.

- You have [OpenSSL](https://www.openssl.org/)_ installed on your machine.
- If you are planning on using a public CA,
such as Let's Encrypt or DigiCert, you know which public CA you are using. If you are planning on using a private CA, you have access to your organization's :abbr:`PKI (Public Key Infrastructure)` information. The process for obtaining certificates might be different based on the CA you use. However, you must end with the same `.pem` files described in the `final result <tls-certificate-final-state>` section of this tutorial.

- You have your preferred command line interface open.
- You know your deployment TLS configuration requirements and whether your certificates
need `clientAuth` :abbr:`EKU (Extended Key Usage)` based on the TLS Planning page.

## Steps

This tutorial creates one certificate called `mongo0.pem` for the first node in your deployment. When generating certificates for additional nodes, be specific in your file names. For example, name the certificate for your first secondary node `mongo1.pem`.

## Final Result

At the end of this tutorial, you have the following `.pem` files in `/etc/ssl/mongodb`:

- For **each node**, you have a `.pem` file that contains the certificate and
private key for that node, such as `mongo0.pem`, `mongo1.pem`, and `mongo2.pem`.

- For the deployment overall, you have the intermediate CA certificate that issued
the certificates for each node, such as `ca.pem`.

## Next Steps

To learn how to configure TLS for your self-managed MongoDB deployment, continue to the next tutorial, `Configure TLS for a Self-Managed Deployment <configure-server-tls-tutorial>`.
