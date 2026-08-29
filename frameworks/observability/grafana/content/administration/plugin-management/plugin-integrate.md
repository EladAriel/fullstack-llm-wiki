---
type: "Framework Learn Page"
framework: "Grafana"
source_repo: "https://github.com/grafana/grafana.git"
source_branch: "main"
source_path: "docs/sources/administration/plugin-management/plugin-integrate.md"
source_commit: "5e3a02f81d2aadf4bf24fe49ed97d872556f5bf9"
source_commit_short: "5e3a02f8"
source_commit_date: "2026-08-29T10:58:19+09:00"
generated_at: "2026-08-29T09:39:37.488254Z"
---
---
title: Plugin backend communication
description: Allow plugin frontends to communicate locally with the backends of other installed plugins.
labels:
  products:
    - enterprise
    - oss
keywords:
  - grafana
  - plugins
  - plugin
  - navigation
  - customize
  - configuration
  - grafana.ini
  - sandbox
  - frontend
weight: 350
---

# Allow plugin backend communication

By default, you can only communicate with plugin backends remotely.

However, you can configure your Grafana instance to let the frontends of installed plugins to directly communicate with the backends of other plugins installed locally. You can use this configuration to, for example, enable a [canvas panel](https://grafana.com/docs/grafana/<GRAFANA_VERSION>/panels-visualizations/visualizations/canvas/) to call an application resource API that is permitted by the `actions_allow_post_url` option.

## Integrate your plugins

To enable backend communication between plugins, set the plugins you want to communicate with. In your configuration file (`grafana.ini` or `custom.ini` depending on your operating system), remove the semicolon to enable and then set the following configuration option:

```
  actions_allow_post_url=
```

This is a comma-separated list that uses glob matching.

- To allow access to all plugins that have a backend, use:

```
actions_allow_post_url=/api/plugins/*
```

- To access the backend of only one plugin, use:

```
actions_allow_post_url=/api/plugins/<GRAFANA_SPECIAL_APP>
```
