---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/readers/keysonlyreader.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: KeysOnlyReader
alwaysopen: false
categories:
- docs
- operate
- stack
description: Gets key names from a database.
linkTitle: KeysOnlyReader
weight: 60
aliases:
- "/operate/oss_and_stack/stack-with-enterprise/gears-v1/jvm/classes/readers/keysonlyreader/"
bannerText: Redis Gears is a deprecated feature that is not recommended or supported
  for new users.
---

The `KeysOnlyReader` only extracts the key names from a database.

## Constructors

You can use one of these constructors to create a new `KeysOnlyReader` object:

```java
public KeysOnlyReader()

public KeysOnlyReader(int scanSize, String pattern)
```

## Parameters

| Name | Type | Default value | Description |
|------|------|---------------|-------------|
| pattern | string | "\*" (match all keys) | Get all keys that match this pattern |
| scanSize | integer | 10000 | The scan command's size limit |

## Output records

Each output record is a string that represents the key's name.

## Examples

Get all keys in the database:

```java
KeysOnlyReader reader = new KeysOnlyReader();
```

Only get keys that start with "user:":

```java
KeysOnlyReader reader = new KeysOnlyReader(1000, "user:*");
```

