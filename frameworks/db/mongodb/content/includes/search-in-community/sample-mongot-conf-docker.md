---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/search-in-community/sample-mongot-conf-docker.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

```yaml
# mongot.conf
syncSource:
   replicaSet:
      hostAndPort: "mongot-community.search-community:27017"
      username: "mongotUser"
      passwordFile: "/passwordFile"
      authSource: "admin"
      tls: false
   replicationReader:
      readPreference: "secondaryPreferred"
storage:
   dataPath: "/data/mongot"
server:
   grpc:
      address: "mongot-community.search-community:27028"
      tls:
         mode: "disabled"
metrics:
   enabled: true
   address: "mongot-community.search-community:9946"
healthCheck:
   address: "mongot-community.search-community:8080"
logging:
   verbosity: INFO
```
