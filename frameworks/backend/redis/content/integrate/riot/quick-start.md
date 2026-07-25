---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/riot/quick-start.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
description: RIOT-X getting started guide
linkTitle: Getting started
title: Getting started
type: integration
weight: 3
---

You can launch RIOT-X with the following command:

```
riotx
```

This will show usage help, which you can also get by running:

```
riotx --help
```

Usage help is available on any command and subcommand:

```
riotx COMMAND --help
```

Redis Command Help

```
riotx file-import file.json json.set --help
```

{{< tip >}}
Run the following command to give riotx TAB completion in the current shell:

`source <(riotx generate-completion)`
{{< /tip >}}

Full documentation is available at [redis.github.io/riotx](https://redis.github.io/riotx/).
