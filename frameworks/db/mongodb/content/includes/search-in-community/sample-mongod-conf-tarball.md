---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/search-in-community/sample-mongod-conf-tarball.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

```yaml
# MongoDB Configuration File

# Network configuration
net:
   port: 27017
   bindIpAll: true  # Equivalent to --bind_ip_all

# Replica set configuration
replication:
   replSetName: rs0

# Security configuration
#security:
#   authorization: enabled  # Equivalent to --auth
#   keyFile: </path/to/keyfile>

# Search configuration parameters
setParameter:
   mongotHost: localhost:27027
   searchIndexManagementHostAndPort: localhost:27027

# Process management configuration
processManagement:
   fork: true

# Logging configuration
systemLog:
   destination: file
   path: /var/log/mongodb/mongod.log
   logAppend: true
```
