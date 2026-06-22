---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/installation/install-search-norefs.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

## Install MongoDB Search and MongoDB Vector Search

> **Important:** |fts| and {+avs+} with MongoDB Community is in Preview. The feature and
the corresponding documentation might change at any time during the
Preview period. To learn more, see `Preview Features
<https://www.mongodb.com/docs/preview-features/>`__.

You can install the search process, `mongot`, in MongoDB Community Edition. The search process is available for deployment as a tarball with the `.tgz` extension and as an image in Docker.

> **Note:** To onboard more quickly with a deployment meant for experimentation, see the
:atlas:`MongoDB Search Quick Start Tutorial </atlas-search/tutorial>` and
select the Self-Managed deployment type.

### Before You Begin

To use `mongot` in a self-managed deployment, you must have the following prerequisites.

> **Important:** The **Deploy using .tgz Tarball** tutorial and **Deploy with Docker**
tutorials have different workflows.
- The **Deploy with .tgz Tarball** tutorial assumes you have a
  `mongod` instance running before you install.
- The **Deploy with Docker** tutorial creates `mongod` on a Docker
  network, so there is no need to set one up in advance.

### Procedure

### Next Steps

- Create :atlas:`MongoDB Search indexes </atlas-search/searching/>`
- Create :atlas:`MongoDB Vector Search indexes </atlas-vector-search/vector-search-stage/>`
