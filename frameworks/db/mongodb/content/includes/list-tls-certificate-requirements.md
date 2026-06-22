---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/list-tls-certificate-requirements.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

- A single Certificate Authority (CA) must issue all X.509 certificates
for the members of a sharded cluster or a replica set.

- At least one of the Subject Alternative Name (`SAN`) entries must
match the server hostname used by other cluster members. When comparing `SAN`\s, MongoDB can compare either DNS names or IP addresses.

If you don't specify `subjectAltName`, MongoDB compares the Common Name (CN) instead. However, this usage of CN is deprecated per [RFC2818](https://datatracker.ietf.org/doc/html/rfc2818)

Key Usage and Extended Key Usage are X.509 extensions that strictly define and restrict the use of the key associated with a certificate. Both of these extensions are optional. If `tlsCertificateKeyFile` or `tlsClusterFile` point to certificates that omit these extensions, no restrictions apply to using the certificate.

If X.509 certificates used for `tlsCertificateKeyFile` or `tlsClusterFile` include the Extended Key Usage (EKU) extension, they must comply with the following rules:

- `tlsCertificateKeyFile` must include `serverAuth` in EKU.
```none
  extendedKeyUsage = serverAuth
```

- `tlsClusterFile` must include `clientAuth` in EKU:
```none
  extendedKeyUsage = clientAuth
```

- If `tlsClusterFile` is omitted and only `tlsCertificateKeyFile`
is configured, then `tlsCertificateKeyFile` must include both `serverAuth` and `clientAuth` in EKU:

```none
  extendedKeyUsage = clientAuth, serverAuth
```

If X.509 certificates used for `tlsCertificateKeyFile` or `tlsClusterFile` include the Key Usage (KU) extension, set it as follows:

- `tlsCertificateKeyFile` should contain `digitalSignature`,
`keyEncipherment`, and `keyAgreement` in its KU extension:

```none
  keyUsage = digitalSignature, keyEncipherment, keyAgreement
```

- `tlsClusterFile` should contain `digitalSignature` in its
KU extension:

```none
  keyUsage = digitalSignature
```
