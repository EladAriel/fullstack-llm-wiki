#!/usr/bin/env python3
"""Generate the top-level system-design wiki from curated topic definitions."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "system-design"


def page(
    topic: str,
    tags: list[str],
    ai_summary: str,
    core: str,
    architecture: str,
    advantages: list[str],
    disadvantages: list[str],
    alternatives: str,
    guidelines: str,
) -> str:
    tags_str = ", ".join(tags)
    adv = "\n".join(f"  * {item}" for item in advantages)
    disadv = "\n".join(f"  * {item}" for item in disadvantages)
    return f"""---
topic: {topic}
tags: {tags_str}
ai_summary: {ai_summary}
---

# {topic}

## 1. Core Concept
{core}

## 2. Architecture & Data Flow
{architecture}

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
{adv}
* **Disadvantages/Risks:**
{disadv}

## 4. Alternatives
{alternatives}

## 5. Team Guidelines & Use Cases
{guidelines}
"""


TOPICS: dict[str, list[dict]] = {
    "foundations": [
        {
            "slug": "scalability",
            "topic": "Scalability (Horizontal vs Vertical)",
            "tags": ["scaling", "capacity", "architecture"],
            "ai_summary": "Scalability is the ability of a system to handle growth in load by adding resources. Horizontal scaling adds more machines; vertical scaling adds more power to existing machines.",
            "core": "Scalability describes how a system grows as traffic, data, or compute demand increases. Vertical scaling (scale-up) upgrades CPU, RAM, or disk on one node. Horizontal scaling (scale-out) adds more nodes behind load distribution. The engineering problem is sustaining target latency and availability as usage grows without unbounded cost or complexity.",
            "architecture": "1. Measure bottlenecks (CPU, memory, I/O, network, locks).\n2. For vertical scale, replace or resize the instance and migrate traffic with downtime or blue/green.\n3. For horizontal scale, put a load balancer or partition key in front of N identical (or sharded) workers.\n4. Ensure the app is stateless or externalize session/state so any node can serve a request.\n5. Autoscale based on metrics (CPU, queue depth, RPS) with cool-downs to avoid thrash.",
            "advantages": [
                "Horizontal scaling improves fault isolation and can grow nearly linearly for stateless workloads.",
                "Vertical scaling is simple operationally for early-stage systems and single-writer databases.",
            ],
            "disadvantages": [
                "Vertical scaling hits hardware ceilings and creates larger blast radius on failure.",
                "Horizontal scaling requires distributed coordination, data partitioning, and often redesign of sticky state.",
            ],
            "alternatives": "Compare with **capacity reservation / overprovisioning** (pay for headroom instead of elastic scale) and **workload shedding / rate limiting** (protect the system by rejecting excess instead of adding capacity).",
            "guidelines": "**SHOULD** prefer horizontal scale for stateless APIs and workers once a single box is near its ceiling. **SHOULD NOT** assume every database or legacy service can scale out without sharding or read replicas—validate state and write paths first.",
        },
        {
            "slug": "availability-reliability",
            "topic": "Availability and Reliability",
            "tags": ["availability", "reliability", "sre"],
            "ai_summary": "Availability measures the fraction of time a system is usable; reliability measures correct continuous operation over time. Both drive redundancy, failover, and error-budget design.",
            "core": "Availability is uptime from the client’s perspective (successful requests / total requests over a window). Reliability is the probability the system performs its required function without failure for a period. The problem they solve is designing for failure so users still get correct service within agreed SLOs.",
            "architecture": "1. Define SLIs (latency, error rate, freshness) and SLOs.\n2. Remove single points of failure with redundancy (multi-AZ, replicas).\n3. Detect failure via health checks and route around bad nodes.\n4. Fail over with controlled promotion (leader election, DNS, LB).\n5. Recover with backups, replays, and runbooks; track error budget burn.",
            "advantages": [
                "Explicit SLOs turn vague “always up” goals into engineering trade-offs.",
                "Redundancy and automated failover reduce mean time to recovery (MTTR).",
            ],
            "disadvantages": [
                "Higher availability targets grow cost and operational complexity nonlinearly.",
                "Over-redundancy can hide bugs until rare correlated failures (region outage, bad deploy).",
            ],
            "alternatives": "Contrast with **disaster recovery (DR)** focus (RPO/RTO for rare catastrophes) and **graceful degradation** (serve partial features instead of hard availability of everything).",
            "guidelines": "**SHOULD** set SLOs per critical user journey and design failover for that budget. **SHOULD NOT** chase five-nines for internal tools where cost exceeds impact.",
        },
        {
            "slug": "latency-throughput",
            "topic": "Latency and Throughput",
            "tags": ["performance", "latency", "throughput"],
            "ai_summary": "Latency is the time to complete one request; throughput is how many requests complete per unit time. Systems must balance per-request speed against overall capacity.",
            "core": "Latency is end-to-end delay (often p50/p95/p99). Throughput is completed work per second (RPS, QPS, messages/sec). The engineering problem is meeting interactive responsiveness while maximizing useful work under resource limits.",
            "architecture": "1. Instrument request timelines (queue wait, compute, I/O, network).\n2. Reduce latency with caching, connection reuse, indexes, and locality.\n3. Increase throughput with concurrency, batching, pipelining, and parallelism.\n4. Watch queueing: Little’s Law links concurrency, latency, and throughput.\n5. Load-test to find the cliff where latency explodes as throughput saturates.",
            "advantages": [
                "Separating the two metrics prevents optimizing averages while ignoring tail latency.",
                "Batching and async pipelines can raise throughput without proportional hardware.",
            ],
            "disadvantages": [
                "Aggressive batching or queueing increases latency.",
                "Optimizing only p50 can leave p99 failures that dominate user experience.",
            ],
            "alternatives": "Compare **synchronous request/response** (low latency target) vs **async job processing** (high throughput, higher completion latency).",
            "guidelines": "**SHOULD** publish latency percentiles and throughput budgets for critical APIs. **SHOULD NOT** trade unbounded queues for “higher throughput” without backpressure and SLOs on wait time.",
        },
        {
            "slug": "cap-theorem",
            "topic": "CAP Theorem",
            "tags": ["distributed-systems", "consistency", "availability"],
            "ai_summary": "CAP states that during a network partition a distributed system must choose between consistency and availability. It frames datastore and replication trade-offs under failure.",
            "core": "The CAP theorem says that in the presence of a network **P**artition, a distributed data system cannot simultaneously guarantee strong **C**onsistency and **A**vailability. It solves the problem of clarifying which guarantees remain when nodes cannot communicate.",
            "architecture": "1. Replicate data across nodes for durability and locality.\n2. When a partition occurs, some nodes cannot confirm latest writes.\n3. CP systems refuse or block conflicting operations until quorum is restored.\n4. AP systems accept writes on both sides and reconcile later (version vectors, CRDTs, last-write-wins).\n5. Outside partitions, many systems optimize for both latency and consistency (see PACELC).",
            "advantages": [
                "Gives a shared vocabulary for datastore selection under failure modes.",
                "Forces explicit product decisions about stale reads vs write rejection.",
            ],
            "disadvantages": [
                "Often oversimplified as a permanent C-vs-A choice rather than a partition-time trade-off.",
                "Does not capture latency trade-offs when the network is healthy.",
            ],
            "alternatives": "**PACELC** extends CAP: if Partition then A/C else Latency vs Consistency. **BASE** (Basically Available, Soft state, Eventual consistency) is an AP-leaning design style vs ACID.",
            "guidelines": "**SHOULD** use CAP language when choosing multi-region databases and defining partition behavior. **SHOULD NOT** claim a system “ignores CAP”; document partition behavior and client-visible anomalies instead.",
        },
        {
            "slug": "pacelc",
            "topic": "PACELC Theorem",
            "tags": ["distributed-systems", "consistency", "latency"],
            "ai_summary": "PACELC extends CAP: under partition choose Availability or Consistency; else choose Latency or Consistency. It explains why strongly consistent systems pay latency even when healthy.",
            "core": "PACELC says: if there is a **P**artition, trade **A** vs **C**; **E**lse trade **L**atency vs **C**onsistency. It solves the blind spot in CAP by explaining normal-operation cost of cross-node coordination.",
            "architecture": "1. Healthy path: synchronous replication or quorum reads/writes add RTT for stronger consistency.\n2. Weaker consistency allows local reads/writes with lower latency.\n3. On partition: CP path blocks; AP path continues with divergence.\n4. Tunable systems (e.g., quorum R + W) let operators slide along the L/C axis per operation.",
            "advantages": [
                "Better mental model for multi-AZ and multi-region latency costs.",
                "Supports per-query consistency tuning instead of one global choice.",
            ],
            "disadvantages": [
                "More knobs increase misconfiguration risk.",
                "Teams may still under-specify client-visible consistency expectations.",
            ],
            "alternatives": "Plain **CAP** for partition-only discussions; **consistency models** (linearizability, causal, eventual) for precise semantics.",
            "guidelines": "**SHOULD** document both partition mode and healthy-path latency/consistency for shared stores. **SHOULD NOT** force global strong consistency for every read when local/eventual reads meet the product need.",
        },
        {
            "slug": "consistency-models",
            "topic": "Consistency Models",
            "tags": ["consistency", "distributed-systems", "database"],
            "ai_summary": "Consistency models define which orderings and visibilities of reads/writes clients may observe. They range from linearizability to eventual consistency and guide API and datastore design.",
            "core": "A consistency model is a contract for how concurrent and distributed operations appear to clients. Strong models (linearizability, sequential consistency) make systems behave like a single copy; weaker models (causal, eventual, read-your-writes) allow more performance and availability. They solve ambiguous “is this data correct?” questions across replicas.",
            "architecture": "1. Client issues reads/writes to one or more replicas.\n2. Replication protocol propagates updates (sync/async, quorum, primary-backup).\n3. Model determines when a write becomes visible and whether stale reads are allowed.\n4. Clients may use session guarantees, fencing tokens, or etags to narrow anomalies.\n5. Conflict resolution runs when concurrent writes diverge under weak models.",
            "advantages": [
                "Precise models enable correct application reasoning and testing.",
                "Weaker models unlock lower latency and higher availability.",
            ],
            "disadvantages": [
                "Weak models introduce subtle anomalies (lost updates, stale reads, non-monotonic reads).",
                "Strong models increase coordination cost and reduce availability under partition.",
            ],
            "alternatives": "Compare **linearizability** (strongest practical single-object model) vs **eventual consistency** (AP-friendly). **Causal consistency** sits in between for many collaborative apps.",
            "guidelines": "**SHOULD** pick the weakest model that still preserves invariants (payments need stronger guarantees than like-counters). **SHOULD NOT** mix ad-hoc caches with a strongly consistent DB without defining freshness rules.",
        },
        {
            "slug": "acid-vs-base",
            "topic": "ACID vs BASE",
            "tags": ["database", "consistency", "transactions"],
            "ai_summary": "ACID emphasizes transactional correctness on a single system of record; BASE emphasizes availability and soft state with eventual consistency. Choosing between them shapes data integrity vs scale.",
            "core": "ACID (Atomicity, Consistency, Isolation, Durability) describes traditional transactional guarantees. BASE (Basically Available, Soft state, Eventual consistency) describes designs that prioritize availability and partition tolerance with deferred reconciliation. The problem is matching integrity needs to distribution and scale constraints.",
            "architecture": "1. ACID path: begin transaction, apply multiple row changes under a concurrency control protocol, commit/abort atomically.\n2. BASE path: accept writes quickly, propagate asynchronously, resolve conflicts with application logic or CRDTs.\n3. Hybrid systems use local ACID transactions plus eventual cross-service propagation (outbox, sagas).",
            "advantages": [
                "ACID simplifies correctness for financial and inventory invariants.",
                "BASE enables global scale and high write availability.",
            ],
            "disadvantages": [
                "Distributed ACID is expensive and often unavailable across services.",
                "BASE shifts complexity into conflict handling and user-visible lag.",
            ],
            "alternatives": "**Sagas** and **transactional outbox** provide cross-service workflows without distributed 2PC. **CQRS** separates strongly consistent write models from eventually consistent read models.",
            "guidelines": "**SHOULD** keep hard money/inventory invariants inside one ACID boundary when possible. **SHOULD NOT** force distributed 2PC across microservices for convenience—prefer explicit eventual workflows.",
        },
    ],
    "networking": [
        {
            "slug": "dns",
            "topic": "DNS (Domain Name System)",
            "tags": ["networking", "discovery", "routing"],
            "ai_summary": "DNS maps human-readable names to addresses and service endpoints. It is foundational for routing, failover, and traffic steering across regions.",
            "core": "DNS is a hierarchical distributed lookup system that resolves names to records (A/AAAA, CNAME, MX, TXT, SRV). Beyond hostname lookup, it solves service discovery and coarse traffic control (failover, weighted/geo routing).",
            "architecture": "1. Client queries a recursive resolver.\n2. Resolver walks root → TLD → authoritative nameservers.\n3. Response is cached according to TTL.\n4. Application connects to returned IPs; load balancers or anycast may sit behind those names.\n5. Health-checked failover DNS updates or switches records when endpoints fail.",
            "advantages": [
                "Universal, highly cached, and operationally familiar.",
                "Enables blue/green and multi-region steering without client code changes.",
            ],
            "disadvantages": [
                "TTL and client caching delay failover.",
                "DNS is not a fine-grained load balancer or auth layer.",
            ],
            "alternatives": "**Service discovery** (Consul, Kubernetes DNS/Endpoints) for internal mesh; **anycast IP** for network-layer failover without waiting on DNS TTLs.",
            "guidelines": "**SHOULD** use short-enough TTLs for failover-critical names and health-checked DNS where supported. **SHOULD NOT** rely on DNS alone for fast L7 load shedding or per-request routing.",
        },
        {
            "slug": "load-balancing",
            "topic": "Load Balancing",
            "tags": ["networking", "scaling", "traffic"],
            "ai_summary": "Load balancers distribute traffic across multiple backends to improve capacity and availability. Algorithms and health checks determine fairness and failover behavior.",
            "core": "A load balancer (LB) fronts a pool of instances and selects a healthy target for each connection or request. It solves uneven load, single-instance limits, and seamless replacement of backends.",
            "architecture": "1. Client connects to the LB VIP/hostname.\n2. LB terminates or forwards L4/L7 traffic.\n3. Selection algorithm chooses a backend (round-robin, least-conn, hash, weighted).\n4. Health checks remove failing targets.\n5. Optional sticky sessions, TLS termination, retries, and circuit breaking apply.",
            "advantages": [
                "Enables horizontal scale and rolling deploys.",
                "Central place for TLS, health checks, and basic traffic policy.",
            ],
            "disadvantages": [
                "LB can become a bottleneck or SPOF if not itself redundant.",
                "Sticky sessions hinder perfect scale-out and failover.",
            ],
            "alternatives": "**Client-side load balancing** (service mesh / gRPC balancers) and **DNS round-robin** (simpler but weaker health awareness).",
            "guidelines": "**SHOULD** put redundant LBs in front of stateless services with active health checks. **SHOULD NOT** use session stickiness unless state cannot be externalized.",
        },
        {
            "slug": "reverse-proxy",
            "topic": "Reverse Proxy",
            "tags": ["networking", "edge", "security"],
            "ai_summary": "A reverse proxy accepts client requests and forwards them to internal servers, adding TLS, caching, routing, and shielding. It is the usual edge entry to application tiers.",
            "core": "A reverse proxy sits in front of origin servers on behalf of clients. Unlike a forward proxy (client-chosen), clients target the proxy’s public endpoint. It solves TLS termination, request routing, compression, and hiding internal topology.",
            "architecture": "1. Client sends HTTPS to the proxy.\n2. Proxy terminates TLS, applies WAF/auth/rate limits as configured.\n3. Routes by path/host to upstream services.\n4. May cache responses or buffer slow clients.\n5. Returns the upstream response with added headers (request IDs, cache status).",
            "advantages": [
                "Consolidates cross-cutting edge concerns.",
                "Simplifies certificate management and origin protection.",
            ],
            "disadvantages": [
                "Misrouting or buffer settings can amplify outages.",
                "Extra hop adds latency if not co-located carefully.",
            ],
            "alternatives": "**API gateway** (API-product focused policies) and **service mesh sidecars** (east-west traffic policy instead of north-south edge).",
            "guidelines": "**SHOULD** terminate public TLS at a reverse proxy/CDN tier. **SHOULD NOT** expose app containers directly to the internet without an edge proxy in normal deployments.",
        },
        {
            "slug": "cdn",
            "topic": "Content Delivery Network (CDN)",
            "tags": ["networking", "caching", "latency"],
            "ai_summary": "A CDN caches and serves content from edge locations close to users to cut latency and origin load. It is primary for static assets and increasingly for dynamic edge logic.",
            "core": "A CDN is a geographically distributed cache/proxy network. Users hit a nearby PoP; cache hits never reach origin. It solves long-haul latency, origin overload, and some DDoS absorption for cacheable content.",
            "architecture": "1. DNS/anycast sends the client to a nearby PoP.\n2. PoP checks cache keyed by URL/headers.\n3. On miss, PoP fetches from origin (or mid-tier), stores per TTLs/cache-control.\n4. Invalidation/purge APIs remove stale objects after deploys.\n5. Optional edge compute runs lightweight request logic.",
            "advantages": [
                "Dramatically lowers TTFB for static and semi-static content.",
                "Shields origin from traffic spikes.",
            ],
            "disadvantages": [
                "Cache invalidation complexity and stale content risk.",
                "Dynamic personalized content often bypasses or fragments the cache.",
            ],
            "alternatives": "**App-level caching** (Redis) for personalized data; **multi-region active-active origins** for uncacheable dynamic APIs.",
            "guidelines": "**SHOULD** put fingerprinted static assets on a CDN with long TTL. **SHOULD NOT** cache authenticated private responses at shared edges without careful cache-key and security design.",
        },
        {
            "slug": "api-gateway",
            "topic": "API Gateway",
            "tags": ["networking", "apis", "microservices"],
            "ai_summary": "An API gateway is a single entry point that routes and polices client API calls to backend services. It centralizes auth, rate limits, and request aggregation for external APIs.",
            "core": "An API gateway fronts one or more backend services for external (and sometimes internal) clients. It solves the problem of duplicating auth, routing, transformation, and monetization concerns across every microservice.",
            "architecture": "1. Client calls gateway endpoint.\n2. Gateway authenticates/authorizes, applies rate limits and schemas.\n3. Routes to the owning service(s); may aggregate BFF-style fan-out.\n4. Transforms protocols/payloads if needed.\n5. Emits metrics/logs/traces for the external API surface.",
            "advantages": [
                "Consistent edge policy for a public API program.",
                "Hides internal service topology and versions.",
            ],
            "disadvantages": [
                "Risk of a bloated “god gateway” with business logic.",
                "Extra hop and operational dependency for all traffic.",
            ],
            "alternatives": "**Reverse proxy + service mesh** for simpler routing; **Backend for Frontend (BFF)** per client type instead of one universal gateway aggregator.",
            "guidelines": "**SHOULD** keep gateways focused on cross-cutting API concerns. **SHOULD NOT** implement core domain business rules in the gateway.",
        },
        {
            "slug": "rate-limiting",
            "topic": "Rate Limiting",
            "tags": ["networking", "reliability", "traffic"],
            "ai_summary": "Rate limiting caps how many requests a client can make in a time window to protect shared resources. Algorithms include token bucket, leaky bucket, and sliding windows.",
            "core": "Rate limiting enforces quotas per key (IP, user, API key, tenant). It solves noisy-neighbor, abuse, and overload problems by shedding excess traffic early.",
            "architecture": "1. Identify a partition key for the client/tenant.\n2. On each request, consult a counter/bucket store (local or Redis).\n3. Algorithm decides allow vs reject (token bucket, fixed/sliding window, concurrency limit).\n4. Return 429 with retry-after when limited.\n5. Optionally apply different limits per endpoint and tier.",
            "advantages": [
                "Protects downstream databases and third-party quotas.",
                "Creates fair multi-tenant behavior.",
            ],
            "disadvantages": [
                "Distributed counters add latency and eventual inaccuracy.",
                "Poor key design can lock out NAT-shared users or miss abusive actors.",
            ],
            "alternatives": "**Load shedding** based on server saturation; **admission control / concurrency limits** that ignore wall-clock rate and focus on in-flight work.",
            "guidelines": "**SHOULD** rate-limit public and expensive endpoints with clear client feedback. **SHOULD NOT** use only global process-local limits in multi-instance deployments without a shared store or coordinated policy.",
        },
        {
            "slug": "tls-termination",
            "topic": "TLS Termination",
            "tags": ["networking", "security", "edge"],
            "ai_summary": "TLS termination decrypts HTTPS at an edge component so backends can speak plain HTTP on a trusted network. It centralizes certificates and reduces app crypto overhead.",
            "core": "TLS termination is decrypting TLS at a proxy/load balancer. Optionally, re-encrypt to upstream (TLS passthrough or TLS bridging). It solves certificate management complexity and CPU cost on every app instance.",
            "architecture": "1. Client completes TLS handshake with the terminator.\n2. Terminator presents certs (often automated via ACME).\n3. Decrypted request is forwarded on a private network (HTTP or mTLS).\n4. Response is encrypted back to the client.\n5. Certificate rotation happens at the edge without app redeploys.",
            "advantages": [
                "Centralized cert lifecycle and cipher policy.",
                "Lower CPU on application pods for high-QPS HTTP.",
            ],
            "disadvantages": [
                "Traffic is plaintext behind the terminator unless re-encrypted.",
                "Terminator compromise exposes request contents.",
            ],
            "alternatives": "**TLS passthrough** to apps (end-to-end encrypt) and **mTLS service mesh** for east-west encryption after edge termination.",
            "guidelines": "**SHOULD** terminate public TLS at the edge and use mTLS or private networking inland as required by threat model. **SHOULD NOT** run expired certs or shared wildcard secrets in every microservice.",
        },
    ],
    "data-storage": [
        {
            "slug": "sql-databases",
            "topic": "Relational (SQL) Databases",
            "tags": ["database", "storage", "transactions"],
            "ai_summary": "Relational databases store structured data in tables with schemas, SQL queries, and ACID transactions. They are the default system of record for strong invariants and complex queries.",
            "core": "SQL databases organize data into normalized tables with declared schemas, constraints, and joins. They solve consistent multi-row updates and ad-hoc relational querying under a transactional model.",
            "architecture": "1. Client begins a transaction and issues SQL.\n2. Query planner uses indexes/statistics to access rows.\n3. Concurrency control (locking/MVCC) isolates concurrent transactions.\n4. WAL/redo ensures durability on commit.\n5. Replicas may serve reads; primary typically handles writes.",
            "advantages": [
                "Strong consistency and mature tooling for integrity constraints.",
                "Expressive queries and joins without denormalizing everything upfront.",
            ],
            "disadvantages": [
                "Horizontal write scaling is hard without sharding.",
                "Rigid schemas and join-heavy designs can become bottlenecks at extreme scale.",
            ],
            "alternatives": "**NoSQL document/KV stores** for flexible schemas and simpler scale-out; **NewSQL / distributed SQL** for relational semantics with sharding.",
            "guidelines": "**SHOULD** use relational DBs for core business entities with rich relationships and invariants. **SHOULD NOT** use a single monolithic SQL database as an unbounded event dump or analytics warehouse.",
        },
        {
            "slug": "nosql-databases",
            "topic": "NoSQL Databases",
            "tags": ["database", "storage", "scaling"],
            "ai_summary": "NoSQL covers document, key-value, wide-column, and graph stores optimized for scale and flexible models. They trade some relational features for partition-friendly access patterns.",
            "core": "NoSQL databases abandon or relax the classic relational model to optimize specific access patterns, availability, or horizontal scale. They solve problems where schema flexibility, massive key lookups, or partition-local operations dominate.",
            "architecture": "1. Model data around query patterns (document per aggregate, KV per key, wide rows).\n2. Partition by key across nodes (often consistent hashing).\n3. Replicate partitions with configurable consistency.\n4. Application handles joins/denormalization that SQL would do server-side.\n5. Secondary indexes or search engines complement primary access paths.",
            "advantages": [
                "Easier horizontal scale for simple key-centric workloads.",
                "Flexible documents speed product iteration for evolving payloads.",
            ],
            "disadvantages": [
                "Less built-in multi-record transaction support in many systems.",
                "Poor access-pattern design causes expensive scans and hot partitions.",
            ],
            "alternatives": "**Relational SQL** for complex joins/invariants; **search engines** (OpenSearch/Elastic) when full-text relevance is the primary need.",
            "guidelines": "**SHOULD** choose NoSQL when access patterns are clear and partition keys are well understood. **SHOULD NOT** pick NoSQL only “for scale” before measuring SQL limits and modeling query paths.",
        },
        {
            "slug": "database-indexing",
            "topic": "Database Indexing",
            "tags": ["database", "performance", "storage"],
            "ai_summary": "Indexes are auxiliary data structures that speed lookups and sorting at the cost of write overhead and storage. B-trees and hash indexes are the most common forms.",
            "core": "An index maps keyed values to row locations so the engine avoids full table scans. Indexing solves high-latency queries on large tables by trading extra storage and slower writes for faster reads.",
            "architecture": "1. Declare indexes on selective columns or composites matching WHERE/ORDER BY/JOIN keys.\n2. On write, the engine updates table heap/clustered structure and each secondary index.\n3. Planner chooses index scan, bitmap scan, or sequential scan by cost.\n4. Covering indexes can satisfy queries without touching base rows.\n5. Monitor bloat, unused indexes, and write amplification.",
            "advantages": [
                "Orders-of-magnitude faster point lookups and range scans when selective.",
                "Enforces uniqueness constraints.",
            ],
            "disadvantages": [
                "Every extra index slows inserts/updates/deletes.",
                "Wrong indexes waste space and can mislead the planner.",
            ],
            "alternatives": "**Materialized views** for expensive prejoined read models; **application-level caches** for ultra-hot keys.",
            "guidelines": "**SHOULD** index foreign keys and high-selectivity filter columns used in production queries. **SHOULD NOT** create many overlapping indexes “just in case”—prove need with EXPLAIN and slow-query logs.",
        },
        {
            "slug": "database-replication",
            "topic": "Database Replication",
            "tags": ["database", "availability", "replication"],
            "ai_summary": "Replication copies data to multiple database nodes for high availability and read scale. Primary-replica and multi-primary topologies define write ownership and lag behavior.",
            "core": "Replication keeps multiple copies of a dataset in sync. It solves durability (survive node loss), read scaling, and geographic locality, at the cost of lag and failover complexity.",
            "architecture": "1. Primary accepts writes and records them to a log (WAL/binlog).\n2. Replicas apply the log asynchronously or synchronously.\n3. Reads may be routed to replicas with freshness awareness.\n4. On primary failure, orchestrator promotes a replica and redirects clients.\n5. Split-brain prevention uses fencing, quorum, or STONITH-style controls.",
            "advantages": [
                "Fast failover and improved read throughput.",
                "Geographic replicas reduce read latency for distant users.",
            ],
            "disadvantages": [
                "Async replicas serve stale data; sync replication adds write latency.",
                "Failover bugs can cause data loss or dual writes.",
            ],
            "alternatives": "**Sharding** for write scale-out; **multi-region distributed databases** with consensus per partition.",
            "guidelines": "**SHOULD** run at least one replica for production systems of record with tested failover. **SHOULD NOT** silently send strongly consistency-sensitive reads to lagged replicas.",
        },
        {
            "slug": "database-sharding",
            "topic": "Database Sharding",
            "tags": ["database", "scaling", "partitioning"],
            "ai_summary": "Sharding partitions data across multiple database instances by a shard key to scale writes and storage. It introduces cross-shard complexity for queries and transactions.",
            "core": "Sharding (horizontal partitioning) splits rows into subsets stored on different nodes. It solves single-primary write and storage ceilings when vertical scale and read replicas are insufficient.",
            "architecture": "1. Choose a shard key with even distribution and locality for common queries.\n2. Router or client embeds key → shard mapping (range, hash, directory).\n3. Single-shard queries go to one node; scatter-gather handles cross-shard reads.\n4. Resharding migrates ranges/buckets as data grows.\n5. Cross-shard transactions use sagas/2PC or are avoided by design.",
            "advantages": [
                "Scales write throughput and dataset size beyond one machine.",
                "Fault isolation: one shard’s outage need not take down all data.",
            ],
            "disadvantages": [
                "Cross-shard joins and transactions become hard.",
                "Hot keys/shards and resharding are operationally painful.",
            ],
            "alternatives": "**Vertical partitioning** (split tables/services by domain); **distributed SQL** that manages shards under a relational API.",
            "guidelines": "**SHOULD** shard only after proving a single primary (plus replicas) cannot meet write/storage needs. **SHOULD NOT** pick high-cardinality random keys that destroy locality for the main query paths.",
        },
        {
            "slug": "consistent-hashing",
            "topic": "Consistent Hashing",
            "tags": ["distributed-systems", "partitioning", "caching"],
            "ai_summary": "Consistent hashing maps keys to nodes on a ring so that adding/removing nodes moves only a small fraction of keys. It underpins distributed caches and many shard routers.",
            "core": "Consistent hashing places nodes and keys on a circular hash space; a key belongs to the next node clockwise (often with virtual nodes). It solves massive remapping when cluster membership changes under naive modulo hashing.",
            "architecture": "1. Hash each node (and vnodes) onto the ring.\n2. Hash the key; walk clockwise to find the owner.\n3. Optionally replicate to the next N distinct nodes for durability.\n4. On node add/remove, only neighboring key ranges move.\n5. Clients or proxies keep a membership view and refresh on changes.",
            "advantages": [
                "Minimizes data movement during scale events.",
                "Supports heterogeneous node capacity via vnode weighting.",
            ],
            "disadvantages": [
                "Without vnodes, load can be uneven.",
                "Membership churn and gossip delays can cause temporary misrouting.",
            ],
            "alternatives": "**Range partitioning** (ordered keys, good for scans) and **rendezvous hashing (HRW)** as another minimal-remapping scheme.",
            "guidelines": "**SHOULD** use consistent hashing for distributed caches and partitioners with elastic node counts. **SHOULD NOT** ignore hot-key mitigation—hashing alone does not fix popularity skew.",
        },
        {
            "slug": "caching",
            "topic": "Caching",
            "tags": ["caching", "performance", "latency"],
            "ai_summary": "Caching stores frequently accessed data in a fast layer to reduce latency and backend load. Designs include cache-aside, read-through, write-through, and write-back.",
            "core": "A cache keeps a subset of data closer/faster than the source of truth. It solves repeated expensive reads (DB, CPU, network) by trading freshness and memory for speed.",
            "architecture": "1. Client requests data.\n2. Cache-aside: app checks cache → on miss loads DB → populates cache.\n3. Read-through/write-through embed load/store in the cache library.\n4. TTLs and explicit invalidation bound staleness.\n5. Eviction (LRU/LFU/etc.) reclaims memory under pressure.",
            "advantages": [
                "Major latency and cost wins for read-heavy workloads.",
                "Protects databases from hot-key stampedes when paired with locking/singleflight.",
            ],
            "disadvantages": [
                "Stale reads and invalidation bugs cause subtle correctness issues.",
                "Cache stampedes and thundering herds can amplify outages.",
            ],
            "alternatives": "**CDN caching** for public HTTP assets; **materialized DB views** for complex but somewhat fresh query results; **bigger/faster primary DB** when hit rates would be poor.",
            "guidelines": "**SHOULD** cache read-heavy, idempotent data with explicit TTL/invalidation ownership. **SHOULD NOT** cache strongly transactional balances without a defined consistency story.",
        },
        {
            "slug": "cache-eviction",
            "topic": "Cache Eviction Policies",
            "tags": ["caching", "memory", "performance"],
            "ai_summary": "Eviction policies decide which cache entries to drop when memory is full. LRU, LFU, FIFO, and TTL-based strategies optimize different access patterns.",
            "core": "When a cache reaches capacity, an eviction policy selects victims to delete. The problem is maximizing hit rate under limited memory for a given workload shape.",
            "architecture": "1. Insert/update entries with metadata (recency, frequency, size, expiry).\n2. On memory pressure, policy ranks candidates (LRU list, LFU counters, random, SLRU/ARC hybrids).\n3. Evict until allocation succeeds.\n4. TTL expiry may remove entries independently of capacity.\n5. Metrics track hit rate, evictions, and scan resistance.",
            "advantages": [
                "Good policy fit can double effective hit rate without more RAM.",
                "TTL eviction bounds staleness even for hot keys.",
            ],
            "disadvantages": [
                "LRU fails on scans that churn the working set.",
                "LFU can retain stale popular keys too long without aging.",
            ],
            "alternatives": "**Admission policies** (TinyLFU) that refuse low-value inserts; **sizing/partitioning caches** per workload instead of one shared policy.",
            "guidelines": "**SHOULD** pick LRU/ARC-like defaults for general web app caches and measure hit rate. **SHOULD NOT** rely on unbounded caches in process memory without eviction and monitoring.",
        },
        {
            "slug": "object-storage",
            "topic": "Object Storage",
            "tags": ["storage", "blob", "scalability"],
            "ai_summary": "Object storage persists immutable blobs addressed by keys in a flat namespace, accessed over HTTP APIs. It excels at durable, cheap, large-scale unstructured data.",
            "core": "Object stores (S3-compatible) manage objects with key, metadata, and value—not POSIX files or DB rows. They solve durable storage of media, backups, lake files, and large artifacts at massive scale.",
            "architecture": "1. Client PUTs an object to a bucket/key with optional encryption and metadata.\n2. Store erasure-codes or replicates across disks/AZs.\n3. GET/LIST via HTTP; pre-signed URLs allow direct client transfer.\n4. Lifecycle policies tier to colder storage or expire objects.\n5. Event notifications can trigger downstream processing.",
            "advantages": [
                "Virtually unlimited scale with high durability classes.",
                "Cheap for large sequential data vs block/DB storage.",
            ],
            "disadvantages": [
                "Higher latency than local disk; not ideal for tiny chatty I/O.",
                "No rich partial-update semantics like a filesystem or database.",
            ],
            "alternatives": "**Block storage** for databases/VMs; **distributed filesystems** when POSIX semantics are required.",
            "guidelines": "**SHOULD** store user uploads, exports, and data-lake files in object storage. **SHOULD NOT** use object storage as a low-latency mutable primary database.",
        },
        {
            "slug": "oltp-vs-olap",
            "topic": "OLTP vs OLAP",
            "tags": ["database", "analytics", "storage"],
            "ai_summary": "OLTP systems serve transactional operational workloads; OLAP systems serve analytical scans and aggregations. Separating them protects production latency while enabling BI.",
            "core": "OLTP (Online Transaction Processing) optimizes many small reads/writes with indexes and ACID. OLAP (Online Analytical Processing) optimizes large scans, columnar storage, and aggregations. The problem is that analytics queries can destroy OLTP latency if colocated.",
            "architecture": "1. OLTP DB handles application transactions.\n2. Changes stream via CDC/ETL into a warehouse/lakehouse.\n3. OLAP engine stores columnar, partitioned data.\n4. BI tools query replicas/warehouses, not the primary OLTP node.\n5. SLAs differ: OLTP is latency-sensitive; OLAP is throughput/scan-sensitive.",
            "advantages": [
                "Isolates analytical load from user-facing transactions.",
                "Each system can use the optimal storage engine.",
            ],
            "disadvantages": [
                "Data pipelines introduce lag and operational surface.",
                "Two models of the truth can drift without governance.",
            ],
            "alternatives": "**HTAP** databases attempting both; **read replicas** as a lightweight but limited analytics offload.",
            "guidelines": "**SHOULD** offload heavy reporting from primary OLTP early. **SHOULD NOT** run unbounded table scans on production primaries for dashboards.",
        },
        {
            "slug": "bloom-filters",
            "topic": "Bloom Filters",
            "tags": ["algorithms", "caching", "storage"],
            "ai_summary": "A Bloom filter is a probabilistic set membership structure with false positives but no false negatives. It cheaply skips unnecessary disk or network lookups.",
            "core": "A Bloom filter hashes elements into a bit array. Querying may say “maybe present” or “definitely absent.” It solves expensive negative lookups (cache miss → DB) by quickly ruling out absences.",
            "architecture": "1. Allocate an m-bit array and k hash functions sized for expected n and false-positive rate.\n2. On insert, set k bits.\n3. On lookup, check k bits—all set means maybe present; any clear means absent.\n4. Used before DB/SSTable access or as a cache admission hint.\n5. Counting/scalable variants exist but cost more memory.",
            "advantages": [
                "Tiny memory footprint for huge keyspaces.",
                "Guarantees no false negatives for standard filters.",
            ],
            "disadvantages": [
                "False positives cause extra work.",
                "Cannot delete entries in the classic non-counting filter.",
            ],
            "alternatives": "**Cuckoo filters** (support delete, different memory trade-offs); **exact hash sets** when memory allows zero false positives.",
            "guidelines": "**SHOULD** use Bloom filters in front of expensive existence checks at scale (LSM reads, large sparse keyspaces). **SHOULD NOT** use them where false positives are unsafe without a definitive follow-up check.",
        },
    ],
    "distributed-systems": [
        {
            "slug": "message-queues",
            "topic": "Message Queues",
            "tags": ["messaging", "async", "decoupling"],
            "ai_summary": "Message queues buffer work between producers and consumers to decouple services and smooth load. They enable asynchronous processing with retry and durability options.",
            "core": "A message queue stores messages until consumers process them. It solves tight coupling, traffic spikes, and reliability of background work by persisting tasks independently of producer uptime.",
            "architecture": "1. Producer sends a message to a queue/topic partition.\n2. Broker persists (memory/disk) and acknowledges per durability settings.\n3. Consumer pulls or receives push delivery.\n4. On success, ack/commit offset; on failure, retry or dead-letter.\n5. Scaling adds consumers within a competing-consumer group.",
            "advantages": [
                "Smooths spikes and isolates failures between services.",
                "Enables retries and durable async workflows.",
            ],
            "disadvantages": [
                "End-to-end latency increases vs synchronous calls.",
                "Poison messages, ordering, and exactly-once semantics add complexity.",
            ],
            "alternatives": "**Pub/sub topics** for broadcast; **synchronous RPC** when the caller must fail/succeed inline; **workflow engines** for long-running orchestrations.",
            "guidelines": "**SHOULD** queue non-interactive work (emails, image processing, webhooks). **SHOULD NOT** hide critical user-facing failures in an unmonitored queue without SLAs and DLQs.",
        },
        {
            "slug": "pub-sub",
            "topic": "Publish-Subscribe Messaging",
            "tags": ["messaging", "event-driven", "decoupling"],
            "ai_summary": "Pub/sub delivers each published event to multiple independent subscribers. It enables fan-out event-driven architectures without producers knowing consumers.",
            "core": "In pub/sub, publishers emit events to a topic; any number of subscribers receive copies (or partition shares). It solves one-to-many notification and independent evolution of consumer groups.",
            "architecture": "1. Publisher writes an event to a topic.\n2. Broker retains events per policy (duration/size).\n3. Each subscription/consumer group tracks its own offset/cursor.\n4. Consumers process independently and scale per group.\n5. Schema registry/contracts reduce breaking changes.",
            "advantages": [
                "Producers stay decoupled from consumer count and logic.",
                "Multiple teams can react to the same domain events.",
            ],
            "disadvantages": [
                "Harder to reason about global ordering and failure cascades.",
                "Fan-out multiplies downstream load.",
            ],
            "alternatives": "**Point-to-point queues** for single-worker task distribution; **webhook callbacks** for simple external integrations.",
            "guidelines": "**SHOULD** use pub/sub for domain events many systems must observe. **SHOULD NOT** treat pub/sub as a queryable source of truth without retention and compaction strategy.",
        },
        {
            "slug": "event-driven-architecture",
            "topic": "Event-Driven Architecture",
            "tags": ["architecture", "event-driven", "messaging"],
            "ai_summary": "Event-driven architecture coordinates services through events representing state changes rather than direct synchronous calls. It improves decoupling and scalability of workflows.",
            "core": "EDA structures systems so components communicate primarily via events (“order placed”) instead of commanding each other synchronously. It solves brittle point-to-point coupling and enables asynchronous reactions at scale.",
            "architecture": "1. Service commits state change and emits an event (ideally via outbox).\n2. Broker distributes the event.\n3. Consumers update their own state, trigger processes, or emit further events.\n4. Choreography lets each service react; orchestration uses a workflow leader.\n5. Observability requires correlation IDs across the event chain.",
            "advantages": [
                "Loose coupling and independent deployability.",
                "Natural fit for audit logs and real-time reactions.",
            ],
            "disadvantages": [
                "Debugging distributed flows is harder.",
                "Eventual consistency requires careful UX and idempotency.",
            ],
            "alternatives": "**Request-driven microservices** (sync APIs); **modular monolith** with in-process domain events when distribution is unnecessary.",
            "guidelines": "**SHOULD** adopt EDA for cross-team workflows that can tolerate async completion. **SHOULD NOT** event-wash simple CRUD apps into unreadable webs of topics.",
        },
        {
            "slug": "consensus",
            "topic": "Consensus Algorithms (Raft / Paxos)",
            "tags": ["distributed-systems", "consensus", "coordination"],
            "ai_summary": "Consensus protocols let distributed nodes agree on a single value or log despite failures. Raft and Paxos underpin strongly consistent coordination and replicated state machines.",
            "core": "Consensus algorithms ensure a cluster agrees on operations (usually an ordered log) even if some nodes crash or messages delay. They solve leader election, configuration changes, and consistent replication for control planes and databases.",
            "architecture": "1. Nodes elect a leader with quorum votes.\n2. Leader proposes log entries to followers.\n3. Entry commits once a majority persists it.\n4. State machine applies committed entries in order.\n5. Minority partitions cannot commit conflicting history.",
            "advantages": [
                "Strong consistency and clear failure semantics under majority rule.",
                "Foundation for reliable metadata stores and failover.",
            ],
            "disadvantages": [
                "Majority requirement limits availability under large outages.",
                "Cross-region consensus adds significant latency.",
            ],
            "alternatives": "**Primary-backup with async replication** (weaker durability); **gossip CRDTs** when conflict-free eventual merges suffice.",
            "guidelines": "**SHOULD** rely on consensus-backed stores for cluster metadata, locks, and configuration. **SHOULD NOT** run chatty application data paths through a global consensus group.",
        },
        {
            "slug": "leader-election",
            "topic": "Leader Election",
            "tags": ["distributed-systems", "coordination", "availability"],
            "ai_summary": "Leader election chooses one node to coordinate work such as writes or scheduling. It prevents conflicting primaries while allowing failover when the leader dies.",
            "core": "Leader election designates a single active coordinator among peers. It solves split responsibility problems (dual writes, duplicate schedulers) while enabling automatic failover.",
            "architecture": "1. Candidates race using consensus, locks (ZooKeeper/etcd), or gossip leases.\n2. Winner holds a lease/fencing token.\n3. Followers redirect writes or wait for tasks.\n4. On lease expiry/failure detection, a new election runs.\n5. Old leader must respect fencing to avoid split-brain actions.",
            "advantages": [
                "Simplifies single-writer and singleton job semantics.",
                "Enables automated failover without human intervention.",
            ],
            "disadvantages": [
                "False failure detection can thrash leadership.",
                "Without fencing, two leaders may briefly act (split-brain).",
            ],
            "alternatives": "**Leaderless quorum protocols** (Dynamo-style); **static primary** with manual failover for tiny systems.",
            "guidelines": "**SHOULD** elect leaders for singleton schedulers and primary-writer DBs with fencing tokens. **SHOULD NOT** build custom election on heartbeats alone without a quorum/lease store.",
        },
        {
            "slug": "quorum",
            "topic": "Quorum Reads and Writes",
            "tags": ["distributed-systems", "consistency", "replication"],
            "ai_summary": "Quorum systems require overlapping majorities of replicas for reads and writes so that the latest value is observed. Tunable R/W quorums balance latency and consistency.",
            "core": "With N replicas, a write quorum W and read quorum R such that R + W > N ensure read sets intersect write sets. Quorums solve the need for consistency without contacting every replica every time.",
            "architecture": "1. Client or coordinator sends a write to N replicas, waits for W acks.\n2. Reads query R replicas and pick the newest timestamp/version.\n3. Read repair or anti-entropy fixes lagging replicas.\n4. Sloppy quorums may write to hinted handoff nodes during failures.\n5. Operators tune N/R/W per latency and durability goals.",
            "advantages": [
                "Tunable consistency without full broadcast on every op.",
                "Survives minority replica failures.",
            ],
            "disadvantages": [
                "Higher R/W increases latency and reduces availability.",
                "Clock/version conflicts still need resolution rules.",
            ],
            "alternatives": "**Primary-backup** (all writes to leader); **full synchronous replication to all nodes** (simpler but less available).",
            "guidelines": "**SHOULD** use R + W > N for data that must not return arbitrarily stale values. **SHOULD NOT** assume W=1, R=1 is safe for critical financial state.",
        },
        {
            "slug": "gossip-protocol",
            "topic": "Gossip Protocols",
            "tags": ["distributed-systems", "membership", "networking"],
            "ai_summary": "Gossip protocols spread membership and state by peer-to-peer periodic exchanges. They provide scalable, eventually consistent cluster awareness.",
            "core": "In gossip (epidemic) protocols, nodes periodically exchange state with random peers until information converges. They solve membership, failure detection, and lightweight metadata propagation without a central broadcaster.",
            "architecture": "1. Each node maintains local membership/metadata.\n2. On an interval, pick a peer and push/pull digests.\n3. Differences are reconciled; version counters rise.\n4. Failure detectors mark suspects after missed gossips.\n5. Eventually, all reachable nodes converge on the same view.",
            "advantages": [
                "Scales to large clusters with low per-node fan-out.",
                "No single coordination server for basic membership.",
            ],
            "disadvantages": [
                "Convergence is eventual; views can temporarily disagree.",
                "Not ideal for strongly consistent configuration alone.",
            ],
            "alternatives": "**Centralized control plane** (Kubernetes API server); **consensus membership** for strong consistency at smaller scale.",
            "guidelines": "**SHOULD** use gossip for large-cluster membership and cache digests. **SHOULD NOT** rely on gossip alone for security-critical authorization data without authenticated, authenticated overlays and stronger stores.",
        },
        {
            "slug": "distributed-transactions",
            "topic": "Distributed Transactions (2PC)",
            "tags": ["transactions", "distributed-systems", "consistency"],
            "ai_summary": "Two-phase commit coordinates atomic commits across multiple participants. It provides all-or-nothing semantics at the cost of blocking and availability risks.",
            "core": "Distributed transactions make multiple resources commit or abort together. Two-phase commit (2PC) uses a prepare phase then a commit phase driven by a coordinator. It solves cross-database atomicity when a single local transaction is impossible.",
            "architecture": "1. Coordinator sends PREPARE to participants.\n2. Each participant votes YES (durably prepared) or NO.\n3. If all YES, coordinator sends COMMIT; else ABORT.\n4. Participants acknowledge final outcome.\n5. On coordinator crash, prepared participants may block until recovery.",
            "advantages": [
                "Strong atomicity across heterogeneous resources.",
                "Familiar ACID-like outcome for multi-resource updates.",
            ],
            "disadvantages": [
                "Blocking and poor availability under coordinator/participant failures.",
                "High latency from multiple round trips and locks held while prepared.",
            ],
            "alternatives": "**Sagas** (compensating transactions); **transactional outbox + async messaging** for eventual consistency across services.",
            "guidelines": "**SHOULD** avoid 2PC across microservices except rare tightly controlled cases. **SHOULD NOT** hold prepared locks across user-interactive network calls.",
        },
        {
            "slug": "saga-pattern",
            "topic": "Saga Pattern",
            "tags": ["transactions", "microservices", "event-driven"],
            "ai_summary": "Sagas manage multi-step business transactions with local commits plus compensating actions on failure. They replace distributed 2PC in microservice architectures.",
            "core": "A saga breaks a long-running business process into a sequence of local transactions. If a step fails, previously completed steps run compensations. It solves cross-service workflows without locking all resources in a distributed transaction.",
            "architecture": "1. Orchestrator (or choreography) starts step 1 local TX and emits success.\n2. Each subsequent service performs its local TX.\n3. On failure at step k, compensations for steps k-1…1 execute.\n4. State machine tracks progress and retries.\n5. Idempotent handlers make retries safe.",
            "advantages": [
                "High availability vs 2PC; no global locks.",
                "Fits natural business processes with explicit undo paths.",
            ],
            "disadvantages": [
                "Compensations are hard (and sometimes impossible) to design perfectly.",
                "Intermediate states are visible to users (eventual consistency).",
            ],
            "alternatives": "**2PC/TCC** for rare strong atomic needs; **single-service transaction** by consolidating the write boundary.",
            "guidelines": "**SHOULD** use sagas for cross-service orders, provisioning, and multi-step bookings. **SHOULD NOT** pretend compensations equal true ACID rollback for money movement without careful ledger design.",
        },
        {
            "slug": "idempotency",
            "topic": "Idempotency",
            "tags": ["reliability", "apis", "messaging"],
            "ai_summary": "Idempotency ensures repeating the same operation yields the same effect, enabling safe retries. It is essential for networks that may deliver requests more than once.",
            "core": "An idempotent operation can be applied multiple times without changing the result beyond the first application. It solves duplicate requests caused by retries, at-least-once messaging, and client double-submits.",
            "architecture": "1. Client sends an idempotency key with a write request.\n2. Server stores key → result in a durable table.\n3. Duplicates return the original result without re-applying side effects.\n4. Consumers of messages dedupe by event ID/offset.\n5. Keys expire after a safe retention window.",
            "advantages": [
                "Makes retries and failover safe.",
                "Prevents double charges and duplicate side effects.",
            ],
            "disadvantages": [
                "Requires durable dedupe storage and key discipline.",
                "Poorly chosen keys can collapse distinct operations together.",
            ],
            "alternatives": "**Exactly-once sinks** in stream processors (still usually rely on idempotent writes); **synchronous user confirmation** flows (insufficient alone on unreliable networks).",
            "guidelines": "**SHOULD** require idempotency keys on payment and create endpoints and make consumers idempotent. **SHOULD NOT** retry non-idempotent writes without dedupe.",
        },
        {
            "slug": "circuit-breaker",
            "topic": "Circuit Breaker",
            "tags": ["reliability", "resilience", "microservices"],
            "ai_summary": "A circuit breaker stops calling a failing dependency after an error threshold, then probes for recovery. It prevents cascading failures and thread exhaustion.",
            "core": "The circuit breaker pattern wraps remote calls with states: closed (normal), open (fail fast), half-open (trial requests). It solves cascading latency and resource pile-ups when a dependency is down.",
            "architecture": "1. Track success/failure rates for a dependency.\n2. Trip open when threshold exceeded; fail fast locally.\n3. After a timeout, allow limited half-open probes.\n4. On probe success, close; on failure, reopen.\n5. Combine with timeouts, bulkheads, and fallbacks.",
            "advantages": [
                "Protects caller resources during dependency outages.",
                "Gives dependencies time to recover.",
            ],
            "disadvantages": [
                "Mis-tuned thresholds cause flapping or prolonged outages.",
                "Fallbacks can return stale/wrong data if not designed carefully.",
            ],
            "alternatives": "**Timeouts + retries with budget** alone; **load shedding** at the callee; **hedged requests** for latency, not outages.",
            "guidelines": "**SHOULD** put circuit breakers on sync calls to unstable or third-party dependencies. **SHOULD NOT** retry aggressively against an open circuit.",
        },
        {
            "slug": "bulkhead",
            "topic": "Bulkhead Pattern",
            "tags": ["reliability", "isolation", "resilience"],
            "ai_summary": "Bulkheads isolate resources into compartments so failure in one area cannot consume all capacity. They limit blast radius across tenants, dependencies, or workloads.",
            "core": "Named after ship compartments, bulkheads partition threads, connections, queues, or clusters. They solve noisy-neighbor and shared-fate problems where one slow dependency starves everything.",
            "architecture": "1. Identify failure domains (per dependency, tenant, or endpoint group).\n2. Assign dedicated pools/limits (thread pools, connection pools, pod counts).\n3. Reject excess in one bulkhead without blocking others.\n4. Monitor utilization per compartment.\n5. Optionally isolate at infrastructure level (separate clusters/accounts).",
            "advantages": [
                "Contains resource exhaustion blasts.",
                "Preserves critical paths when noncritical paths overload.",
            ],
            "disadvantages": [
                "Idle capacity in one bulkhead cannot always help another (lower packing efficiency).",
                "More pools mean more tuning and ops complexity.",
            ],
            "alternatives": "**Global concurrency limits** (simpler, less isolation); **separate microservices/clusters** for hard isolation.",
            "guidelines": "**SHOULD** isolate thread/connection pools per critical dependency. **SHOULD NOT** share one unbounded executor across all outbound I/O.",
        },
        {
            "slug": "retry-backoff",
            "topic": "Retries and Exponential Backoff",
            "tags": ["reliability", "networking", "resilience"],
            "ai_summary": "Retries reattempt failed operations; exponential backoff spaces attempts to reduce overload. Jitter prevents synchronized retry storms.",
            "core": "Transient failures (network blips, 503s) often succeed on retry. Exponential backoff increases delay between attempts; jitter randomizes delays. Together they solve flaky networks without stampedes.",
            "architecture": "1. Classify errors as retryable vs permanent.\n2. Retry with capped exponential delays and jitter.\n3. Enforce max attempts and overall deadline.\n4. Propagate idempotency keys on write retries.\n5. Prefer client-side + server load shedding over infinite retries.",
            "advantages": [
                "Improves success rate under brief faults.",
                "Backoff/jitter protect recovering services.",
            ],
            "disadvantages": [
                "Retries amplify load during outages (retry storms).",
                "Can duplicate side effects without idempotency.",
            ],
            "alternatives": "**Fail fast + circuit breaker**; **hedged requests** for tail latency on idempotent reads; **async queues** that naturally retry.",
            "guidelines": "**SHOULD** retry idempotent reads and explicitly idempotent writes with budgets. **SHOULD NOT** blindly retry all 4xx errors or stack unbounded retries at every layer.",
        },
        {
            "slug": "backpressure",
            "topic": "Backpressure",
            "tags": ["reliability", "streaming", "traffic"],
            "ai_summary": "Backpressure signals upstream producers to slow down when consumers cannot keep up. It prevents unbounded queues and memory exhaustion.",
            "core": "Backpressure is flow control from a busy consumer toward producers. It solves the mismatch between produce rate and process rate that otherwise causes OOM or multi-minute lag.",
            "architecture": "1. Consumer monitors queue depth, lag, or in-flight limits.\n2. When saturated, it stops pulling, closes windows, or returns 429/503.\n3. Producers block, buffer with limits, or drop per policy.\n4. Protocols (TCP windows, reactive streams, gRPC) may carry credit-based control.\n5. Autoscale may add consumers before applying hard reject policies.",
            "advantages": [
                "Keeps systems stable under overload.",
                "Makes overload visible instead of hiding it in infinite buffers.",
            ],
            "disadvantages": [
                "Pushing back can propagate latency upstream to users.",
                "Requires coordinated policies across many services.",
            ],
            "alternatives": "**Unbounded buffering** (dangerous); **load shedding/dropping** oldest or newest data when freshness matters more than completeness.",
            "guidelines": "**SHOULD** bound all queues and define what happens at the limit. **SHOULD NOT** “fix with an infinite buffer” as a scalability strategy.",
        },
        {
            "slug": "service-discovery",
            "topic": "Service Discovery",
            "tags": ["networking", "microservices", "discovery"],
            "ai_summary": "Service discovery lets clients locate healthy instances of a service in dynamic environments. Mechanisms include DNS, registries, and platform endpoints APIs.",
            "core": "In elastic infrastructure, IPs change constantly. Service discovery maintains a directory of instances and health so callers can find targets without hardcoding addresses.",
            "architecture": "1. Service registers on startup with a registry or platform control plane.\n2. Health checks update readiness.\n3. Clients query DNS/registry/mesh and cache results.\n4. Load balancing chooses an instance.\n5. Deregistration on shutdown or failed checks removes stale targets.",
            "advantages": [
                "Enables autoscaling and replaceable compute.",
                "Central health view for routing.",
            ],
            "disadvantages": [
                "Stale registry entries cause connection errors.",
                "Another critical dependency for request paths.",
            ],
            "alternatives": "**Static config** for tiny fixed fleets; **service mesh sidecar DNS/xDS** as the discovery+LB plane.",
            "guidelines": "**SHOULD** use platform-native discovery (K8s Services) unless multi-cluster needs demand a richer registry. **SHOULD NOT** hardcode pod IPs in clients.",
        },
    ],
    "architecture-patterns": [
        {
            "slug": "monolith-vs-microservices",
            "topic": "Monolith vs Microservices",
            "tags": ["architecture", "microservices", "organization"],
            "ai_summary": "A monolith deploys as one unit; microservices split independently deployable services by domain. The choice hinges on team scale, deployment independence, and operational maturity.",
            "core": "Monoliths colocated modules share a process/DB boundary. Microservices split bounded contexts into separately deployed services communicating over the network. The problem is balancing delivery speed, complexity, and scaling independence.",
            "architecture": "1. Monolith: single build artifact, in-process calls, often one primary DB.\n2. Microservices: service-per-capability, own data where possible, sync/async remote calls.\n3. Gateways and meshes handle cross-cutting traffic policy.\n4. Distributed observability becomes mandatory for microservices.\n5. Evolution path often starts modular monolith → extract services at pain points.",
            "advantages": [
                "Monolith: simpler tracing, transactions, and local refactors.",
                "Microservices: independent scale/deploy and clearer team ownership boundaries.",
            ],
            "disadvantages": [
                "Monolith: can become a deployment bottleneck and tangled dependency ball.",
                "Microservices: distributed failure modes, ops overhead, and data consistency challenges.",
            ],
            "alternatives": "**Modular monolith** (strong module boundaries, one deploy); **mini-services** / service-oriented hybrids.",
            "guidelines": "**SHOULD** default to a modular monolith until team/scale pressures justify extraction. **SHOULD NOT** split microservices by technical layers alone (e.g., “the DAO service”).",
        },
        {
            "slug": "cqrs",
            "topic": "CQRS (Command Query Responsibility Segregation)",
            "tags": ["architecture", "patterns", "scalability"],
            "ai_summary": "CQRS separates write (command) models from read (query) models so each can scale and optimize independently. It fits domains with asymmetric read/write complexity.",
            "core": "CQRS uses different models/paths for updating state versus reading it. Writes enforce invariants on a transactional model; reads use denormalized projections. It solves conflicting optimization needs between complex writes and high-volume queries.",
            "architecture": "1. Client sends commands to the write side.\n2. Write model validates and persists.\n3. Events/updates propagate to read projections asynchronously.\n4. Queries hit read DB/cache shaped for UI/API needs.\n5. Clients tolerate brief read lag or use read-your-writes techniques.",
            "advantages": [
                "Independent scaling and schema design for reads vs writes.",
                "Clearer command semantics and auditability when paired with events.",
            ],
            "disadvantages": [
                "More moving parts and eventual consistency complexity.",
                "Easy to over-engineer simple CRUD domains.",
            ],
            "alternatives": "**Single model CRUD** with indexes/caches; **event sourcing** (often paired with CQRS but not required).",
            "guidelines": "**SHOULD** consider CQRS when read models diverge heavily from write invariants. **SHOULD NOT** apply CQRS everywhere as a default microservice template.",
        },
        {
            "slug": "event-sourcing",
            "topic": "Event Sourcing",
            "tags": ["architecture", "events", "storage"],
            "ai_summary": "Event sourcing stores state as an append-only sequence of domain events and rebuilds current state by replaying them. It provides a complete audit log and temporal queries.",
            "core": "Instead of persisting only latest row state, event sourcing appends immutable events (“ItemAdded”). Current state is a fold over the stream (with snapshots). It solves auditability, debugging, and reconstructing historical state.",
            "architecture": "1. Command handler validates against current aggregate state.\n2. New events append to the event store.\n3. Aggregates rehydrate via snapshot + newer events.\n4. Projections subscribe to build read models.\n5. Upcasters evolve old event schemas carefully.",
            "advantages": [
                "Full audit trail and time-travel debugging.",
                "Natural integration with event-driven consumers.",
            ],
            "disadvantages": [
                "Operational complexity: replay, schema evolution, GDPR erasure.",
                "Not intuitive for teams used to mutable CRUD tables.",
            ],
            "alternatives": "**State + change data capture (CDC)** for audit-ish streams; **append-only audit tables** without making events the primary store.",
            "guidelines": "**SHOULD** use event sourcing for domains that need rich history and complex state transitions. **SHOULD NOT** event-source every entity; prefer selective aggregates.",
        },
        {
            "slug": "strangler-fig",
            "topic": "Strangler Fig Pattern",
            "tags": ["architecture", "migration", "legacy"],
            "ai_summary": "The strangler fig pattern incrementally replaces a legacy system by routing slices of traffic to new implementations. It reduces big-bang migration risk.",
            "core": "Named after vines that gradually envelop a tree, this pattern places a facade in front of legacy and peels off functionality piece by piece. It solves risky all-at-once rewrites.",
            "architecture": "1. Put a routing facade/proxy in front of the legacy system.\n2. Identify a bounded feature to reimplement.\n3. Route that slice to the new service; keep the rest on legacy.\n4. Sync data as needed during coexistence.\n5. Repeat until legacy can be decommissioned.",
            "advantages": [
                "Continuous delivery of value with rollback per slice.",
                "Lower risk than a full rewrite cutover.",
            ],
            "disadvantages": [
                "Prolonged dual-running increases cost and complexity.",
                "Data synchronization during coexistence can be thorny.",
            ],
            "alternatives": "**Big-bang rewrite** (rarely justified); **branch by abstraction** inside a monolith without an edge facade.",
            "guidelines": "**SHOULD** strangler-migrate critical legacy when you can carve clear seams. **SHOULD NOT** run forever in dual mode without a decommission plan.",
        },
        {
            "slug": "sidecar",
            "topic": "Sidecar Pattern",
            "tags": ["architecture", "patterns", "infrastructure"],
            "ai_summary": "A sidecar colocates a helper process with the main app container to provide platform features like proxying, logging, or secrets. It separates infrastructure concerns from business code.",
            "core": "The sidecar pattern attaches an auxiliary container/process in the same network namespace as the app. It solves cross-cutting operational needs without baking them into every language runtime.",
            "architecture": "1. Deploy app + sidecar as a unit (pod).\n2. App talks to localhost sidecar for proxy/telemetry/secrets.\n3. Sidecar talks to the broader mesh/control plane.\n4. Lifecycle hooks manage startup ordering and drains.\n5. Upgrading sidecars can ship platform features independently of app code.",
            "advantages": [
                "Consistent infrastructure features across polyglot services.",
                "Keeps business containers smaller and focused.",
            ],
            "disadvantages": [
                "Extra CPU/memory per pod and more complex networking.",
                "Troubleshooting spans two processes.",
            ],
            "alternatives": "**Library SDKs** embedded in-process; **node agents** shared per host; **ambient mesh** modes without per-pod proxies.",
            "guidelines": "**SHOULD** use sidecars for fleet-wide mTLS/metrics when a mesh is adopted. **SHOULD NOT** put business logic in sidecars.",
        },
        {
            "slug": "bff",
            "topic": "Backend for Frontend (BFF)",
            "tags": ["architecture", "apis", "frontend"],
            "ai_summary": "A BFF is an API layer tailored to a specific client experience (web, mobile, partner). It aggregates and shapes backend data to reduce chatty UI coupling.",
            "core": "Instead of one generic API for all clients, each client type gets a dedicated backend that speaks its UI’s language. It solves overfetching, awkward payloads, and coupling many UIs to internal microservices.",
            "architecture": "1. Client calls its BFF only.\n2. BFF authenticates the user session/device context.\n3. BFF fans out to internal services and aggregates/shapes responses.\n4. Returns a screen-oriented payload.\n5. Ownership usually sits with the client team.",
            "advantages": [
                "Faster UI iteration without breaking other clients.",
                "Hides microservice sprawl from frontends.",
            ],
            "disadvantages": [
                "Duplication across BFFs if not carefully shared.",
                "Risk of BFFs becoming mini-monoliths of business rules.",
            ],
            "alternatives": "**GraphQL gateway** as a flexible general API; **single public API + client-side aggregation** (more chattiness).",
            "guidelines": "**SHOULD** use BFFs when web and mobile needs diverge strongly. **SHOULD NOT** reimplement core domain invariants in every BFF—call domain services.",
        },
    ],
    "communication": [
        {
            "slug": "rest",
            "topic": "REST APIs",
            "tags": ["apis", "communication", "http"],
            "ai_summary": "REST uses HTTP resources, methods, and status codes for synchronous service interfaces. It is the default public API style due to simplicity and broad tooling.",
            "core": "RESTful APIs expose resources via URLs and manipulate them with HTTP verbs, leveraging status codes and caching headers. They solve language-agnostic service communication with ubiquitous HTTP infrastructure.",
            "architecture": "1. Client sends HTTP request to a resource URL.\n2. Gateway/service authenticates and authorizes.\n3. Handler loads/updates domain state.\n4. Response returns JSON/encoded body with cache validators.\n5. Idempotent methods and pagination conventions shape large collections.",
            "advantages": [
                "Simple, cacheable, universally supported.",
                "Easy to debug with standard HTTP tools.",
            ],
            "disadvantages": [
                "Chatty multi-resource pages without aggregation.",
                "Weak formal contracts unless OpenAPI is enforced.",
            ],
            "alternatives": "**gRPC** for efficient internal RPC; **GraphQL** for flexible client-driven queries.",
            "guidelines": "**SHOULD** use REST for public HTTP APIs and simple CRUD services. **SHOULD NOT** invent non-HTTP semantics that ignore verbs, status codes, and idempotency norms.",
        },
        {
            "slug": "grpc",
            "topic": "gRPC",
            "tags": ["apis", "communication", "rpc"],
            "ai_summary": "gRPC is a high-performance RPC framework using HTTP/2 and Protocol Buffers. It excels at efficient internal service-to-service calls and streaming.",
            "core": "gRPC defines strongly typed service contracts in protobuf and generates clients/servers. It solves efficient binary RPC, streaming, and strict schema evolution for internal microservices.",
            "architecture": "1. Define .proto services and messages.\n2. Generate stubs; servers implement RPC methods.\n3. Clients open HTTP/2 channels with optional mTLS.\n4. Unary or streaming calls exchange protobuf payloads.\n5. Deadlines, retries, and interceptors enforce policy.",
            "advantages": [
                "Compact payloads and multiplexed streams.",
                "First-class deadlines and code-generated contracts.",
            ],
            "disadvantages": [
                "Harder for browsers without a proxy; less human-debuggable than JSON.",
                "Protobuf evolution requires discipline.",
            ],
            "alternatives": "**JSON/HTTP REST** for public/simple APIs; **GraphQL** when clients need flexible graphs of data.",
            "guidelines": "**SHOULD** prefer gRPC for internal low-latency service meshes. **SHOULD NOT** expose raw gRPC to anonymous public web clients without a gateway.",
        },
        {
            "slug": "graphql",
            "topic": "GraphQL",
            "tags": ["apis", "communication", "frontend"],
            "ai_summary": "GraphQL lets clients specify exactly the data graph they need in one request. It reduces overfetching for complex UIs while centralizing a schema.",
            "core": "GraphQL exposes a typed schema of queries, mutations, and subscriptions. Clients ask for precise field trees. It solves mobile/web overfetching and round-trip chattiness against many REST endpoints.",
            "architecture": "1. Client sends a query document to the GraphQL endpoint.\n2. Server validates against the schema.\n3. Resolvers fetch fields, often batching with DataLoader patterns.\n4. Response mirrors the query shape.\n5. Persisted queries and complexity limits protect the server.",
            "advantages": [
                "Clients evolve UI data needs without many backend versions.",
                "Single endpoint aggregates microservice data carefully.",
            ],
            "disadvantages": [
                "Caching and authorization are harder than simple REST paths.",
                "Unbounded queries can create expensive resolver trees.",
            ],
            "alternatives": "**BFF REST aggregators**; **gRPC + gateway** for internal efficiency with client-specific REST.",
            "guidelines": "**SHOULD** use GraphQL when multiple clients need varied shapes of the same graph. **SHOULD NOT** treat GraphQL as a DB query language exposed without authz and cost limits.",
        },
        {
            "slug": "realtime-communication",
            "topic": "Real-Time Communication (WebSockets, SSE, Long Polling)",
            "tags": ["communication", "realtime", "networking"],
            "ai_summary": "WebSockets, Server-Sent Events, and long polling deliver low-latency server updates to clients. Choice depends on bidirectional needs, proxies, and scale.",
            "core": "Interactive apps need server push beyond request/response. WebSockets provide full-duplex channels; SSE is server-to-client over HTTP; long polling holds requests until events arrive. They solve live feeds, collab cursors, and notifications.",
            "architecture": "1. Client upgrades to WebSocket or opens SSE/long-poll.\n2. Gateway sticky-routes or uses a pub/sub backplane for multi-instance fan-out.\n3. App publishes events to the backplane.\n4. Owning connection node pushes to the client.\n5. Heartbeats detect dead connections and reconnect with backoff.",
            "advantages": [
                "Low-latency updates without constant client polling.",
                "Better UX for collaborative and live data products.",
            ],
            "disadvantages": [
                "Stateful connections complicate horizontal scale.",
                "Proxies/load balancers need timeout and sticky configuration.",
            ],
            "alternatives": "**Short polling** (simpler, higher overhead); **push notifications** for mobile background delivery.",
            "guidelines": "**SHOULD** use SSE for one-way feeds and WebSockets for bidirectional interaction. **SHOULD NOT** open unbounded connections without auth, fan-out design, and idle timeouts.",
        },
    ],
    "data-processing": [
        {
            "slug": "batch-processing",
            "topic": "Batch Processing",
            "tags": ["processing", "data", "etl"],
            "ai_summary": "Batch processing computes over bounded datasets on a schedule or trigger. It efficiently handles large ETL and reporting where immediate results are unnecessary.",
            "core": "Batch jobs read a finite input, transform it, and write outputs (tables, files, reports). They solve high-throughput data transformation when minutes-to-hours latency is acceptable.",
            "architecture": "1. Scheduler triggers a job (time or dependency-based).\n2. Workers read partitioned inputs from storage/DB.\n3. Transform/aggregate stages run with retries per partition.\n4. Outputs commit atomically where possible (write temp then publish).\n5. Metrics track SLA duration and data quality checks.",
            "advantages": [
                "High efficiency via large scans and bulk I/O.",
                "Simpler exactly-once-ish outcomes with atomic output swaps.",
            ],
            "disadvantages": [
                "High latency to insights.",
                "Bursty resource usage and catch-up pain after failures.",
            ],
            "alternatives": "**Stream processing** for continuous low-latency; **micro-batch** hybrids (small frequent batches).",
            "guidelines": "**SHOULD** batch nightly reconciliations, warehouse loads, and large ML feature builds. **SHOULD NOT** use multi-hour batches for user-facing features that need seconds of freshness.",
        },
        {
            "slug": "stream-processing",
            "topic": "Stream Processing",
            "tags": ["processing", "streaming", "realtime"],
            "ai_summary": "Stream processing continuously transforms unbounded event streams with low latency. It powers real-time analytics, fraud checks, and incremental pipelines.",
            "core": "Stream processors ingest events as they arrive, maintain state, and emit derived streams or actions. They solve freshness requirements that batch windows cannot meet.",
            "architecture": "1. Events land on a log/topic.\n2. Stream job consumes with offsets and keyed state stores.\n3. Windowing/aggregations update continuously.\n4. Results write to sinks (DB, indexes, alerts).\n5. Checkpointing enables recovery with defined processing guarantees.",
            "advantages": [
                "Seconds-level freshness for analytics and reactions.",
                "Smooth resource usage vs giant batch peaks.",
            ],
            "disadvantages": [
                "State, late data, and exactly-once sinks are complex.",
                "Harder operational debugging than batch jobs.",
            ],
            "alternatives": "**Micro-batch**; **request-time computation** for rare queries; **CDC + materialized views**.",
            "guidelines": "**SHOULD** stream when product value depends on near-real-time signals. **SHOULD NOT** build streaming for tiny volumes where a cron job meets the SLA with less complexity.",
        },
        {
            "slug": "mapreduce",
            "topic": "MapReduce",
            "tags": ["processing", "batch", "distributed-systems"],
            "ai_summary": "MapReduce is a programming model that maps over partitioned inputs then shuffles and reduces by key. It popularized large-scale distributed batch computation.",
            "core": "MapReduce splits computation into map (per-record emit key/value) and reduce (aggregate by key) with a distributed shuffle. It solves parallel processing of huge datasets on commodity clusters.",
            "architecture": "1. Inputs split across workers.\n2. Map tasks emit intermediate pairs.\n3. Shuffle partitions by key to reducers.\n4. Reduce tasks aggregate and write outputs.\n5. Framework handles retries of failed tasks and speculative execution.",
            "advantages": [
                "Simple model for massive parallel batch jobs.",
                "Automatic fault tolerance for task failures.",
            ],
            "disadvantages": [
                "High disk shuffle overhead; poor fit for iterative algorithms.",
                "Superseded in many stacks by DAG engines (Spark) and streams.",
            ],
            "alternatives": "**Spark/Flink-style DAG engines**; **SQL warehouses** for many aggregations without custom code.",
            "guidelines": "**SHOULD** understand MapReduce as the conceptual base for modern batch engines. **SHOULD NOT** implement raw MapReduce when a managed SQL/DAG engine meets the need.",
        },
        {
            "slug": "write-ahead-log",
            "topic": "Write-Ahead Logging (WAL)",
            "tags": ["database", "durability", "storage"],
            "ai_summary": "A write-ahead log durably records changes before applying them to primary storage structures. It enables crash recovery and replication feeds.",
            "core": "WAL (or redo log) appends intended mutations to sequential storage before updating pages/files. After a crash, redo brings data files to a consistent committed state. It solves durability and powers replication.",
            "architecture": "1. Transaction produces log records.\n2. On commit, log is fsynced (per durability settings).\n3. Dirty pages flush asynchronously.\n4. Recovery replays log from last checkpoint.\n5. Replicas may stream the same log.",
            "advantages": [
                "Strong durability with sequential write performance.",
                "Enables point-in-time recovery and replication.",
            ],
            "disadvantages": [
                "Sync commits add latency.",
                "Log disk saturation stalls all writes.",
            ],
            "alternatives": "**Async durability** (risk data loss); **event sourcing** as an application-level log-first design.",
            "guidelines": "**SHOULD** keep WAL disks fast and monitored for production databases. **SHOULD NOT** disable fsync in production to “gain performance” without accepting data-loss risk.",
        },
        {
            "slug": "cdc",
            "topic": "Change Data Capture (CDC)",
            "tags": ["data", "integration", "streaming"],
            "ai_summary": "CDC streams database row changes into downstream systems in near real time. It powers caches, search indexes, and analytics without dual writes.",
            "core": "CDC reads the database transaction log (or triggers) and emits insert/update/delete events. It solves keeping derived systems synchronized without burdening app code with dual writes.",
            "architecture": "1. Connector tails WAL/binlog with a consistent offset.\n2. Changes are published to a stream with schema metadata.\n3. Consumers update search, caches, warehouses, or other DBs.\n4. Snapshots bootstrap initial state before streaming.\n5. Schema changes require compatible evolution handling.",
            "advantages": [
                "Avoids brittle dual-write application logic.",
                "Low-latency propagation from the system of record.",
            ],
            "disadvantages": [
                "Operational coupling to DB log formats and permissions.",
                "Consumers must handle out-of-order and tombstones carefully.",
            ],
            "alternatives": "**Transactional outbox** from app writes; **periodic ETL dumps** for non-urgent sync.",
            "guidelines": "**SHOULD** use CDC to feed search/analytics from OLTP. **SHOULD NOT** treat CDC streams as a substitute for well-defined domain events when business meaning differs from row diffs.",
        },
    ],
    "reliability": [
        {
            "slug": "health-checks",
            "topic": "Health Checks and Heartbeats",
            "tags": ["reliability", "operations", "networking"],
            "ai_summary": "Health checks and heartbeats detect failed or stuck processes so traffic can be routed away. Liveness vs readiness probes distinguish restart needs from temporary unavailability.",
            "core": "Health checks periodically verify a process can serve; heartbeats signal liveness to peers/coordinators. They solve silent failures where a process is up but not useful.",
            "architecture": "1. Platform probes /healthz (liveness) and /ready (readiness).\n2. Failed liveness restarts the process.\n3. Failed readiness removes it from load balancers.\n4. Distributed systems send heartbeats to leases/failure detectors.\n5. Alerting fires when check failure rates burn error budgets.",
            "advantages": [
                "Automates failover and self-healing.",
                "Prevents routing to starting/broken instances.",
            ],
            "disadvantages": [
                "Overly deep checks can cascade failures (dependencies down → all pods unready).",
                "Aggressive timeouts cause flapping.",
            ],
            "alternatives": "**Passive health** via error rates at the LB; **synthetic monitoring** from outside the cluster.",
            "guidelines": "**SHOULD** separate liveness (process sane) from readiness (able to serve). **SHOULD NOT** make liveness depend on downstream dependencies.",
        },
        {
            "slug": "failover",
            "topic": "Failover Strategies",
            "tags": ["reliability", "availability", "operations"],
            "ai_summary": "Failover switches traffic from a failed component to a standby or peer. Strategies range from automatic multi-AZ failover to manual disaster recovery.",
            "core": "Failover is the controlled promotion/redirection when a primary path fails. It solves continuity when instances, AZs, or regions become unavailable.",
            "architecture": "1. Detect failure (health checks, quorum loss, error budgets).\n2. Choose target (standby replica, alternate region).\n3. Promote/reconfigure data plane (DNS, LB, leader election).\n4. Fence the old primary to prevent split-brain.\n5. Verify, then run failback when safe.",
            "advantages": [
                "Reduces MTTR versus manual rebuilds.",
                "Supports tiered RPO/RTO objectives.",
            ],
            "disadvantages": [
                "Automated failover can amplify partial network faults.",
                "Unused standbys still cost money (active-passive).",
            ],
            "alternatives": "**Active-active multi-primary** (no single failover, more conflict handling); **stateless rebuild from scratch** for ephemeral workers.",
            "guidelines": "**SHOULD** regularly game-day test failover for datastores and critical paths. **SHOULD NOT** assume DNS-only failover meets aggressive RTO without measuring TTL and client behavior.",
        },
        {
            "slug": "multi-region",
            "topic": "Multi-Region Architecture",
            "tags": ["scaling", "availability", "networking"],
            "ai_summary": "Multi-region architectures deploy services in geographically separate regions for latency and disaster resilience. Data replication topology determines consistency and failover.",
            "core": "Running in multiple cloud regions protects against regional outages and brings compute closer to users. The hard problem is data: how to replicate, conflict, and fail over without corrupting state.",
            "architecture": "1. Deploy stateless services in two+ regions behind geo-DNS/anycast.\n2. Choose data mode: active-passive (primary region writes), active-active (multi-writer), or regional pin.\n3. Replicate data asynchronously or via consensus globally (rare/expensive).\n4. Route users to nearest healthy region.\n5. Practice region evacuation runbooks.",
            "advantages": [
                "Higher availability and better global latency.",
                "Regulatory data residency options with regional pinning.",
            ],
            "disadvantages": [
                "Significant cost and operational complexity.",
                "Cross-region consistency and conflict resolution are hard.",
            ],
            "alternatives": "**Multi-AZ single region** (covers most failure domains cheaper); **static DR cold standby** for lower tiers.",
            "guidelines": "**SHOULD** go multi-region when business RTO/RPO or latency truly requires it. **SHOULD NOT** invent active-active multi-writer data before exhausting multi-AZ and read-local designs.",
        },
        {
            "slug": "observability",
            "topic": "Observability (Metrics, Logs, Traces)",
            "tags": ["observability", "reliability", "operations"],
            "ai_summary": "Observability uses metrics, logs, and traces to infer internal system state from external outputs. It enables debugging distributed systems and SLO-driven operations.",
            "core": "Metrics quantify aggregates, logs record discrete events, traces follow a request across services. Together they solve “why is it broken?” in systems too complex to inspect directly.",
            "architecture": "1. Instrument code and infra with consistent labels and trace context.\n2. Agents/collectors export to backends.\n3. Dashboards and alerts evaluate SLOs.\n4. On incident, metrics locate symptoms; traces find latency spans; logs explain errors.\n5. Sampling and retention balance cost vs fidelity.",
            "advantages": [
                "Faster incident response and performance optimization.",
                "Enables error budgets and capacity planning.",
            ],
            "disadvantages": [
                "High cardinality and retention can explode cost.",
                "Poor instrumentation creates false confidence.",
            ],
            "alternatives": "**Only logs** (insufficient at scale); **synthetic monitoring alone** (misses deep internal failure modes).",
            "guidelines": "**SHOULD** adopt metrics+logs+traces for production microservices with trace context propagation. **SHOULD NOT** alert on every raw metric—alert on user-impacting SLOs.",
        },
        {
            "slug": "authentication-authorization",
            "topic": "Authentication and Authorization",
            "tags": ["security", "apis", "architecture"],
            "ai_summary": "Authentication verifies identity; authorization decides permitted actions. System design must place these checks consistently at edges and service boundaries.",
            "core": "AuthN establishes who the caller is (session, token, mTLS). AuthZ evaluates policies (RBAC, ABAC, ReBAC) against that identity. They solve protecting APIs and data from anonymous or over-privileged access.",
            "architecture": "1. Client authenticates with IdP (OAuth/OIDC, SAML, passwords).\n2. Edge validates tokens/sessions.\n3. Identity propagates via signed tokens or internal identity headers/mTLS.\n4. Services enforce fine-grained authz on resources.\n5. Audit logs record access decisions for sensitive operations.",
            "advantages": [
                "Central IdP improves UX and security controls.",
                "Explicit authz prevents accidental public data leaks.",
            ],
            "disadvantages": [
                "Token confusion and inconsistent enforcement across services.",
                "Overly central “auth service” round-trips can add latency/SPOF if misdesigned.",
            ],
            "alternatives": "**Network-only trust** (insufficient alone); **mutual TLS without user-level authz** (machine identity only).",
            "guidelines": "**SHOULD** authenticate at the edge and re-enforce authz in each sensitive service. **SHOULD NOT** pass mutable `userId` headers without cryptographic service identity.",
        },
        {
            "slug": "rate-limiting-vs-load-shedding",
            "topic": "Load Shedding",
            "tags": ["reliability", "traffic", "scaling"],
            "ai_summary": "Load shedding deliberately drops or rejects work when a system is overloaded to protect critical capacity. Unlike client quotas, it reacts to server saturation.",
            "core": "Load shedding is admission control based on server health (CPU, queue time, hedged overload) rather than only per-client quotas. It solves survival under unexpected traffic or dependency slowdowns.",
            "architecture": "1. Monitor saturation signals (queue latency, thread pool utilization).\n2. When thresholds trip, reject low-priority requests first.\n3. Return fast failures (503) with retry hints.\n4. Preserve capacity for health checks and critical endpoints.\n5. Combine with autoscaling, but shed during scale-up delay.",
            "advantages": [
                "Prevents total collapse and multi-hour recovery.",
                "Keeps critical user journeys alive under stress.",
            ],
            "disadvantages": [
                "Users see errors; fairness policies can be contentious.",
                "Bad signals cause premature shedding.",
            ],
            "alternatives": "**Rate limiting** (per-client fairness); **autoscaling alone** (too slow for sudden spikes).",
            "guidelines": "**SHOULD** implement server-side shedding for public tiers and expensive endpoints. **SHOULD NOT** queue unboundedly hoping more capacity appears.",
        },
    ],
}


CATEGORY_TITLES = {
    "foundations": "Foundations",
    "networking": "Networking & Traffic",
    "data-storage": "Data Storage",
    "distributed-systems": "Distributed Systems",
    "architecture-patterns": "Architecture Patterns",
    "communication": "Communication",
    "data-processing": "Data Processing",
    "reliability": "Reliability & Operations",
}


def write_topic_pages() -> list[tuple[str, str, str]]:
    """Write all topic pages; return list of (category, slug, topic)."""
    catalog: list[tuple[str, str, str]] = []
    for category, topics in TOPICS.items():
        cat_dir = ROOT / category
        cat_dir.mkdir(parents=True, exist_ok=True)
        links: list[str] = []
        for t in topics:
            body = page(
                topic=t["topic"],
                tags=t["tags"],
                ai_summary=t["ai_summary"],
                core=t["core"],
                architecture=t["architecture"],
                advantages=t["advantages"],
                disadvantages=t["disadvantages"],
                alternatives=t["alternatives"],
                guidelines=t["guidelines"],
            )
            # Fix accidental escaped newlines in advantages/disadvantages if any
            path = cat_dir / f"{t['slug']}.md"
            path.write_text(body, encoding="utf-8")
            links.append(f"- [{t['topic']}]({t['slug']}.md)")
            catalog.append((category, t["slug"], t["topic"]))

        index = f"""# {CATEGORY_TITLES[category]}

