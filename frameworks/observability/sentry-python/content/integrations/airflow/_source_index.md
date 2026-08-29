---
type: "Framework Learn Page"
framework: "Sentry Python"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/python/integrations/airflow/index.mdx"
source_commit: "8b4e4a23b18ee70f5fdb05bcda48869c10be2f60"
source_commit_short: "8b4e4a2"
source_commit_date: "2026-08-28T22:17:56+00:00"
generated_at: "2026-08-29T09:40:09.060972Z"
---
# Index

---
title: Apache Airflow
description: "Learn about using Sentry with Apache Airflow."
---

[Apache Airflow](https://airflow.apache.org/) **1.10.6** and above can be set up to send errors to Sentry.

## Installation

Install the `apache-airflow` package with the `sentry` requirement.


```bash {tabTitle:pip}
pip install "apache-airflow[sentry]"
```
```bash {tabTitle:uv}
uv add "apache-airflow[sentry]"
```

Then, add your Sentry DSN to your configuration file (ex. `airflow.cfg`) under the `[sentry]` field.


```ini {filename:airflow.cfg}
[sentry]
sentry_dsn = ___PUBLIC_DSN___
```

Now, Airflow should report errors to Sentry automatically. Airflow will also generate custom tags and breadcrumbs based on the current Directed Acyclic Graph (DAG) and tasks at the time of the error.

Please see the official [Apache Airflow documentation](https://airflow.apache.org/docs/stable/errors.html) for more details.

### Configuration

Please see the official [Apache Airflow documentation](https://airflow.apache.org/docs/stable/configurations-ref.html#sentry) for the full list of configuration options available.
