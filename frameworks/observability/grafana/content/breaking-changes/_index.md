---
type: "Framework Learn Page"
framework: "Grafana"
source_repo: "https://github.com/grafana/grafana.git"
source_branch: "main"
source_path: "docs/sources/breaking-changes/_index.md"
source_commit: "5e3a02f81d2aadf4bf24fe49ed97d872556f5bf9"
source_commit_short: "5e3a02f8"
source_commit_date: "2026-08-29T10:58:19+09:00"
generated_at: "2026-08-29T09:39:37.400628Z"
---
---
aliases:
  - guides/
description: Learn about breaking changes in Grafana
labels:
  products:
    - cloud
    - enterprise
    - oss
title: Breaking changes
weight: 2
---

# Breaking changes in Grafana

{{< admonition type="note" >}}
As of Grafana v12.0 we no longer publish a dedicated breaking changes page and we, instead, publish breaking changes information in our [What's new](../whatsnew/) page.
{{< /admonition >}}

In some cases, major releases that introduce many new features also introduce breaking changes. These changes are described, along with information about what to do, in the breaking changes pages specific to each release.

For our purposes, a breaking change is any change that requires users or operators to do something. This includes:

- Changes in one part of the system that could cause other components to fail
- Deprecations or removal of a feature
- Changes to an API that could break automation
- Changes that affect some plugins or functions of Grafana
- Migrations that can’t be rolled back

{{< admonition type="note" >}}

To learn what's available in a Grafana release, refer to the [What's new ](../whatsnew/) page for each version. For the steps we recommend when you upgrade, check out the [Upgrade guide](../upgrade-guide/) for each version.

{{< /admonition >}}

Refer to any of the following breaking changes guides:

{{< section menuTitle="true">}}
