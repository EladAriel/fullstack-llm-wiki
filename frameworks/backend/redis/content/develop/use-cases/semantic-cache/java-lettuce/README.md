---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/develop/use-cases/semantic-cache/java-lettuce/README.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

# Redis semantic-cache demo (Java + Lettuce)

See `_index.md` for the full walkthrough. Quick start:

```bash
# 1. Make sure Redis with the Search module is running on localhost:6379.
# 2. Build the fat jar (first build pulls Lettuce, DJL, and the PyTorch
#    native libraries; takes a minute or two):
mvn -q package

# 3. Run. The first run downloads the sentence-transformers/all-MiniLM-L6-v2
#    PyTorch weights into the local DJL cache (~90 MB).
java -jar target/semantic-cache-lettuce.jar

# Or with Maven directly:
mvn -q exec:java
```

Then open <http://localhost:8090>.

Notable flags (full list with `--help`):

| Flag                      | Default            |
|---------------------------|--------------------|
| `--port`                  | `8090`             |
| `--redis-host`            | `localhost`        |
| `--redis-port`            | `6379`             |
| `--index-name`            | `semcache:idx`     |
| `--key-prefix`            | `cache:`           |
| `--ttl-seconds`           | `3600`             |
| `--threshold`             | `0.5`              |
| `--llm-latency-ms`        | `1500.0`           |
| `--no-reset`              | (re-seeds by default) |
