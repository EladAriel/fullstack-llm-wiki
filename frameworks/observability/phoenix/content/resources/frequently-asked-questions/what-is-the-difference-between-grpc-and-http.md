---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/resources/frequently-asked-questions/what-is-the-difference-between-grpc-and-http.mdx"
source_commit: "c48e50e9906fcc56c1c103ebd93ef3c95ed6b6e7"
source_commit_short: "c48e50e"
source_commit_date: "2026-08-29T01:45:20-06:00"
generated_at: "2026-08-29T09:39:58.948707Z"
---
# What Is The Difference Between Grpc And Http

---
title: "What is the difference between GRPC and HTTP?"
description: "gRPC and HTTP are communication protocols used to transfer data between client and server applications."
---

* **HTTP (Hypertext Transfer Protocol)** is a stateless protocol primarily used for website and web application requests over the internet.
* **gRPC (gRemote Procedure Call)** is a modern, open-source communication protocol from Google that uses HTTP/2 for transport, protocol buffers as the interface description language, and provides features like bi-directional streaming, multiplexing, and flow control.

gRPC is more efficient in a tracing context than HTTP, but HTTP is more widely supported.

Phoenix can send traces over either HTTP or gRPC.
