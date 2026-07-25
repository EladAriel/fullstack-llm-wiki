---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/self-hosting/deployment-options/kubernetes-helm.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.941339Z"
---
# Kubernetes Helm

---
title: "Kubernetes (helm)"
description: Deploy Phoenix via Helm
---

## Prerequisites

You must have a working Kubernetes cluster accessible via `kubectl` as well as the [`helm` client](https://helm.sh/docs/intro/install/) installed locally.

## Installing

The Phoenix Helm chart is hosted on [Dockerhub](https://hub.docker.com/r/arizephoenix/phoenix-helm). First, save the chart URL to a variable.

```bash
export CHART_URL=oci://registry-1.docker.io/arizephoenix/phoenix-helm
```

It's recommended to install a specific version of the Helm chart. Select the latest Helm chart version [here](https://hub.docker.com/r/arizephoenix/phoenix-helm/tags) (e.g., `0.1.0`) and save to a variable.

```python
export CHART_VERSION=x.x.x  # replace your version here
```

<Info>
New patch versions of the Helm chart defaulting to the latest version of Phoenix are regularly released.

</Info>

Phoenix can be deployed with PostgreSQL and the default configuration by running

```php
helm install phoenix $CHART_URL --version $CHART_VERSION
```

To customize the configuration of your deployment, create a `values.yaml` file describing your desired settings. For example, the following file changes the default Phoenix port from 6006 to 6007:

```yaml
server:
  port: 6007
```

To install with your custom configuration, run

```sh
helm install phoenix $CHART_URL --version $CHART_VERSION -f values.yaml
```

A comprehensive list of configurable values can be found in the [Dockerhub repo overview](https://hub.docker.com/r/arizephoenix/phoenix-helm).

## Upgrading and Uninstalling

After the initial installation, subsequent upgrades can be applied with

```sh
helm upgrade phoenix $CHART_URL --version $CHART_VERSION -f values.yaml
```

The Helm chart can be uninstalled with

```sh
helm uninstall phoenix
```

Uninstalling will remove all Kubernetes resources (deployments, services, pods, ingresses, etc.) except for the persistent volume claim containing the PostgreSQL database.


