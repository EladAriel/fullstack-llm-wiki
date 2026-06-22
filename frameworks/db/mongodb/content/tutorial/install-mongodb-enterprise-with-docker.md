---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/install-mongodb-enterprise-with-docker.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================================

# Install MongoDB Enterprise with Docker

.. include:: /includes/minor-release.rst

> **Important:** The recommended solutions for using containers with MongoDB are:
- For development and testing use the
  [MongoDB Community Docker container](https://hub.docker.com/r/mongodb/mongodb-community-server/)_.
  This image is maintained by MongoDB. The image contains the
  Community Edition of MongoDB.
- For MongoDB Enterprise production installations, use the
  [Enterprise Kubernetes Operator](https://www.mongodb.com/docs/kubernetes-operator/master/kind-quick-start/)_
  to deploy and manage MongoDB clusters within Kubernetes.

You can run MongoDB Enterprise Edition as a Docker container using the official MongoDB Enterprise image. Use a Docker container to run your MongoDB deployment if you want to:

- Quickly set up a deployment.
- Avoid editing configuration files.
- Test features from multiple versions of MongoDB.
## About This Task

- This page assumes prior knowledge of Docker. A full description of
[Docker](https://docs.docker.com/)_ is beyond the scope of this documentation.

- This procedure uses the official `MongoDB Enterprise Advanced Server
<https://hub.docker.com/r/mongodb/mongodb-enterprise-server>`__ container, which is maintained by MongoDB.

.. include:: /includes/fact-avx-support-docker

## Before You Begin

- Install [Docker](https://docs.docker.com/install/)_
- Install [mongosh](https://www.mongodb.com/docs/mongodb-shell/install/)_
## Steps

## Next Steps (Optional)

.. include:: /includes/installation/docker/verify-signature-intro.rst

## Learn More

For compatibility information, see [Docker & MongoDB](https://www.mongodb.com/compatibility/docker)_.
