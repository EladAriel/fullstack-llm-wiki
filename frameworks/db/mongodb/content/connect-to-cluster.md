---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/connect-to-cluster.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

:orphan:

======================

# Connect to a Cluster

Learn how to connect to MongoDB clusters whether they are hosted on {+atlas+} or self-managed.

## Connection String Formats

To connect to your deployment, you need a connection string. The connection string format depends on whether you connect to a replica set, sharded cluster, or standalone deployment.

**Replica Set:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com/?authSource=admin&replicaSet=myRepl
```

**Sharded Cluster:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com/?authSource=admin
```

**Standalone:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com/?authSource=admin
```

.. include:: /includes/fact-pct-encode-uri.rst

For detailed information about connection string formats and options, see `find-connection-string`.

## Get Your Connection String

How you obtain your connection string depends on whether your deployment is hosted on {+atlas+} or self-managed.

### {+atlas+} Deployments

To connect to a cluster hosted on {+atlas+}, see `atlas-connect-to-deployment`, which covers how to:

- Get your connection string via the {+atlas-cli+} or {+atlas-ui+}.
- Configure your IP access list.
- Create database users.
- Use various connection methods including drivers, Compass, `mongosh`, and more.
### Self-Managed Deployments

Before you connect to a self-managed deployment:

- Ensure your MongoDB deployment is running and accessible.
- Create a database user with the appropriate privileges.
- Verify network connectivity between your client and the MongoDB deployment.
To construct your connection string, use the appropriate `connection string format <connection-string-formats>` for your deployment topology.

### Connection Methods

After you have your connection string, you can connect using the following methods:

- `connect-via-driver` - MongoDB drivers for various programming languages
- `atlas-connect-via-compass` - MongoDB Compass GUI
- `connect-mongo-shell` - `mongosh`
- `mongodb-for-vscode` - MongoDB for VS Code
- `bi-connection` - MongoDB BI Connector
- `Command Line Tools <command-line-tools>` - mongodump, mongorestore, and other tools
## Learn More

- `Connection String Formats <find-connection-string>`
- `Connection String Options <connections-connection-options>`
- `test-failover`
- `connection-limits`
