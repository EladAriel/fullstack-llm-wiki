---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-distributed-rs-siteB-config.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

a. View the replica set configuration to determine the :rsconf:`members` array position for the member.

> **Note:**    The array position is not the same as the `_id`.
.. code-block:: javascript
   rs.conf()

b. Copy the replica set configuration object to a variable (to `cfg` in the example below). Then, in the variable, set the correct priority for the member. Pass the variable to :method:`rs.reconfig()` to update the replica set configuration.

For example, to set priority for the third member in the array (i.e., the member at position 2), issue the following sequence of commands:

```javascript
   cfg = rs.conf()
   cfg.members[2].priority = 0.5
   rs.reconfig(cfg)

.. note::

   The :method:`rs.reconfig()` shell method can force the current
   primary to step down, causing an election. When the primary steps
   down, all clients disconnect. This is the intended behavior.
   While median time to elect a new primary should not typically
   exceed 12 seconds, make sure any replica configuration
   changes occur during scheduled maintenance periods.
```
