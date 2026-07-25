---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsfuture/seterror.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
Title: SetError
alwaysopen: false
categories:
- docs
- operate
- stack
description: Sets an error message.
linkTitle: setError
weight: 50
aliases:
- "/operate/oss_and_stack/stack-with-enterprise/gears-v1/jvm/classes/gearsfuture/seterror/"
bannerText: Redis Gears is a deprecated feature that is not recommended or supported
  for new users.
---

```java
public void setError​(java.lang.String error) 
	throws java.lang.Exception
```

Sets an error message for an asynchronous computation.

## Parameters

| Name | Type | Description |
|------|------|-------------|
| error | string | An error message |

## Returns

None

## Example

```java
GearsFuture<Boolean> f = new GearsFuture<Boolean>();
try {
	f.setError("An error has occurred during asyncForeach");
} catch (Exception e) {
	e.printStackTrace();
}
```
