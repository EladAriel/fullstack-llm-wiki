---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/configuration-options.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=======================================

# Self-Managed Configuration File Options

The configuration file options on this page apply to MongoDB {+latest-lts-version+}. For options in other versions, see the appropriate version of the MongoDB Manual.

> **Note:** If you're using {+atlas+} to manage your MongoDB deployments in the
cloud, you don't need to create a configuration file. To learn how
to configure settings for your {+atlas+} deployment, see
:atlas:`Configure Additional Settings </cluster-additional-settings/>`.

MongoDB binaries also read operating system environment variables.

## Configuration File

You can configure :binary:`~bin.mongod` and :binary:`~bin.mongos` instances at startup using a configuration file. The configuration file contains settings that are equivalent to the :binary:`~bin.mongod` and :binary:`~bin.mongos` command-line options. See `conf-file-command-line-mapping`.

You can also add comments to the configuration file to explain the server's settings.

.. include:: /includes/fact-default-conf-file.rst

### File Format

MongoDB configuration files use the [YAML](http://www.yaml.org) format [#yaml-json]_.

The following sample configuration file includes several :binary:`~bin.mongod` settings:

> **Note:** YAML does not support tab characters for indentation: use spaces instead.

```yaml
systemLog:
   destination: file
   path: "/var/log/mongodb/mongod.log"
   logAppend: true
processManagement:
   fork: true
net:
   bindIp: 127.0.0.1
   port: 27017
setParameter:
   enableLocalhostAuthBypass: false
...
```

The Linux package init scripts included in the official MongoDB packages depend on specific values for :setting:`systemLog.path`, :setting:`storage.dbPath`, and :setting:`processManagement.fork` or `MONGODB_CONFIG_OVERRIDE_NOFORK` system environment variable. If you modify these settings in the default configuration file, :binary:`~bin.mongod` may not start.

Externally Sourced Values `````````````````````````

> **Note:** .. include:: /includes/fact-expansion-directive-intro.rst

The following expansion directives are available:

For complete documentation, see `externally-sourced-values`.

### Use the Configuration File

To configure :binary:`~bin.mongod` or :binary:`~bin.mongos` using a config file, specify the config file with the `--config` option or the `-f` option, as in the following examples:

```bash
mongod --config /etc/mongod.conf

mongos --config /etc/mongos.conf
```

You can also use the `-f` alias:

```bash
mongod -f /etc/mongod.conf

mongos -f /etc/mongos.conf
```

If you installed from a package and have started MongoDB using your system's `init script`, you are already using a configuration file.

Expansion Directives and `--configExpand` ```````````````````````````````````````````

If you are using `expansion directives <expansion-directives>` in the configuration file, you must include the :option:`--configExpand <mongod --configExpand>` option when starting the :binary:`~bin.mongod` or :binary:`~bin.mongos`. For example:

```bash
mongod --config /etc/mongod.conf  --configExpand "rest,exec"
mongos --config /etc/mongos.conf  --configExpand "rest,exec"
```

If the configuration file includes an expansion directive and you start the :binary:`mongod` / :binary:`mongos` without specifying that directive in the :option:`--configExpand <mongod --configExpand>` option, the :binary:`mongod` / :binary:`mongos` fails to start.

## Core Options

### `systemLog` Options

```yaml
systemLog:
   verbosity: <int>
   quiet: <boolean>
   traceAllExceptions: <boolean>
   syslogFacility: <string>
   path: <string>
   logAppend: <boolean>
   logRotate: <string>
   destination: <string>
   timeStampFormat: <string>
   component:
      accessControl:
         verbosity: <int>
      command:
         verbosity: <int>

      # COMMENT additional component verbosity settings omitted for brevity
```

`systemLog.component` Options ```````````````````````````````

```yaml
systemLog:
   component:
      accessControl:
         verbosity: <int>
      command:
         verbosity: <int>

      # COMMENT some component verbosity settings omitted for brevity

      replication:
         verbosity: <int>
         election:
            verbosity: <int>
         heartbeats:
            verbosity: <int>
         initialSync:
            verbosity: <int>
         rollback:
            verbosity: <int>
      storage:
         verbosity: <int>
         journal:
            verbosity: <int>
         recovery:
            verbosity: <int>
      write:
         verbosity: <int>
```

> **Note:** .. include:: /includes/extracts/4.2-changes-debug-log-message.rst

### `processManagement` Options

```yaml
processManagement:
   fork: <boolean>
   pidFilePath: <string>
   timeZoneInfo: <string>
```

### `net` Options

.. versionchanged:: 5.0

```yaml
net:
   port: <int>
   bindIp: <string>
   bindIpAll: <boolean>
   maxIncomingConnections: <int>
   wireObjectCheck: <boolean>
   ipv6: <boolean>
   unixDomainSocket:
      enabled: <boolean>
      pathPrefix: <string>
      filePermissions: <int>
   tls:
      certificateSelector: <string>
      clusterCertificateSelector: <string>
      mode: <string>
      certificateKeyFile: <string>
      certificateKeyFilePassword: <string>
      clusterFile: <string>
      clusterPassword: <string>
      CAFile: <string>
      clusterCAFile: <string>
      clusterAuthX509:
        attributes: <string>
        extensionValue: <string>
      CRLFile: <string>
      allowConnectionsWithoutCertificates: <boolean>
      allowInvalidCertificates: <boolean>
      allowInvalidHostnames: <boolean>
      disabledProtocols: <string>
      FIPSMode: <boolean>
      logVersions: <string>
   compression:
      compressors: <string>
```

`net.unixDomainSocket` Options ````````````````````````````````

```yaml
net:
   unixDomainSocket:
      enabled: <boolean>
      pathPrefix: <string>
      filePermissions: <int>
```

`net.tls` Options ```````````````````

> **Note:** The `tls` options provide identical functionality as the
previous `ssl` options.

```yaml
net:
   tls:
      mode: <string>
      certificateKeyFile: <string>
      certificateKeyFilePassword: <string>
      certificateSelector: <string>
      clusterCertificateSelector: <string>
      clusterFile: <string>
      clusterPassword: <string>
      clusterAuthX509:
        attributes: <string>
        extensionValue: <string>
      CAFile: <string>
      clusterCAFile: <string>
      CRLFile: <string>
      allowConnectionsWithoutCertificates: <boolean>
      allowInvalidCertificates: <boolean>
      allowInvalidHostnames: <boolean>
      disabledProtocols: <string>
      FIPSMode: <boolean>
      logVersions: <string>
```

`net.compression` Option ``````````````````````````

```yaml
net:
   compression:
      compressors: <string>
```

### `security` Options

```yaml
security:
   keyFile: <string>
   clusterAuthMode: <string>
   authorization: <string>
   transitionToAuth: <boolean>
   javascriptEnabled:  <boolean>
   redactClientLogData: <boolean>
   clusterIpSourceAllowlist:
     - <string>
   sasl:
      hostName: <string>
      serviceName: <string>
      saslauthdSocketPath: <string>
   enableEncryption: <boolean>
   encryptionCipherMode: <string>
   encryptionKeyFile: <string>
   kmip:
      keyIdentifier: <string>
      rotateMasterKey: <boolean>
      serverName: <string>
      port: <string>
      clientCertificateFile: <string>
      clientCertificatePassword: <string>
      clientCertificateSelector: <string>
      serverCAFile: <string>
      connectRetries: <int>
      connectTimeoutMS: <int>
   ldap:
      servers: <string>
      bind:
         method: <string>
         saslMechanisms: <string>
         queryUser: <string>
         queryPassword: <string | array>
         useOSDefaults: <boolean>
      transportSecurity: <string>
      timeoutMS: <int>
      userToDNMapping: <string>
      authz:
         queryTemplate: <string>
      validateLDAPServerConfig: <boolean>
```

Key Management Configuration Options ````````````````````````````````````

```yaml
security:
   enableEncryption: <boolean>
   encryptionCipherMode: <string>
   encryptionKeyFile: <string>
   kmip:
      keyIdentifier: <string>
      rotateMasterKey: <boolean>
      serverName: <string>
      port: <int>
      clientCertificateFile: <string>
      clientCertificatePassword: <string>
      clientCertificateSelector: <string>
      serverCAFile: <string>
      connectRetries: <int>
      connectTimeoutMS: <int>
      activateKeys: <boolean>
      keyStatePollingSeconds: <int>
      useLegacyProtocol: <boolean>
```

`security.sasl` Options `````````````````````````

```yaml
security:
   sasl:
      hostName: <string>
      serviceName: <string>
      saslauthdSocketPath: <string>
```

`security.ldap` Options `````````````````````````

.. include:: /includes/LDAP-deprecated.rst

```yaml
security:
   ldap:
      servers: <string>
      bind:
         method: <string>
         saslMechanisms: <string>
         queryUser: <string>
         queryPassword: <string | array>
         useOSDefaults: <boolean>
      transportSecurity: <string>
      timeoutMS: <int>
      retryCount: <int>
      userToDNMapping: <string>
      authz:
         queryTemplate: <string>
      validateLDAPServerConfig: <boolean>
```

### `setParameter` Option

### `setParameter` LDAP Options

```yaml
setParameter:
   ldapUserCacheInvalidationInterval: <int>
```

### `setParameter` MongoDB Search Options

```yaml
setParameter:
   searchIndexManagementHostAndPort: <hostname|IP:port>
```

```yaml
setParameter:
   skipAuthenticationToSearchIndexManagementServer: <true|false>
```

```yaml
setParameter:
   mongotHost: <hostname|IP:port>
```

```yaml
setParameter:
   skipAuthenticationToMongot: <true|false>
```

```yaml
setParameter:
   useGrpcForSearch: <true|false>
```

```yaml
setParameter:
   searchTLSMode: <globalTLS|disabled|allowTLS|preferTLS|requireTLS>
```

### `storage` Options

.. versionchanged:: 6.1

```yaml
storage:
   dbPath: <string>
   journal:
      commitIntervalMs: <num>
   directoryPerDB: <boolean>
   syncPeriodSecs: <int>
   engine: <string>
   wiredTiger:
      engineConfig:
         cacheSizeGB: <number>
         journalCompressor: <string>
         directoryForIndexes: <boolean>
         maxCacheOverflowFileSizeGB: <number> 
      collectionConfig:
         blockCompressor: <string>
      indexConfig:
         prefixCompression: <boolean>
   inMemory:
      engineConfig:
         inMemorySizeGB: <number>
   oplogMinRetentionHours: <double>
```

`storage.wiredTiger` Options ``````````````````````````````

```yaml
storage:
   wiredTiger:
      engineConfig:
         cacheSizeGB: <number>
         cacheSizePct: <number>
         journalCompressor: <string>
         directoryForIndexes: <boolean>
         maxCacheOverflowFileSizeGB: <number> 
      collectionConfig:
         blockCompressor: <string>
      indexConfig:
         prefixCompression: <boolean>
```

`storage.inmemory` Options ````````````````````````````

```yaml
storage:
   inMemory:
      engineConfig:
         inMemorySizeGB: <number>
```

### `operationProfiling` Options

```yaml
operationProfiling:
   mode: <string>
   slowOpThresholdMs: <int>
   slowOpInProgressThresholdMs: <int>
   slowOpSampleRate: <double>
   filter: <string>
```

### `replication` Options

```yaml
replication:
   oplogSizeMB: <int>
   replSetName: <string>
   enableMajorityReadConcern: <boolean>  
```

### `sharding` Options

```yaml
sharding:
   clusterRole: <string>
```

### `auditLog` Options

.. include:: /includes/note-audit-in-enterprise-only.rst

```yaml
auditLog:
   destination: <string>
   format: <string>
   path: <string>
   filter: <string>
   schema: <string>
```

## `mongot`\ Options

Use the following options to configure `mongot` with `mongod` in Public Preview.

```yaml
syncSource:
   replicaSet: <object>
      hostAndPort: <string>
      username: <string>
      passwordFile: <string>
      authSource: <string>
      tls: <boolean>
      x509:
         tlsCertificateKeyFile: <string>
         tlsCertificateKeyFilePasswordFile: <string>
      readPreference: <string>
   router: <object>
      hostAndPort: <string>
      username: <string>
      passwordFile: <string>
      tls: <boolean>
      x509:
         tlsCertificateKeyFile: <string>
         tlsCertificateKeyFilePasswordFile: <string>
   replicationReader: <object>
      readPreference: <string>
      tagSets: <array>
   caFile: <string>
storage:
   dataPath: <string>
server:
   grpc:
      address: <string>
      tls:
         mode: <string>
         certificateKeyFile: <string>
         caFile: <string>
   name: <string>
metrics:
   enabled: <boolean>
   address: <boolean>
healthCheck:
   address: <string>
logging:
   verbosity: <string>
   logPath: <string>
```

## `mongos`\ -only Options

```yaml
replication:
   localPingThresholdMs: <int>

sharding:
   configDB: <string>
```

## Windows Service Options

```yaml
processManagement:
   windowsService:
      serviceName: <string>
      displayName: <string>
      description: <string>
      serviceUser: <string>
      servicePassword: <string>
```

## Removed MMAPv1 Options

MongoDB removed the deprecated MMAPv1 storage engine and the MMAPv1-specific configuration options:

.. include:: /includes/removed-mmapv1-options.rst

For earlier versions of MongoDB, refer to the [legacy documentation](https://www.mongodb.com/docs/legacy/).

## Contents

- Externally Sourced Values </reference/expansion-directives>
- Convert Command-Line Options to YAML </tutorial/convert-command-line-options-to-yaml>
- Configuration File Settings and Command-Line Options Mapping </reference/configuration-file-settings-command-line-options-mapping>
