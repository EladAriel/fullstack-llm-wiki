---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/views.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=====

# Views

A MongoDB view is a read-only queryable object whose contents are defined by an `aggregation pipeline <aggregation-pipeline>` on other collections or views.

MongoDB does not persist the view contents to disk. A view's content is computed on-demand when a client queries the view.

.. include:: /includes/views/disambiguate-standard-materialized.rst

## Use Cases

You can use views to:

- Create a view on a collection of employee data to exclude any
personally identifiable information (PII).

- Create a view on a collection of sensor data to add computed
fields and metrics.

- Create a view that joins two collections containing inventory and
order history. Your application can query the view without managing or understanding the underlying pipeline.

- Create a {+fts+} or {+avs+} index on a view to partially
index a collection, support incompatible data types or data models, and more. To learn more, see `fts-transform-documents-collections` and `avs-transform-documents-collections`.

## Create and Manage Views

To learn how to create and manage views, see the following resources:

- `atlas-ui-views`
- `manual-views-create`
- `manual-views-lookup`
- `manual-views-collation`
- `manual-views-modify`
- `manual-views-remove`
## Comparison with On-Demand Materialized Views

.. include:: /includes/views/fact-compare-view-and-materialized-view.rst

## Behavior

### Read Only

Views are read-only. Write operations on views return an error.

### Snapshot Isolation

Views do not maintain timestamps of collection changes and do not support point-in-time or snapshot read isolation.

### View Pipelines

The view's underlying aggregation pipeline is subject to the 100 megabyte memory limit for blocking sort and blocking group operations.

.. include:: /includes/fact-allowDiskUseByDefault.rst

> **Note:** .. include:: /includes/fact-atlas-enable-autoscaling.rst

### Time Series Collections

`Time series collections <manual-timeseries-collection>` are writable non-materialized views. Limitations for views apply to time series collections. For more information, see `Time Series Collection Limitations <manual-timeseries-collection-limitations>`.

## Access Control

.. include:: /includes/extracts/views-access-control.rst

## Contents

- Create & Query </core/views/create-view>
- Join Collections </core/views/join-collections-with-view>
- Use Default Collation </core/views/specify-collation>
- Modify or Remove </core/views/update-view>
- Supported Operations </core/views/supported-operations>
