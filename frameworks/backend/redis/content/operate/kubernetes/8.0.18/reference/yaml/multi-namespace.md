---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/kubernetes/8.0.18/reference/yaml/multi-namespace.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Multi-namespace examples
alwaysopen: false
categories:
- docs
- operate
- kubernetes
description: YAML examples for deploying Redis Enterprise across multiple Kubernetes namespaces.
linkTitle: Multi-namespace
weight: 40
url: '/operate/kubernetes/8.0.18/reference/yaml/multi-namespace/'
---

Multi-namespace deployment lets a single Redis Enterprise operator manage clusters and databases in different namespaces, providing better resource isolation and organization.

Multi-namespace deployment enables:
- Namespace isolation: Separate Redis Enterprise resources by team, environment, or application
- Centralized management: Single operator manages multiple namespaces
- Resource sharing: Efficient use of cluster resources across namespaces
- Flexible RBAC: Fine-grained permissions per namespace

This example shows:
- Operator namespace: `redis-enterprise-operator` (where the operator and REC run)
- Consumer namespaces: `app-production`, `app-staging` (where REDB resources are created)

For complete deployment instructions, see [Manage databases in multiple namespaces]({{< relref "/operate/kubernetes/8.0.18/re-clusters/multi-namespace" >}}).

## Operator service account

Deploy these resources in the namespace where the Redis Enterprise operator runs.

{{<embed-yaml "k8s/service_account.md" "operator-service-account.yaml">}}

## Operator cluster role

Grant the operator cluster-wide permissions to manage resources across namespaces.

{{<embed-yaml "k8s/multi-ns_operator_cluster_role.md" "operator-cluster-role.yaml">}}

## Operator cluster role binding

{{<embed-yaml "k8s/multi-ns_operator_cluster_role_binding.md" "operator-cluster-role-binding.yaml">}}

## Consumer role

{{<embed-yaml "k8s/multi-ns_role.md" "consumer-role.yaml">}}

## Consumer role binding

{{<embed-yaml "k8s/multi-ns_role_binding.md" "consumer-role-binding.yaml">}}

Consumer namespace configuration:

- `subjects.name`: Must match the operator service account name
- `subjects.namespace`: Must be the operator namespace, not the consumer namespace
- `roleRef.name`: Must match the consumer role name

## Next steps

- [Configure networking across namespaces]({{< relref "/operate/kubernetes/8.0.18/networking" >}})
- [Set up monitoring for multi-namespace deployment]({{< relref "/operate/kubernetes/8.0.18/re-clusters/connect-prometheus-operator" >}})
- [Learn about resource management]({{< relref "/operate/kubernetes/8.0.18/recommendations" >}})

## Related documentation

- [Manage databases in multiple namespaces]({{< relref "/operate/kubernetes/8.0.18/re-clusters/multi-namespace" >}})
- [RBAC configuration]({{< relref "/operate/kubernetes/8.0.18/security" >}})
- [Kubernetes namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/)
