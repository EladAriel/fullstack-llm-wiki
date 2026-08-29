---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/define-privilege.rst"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:20.308797Z"
---
.. renamed as an rst file to prevent this from being published in case
   this is a stub. If its not we should remove this as it seems
   redundant.

# Define a Privilege

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

MongoDB privileges exist within roles. Defining a privilege as part of
role creation.

When creating a role, specify each privilege in its own :ref:`resource
document <resource-document>` in :data:`~admin.system.roles.privileges`
array.