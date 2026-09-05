---
topic: Object Storage
tags: storage, blob, scalability
ai_summary: Object storage persists immutable blobs addressed by keys in a flat namespace, accessed over HTTP APIs. It excels at durable, cheap, large-scale unstructured data.
---

# Object Storage

## 1. Core Concept
Object stores (S3-compatible) manage objects with key, metadata, and value—not POSIX files or DB rows. They solve durable storage of media, backups, lake files, and large artifacts at massive scale.

## 2. Architecture & Data Flow
1. Client PUTs an object to a bucket/key with optional encryption and metadata.
2. Store erasure-codes or replicates across disks/AZs.
3. GET/LIST via HTTP; pre-signed URLs allow direct client transfer.
4. Lifecycle policies tier to colder storage or expire objects.
5. Event notifications can trigger downstream processing.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Virtually unlimited scale with high durability classes.
  * Cheap for large sequential data vs block/DB storage.
* **Disadvantages/Risks:**
  * Higher latency than local disk; not ideal for tiny chatty I/O.
  * No rich partial-update semantics like a filesystem or database.

## 4. Alternatives
**Block storage** for databases/VMs; **distributed filesystems** when POSIX semantics are required.

## 5. Team Guidelines & Use Cases
**SHOULD** store user uploads, exports, and data-lake files in object storage. **SHOULD NOT** use object storage as a low-latency mutable primary database.
