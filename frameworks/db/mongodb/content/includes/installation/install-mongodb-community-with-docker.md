---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/installation/install-mongodb-community-with-docker.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================================

# Install MongoDB Community with Docker

You can run MongoDB community Edition as a Docker container using the official MongoDB Community image. Using a Docker image for running your MongoDB deployment is useful to:

- Stand up a deployment quickly.
- Help manage configuration files.
- Test different features on multiple versions of MongoDB.
## About This Task

- This page describes the Docker install instructions for MongoDB Community
edition. The [MongoDB Enterprise Docker image](https://hub.docker.com/r/mongodb/mongodb-enterprise-server)_ and [MongoDB Enterprise Kubernetes Operator](https://www.mongodb.com/docs/kubernetes-operator)_ are recommended for production deployments and should be used together.

- This procedure uses the official `MongoDB community image
<https://hub.docker.com/r/mongodb/mongodb-community-server>`__, which is maintained by MongoDB.

- A full description of [Docker](https://docs.docker.com/)_ is beyond
the scope of this documentation. This page assumes prior knowledge of Docker.

.. include:: /includes/fact-avx-support-docker

- .. include:: /includes/fact-fsync-caveat-docker
To avoid a filesystem issue while running MongoDB in Docker, use the official MongoDB community image above.

## Before You Begin

- Install [Docker](https://docs.docker.com/install/)_
- Install [mongosh](https://www.mongodb.com/docs/mongodb-shell/install/)_
## Procedure

## Next Steps (Optional)

.. include:: /includes/installation/docker/verify-signature-intro.rst
