---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/configure-ldap-sasl-openldap.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

===========================================================

# Authenticate Using Self-Managed SASL and LDAP with OpenLDAP

.. include:: /includes/LDAP-deprecated.rst

MongoDB Enterprise provides support for proxy authentication of users. This allows administrators to configure a MongoDB cluster to authenticate users by proxying authentication requests to a specified Lightweight Directory Access Protocol (LDAP) service.

> **Note:** .. include:: /includes/extracts/4.2-changes-libldap.rst

## Considerations

> **Warning:** .. include:: /includes/admonition-mongodb-enterprise-windows-ldap.rst

.. include:: /includes/admonition-saslauthd-ldap-considerations.rst

## Configure `saslauthd`

LDAP support for user authentication requires proper configuration of the `saslauthd` daemon process as well as the MongoDB server.

.. include:: /includes/steps/configure-ldap-saslauthd-openldap.rst

## Configure MongoDB

.. include:: /includes/steps/configure-ldap-mongodb.rst
