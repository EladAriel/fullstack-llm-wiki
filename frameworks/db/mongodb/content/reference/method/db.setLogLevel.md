---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.setLogLevel.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=================================

# db.setLogLevel() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-no-atlas-support.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Behavior

:method:`db.setLogLevel()` sets a single verbosity level. To set multiple verbosity levels in a single operation, use either the :dbcommand:`setParameter` command to set the :parameter:`logComponentVerbosity` parameter. You can also specify the verbosity settings in the `configuration file </reference/configuration-options>`. See `log-messages-configure-verbosity` for examples.

> **Note:** .. include:: /includes/extracts/4.2-changes-debug-log-message.rst

## Examples

### Set Default Verbosity Level

Omit the `<component>` parameter to set the default verbosity for all components; i.e. the :setting:`systemLog.verbosity` setting. The operation sets the default verbosity to `1`:

### Set Verbosity Level for a Component

Specify the `<component>` parameter to set the verbosity for the component. The following operation updates the :setting:`systemLog.component.storage.journal.verbosity` to `2`:

### Get Global Log Level For a Deployment

The following operation gets the default logging level verbosity for a deployment:

> **Note:** You can also get log verbosity levels for MongoDB components.
For details, see :method:`db.getLogComponents()`.
