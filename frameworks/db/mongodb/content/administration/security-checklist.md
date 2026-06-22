---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/administration/security-checklist.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================================

# Security Checklist for Self-Managed Deployments

This page lists security measures to protect your MongoDB installation. The list is not exhaustive.

## Pre-production Checklist/Considerations

### |arrow| Enable Access Control and Enforce Authentication

- Enable access control and specify an authentication mechanism.
MongoDB Community supports the following `authentication mechanisms <security-authentication-mechanisms>`:

- `authentication-scram` (Default)
- `X.509 Certificate Authentication <security-auth-x509>`.
In addition to the preceding mechanisms, MongoDB Atlas and MongoDB Enterprise support the following mechanisms:

- `LDAP proxy authentication <security-auth-ldap>`, and
- `Kerberos authentication <security-auth-kerberos>`.
These mechanisms allow MongoDB to integrate into your existing authentication system.

> **Seealso:** - `/core/authentication`
- `/tutorial/enable-authentication`

### |arrow| Configure Role-Based Access Control

- Create a `user administrator <create-user-admin>` **first**, then
create additional users. Create a unique MongoDB user for each person/application that accesses the system.

- Follow the principle of least privilege. Create roles that define the
exact access rights required by a set of users. Then create users and assign them only the roles they need to perform their operations. A user can be a person or a client application.

> **Note:**   A user can have privileges across different databases. If a user
  requires privileges on multiple databases, create a single user
  with roles that grant applicable database privileges instead of
  creating the user multiple times in different databases.

> **Seealso:** - `/core/authorization`
- `/tutorial/create-users`
- `/tutorial/manage-users-and-roles`

### |arrow| Encrypt Communication (TLS/SSL)

- Configure MongoDB to use TLS/SSL for all incoming and outgoing
connections, including between :binary:`~bin.mongod` and :binary:`~bin.mongos` components and between all applications and MongoDB.

.. include:: /includes/fact-tls-libraries.rst

> **Seealso:** `/tutorial/configure-ssl`.

### |arrow| Encrypt and Protect Data

- You can encrypt data in the storage layer with the WiredTiger storage
engine's native `/core/security-encryption-at-rest`.

- If you are not using WiredTiger's encryption at rest, MongoDB
data should be encrypted on each host using file-system, device, or physical encryption (for example dm-crypt). You should also protect MongoDB data using file-system permissions. MongoDB data includes data files, configuration files, auditing logs, and key files.

- You can use `qe-manual-feature-qe` or `manual-csfle-feature`
to encrypt fields in documents application-side prior to transmitting data over the wire to the server.

- Collect logs to a central log store. These logs contain database
authentication attempts including source IP addresses.

### |arrow| Limit Network Exposure

- Ensure that MongoDB runs in a trusted network environment and
configure firewall or security groups to control inbound and outbound traffic for your MongoDB instances.

- Disable direct SSH root access.
- Allow only trusted clients to access the network interfaces and
ports on which MongoDB instances are available.

> **Seealso:** - `/core/security-hardening`
- the :setting:`net.bindIp` configuration setting
- the :setting:`security.clusterIpSourceAllowlist` configuration
  setting
- the :ref:`authenticationRestrictions
  <db-createUser-authenticationRestrictions>` field to the
  :method:`db.createUser()` command to specify a per-user IP
  allow list.

### |arrow| Audit System Activity

- `MongoDB Enterprise
<http://www.mongodb.com/products/mongodb-enterprise-advanced>`_ includes a system auditing facility that can record system events (including user operations and connection events) on a MongoDB instance. Audit records permit forensic analysis and allow administrators to exercise proper controls. You can set up filters to record only specific events, such as authentication events.

> **Seealso:** - `/core/auditing`
- `/tutorial/configure-auditing`

### |arrow| Run MongoDB with a Dedicated User

- Run MongoDB processes with a dedicated operating system user
account. Ensure that the account has permissions to access data but no unnecessary permissions.

> **Seealso:** `/installation`

### |arrow| Run MongoDB with Secure Configuration Options

- MongoDB supports the execution of JavaScript code for certain
server-side operations: :dbcommand:`mapReduce`, :query:`$where`, :group:`$accumulator`, and :expression:`$function`. If you do not use these operations, disable server-side scripting by using the :option:`--noscripting <mongod --noscripting>` option.

- Keep input validation enabled. MongoDB enables input validation
by default through the :setting:`net.wireObjectCheck` setting. This ensures that all documents stored by the :binary:`~bin.mongod` instance are valid `BSON`.

### |arrow| Request a Security Technical Implementation Guide (where applicable)

- The Security Technical Implementation Guide (STIG) contains
security guidelines for deployments within the United States Department of Defense. MongoDB Inc. provides its STIG, upon [request](http://www.mongodb.com/lp/contact/stig-requests).

### |arrow| Consider Security Standards Compliance

- To learn how to build HIPAA or PCI-DSS compliant application
infrastructure using MongoDB security capabilities, see the [MongoDB Security Reference Architecture](https://www.mongodb.com/collateral/mongodb-security-architecture).

## Antivirus and Endpoint Detection and Response Scanning

.. include:: /includes/security/fact-antivirus-scan.rst

## Periodic/Ongoing Production Checks

- Periodically check for `MongoDB Product CVE
<https://www.mongodb.com/alerts>`_ and upgrade your products .

- Consult the `MongoDB end of life dates
<https://www.mongodb.com/support-policy>`_ and upgrade to the latest version.

- Ensure that your information security management system policies
and procedures extend to your MongoDB installation, including performing the following:

- Periodically apply patches to your machine.
- Review policy/procedure changes, especially changes to your
network rules to prevent inadvertent MongoDB exposure to the Internet.

- Review MongoDB database users and periodically rotate them.
- If you're using {+qe+}, compact the metadata collections as directed in
`Scheduling Metadata Compaction <qe-metadata-compaction>` to reduce storage space.

## Report Suspected Security Bugs

If you suspect that you have identified a security bug in any MongoDB products, please report the issue through the MongoDB [Bug Submission Form](https://www.mongodb.com/security).
