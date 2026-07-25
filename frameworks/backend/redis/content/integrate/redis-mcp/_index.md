---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/redis-mcp/_index.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
Title: Redis MCP
alwaysopen: false
categories:
- docs
- integrate
- rs
description: Access a Redis server using any MCP client.
group: service
hideListLinks: false
linkTitle: Redis MCP
summary: Redis MCP server lets MCP clients access the features of Redis.
type: integration
weight: 1
---

The [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction)
is a standard that lets AI agents access data and perform actions. Using MCP,
your server can publish a set of commands that are usable by any MCP-compatible
client app (such as [Claude Desktop](https://claude.ai/download) or
[VS Code](https://code.visualstudio.com/)). These commands can retrieve
whatever data you wish to provide and you can also let the agent make
changes to the data. For example, you could publish a feed of news items that
an agent can use in its responses, and also let the agent add the user's
comments to those items.

Redis MCP is a general-purpose implementation that lets agents read, write, and
query data in Redis and also has some basic commands to manage the Redis
server. With this enabled, you can use an LLM client as a very high-level
interface to Redis. Add, query, and analyze any Redis data set directly from
an LLM chat using instructions and questions like the following:

- "Store the entire conversation in the 'recent_chats' stream"
- "Cache this item"
- "How many keys does my database have?"
- "What is user:1's email?"

See the other pages in this section to learn how to set up and use Redis MCP.
See also the [GitHub repository](https://github.com/redis/mcp-redis) for
the latest changes.
