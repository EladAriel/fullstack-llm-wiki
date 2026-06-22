---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.rotateCertificates.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

========================================

# db.rotateCertificates() (mongosh method)

## Definition

.. versionadded:: 5.0

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-no-atlas-support.rst

.. include:: /includes/fact-environments-onprem-only.rst

.. include:: /includes/rotate-certificates.rst

## Output

The :method:`db.rotateCertificates()` method returns a document with the following field:

## Behavior

Rotation includes the following certificates:

- :setting:`TLS Certificates <net.tls.certificateKeyFile>`
- :setting:`CRL (Certificate Revocation List) files <net.tls.CRLFile>`
(on Linux and Windows platforms)

- :setting:`CA (Certificate Authority) files <net.tls.CAFile>`
To rotate one or more of these certificates:

#. Replace the certificate or certificates you wish to rotate on the filesystem, noting the following constraints:

- Each new certificate must have the same filename and
same filepath as the certificate it is replacing.

- If rotating an encrypted :setting:`TLS Certificate
<net.tls.certificateKeyFile>`, its password must be the same as the password for the old certificate (as specified to the :setting:`~net.tls.certificateKeyFilePassword` configuration file setting). Certificate rotation does not support the interactive password prompt.

#. Connect :binary:`~bin.mongosh` to the :binary:`~bin.mongod` or :binary:`~bin.mongos` instance that you wish to perform certificate rotation on.

#. Run :method:`db.rotateCertificates()` to rotate the certificates used by the :binary:`~bin.mongod` or :binary:`~bin.mongos` instance.

When certificate rotation takes place:

- Existing connections to the :binary:`~bin.mongod` or
:binary:`~bin.mongos` instance are not terminated, and will continue to use the old certificates.

- Any new connections will use the new certificates.
If you have configured :parameter:`OCSP <ocspEnabled>` for your deployment, the :method:`db.rotateCertificates()` method will also fetch stapled OCSP responses during rotation.

The :method:`db.rotateCertificates()` method may be run on a running :binary:`~bin.mongod` or :binary:`~bin.mongos` regardless of replication status.

Only one instance of :method:`db.rotateCertificates()` or :dbcommand:`rotateCertificates` may run on each :binary:`~bin.mongod` or :binary:`~bin.mongos` process at a time. Attempting to initiate a second instance while one is already running will result in an error.

Incorrect, expired, revoked, or missing certificate files will cause the certificate rotation to fail, but will not invalidate the existing TLS configuration or terminate the running :binary:`~bin.mongod` or :binary:`~bin.mongos` process.

If the :binary:`~bin.mongod` or :binary:`~bin.mongos` is running with :option:`--tlsCertificateSelector <mongod --tlsCertificateSelector>` set to `thumbprint`, :method:`db.rotateCertificates()` will fail and write a warning message to the log file.

## Logging

On successful rotation, the subject names, thumbprints, and the validity period of the server and cluster certificate thumbprints are logged to the configured `log destination <log-message-destinations>`. If `auditing <auditing>` is enabled, this information is also written to the audit log.

On Linux and Windows platforms, if a :setting:`CRL file <net.tls.CRLFile>` is present, its thumbprint and validity period are also logged to these locations.

## Required Access

.. include:: /includes/access-rotate-certificates.rst

## Example

The following operation rotates the certificates on a running :binary:`~bin.mongod` instance, after having made the appropriate updates to the configuration file to specify the updated certificate information:

```javascript
db.rotateCertificates()
```

The following performs the same as above, but also writes a custom log message at rotation time to the `log file <log-message-destinations>` and `audit file <auditing>`:

```javascript
db.rotateCertificates("message": "Rotating certificates")
```
