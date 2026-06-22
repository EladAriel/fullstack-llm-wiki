---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/riot/quick-start.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
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
