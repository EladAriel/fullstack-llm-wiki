---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/considerations-deploying-replica-set.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

### Architecture

In production, deploy each member of the replica set to its own machine. If possible, ensure that MongoDB listens on the default port of `27017`.

.. include:: /includes/replication/note-replica-set-major-versions.rst

For more information, see `/core/replica-set-architectures`.

### Hostnames

.. include:: /includes/important-hostnames.rst

### IP Binding

Use the :option:`--bind_ip <mongod --bind_ip>` option to ensure that MongoDB listens for connections from applications on configured addresses.

.. include:: /includes/fact-default-bind-ip.rst

### Connectivity

Ensure that network traffic can pass securely between all members of the set and all clients in the network .

Consider the following:

- Establish a virtual private network. Ensure that your network topology
routes all traffic between members within a single site over the local area network.

- Configure access control to prevent connections from unknown clients
to the replica set.

- Configure networking and firewall rules so that incoming and outgoing
packets are permitted only on the default MongoDB port and only from within your deployment. See the IP Binding considerations.

Ensure that each member of a replica set is accessible by way of resolvable DNS or hostnames. You should either configure your DNS names appropriately or set up your systems' `/etc/hosts` file to reflect this configuration.

Each member must be able to connect to every other member. For instructions on how to check your connection, see `replica-set-troubleshooting-check-connection`.

### Configuration

Create the directory where MongoDB stores data files before deploying MongoDB.

Specify the :binary:`~bin.mongod` configuration in a `configuration file </reference/configuration-options>` stored in `/etc/mongod.conf` or a related location.

For more information about configuration options, see `/reference/configuration-options`.
