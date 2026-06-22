---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/configure-auditing.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================

# Configure Auditing

> **Note:** MongoDB Atlas supports auditing for all `M10` and larger
clusters. Atlas supports specifying a JSON-formatted audit
filter as documented in `/tutorial/configure-audit-filters`
and using the Atlas audit filter builder for simplified auditing
configuration. To learn more, see the Atlas documentation for
:atlas:`Set Up Database Auditing </database-auditing>`
and
`Configure a Custom Auditing Filter <auditing-custom-filter>`.

:products:`MongoDB Enterprise </mongodb-enterprise-advanced>` supports `auditing <auditing>` of various operations. A complete auditing solution must involve **all** :binary:`~bin.mongod` server and :binary:`~bin.mongos` router processes.

The audit facility can write audit events to the console, the `syslog` (option is unavailable on Windows), a JSON file, or a BSON file. For details on the audited operations and the audit log messages, see `/reference/audit-message`.

## Enable and Configure Audit Output

To enable auditing in MongoDB Enterprise, set an audit output destination with :option:`--auditDestination <mongod --auditDestination>`.

> **Warning:** For sharded clusters, if you enable auditing on
:binary:`~bin.mongos` instances you must also enable auditing on the
cluster's :binary:`~bin.mongod` instances. Configure auditing for
:binary:`~bin.mongod` on all of the shards and config servers.

### Output to Syslog

To enable auditing and print audit events to the syslog (option is unavailable on Windows) in JSON format, specify `syslog` for the :option:`--auditDestination <mongod --auditDestination>` setting. For example:

```bash
mongod --dbpath data/db --auditDestination syslog
```

.. include:: /includes/extracts/default-bind-ip-security-additional-command-line.rst

> **Important:** Before you bind to other ip addresses, consider :ref:`enabling
access control <checklist-auth>` and other security measures listed
in `/administration/security-checklist` to prevent unauthorized
access.

> **Warning:** The syslog message limit can result in the truncation of the audit
messages. The auditing system will neither detect the truncation nor
error upon its occurrence.
.. include:: /includes/linux-syslog-limitations.rst

You may also specify these options in the `configuration file </reference/configuration-options>`:

```yaml
storage:
   dbPath: data/db
auditLog:
   destination: syslog
```

### Output to Console

To enable auditing and print the audit events to standard output (i.e. `stdout`), specify `console` for the :option:`--auditDestination <mongod --auditDestination>` setting. For example:

```bash
mongod --dbpath data/db --auditDestination console
```

.. include:: /includes/extracts/default-bind-ip-security-additional-command-line.rst

> **Important:** Before you bind to other ip addresses, consider :ref:`enabling
access control <checklist-auth>` and other security measures listed
in `/administration/security-checklist` to prevent unauthorized
access.

You may also specify these options in the `configuration file </reference/configuration-options>`:

```yaml
storage:
   dbPath: data/db
auditLog:
   destination: console
```

### Output to JSON File

To enable auditing and print audit events to a file in JSON format, specify the following options:

For example, the following enables auditing and records audit events to a file with the relative path name of `data/db/auditLog.json`:

```bash
mongod --dbpath data/db --auditDestination file --auditFormat JSON --auditPath data/db/auditLog.json
```

.. include:: /includes/extracts/default-bind-ip-security-additional-command-line.rst

> **Important:** Before you bind to other ip addresses, consider :ref:`enabling
access control <checklist-auth>` and other security measures listed
in `/administration/security-checklist` to prevent unauthorized
access.

The audit file may be rotated with the :dbcommand:`logRotate` command, either alongside  the server log or independently. Rotation specifics may be configured with the :setting:`systemLog.logRotate` configuration file option or the :option:`--logRotate <mongod --logRotate>` command-line option.

You may also specify these options in the `configuration file </reference/configuration-options>`:

```yaml
storage:
   dbPath: data/db
auditLog:
   destination: file
   format: JSON
   path: data/db/auditLog.json
```

> **Note:** server performance more than printing to a file in BSON format.

