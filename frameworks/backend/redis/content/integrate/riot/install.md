---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/riot/install.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
description: Install RIOT-X on macOS, Linux, Windows, and Docker
linkTitle: Install
title: Install
type: integration
weight: 2
---

RIOT-X can be installed in different ways depending on your environment and preference.

## macOS and Linux via Homebrew

```
brew install redis/tap/riotx
```

## Windows via Scoop

```
scoop bucket add redis https://github.com/redis/scoop.git
scoop install riotx
```

## Docker

```
docker run riotx/riotx [OPTIONS] [COMMAND]
```

## Manual installation on all supported platforms

Download the pre-compiled binary from [RIOT-X Releases](https://github.com/redis/riotx-dist/releases), uncompress, and copy to the desired location.

Full installation documentation is available [here](https://redis.github.io/riotx/quick-start/install.html).
