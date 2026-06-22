---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/kubernetes/7.8.4/logs/_index.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Redis Enterprise Software logs on Kubernetes
alwaysopen: false
categories:
- docs
- operate
- kubernetes
description: This section provides information about how logs are stored and accessed.
hideListLinks: true
linkTitle: Logs
weight: 60
url: '/operate/kubernetes/7.8.4/logs/'
---

## Logs

Each redis-enterprise container stores its logs under `/var/opt/redislabs/log`.
When using persistent storage this path is automatically mounted to the
`redis-enterprise-storage` volume.
This volume can easily be accessed by a sidecar, i.e. a container residing on the same pod.

For example, in the REC (Redis Enterprise Cluster) spec you can add a sidecar container, such as a busybox, and mount the logs to there:

```yaml
sideContainersSpec:
  - name: busybox
    image: busybox
    args:
      - /bin/sh
      - -c
      - while true; do echo "hello"; sleep 1; done

    volumeMounts:
    - name: redis-enterprise-storage
      mountPath: /home/logs
      subPath: logs
```

Now the logs can be accessed from in the sidecar. For example by running

```kubectl exec -it <pod-name> -c busybox tail home/logs/supervisord.log```

The sidecar container is user determined and can be used to format, process and share logs in a specified format and protocol.
