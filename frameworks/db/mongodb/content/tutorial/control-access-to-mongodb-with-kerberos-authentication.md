---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/control-access-to-mongodb-with-kerberos-authentication.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=======================================================

# Configure MongoDB with Kerberos Authentication on Linux

## Overview

MongoDB Enterprise supports authentication using a `Kerberos service </core/kerberos>`. Kerberos is an industry standard authentication protocol for large client/server systems. MongoDB Enterprise only supports the [MIT implementation](https://kerberos.org/)_ of Kerberos.

## Prerequisites

.. include:: /includes/fact-confirm-enterprise-binaries.rst

.. include:: /includes/fact-kerberos-FQDN-repica-sets.rst

Setting up and configuring a Kerberos deployment is beyond the scope of this document. Please refer to the [MIT Kerberos documentation](https://web.mit.edu/kerberos/krb5-latest/doc/) or your operating system documentation for information on how to configure a Kerberos deployment.

In order to use MongoDB with Kerberos, a `Kerberos service principal <kerberos-service-principal>` for each :binary:`~bin.mongod` and :binary:`~bin.mongos` instance in your MongoDB deployment must be [added to the Kerberos database](https://web.mit.edu/kerberos/krb5-latest/doc/admin/database.html#add-principal). You can add the service principal by running a command similar to the following on your KDC:

```bash
kadmin.local addprinc mongodb/m1.example.com@EXAMPLE.COM
```

On each system running :binary:`~bin.mongod` or :binary:`~bin.mongos`, a `keytab file <keytab-files>` must be [created](https://web.mit.edu/kerberos/krb5-latest/doc/admin/appl_servers.html#keytabs) for the respective service principal. You can create the keytab file by running a command similar to the following on the system running :binary:`~bin.mongod` or :binary:`~bin.mongos`:

```bash
kadmin.local ktadd mongodb/m1.example.com@EXAMPLE.COM
```

## Procedure

The following procedure outlines the steps to add a Kerberos user principal to MongoDB, configure a standalone :binary:`~bin.mongod` instance for Kerberos support, and connect using :binary:`~bin.mongosh` and authenticate the user principal.

.. include:: /includes/steps/control-access-to-mongodb-with-kerberos-authentication.rst

## Additional Considerations

### KRB5_KTNAME

If you installed MongoDB Enterprise using one of the official `.deb` or `.rpm` packages, and you use the included init/upstart scripts to control the :binary:`~bin.mongod` instance, you can set the `KRB5_KTNAME` variable in the default environment settings file instead of setting the variable each time.

Recent versions of Red Hat and Debian-based systems use `systemd`. Older versions use `init` for system initialization. Follow the appropriate instructions to configure the `KRB5_KTNAME` variable for your system.

`systemd` Configuration Files ```````````````````````````````

`systemd` stores configuration in unit files. Update the unit file to set the `KRB5_KTNAME` variable.

`init` Configuration Files ````````````````````````````

For `.rpm` installations, the default environment settings file is :file:`/etc/sysconfig/mongod`.

For `.deb` installations, the file is :file:`/etc/default/mongodb`.

Set the `KRB5_KTNAME` value by adding a line that resembles the following:

```javascript
KRB5_KTNAME="<path to keytab>"
```

### Configure `mongos` for Kerberos

To start :binary:`~bin.mongos` with Kerberos support, set the environmental variable `KRB5_KTNAME` to the path of its `keytab file <keytab-files>` and the :binary:`~bin.mongos` parameter :parameter:`authenticationMechanisms` to `GSSAPI` in the following form:

```bash
env KRB5_KTNAME=<path to keytab file> \
mongos \
--setParameter authenticationMechanisms=GSSAPI \
<additional mongos options>
```

.. include:: /includes/extracts/default-bind-ip-security-additional-command-line.rst

For example, the following starts a :binary:`~bin.mongos` instance with Kerberos support:

```bash
env KRB5_KTNAME=/opt/mongodb/mongos.keytab \
mongos \
--setParameter authenticationMechanisms=GSSAPI \
--configdb shard0.example.net, shard1.example.net,shard2.example.net \
--keyFile /opt/mongodb/mongos.keyfile \
--bind_ip localhost,<hostname(s)|ip address(es)>
```

The path to your :binary:`~bin.mongos` as well as your `keytab file <keytab-files>` may differ. The `keytab file <keytab-files>` must be only accessible to the owner of the :binary:`~bin.mongos` process.

Modify or include any additional :binary:`~bin.mongos` options as required for your configuration. For example, instead of using :option:`--keyFile <mongos --keyFile>` for internal authentication of sharded cluster members, you can use `X.509 member authentication <x509-internal-authentication>` instead.

### Use a Config File

To configure :binary:`~bin.mongod` or :binary:`~bin.mongos` for Kerberos support using a `configuration file </reference/configuration-options>`, specify the :parameter:`authenticationMechanisms` setting in the configuration file.

If using the `YAML configuration file format </reference/configuration-options>`:

```yaml
setParameter:
   authenticationMechanisms: GSSAPI
```

.. include:: /includes/extracts/default-bind-ip-security-additional-config-file.rst

For example, if :file:`/opt/mongodb/mongod.conf` contains the following configuration settings for a standalone :binary:`~bin.mongod`:

```yaml
security:
   authorization: enabled
setParameter:
   authenticationMechanisms: GSSAPI
storage:
   dbPath: /opt/mongodb/data
net:
   bindIp: localhost,<hostname(s)|ip address(es)>
```

To start :binary:`~bin.mongod` with Kerberos support, use the following form:

```bash
env KRB5_KTNAME=/opt/mongodb/mongod.keytab \
/opt/mongodb/bin/mongod --config /opt/mongodb/mongod.conf
```

The path to your :binary:`~bin.mongod`, `keytab file <keytab-files>`, and configuration file may differ. The `keytab file <keytab-files>` must be only accessible to the owner of the :binary:`~bin.mongod` process.

### Troubleshoot Kerberos Setup for MongoDB

If you encounter problems when starting :binary:`~bin.mongod` or :binary:`~bin.mongos` with Kerberos authentication, see `/tutorial/troubleshoot-kerberos`.

### Incorporate Additional Authentication Mechanisms

Kerberos authentication (`GSSAPI <security-auth-kerberos>` (Kerberos)) can work alongside:

- MongoDB's SCRAM authentication mechanism:
- `SCRAM-SHA-1 <authentication-scram>`
- `SCRAM-SHA-256 <authentication-scram>`
- MongoDB's authentication mechanism for LDAP:
- `PLAIN <security-auth-ldap>` (LDAP SASL)
- MongoDB's authentication mechanism for X.509:
- `MONGODB-X509 <security-auth-x509>`)
Specify the mechanisms as follows:

```bash
--setParameter authenticationMechanisms=GSSAPI,SCRAM-SHA-256
```

Only add the other mechanisms if in use. This parameter setting does not affect MongoDB's internal authentication of cluster members.

## Testing and Verification

.. include:: /includes/fact-mongokerberos.rst
