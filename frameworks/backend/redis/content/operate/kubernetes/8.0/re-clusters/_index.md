---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/kubernetes/8.0/re-clusters/_index.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Redis Enterprise clusters (REC)
alwaysopen: false
categories:
- docs
- operate
- kubernetes
description: Create and manage Redis Enterprise clusters (REC) on Kubernetes using the Redis Enterprise operator.
hideListLinks: true
linkTitle: Redis Enterprise clusters (REC)
weight: 30
url: '/operate/kubernetes/8.0/re-clusters/'
---

A Redis Enterprise cluster (REC) is a custom Kubernetes resource that represents a Redis Enterprise cluster deployment. The Redis Enterprise operator manages the lifecycle of REC resources, including deployment, scaling, upgrades, and recovery operations.

REC resources define the cluster configuration, including node specifications, storage requirements, security settings, and networking configuration. After you deploy the cluster, it provides a foundation for creating and managing Redis Enterprise databases (REDB).

## Cluster management

Manage your Redis Enterprise cluster lifecycle and configuration:

- [Connect to admin console]({{< relref "/operate/kubernetes/8.0/re-clusters/connect-to-admin-console" >}}) - Access the Redis Enterprise web UI for cluster management
- [Multi-namespace deployment]({{< relref "/operate/kubernetes/8.0/re-clusters/multi-namespace" >}}) - Deploy clusters across multiple Kubernetes namespaces
- [Delete custom resources]({{< relref "/operate/kubernetes/8.0/re-clusters/delete-custom-resources" >}}) - Safely remove REC and related resources

## Storage and performance

Optimize storage and performance for your Redis Enterprise cluster:

- [Redis Flex]({{< relref "/operate/kubernetes/8.0/flex" >}}) - Configure automatic data tiering between RAM and flash storage
- [Expand PVC]({{< relref "/operate/kubernetes/8.0/re-clusters/expand-pvc" >}}) - Expand persistent volume claims for additional storage

## Monitoring and observability

Monitor cluster health and performance:

- [Connect to Prometheus operator]({{< relref "/operate/kubernetes/8.0/re-clusters/connect-prometheus-operator" >}}) - Integrate with Prometheus for metrics collection and monitoring

### Call home client

The call home client sends health or error data from your deployment(s) back to Redis. You can disable it by adding the following to your REC specification:

```yaml
spec:
  usageMeter:
    callHomeClient:
      disabled: true
```

{{<note>}}
The REST API approach used for Redis Software deployments will have no effect on Kubernetes deployments. You must use the REC specification method shown above.
{{</note>}}

## Recovery and troubleshooting

Handle cluster recovery and troubleshooting scenarios:

- [Cluster recovery]({{< relref "/operate/kubernetes/8.0/re-clusters/cluster-recovery" >}}) - Recover from cluster failures and restore operations

## Related topics

- [Redis Enterprise databases (REDB)]({{< relref "/operate/kubernetes/8.0/re-databases" >}}) - Create and manage databases on your cluster
- [Security]({{< relref "/operate/kubernetes/8.0/security" >}}) - Configure security settings for your cluster
- [Networking]({{< relref "/operate/kubernetes/8.0/networking" >}}) - Set up networking and ingress for cluster access
- [REC API reference]({{< relref "/operate/kubernetes/8.0/reference/api/redis_enterprise_cluster_api" >}}) - Complete API specification for REC resources
