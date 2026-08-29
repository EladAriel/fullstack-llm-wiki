---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsfuture/seterror.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.262888Z"
---
# Seterror

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
