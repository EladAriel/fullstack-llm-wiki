---
topic: gRPC
tags: apis, communication, rpc
ai_summary: gRPC is a high-performance RPC framework using HTTP/2 and Protocol Buffers. It excels at efficient internal service-to-service calls and streaming.
---

# gRPC

## 1. Core Concept
gRPC defines strongly typed service contracts in protobuf and generates clients/servers. It solves efficient binary RPC, streaming, and strict schema evolution for internal microservices.

## 2. Architecture & Data Flow
1. Define .proto services and messages.
2. Generate stubs; servers implement RPC methods.
3. Clients open HTTP/2 channels with optional mTLS.
4. Unary or streaming calls exchange protobuf payloads.
5. Deadlines, retries, and interceptors enforce policy.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Compact payloads and multiplexed streams.
  * First-class deadlines and code-generated contracts.
* **Disadvantages/Risks:**
  * Harder for browsers without a proxy; less human-debuggable than JSON.
  * Protobuf evolution requires discipline.

## 4. Alternatives
**JSON/HTTP REST** for public/simple APIs; **GraphQL** when clients need flexible graphs of data.

## 5. Team Guidelines & Use Cases
**SHOULD** prefer gRPC for internal low-latency service meshes. **SHOULD NOT** expose raw gRPC to anonymous public web clients without a gateway.
