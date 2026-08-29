---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/administration/replica-set-member-configuration.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.757393Z"
---
.. _member-config-tutorials:

# Self-Managed Member Configuration Tutorials

**meta:** :keywords: on-prem
   :description: Explore tutorials on configuring replica set members for specific operations like dedicated backups, reporting, or acting as a cold standby.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

The following tutorials provide information on configuring replica set
members to support specific operations, such as to provide dedicated
backups, to support reporting, or to act as a cold standby.

**warning:** .. include:: /includes/warning-mixed-version-rs-config.rst

:doc:`/tutorial/adjust-replica-set-member-priority`
   Change the precedence given to a replica set members in an
   election for primary.

:doc:`/tutorial/configure-secondary-only-replica-set-member`
   Make a secondary member ineligible for election as primary.

:doc:`/tutorial/configure-a-hidden-replica-set-member`
   Configure a secondary member to be invisible to applications in
   order to support significantly different usage, such as a
   dedicated backups.

:doc:`/tutorial/configure-a-delayed-replica-set-member`
   Configure a secondary member to keep a delayed copy of the data
   set in order to provide a rolling backup.

:doc:`/tutorial/configure-a-non-voting-replica-set-member`
   Create a secondary member that keeps a copy of the data set but
   does not vote in an election.

:doc:`/tutorial/convert-secondary-into-arbiter`
   Convert a secondary to an arbiter.


**toctree:** :titlesonly: 
   :hidden: 

   Hidden Members </tutorial/configure-a-hidden-replica-set-member>
   Delayed Members </tutorial/configure-a-delayed-replica-set-member>
   Non-Voting Members </tutorial/configure-a-non-voting-replica-set-member>
   Adjust Member Priority </tutorial/adjust-replica-set-member-priority>
   Block Secondary Priority </tutorial/configure-secondary-only-replica-set-member>
   Convert Secondary to Arbiter </tutorial/convert-secondary-into-arbiter>