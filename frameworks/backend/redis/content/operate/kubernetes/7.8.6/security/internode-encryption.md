---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/kubernetes/7.8.6/security/internode-encryption.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
Title: Enable internode encryption
categories:
- docs
- operate
- kubernetes
description: Enable encryption for communication between REC nodes in your K8s cluster.
linkTitle: Internode encryption
weight: 99
url: '/operate/kubernetes/7.8.6/security/internode-encryption/'
---

Internode encryption provides added security by encrypting communication between nodes in your Redis Enterprise cluster (REC).

Enable internode encryption in the `spec` section of your REC custom resource file.

```yaml
spec:
    dataInternodeEncryption: true
```

This change will apply to all databases created in the REC. You can override the cluster-wide setting for individual databases.

Edit your Redis Enterprise database (REDB) custom resource file to disable internode encryption for only that database.

```yaml
spec: 
    dataInternodeEncryption: false
```

To learn more about internode encryption, see [Internode encryption for Redis Enterprise Software]({{< relref "/operate/rs/security/encryption/internode-encryption.md" >}}).
