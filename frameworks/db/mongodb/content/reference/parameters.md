---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/parameters.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=======================================================

# MongoDB Server Parameters for a Self-Managed Deployment

.. include:: /includes/LDAP-deprecated.rst

## Synopsis

MongoDB provides several configuration options that you can set using:

- the :dbcommand:`setParameter` command:
```javascript
  db.adminCommand( { setParameter: 1, <parameter>: <value>  } )
```

- the :setting:`setParameter` configuration setting:
```yaml
  setParameter:
     <parameter1>: <value1>
     ...
```

- the `--setParameter` command-line option for :option:`mongod <mongod --setParameter>`
and :option:`mongos <mongos --setParameter>`:

```bash
  mongod --setParameter <parameter>=<value>
  mongos --setParameter <parameter>=<value>
```

For additional configuration options, see `configuration-options`, :binary:`~bin.mongod` and :binary:`~bin.mongos`.

## Parameters

### Authentication Parameters

### General Parameters

.. warning :

```
``tcmallocAggressiveMemoryDecommit`` is deprecated in 8.0. MongoDB 8.0 uses an 
updated version of ``tcmalloc`` that improves memory fragmentation and management. 
See :ref:`tcmalloc upgrade <8.0-tcmalloc-upgrade>` for more information. To release 
memory back to the operating system, consider using :parameter:`tcmallocEnableBackgroundThread` 
instead.
```

### Logging Parameters

### Diagnostic Parameters

To facilitate analysis of the MongoDB server behavior by MongoDB engineers, MongoDB logs server statistics to diagnostic files at periodic intervals.

For :binary:`~bin.mongod`, the diagnostic data files are stored in the `diagnostic.data` directory under the :binary:`~bin.mongod` instance's `--dbpath` or :setting:`storage.dbPath`.

For :binary:`~bin.mongos`, the diagnostic data files, by default, are stored in a directory under the :binary:`~bin.mongos` instance's `--logpath` or :setting:`systemLog.path` directory. The diagnostic data directory is computed by truncating the logpath's file extension(s) and concatenating `diagnostic.data` to the remaining name.

For example, if :binary:`~bin.mongos` has `--logpath /var/log/mongodb/mongos.log.201708015`, then the diagnostic data directory is `/var/log/mongodb/mongos.diagnostic.data/` directory. To specify a different diagnostic data directory for :binary:`~bin.mongos`, set the :parameter:`diagnosticDataCollectionDirectoryPath` parameter.

The following parameters support diagnostic data capture (FTDC):

> **Note:** The default values for the diagnostic data capture interval and the
maximum sizes are configured to provide data to MongoDB engineers
with minimal impact on performance and storage size. Typically, these
values need modification only when requested by MongoDB engineers
for specific diagnostic purposes.

### Replication and Consistency

### Sharding Parameters

.. versionadded:: 7.0

.. include:: /includes/health-manager-short-names.rst

### Health Manager Parameters

### Storage Parameters

### WiredTiger Parameters

See the WiredTiger documentation for all available :wtdocs-v5.0:`WiredTiger configuration options </struct_w_t___c_o_n_n_e_c_t_i_o_n.html#>`.

### Auditing Parameters

### Transaction Parameters

### Slot-Based Execution Parameters

### Database Profiler Parameters