System design theory pages in this category.

{chr(10).join(links)}
"""
        (cat_dir / "index.md").write_text(index, encoding="utf-8")
    return catalog


def write_root_index(catalog: list[tuple[str, str, str]]) -> None:
    sections: list[str] = []
    for category, title in CATEGORY_TITLES.items():
        items = [c for c in catalog if c[0] == category]
        links = "\n".join(f"- [{topic}]({category}/{slug}.md)" for _, slug, topic in items)
        sections.append(f"## {title}\n\n{links}")

    body = f"""# System Design Wiki

Local system design theory wiki for human engineers and AI assistants (RAG context).

Each topic page uses a fixed structure: core concept, architecture & data flow, trade-offs, alternatives, and team guidelines.

## How to use

1. Start here or open a category `index.md`.
2. Open the most specific topic page.
3. Prefer this wiki for architecture/theory questions; use `frameworks/` for library-specific docs.

## Categories

{chr(10).join(f"- [{title}]({cat}/index.md)" for cat, title in CATEGORY_TITLES.items())}

{chr(10).join(sections)}
"""
    ROOT.mkdir(parents=True, exist_ok=True)
    (ROOT / "index.md").write_text(body, encoding="utf-8")


def main() -> None:
    catalog = write_topic_pages()
    write_root_index(catalog)
    print(f"Wrote {len(catalog)} topics under {ROOT}")


if __name__ == "__main__":
    main()
