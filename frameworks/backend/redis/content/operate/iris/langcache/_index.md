---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/iris/langcache/_index.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.317681Z"
---
# _Index

---
alwaysopen: false
categories:
- docs
- operate
- iris
description: Store LLM responses for AI applications in Redis Cloud.
hideListLinks: true
linktitle: LangCache
title: Semantic caching with LangCache on Redis Cloud
weight: 30
bannerText: LangCache on Redis Cloud is currently available as a public preview. Features and behavior are subject to change.
bannerChildren: true
aliases:
- /operate/rc/langcache
---

LangCache is a semantic caching service available as a REST API that stores LLM responses for fast and cheaper retrieval, built on the Redis vector database. By using semantic caching, you can significantly reduce API costs and lower the average latency of your generative AI applications.

For more information about how LangCache works, see the [LangCache overview]({{< relref "/develop/ai/context-engine/langcache" >}}).

## LLM cost reduction with LangCache

{{< embed-md "langcache-cost-reduction.md"  >}}

## Get started with LangCache on Redis Cloud

{{< embed-md "rc-langcache-get-started.md"  >}}
