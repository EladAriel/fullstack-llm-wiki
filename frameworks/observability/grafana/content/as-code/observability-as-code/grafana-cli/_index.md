---
type: "Framework Learn Page"
framework: "Grafana"
source_repo: "https://github.com/grafana/grafana.git"
source_branch: "main"
source_path: "docs/sources/as-code/observability-as-code/grafana-cli/_index.md"
source_commit: "5e3a02f81d2aadf4bf24fe49ed97d872556f5bf9"
source_commit_short: "5e3a02f8"
source_commit_date: "2026-08-29T10:58:19+09:00"
generated_at: "2026-08-29T09:39:37.534580Z"
---
---
description: Overview of Grafana CLI, a command line tool for managing Grafana resources as code.
keywords:
  - observability
  - configuration
  - as code
  - as-code
  - dashboards
  - git integration
  - git sync
  - github
labels:
  products:
    - cloud
    - enterprise
    - oss
cards:
  items:
    - description: Overview of the Grafana CLI `gcx`, compatible with AI agents
      height: 24
      href: ./gcx
      title: gcx CLI (recommended)
    - description: Learn how to install, set up and use the Grafana CLI `grafanactl`
      height: 24
      href: ./grafanactl
      title: grafanactl CLI (deprecated)
  title_class: pt-0 lh-1
title: Introduction to the Grafana CLI
menuTitle: Grafana CLI
weight: 100
canonical: https://grafana.com/docs/grafana/latest/as-code/observability-as-code/grafana-cli/
aliases:
  - ../../observability-as-code/grafana-cli/ # /docs/grafana/next/observability-as-code/grafana-cli/
---

# Introduction to the Grafana CLI

Grafana command-line tools are designed to simplify interaction with Grafana instances. You can authenticate, manage multiple environments, and perform administrative tasks through the Grafana REST API, all from the terminal. Whether you're automating workflows in CI/CD pipelines or switching between staging and production environments, the Grafana CLI tool provides a flexible and efficient way to manage your Grafana setup as code.

`gcx` works across all environments for Grafana OSS, Enterprise, and Cloud. **Use `gcx` to work with AI agents**.

## Explore

{{< card-grid key="cards" type="simple" >}}
