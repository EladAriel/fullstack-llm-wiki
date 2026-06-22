---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.22/references/cli-utilities/rladmin/cluster/recover.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: rladmin cluster recover
alwaysopen: false
categories:
- docs
- operate
- rs
description: Recovers a cluster from a backup file.
headerRange: '[1-2]'
linkTitle: recover
tags:
- non-configured
toc: 'true'
weight: $weight
url: '/operate/rs/7.22/references/cli-utilities/rladmin/cluster/recover/'
---

Recovers a cluster from a backup file. The default location of the configuration backup file is `/var/opt/redislabs/persist/ccs/ccs-redis.rdb`.

```sh
rladmin cluster recover
        filename <recovery filename>
        [ ephemeral_path <path> ]
        [ persistent_path <path> ]
        [ ccs_persistent_path <path> ]
        [ rack_id <ID> ]
        [ second_rack_id <ID> ]
        [ override_rack_id ]
        [ node_uid <number> ]
        [ flash_enabled ]
        [ flash_path <path> ]
        [ addr <IP address> ]
        [ external_addr <IP address> ]
```

### Parameters

| Parameter | Type/Value | Description |
|-----------|------------|-------------|
| addr | IP address | Sets a node's internal IP address. If not provided, the node sets the address automatically. (optional) |
| ccs_persistent_path | filepath | Path to the location of CCS snapshots (default is the same as persistent_path) (optional) |
| external_addr | IP address | Sets a node's external IP address. If not provided, the node sets the address automatically. (optional) |
| ephemeral_path | filepath (default:&nbsp;/var/opt/redislabs) | Path to an ephemeral storage location (optional) |
| filename | filepath | Backup file to use for recovery |
| flash_enabled | | Enables flash storage (optional) |
| flash_path | filepath (default:&nbsp;/var/opt/redislabs/flash) | Path to the flash storage location in case the node does not support CAPI (required if flash_enabled) |
| node_uid | integer (default:&nbsp;1) | Specifies which node will recover first and become master (optional) |
| override_rack_id | | Changes to a new rack, specified by `rack_id` (optional) |
| persistent_path | filepath | Path to the persistent storage location (optional) |
| rack_id | string | Switches to the specified rack (optional) |
| second_rack_id | string | The unique identifier of a second rack ID for two-dimensional rack awareness (optional) |

### Returns

Returns `ok` if the cluster recovered successfully. Otherwise, it returns an error message.

### Example

```sh
$ rladmin cluster recover filename /tmp/persist/ccs/ccs-redis.rdb node_uid 1 rack_id 5
Initiating cluster recovery... ok
```
