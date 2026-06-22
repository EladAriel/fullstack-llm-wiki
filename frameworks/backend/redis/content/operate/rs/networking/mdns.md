---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/networking/mdns.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Client prerequisites for mDNS
alwaysopen: false
categories:
- docs
- operate
- rs
description: Requirements for using the mDNS protocol in development and testing environments.
linkTitle: mDNS client prerequisites
weight: $weight
---
{{< note >}}
mDNS is only supported for development and testing environments.
{{< /note >}}

If you choose to use the mDNS protocol when [you set the cluster name]({{< relref "/operate/rs/networking/cluster-dns" >}}),
make sure that the configurations and prerequisites for resolving database endpoints are met on the client machines.
If you have [Replica Of]({{< relref "/operate/rs/databases/import-export/replica-of/" >}}) databases on the cluster,
the configurations and prerequisites are also required for the Redis Software nodes.

To prepare a client or node for mDNS:

1. Make sure that the clients and cluster nodes are on the same physical network
    or have the network infrastructure configured to allow multicasting between them.
1. Install these prerequisite packages:

    - For Ubuntu:

        ```sh
        apt-get install libnss-mdns
        ```

    - For RHEL/CentOS 6.x:

        ```sh
        $ rpm -ivh http://download.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
        $ yum install nss-mdns
        $ service avahi-daemon start
        ```

    - For RHEL/CentOS 7:

        ```sh
        $ rpm -ivh https://dl.fedoraproject.org/pub/epel/7/x86_64/Packages/e/epel-release-7-12.noarch.rpm
        $ yum install nss-mdns
        $ service avahi-daemon start
        ```

1. If you are using [mDNS with IPv6 addresses]({{< relref "/operate/rs/networking/multi-ip-ipv6.md" >}}),
    update the hosts line in `/etc/nsswitch.conf` to:

    ```yaml
    hosts: files mdns4_minimal
    \[NOTFOUND=return\] mdns
    ```
