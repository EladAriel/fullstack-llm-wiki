---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rc/context-engine/langcache/_index.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
alwaysopen: false
categories:
- docs
- operate
- rc
description: Store LLM responses for AI applications in Redis Cloud.
hideListLinks: true
linktitle: LangCache
title: Semantic caching with LangCache on Redis Cloud
weight: 36
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