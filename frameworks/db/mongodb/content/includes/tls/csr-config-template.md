---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/tls/csr-config-template.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

[ req ] distinguished_name = dn prompt             = no req_extensions     = req_ext

# Replace values in this section with your own information.

[ dn ] C  = US                    # 2-letter country code ST = New-York              # State or province L  = New York City         # City or locality O  = Example Corp          # Organization name CN = mongo0.example.com    # Hostname of your MongoDB node

[ req_ext ] subjectAltName = @alt_names keyUsage = digitalSignature extendedKeyUsage = serverAuth

# Replace values in this section with any alternative # hostnames or IP addresses for your MongoDB node.

[ alt_names ] DNS.1 = mongo0.example.com DNS.2 = localhost IP.1 = 127.0.0.1
