---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/kubernetes/8.0/reference/api/_index.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
title: API reference
categories:
- docs
- operate
- kubernetes
linkTitle: API reference
description: Reference documentation for Redis Enterprise operator APIs
weight: 30
alwaysopen: false
hideListLinks: true
aliases:
url: '/operate/kubernetes/8.0/reference/api/'
---

The Redis Enterprise operator provides Kubernetes custom resource definitions (CRDs) that let you manage Redis Enterprise clusters and databases declaratively. This section contains the complete API reference for all operator resources.

## API versions and stability

The operator uses different API versions to indicate stability and feature maturity:

- **`app.redislabs.com/v1`** - Stable APIs for production use
- **`app.redislabs.com/v1alpha1`** - Alpha APIs that may change in future releases

## Custom resources

| Resource | API Version | Purpose |
|----------|-------------|---------|
| [RedisEnterpriseCluster (REC)](redis_enterprise_cluster_api) | `v1` | Manages Redis Enterprise cluster deployments |
| [RedisEnterpriseDatabase (REDB)](redis_enterprise_database_api) | `v1alpha1` | Creates and configures Redis databases |
| [RedisEnterpriseActiveActiveDatabase (REAADB)](redis_enterprise_active_active_database_api) | `v1alpha1` | Sets up active-active databases across clusters |
| [RedisEnterpriseRemoteCluster (RERC)](redis_enterprise_remote_cluster_api) | `v1alpha1` | Defines remote cluster connections for active-active |

## Working with the APIs

### Using kubectl

Manage all resources using standard `kubectl` commands:

```bash
# List all Redis Enterprise clusters
kubectl get rec

# Get detailed information about a specific database
kubectl describe redb my-database

# Apply a configuration from a YAML file
kubectl apply -f my-redis-config.yaml
```

### Resource relationships

- Create a `RedisEnterpriseCluster` (REC) first to provide the Redis Enterprise infrastructure
- Create `RedisEnterpriseDatabase` (REDB) resources within a cluster to provision individual databases
- Use `RedisEnterpriseActiveActiveDatabase` (REAADB) with `RedisEnterpriseRemoteCluster (RERC)` resources to define participating clusters

For complete YAML configuration examples, see the [YAML examples]({{< relref "/operate/kubernetes/8.0/reference/yaml/" >}}) section.
