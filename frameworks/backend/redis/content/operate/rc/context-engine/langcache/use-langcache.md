---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rc/context-engine/langcache/use-langcache.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
alwaysopen: false
categories:
- docs
- operate
- rc
description: null
hideListLinks: true
linktitle: Use LangCache
title: Use the LangCache API on Redis Cloud
weight: 10
aliases:
- /operate/rc/langcache/use-langcache
---

You can use the [LangCache API and SDK]({{< relref "/develop/ai/context-engine/langcache/api-examples" >}}) from your client app to store and retrieve LLM, RAG, or agent responses. 

To access the LangCache API, you need:

- LangCache API base URL
- LangCache service API key
- Cache ID

For LangCache on Redis Cloud, the base URL and cache ID are available in the LangCache service's **Configuration** page in the [**Connectivity** section]({{< relref "/operate/rc/context-engine/langcache/view-edit-cache#connectivity" >}}).

The LangCache API key is only available immediately after you create the LangCache service. If you lost this value, you will need to [replace the service API key]({{< relref "/operate/rc/context-engine/langcache/view-edit-cache#replace-service-api-key" >}}) to be able to use the LangCache API.

When you call the API, you need to pass the LangCache API key in the `Authorization` header as a Bearer token and the Cache ID as the `cacheId` path parameter. 

See the [LangCache API and SDK examples]({{< relref "/develop/ai/context-engine/langcache/api-examples" >}}) for more information on how to use the LangCache API.
