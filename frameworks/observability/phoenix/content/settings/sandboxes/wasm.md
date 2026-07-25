---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/settings/sandboxes/wasm.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.978606Z"
---
# Wasm

---
title: "WebAssembly"
description: "Run simple Python code evaluators locally inside the Phoenix server."
---

<div style={{ display: 'flex', alignItems: 'center', gap: '1.5rem', marginTop: '1.5rem', marginBottom: '1.5rem' }}>
<img src="https://storage.googleapis.com/arize-phoenix-assets/assets/svgs/wasm.svg" alt="WebAssembly" style={{ height: '112px', flexShrink: 0 }} />
<div>

The **WebAssembly** sandbox is a **local sandbox** for **simple Python evaluators** — pure-logic checks like regex matches, JSON parsing, and scoring functions. It runs locally inside the Phoenix server, starts in milliseconds, and needs no credentials.

</div>
</div>

Configure it from [Settings → Sandboxes](/docs/phoenix/settings/sandboxes).

## What it supports

The WebAssembly sandbox runs your Python in an isolated [WebAssembly](https://webassembly.org/) runtime on the Phoenix server. It is intentionally limited to **self-contained code**:

| Capability | Supported? |
| :-- | :-- |
| Environment variables | ❌ Not supported — use a hosted sandbox |
| Network access | ❌ Not supported — use a hosted sandbox |
| Third-party dependencies | ❌ Not supported — use a hosted sandbox |

If your evaluator needs **any** of the above, it cannot run on WebAssembly. Use a [hosted sandbox](/docs/phoenix/settings/sandboxes#local-vs-hosted-sandboxes) (E2B, Daytona, Vercel, or Modal) instead — those run each evaluation on an isolated remote VM with full support for environment variables, outbound network access, and installed packages.

## Running untrusted code

WebAssembly runs the Python interpreter inside a strictly isolated environment — memory is partitioned and the script has no built-in access to the filesystem, network, or operating system. The sandbox still runs in the Phoenix server process, so the script shares CPU and memory with Phoenix. For the full security model, see WebAssembly's [Security](https://webassembly.org/docs/security/) documentation.
