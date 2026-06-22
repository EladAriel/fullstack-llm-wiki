---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/configure-ldap-sasl-activedirectory.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================================================

# Authenticate Using SASL and LDAP with Active Directory

.. include:: /includes/LDAP-deprecated.rst

MongoDB Enterprise provides support for proxy authentication of users. This allows administrators to configure a MongoDB cluster to authenticate users by proxying authentication requests to a specified Lightweight Directory Access Protocol (LDAP) service.

> **Note:** .. include:: /includes/extracts/4.2-changes-libldap.rst

## Considerations

> **Warning:** .. include:: /includes/admonition-mongodb-enterprise-windows-ldap.rst

.. include:: /includes/admonition-saslauthd-ldap-considerations.rst

## Configure `saslauthd`

LDAP support for user authentication requires proper configuration of the `saslauthd` daemon process as well as the MongoDB server.

.. include:: /includes/steps/configure-ldap-saslauthd-activedir.rst

## Configure MongoDB

.. include:: /includes/steps/configure-ldap-mongodb.rst
