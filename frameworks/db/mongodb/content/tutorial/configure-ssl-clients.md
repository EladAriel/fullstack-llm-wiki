---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/configure-ssl-clients.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=================================

# TLS/SSL Configuration for Clients

Clients must have support for TLS/SSL to connect to a :binary:`~bin.mongod` or a :binary:`~bin.mongos` instance that require `TLS/SSL connections <configure-mongod-mongos-for-tls-ssl>`.

> **Note:** - The Linux 64-bit legacy x64 binaries of MongoDB do **not** include
  support for TLS/SSL.
- .. include:: /includes/fact-tls-1.0.rst

> **Important:** .. include:: /includes/extracts/security-prereq-configure-ssl-clients.rst

## MongoDB Shell

:binary:`~bin.mongosh` provides various TLS/SSL settings, including:

For a complete list of :binary:`~bin.mongosh`'s `tls` options, see :mongosh:`TLS options </reference/options/#tls-options>`.

For TLS/SSL connections, :binary:`~bin.mongosh` validates the certificate presented by the :binary:`~bin.mongod` or :binary:`~bin.mongos` instance:

- :binary:`~bin.mongosh` verifies that the certificate is from
the specified Certificate Authority (:option:`--tlsCAFile <mongosh --tlsCAFile>`. If the certificate is not from the specified CA, :binary:`~bin.mongosh` will fail to connect.

- .. include:: /includes/extracts/ssl-facts-mongo-ssl-hostname-verification.rst
To connect :binary:`~bin.mongosh` to a :binary:`~bin.mongod` or :binary:`~bin.mongos` that requires TLS/SSL, specify the :option:`--host <mongosh --host>` option or use a `connection string </reference/connection-string>` to specify the hostname. All other `TLS/SSL` options must be specified using the command-line options.

### Connect to MongoDB Instances Using Encryption

To connect to a :binary:`~bin.mongod` or :binary:`~bin.mongos` instance that requires `encrypted communication <ssl-mongod-ssl-cert-key>`, start :binary:`~bin.mongosh` with:

- :option:`--tls <mongosh --tls>`
- :option:`--host <mongosh --host>` and :option:`--tlsCAFile <mongosh
--tlsCAFile>` to validate the server certificate.

For example, consider a :binary:`~bin.mongod` instance running on `hostname.example.com` with the following options:

```bash
mongod --tlsMode requireTLS --tlsCertificateKeyFile <pem> 
```

To connect to the instance, start :binary:`~bin.mongosh` with the following options:

```bash
mongosh --tls --host hostname.example.com --tlsCAFile /etc/ssl/caToValidateServerCertificates.pem
```

:binary:`~bin.mongosh` verifies the certificate presented by the :binary:`~bin.mongod` instance against the specified hostname and the CA file.

### Connect to MongoDB Instances that Require Client Certificates

To connect to a :binary:`~bin.mongod` or :binary:`~bin.mongos` that requires `CA-signed client certificates <ssl-mongod-ca-signed-ssl-cert-key>`, start :binary:`~bin.mongosh` with:

- :option:`--tls <mongosh --tls>`
- :option:`--host <mongosh --host>` and the :option:`--tlsCAFile
<mongosh --tlsCAFile>` to validate the server certificate,

- :option:`--tlsCertificateKeyFile <mongosh --tlsCertificateKeyFile>` option to specify
the client certificate to present to the server.

For example, consider a :binary:`~bin.mongod` instance running on `hostname.example.com` with the following options:

```bash
mongod --tlsMode requireTLS --tlsCertificateKeyFile /etc/ssl/mongodb.pem --tlsCAFile /etc/ssl/caToValidateClientCertificates.pem
```

To connect to the instance, start :binary:`~bin.mongosh` with the following options:

```bash
mongosh --tls --host hostname.example.com --tlsCertificateKeyFile /etc/ssl/client.pem --tlsCAFile /etc/ssl/caToValidateServerCertificates.pem
```

Windows and macOS `````````````````

To specify a client certificate from the system certificate store, use the :option:`--tlsCertificateSelector <mongosh --tlsCertificateSelector>` option instead of :option:`--tlsCertificateKeyFile <mongosh --tlsCertificateKeyFile>`.

If the CA file is also in the system certificate store, you can omit the :option:`--tlsCAFile <mongosh --tlsCAFile>` option.

For example, if a certificate with the `CN` (Common Name) of `myclient.example.net` and the accompanying CA file are both in the macOS system certificate store, you can connect like this:

```bash
mongosh --tls  --host hostname.example.com --tlsCertificateSelector subject="myclient.example.net"
```

There are available in `mongosh`, but you should use the `tls` alternatives instead.

### Avoid Use of `--tlsAllowInvalidCertificates` Option

> **Warning:** Although available, avoid using the
:option:`--tlsAllowInvalidCertificates <mongosh
--tlsAllowInvalidCertificates>` option if possible. If the use of
:option:`--tlsAllowInvalidCertificates <mongosh
--tlsAllowInvalidCertificates>` is necessary, only use the option on
systems where intrusion is not possible.
If :binary:`~bin.mongosh` runs with the
:option:`--tlsAllowInvalidCertificates <mongosh
--tlsAllowInvalidCertificates>` option, :binary:`~bin.mongosh`
will not attempt to validate the server certificates. This
creates a vulnerability to expired :binary:`~bin.mongod` and
:binary:`~bin.mongos` certificates as well as to foreign processes
posing as valid :binary:`~bin.mongod` or :binary:`~bin.mongos`
instances. If you only need to disable the validation of the
hostname in the TLS/SSL certificates, see
:option:`--tlsAllowInvalidHostnames <mongosh --tlsAllowInvalidHostnames>`.

## |atlas|, |MMS| and MongoDB Ops Manager

|atlas| uses TLS/SSL to encrypt the connections to your databases.

The |MMS| and Ops Manager Monitoring agents use encrypted communication to gather its statistics. Because the agents already encrypt communications to the |MMS|/Ops Manager servers, this is just a matter of enabling TLS/SSL support in |MMS|/Ops Manager on a per host basis.

For more information, see:

- [MongoDB Atlas documentation](https://docs.atlas.mongodb.com/setup-cluster-security/)
- |mms-docs|
- :opsmgr:`MongoDB Ops Manager documentation </>`.
.. include:: /includes/replacement-mms.rst

## MongoDB Drivers

The MongoDB Drivers support encrypted communication. For details, see:

- [C Driver](https://www.mongodb.com/docs/languages/c/c-driver/current/libmongoc/guides/configuring_tls/)
- [C++ Driver](https://www.mongodb.com/docs/languages/cpp/cpp-driver/current/configuration/#configuring-tls-ssl)
- [C# Driver](https://www.mongodb.com/docs/drivers/csharp/current/fundamentals/connection/tls/)
- [Java Driver](https://www.mongodb.com/docs/drivers/java/sync/current/fundamentals/connection/tls/)
- [Node.js Driver](https://www.mongodb.com/docs/drivers/node/current/fundamentals/connection/tls/)
- [PHP Driver](https://php.net/manual/en/mongodb-driver-manager.construct.php)
- [Python Driver](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/connect/tls/)
- [Ruby Driver](https://www.mongodb.com/docs/ruby-driver/current/reference/authentication/#client-certificate--x.509-)
- [Scala Driver](https://www.mongodb.com/docs/languages/scala/scala-driver/current/tutorials/connect/tls/)
## MongoDB Tools

Various MongoDB utility programs support encrypted communication. These tools include:

- :binary:`~bin.mongodump`
- :binary:`~bin.mongoexport`
- :binary:`~bin.mongofiles`
- :binary:`~bin.mongoimport`
- :binary:`~bin.mongorestore`
- :binary:`~bin.mongostat`
- :binary:`~bin.mongotop`
To use encrypted communication with these tools, use the same `tls` options as :binary:`~bin.mongosh`. See `mongo-shell-tls-connect`.

> **Seealso:** `configure-mongod-mongos-for-tls-ssl`