### Output to BSON File

To enable auditing and print audit events to a file in BSON binary format, specify the following options:

For example, the following enables auditing and records audit events to a BSON file with the relative path name of `data/db/auditLog.bson`:

```bash
mongod --dbpath data/db --auditDestination file --auditFormat BSON --auditPath data/db/auditLog.bson
```

.. include:: /includes/extracts/default-bind-ip-security-additional-command-line.rst

> **Important:** Before you bind to other ip addresses, consider :ref:`enabling
access control <checklist-auth>` and other security measures listed
in `/administration/security-checklist` to prevent unauthorized
access.

The audit file is :dbcommand:`rotated <logRotate>` at the same time as the server log file. Rotation specifics may be configured with the :setting:`systemLog.logRotate` configuration file option or the :option:`--logRotate <mongod --logRotate>` command-line option.

You may also specify these options in the `configuration file </reference/configuration-options>`:

```yaml
storage:
   dbPath: data/db
auditLog:
   destination: file
   format: BSON
   path: data/db/auditLog.bson
```

The following example converts the audit log into readable form using :binary:`~bin.bsondump` and outputs the result:

```bash
bsondump data/db/auditLog.bson
```

### Output Messages in OCSF Format

Starting in MongoDB 8.0, MongoDB can write log messages in {+ocsf+} format. The OCSF schema provides logs in a standardized format compatible with log processors.

To use the OCSF schema for log messages, set the :option:`--auditSchema <mongod --auditSchema>` option to `OCSF`. For example:

```bash
mongod --dbpath data/db --auditDestination file --auditFormat JSON --auditPath data/db/auditLog.json --auditSchema OCSF
```

You can also specify the OCSF schema in the :setting:`auditLog.schema` configuration file option:

```yaml
storage:
   dbPath: data/db
auditLog:
   destination: file
   format: JSON
   path: data/db/auditLog.json
   schema: OCSF
```

For more information on the OCSF schema, see `event-audit-messages-ocsf`.

## Runtime Audit Filter Management

Starting in MongoDB 5.0, audit filters can be configured at runtime. Runtime Audit Filter Management provides three benefits compared to audit filter configurations that are specified in a local :binary:`~bin.mongod` or :binary:`~bin.mongos` configuration file:

- `rafm-separation`
- `rafm-configurability`
- `rafm-consistency`
### Separation of Concerns

Prior to MongoDB 5.0, anyone auditing a MongoDB :binary:`~bin.mongod` or :binary:`~bin.mongos` instance had to have write access to the host server's file system in order to update audit filters. Runtime Audit Filter Management improves security by separating audit access from administrative access.

Using Runtime Audit Filter Management instead of editing configuration files directly means:

- File system access is not required so an auditor does not need access
to the :binary:`~bin.mongod` or :binary:`~bin.mongos` host server.

- There is no direct access to the :binary:`~bin.mongod` or
:binary:`~bin.mongos` instance's configuration file.

- Runtime Audit Filter Management only exposes :ref:`audit filters
<audit-filter>` and the :parameter:`auditAuthorizationSuccess` parameter.

### Runtime Configurability

Starting in MongoDB 5.0, when Runtime Audit Filter Management is enabled, auditing can be reconfigured at runtime without restarting the :binary:`~bin.mongod` or :binary:`~bin.mongos` instance. A statically configured instance has to be restarted to update its audit settings.

Audit filter modifications made at runtime persist when an instance is shutdown and restarted.

### Consistency

Within a cluster, if all participating :binary:`~bin.mongod` and :binary:`~bin.mongos` nodes are configured to use Runtime Audit Filter Management, then every node will use the same audit filters. In contrast, if each node has its own locally configured audit filters, there is no guarantee of audit filter consistency across nodes.

### Enable Runtime Audit Filter Management

.. include:: /includes/fact-enable-runtime-audit-configuration.rst

> **Seealso:** - `audit-filter`
- `auditing`
- `audit-message`
- `auditConfig`
