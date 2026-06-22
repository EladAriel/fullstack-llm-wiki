---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/search-in-community/sample-mongod-conf-docker.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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

# Search configuration parameters
setParameter:
   # Server parameters to advise mongod of mongot availability for search index management and querying
   searchIndexManagementHostAndPort: mongot-community.search-community:27028
   mongotHost: mongot-community.search-community:27028
   skipAuthenticationToSearchIndexManagementServer: false
   useGrpcForSearch: true

# Security configuration
security:
   authorization: enabled  # Equivalent to --auth
   keyFile: /keyfile
```
