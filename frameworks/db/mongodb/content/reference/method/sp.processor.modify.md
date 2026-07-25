---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sp.processor.modify.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

======================================

# sp.processor.modify() (mongosh method)

## Definition

Modifies a named :atlas:`Stream Processor </atlas-sp/overview/#mongodb-expression-exp.Stream-Processor>` on the current :atlas:`Stream Processing Workspace </atlas-sp/overview/#mongodb-expression-exp.Stream-Processing-Instance>`.

## Compatibility

.. include:: /includes/fact-environments-atlas-support-stream-processing-only.rst

## Syntax

The :method:`sp.processor.modify()` method has the following syntax:

```javascript
sp.processor.modify({
  pipeline: [
    <pipeline>
  ],
  name: <name>,
  dlq: {
    connectionName: <connectionName>,
    db: <db>,
    coll: <coll>
  },
  resumeFromCheckpoint: <resumeFromCheckpoint>,
  tier: <tier>
})
```

## Command Fields

`sp.processor.modify()` takes the following fields:

## Behavior

The stream processor must be in a `STOPPED` state before you invoke this method. The `pipeline` argument replaces the processor's entire existing pipeline, including stages that you do not change.

By default, the modified processor resumes from its last checkpoint. If you set `resumeFromCheckpoint` to `false`, the modified processor retains only summary statistics. When you modify a processor with open windows, {+atlas-sp+} recomputes those windows on the updated pipeline.

For limitations that apply when you modify stream processors, see :atlas:`Modify a Stream Processor </atlas-sp/manage-stream-processor/#limitations>`.

## Access Control

To run `sp.processor.modify()`, you must have the :atlasrole:`atlasAdmin` role.

## Example

The example changes a stopped stream processor named `solarDemo` to add a `$match` stage, rename it, update its tier, and configure a dead letter queue:

Start the renamed processor, then run `sp.listStreamProcessors()` to verify the name, tier, and dead letter queue changes:

Run :method:`sp.processor.sample()` to verify the pipeline change:

## Learn More

- :atlas:`Manage Stream Processors </atlas-sp/manage-stream-processor>`
