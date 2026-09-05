# System Design Wiki

Local system design theory wiki for human engineers and AI assistants (RAG context).

Each topic page uses a fixed structure: core concept, architecture & data flow, trade-offs, alternatives, and team guidelines.

## How to use

1. Start here or open a category `index.md`.
2. Open the most specific topic page.
3. Prefer this wiki for architecture/theory questions; use `frameworks/` for library-specific docs.

## Categories

- [Foundations](foundations/index.md)
- [Networking & Traffic](networking/index.md)
- [Data Storage](data-storage/index.md)
- [Distributed Systems](distributed-systems/index.md)
- [Architecture Patterns](architecture-patterns/index.md)
- [Communication](communication/index.md)
- [Data Processing](data-processing/index.md)
- [Reliability & Operations](reliability/index.md)

## Foundations

- [Scalability (Horizontal vs Vertical)](foundations/scalability.md)
- [Availability and Reliability](foundations/availability-reliability.md)
- [Latency and Throughput](foundations/latency-throughput.md)
- [CAP Theorem](foundations/cap-theorem.md)
- [PACELC Theorem](foundations/pacelc.md)
- [Consistency Models](foundations/consistency-models.md)
- [ACID vs BASE](foundations/acid-vs-base.md)
## Networking & Traffic

- [DNS (Domain Name System)](networking/dns.md)
- [Load Balancing](networking/load-balancing.md)
- [Reverse Proxy](networking/reverse-proxy.md)
- [Content Delivery Network (CDN)](networking/cdn.md)
- [API Gateway](networking/api-gateway.md)
- [Rate Limiting](networking/rate-limiting.md)
- [TLS Termination](networking/tls-termination.md)
## Data Storage

- [Relational (SQL) Databases](data-storage/sql-databases.md)
- [NoSQL Databases](data-storage/nosql-databases.md)
- [Database Indexing](data-storage/database-indexing.md)
- [Database Replication](data-storage/database-replication.md)
- [Database Sharding](data-storage/database-sharding.md)
- [Consistent Hashing](data-storage/consistent-hashing.md)
- [Caching](data-storage/caching.md)
- [Cache Eviction Policies](data-storage/cache-eviction.md)
- [Object Storage](data-storage/object-storage.md)
- [OLTP vs OLAP](data-storage/oltp-vs-olap.md)
- [Bloom Filters](data-storage/bloom-filters.md)
## Distributed Systems

- [Message Queues](distributed-systems/message-queues.md)
- [Publish-Subscribe Messaging](distributed-systems/pub-sub.md)
- [Event-Driven Architecture](distributed-systems/event-driven-architecture.md)
- [Consensus Algorithms (Raft / Paxos)](distributed-systems/consensus.md)
- [Leader Election](distributed-systems/leader-election.md)
- [Quorum Reads and Writes](distributed-systems/quorum.md)
- [Gossip Protocols](distributed-systems/gossip-protocol.md)
- [Distributed Transactions (2PC)](distributed-systems/distributed-transactions.md)
- [Saga Pattern](distributed-systems/saga-pattern.md)
- [Idempotency](distributed-systems/idempotency.md)
- [Circuit Breaker](distributed-systems/circuit-breaker.md)
- [Bulkhead Pattern](distributed-systems/bulkhead.md)
- [Retries and Exponential Backoff](distributed-systems/retry-backoff.md)
- [Backpressure](distributed-systems/backpressure.md)
- [Service Discovery](distributed-systems/service-discovery.md)
## Architecture Patterns

- [Monolith vs Microservices](architecture-patterns/monolith-vs-microservices.md)
- [CQRS (Command Query Responsibility Segregation)](architecture-patterns/cqrs.md)
- [Event Sourcing](architecture-patterns/event-sourcing.md)
- [Strangler Fig Pattern](architecture-patterns/strangler-fig.md)
- [Sidecar Pattern](architecture-patterns/sidecar.md)
- [Backend for Frontend (BFF)](architecture-patterns/bff.md)
## Communication

- [REST APIs](communication/rest.md)
- [gRPC](communication/grpc.md)
- [GraphQL](communication/graphql.md)
- [Real-Time Communication (WebSockets, SSE, Long Polling)](communication/realtime-communication.md)
## Data Processing

- [Batch Processing](data-processing/batch-processing.md)
- [Stream Processing](data-processing/stream-processing.md)
- [MapReduce](data-processing/mapreduce.md)
- [Write-Ahead Logging (WAL)](data-processing/write-ahead-log.md)
- [Change Data Capture (CDC)](data-processing/cdc.md)
## Reliability & Operations

- [Health Checks and Heartbeats](reliability/health-checks.md)
- [Failover Strategies](reliability/failover.md)
- [Multi-Region Architecture](reliability/multi-region.md)
- [Observability (Metrics, Logs, Traces)](reliability/observability.md)
- [Authentication and Authorization](reliability/authentication-authorization.md)
- [Load Shedding](reliability/rate-limiting-vs-load-shedding.md)
