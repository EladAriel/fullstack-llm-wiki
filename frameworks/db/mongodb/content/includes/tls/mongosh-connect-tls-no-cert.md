---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/tls/mongosh-connect-tls-no-cert.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

```bash
mongosh "mongodb://mongo0.example.com:27017,mongo1.example.com:27017,mongo2.example.com:27017" \
    --tls --tlsCAFile /etc/ssl/mongodb/ca.pem
```

- :option:`--tls <mongosh --tls>` enables TLS encryption
for the connection.

- :option:`--tlsCAFile <mongosh --tlsCAFile>` is set to the CA
certificate that signed the server certificates so that `mongosh` can verify the server's certificates.
