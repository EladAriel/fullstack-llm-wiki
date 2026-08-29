---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/riot/install.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:56.151273Z"
---
# Install

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
