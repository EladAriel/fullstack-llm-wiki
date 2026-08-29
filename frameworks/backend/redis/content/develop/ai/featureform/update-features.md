---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/develop/ai/featureform/update-features.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.821950Z"
---
# Update Features

---
title: Update features
description: Iterate on a Redis Feature Form definitions file with plan, merge, and re-apply workflows.
linkTitle: Update features
weight: 50
---

After the first `ff apply`, most changes will be iterative: edit the definitions file, preview the delta, apply, and verify. For the full apply mechanics and failure modes, see [Define and deploy features]({{< relref "/develop/ai/featureform/define-and-deploy-features" >}}).

## Typical cycle

1. Change a resource definition.
2. Run a plan.
3. Apply the change.
4. Verify the resulting graph or catalog state.

Preview the change first:

```bash
ff apply \
  --workspace <workspace-id> \
  --file examples/featureform/docs/resources.py \
  --plan
```

Then apply:

```bash
ff apply \
  --workspace <workspace-id> \
  --file examples/featureform/docs/resources.py \
  --wait \
  --wait-for finished
```

## When to use `--merge`

Use `--merge` when your file is intentionally partial and omitted resources should not be treated as deletions.

## Verify the outcome

```bash
ff graph workspace stats --workspace <workspace-id>
ff catalog list --workspace <workspace-id>
```
