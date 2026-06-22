---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.22/references/cli-utilities/rladmin/suffix.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: rladmin suffix
alwaysopen: false
categories:
- docs
- operate
- rs
description: Manages the DNS suffixes in the cluster.
headerRange: '[1-2]'
linkTitle: suffix
toc: 'true'
weight: $weight
url: '/operate/rs/7.22/references/cli-utilities/rladmin/suffix/'
---

Manages the DNS suffixes in the cluster.

## `suffix add`

Adds a DNS suffix to the cluster.

``` sh
rladmin suffix add name <name>
        [default]
        [internal]
        [mdns]
        [use_aaaa_ns]
        [slaves <ip>..]
```

### Parameters

| Parameter | Type/Value       | Description                                                                                   |
|-----------|------------------|-----------------------------------------------------------------------------------------------|
| name      | string           | DNS suffix to add to the cluster                                                             |
| default   |                  | Sets the given suffix as the default. If a default already exists, this overwrites it.  |
| internal  |                  | Forces the given suffix to use private IPs                                                    |
| mdns      |                  | Activates multicast DNS support for the given suffix                                           |
| slaves    | list of IPv4 addresses | The given suffix will notify the frontend DNS servers when a change in the frontend DNS has occurred |
| use_aaaa_ns |                | Activates IPv6 address support |

### Returns

Returns `Added suffixes successfully` if the suffix was added. Otherwise, it returns an error.

### Example

``` sh
$ rladmin suffix add name new.rediscluster.local
Added suffixes successfully
```

## `suffix delete`

Deletes an existing DNS suffix from the cluster.

``` sh
rladmin suffix delete name <name>
```

### Parameters

| Parameter | Type/Value       | Description                                                                                   |
|-----------|------------------|-----------------------------------------------------------------------------------------------|
| name      | string           | DNS suffix to delete from the cluster                                                         |

### Returns

Returns `Suffix deleted successfully` if the suffix was deleted. Otherwise, it returns an error.

### Example

``` sh
$ rladmin suffix delete name new.rediscluster.local
Suffix deleted successfully
```

## `suffix list`

Lists the DNS suffixes in the cluster.

```sh
rladmin suffix list
```

### Parameters

None

### Returns

Returns a list of the DNS suffixes.

### Example

``` sh
$ rladmin suffix list
List of all suffixes:
cluster.local
new.rediscluster.local
```
