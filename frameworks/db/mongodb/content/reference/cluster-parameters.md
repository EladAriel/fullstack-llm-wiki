---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/cluster-parameters.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

================================================

# Cluster Parameters for a Self-Managed Deployment

You can use MongoDB cluster parameters to specify configuration options that affect all nodes in a replica set or sharded cluster.

## Syntax

To set cluster parameters for your deployment, run the following command on the `admin` database:

```javascript
db.adminCommand( { setClusterParameter:{ <parameter>: <value> } } )
```

To view the current cluster parameter values, run the following command on the `admin` database:

```javascript
db.adminCommand( { getClusterParameter: "*" } )
```

To learn more about setting and viewing cluster parameters, see :dbcommand:`setClusterParameter` and :dbcommand:`getClusterParameter`.

## Access Control

.. include:: /includes/cluster-parameters/access-control.rst

## Parameters

MongoDB provides the following cluster parameters:

## Learn More

- :dbcommand:`getClusterParameter`
- :dbcommand:`setClusterParameter`
## Contents

- auditConfig </reference/cluster-parameters/auditConfig>
- changeStreamOptions </reference/cluster-parameters/changeStreamOptions>
- defaultMaxTimeMS </reference/cluster-parameters/defaultMaxTimeMS>
- fleDisableSubstringPreviewParameterLimits </reference/cluster-parameters/fleDisableSubstringPreviewParameterLimits>
