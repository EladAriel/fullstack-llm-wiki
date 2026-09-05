---
topic: MapReduce
tags: processing, batch, distributed-systems
ai_summary: MapReduce is a programming model that maps over partitioned inputs then shuffles and reduces by key. It popularized large-scale distributed batch computation.
---

# MapReduce

## 1. Core Concept
MapReduce splits computation into map (per-record emit key/value) and reduce (aggregate by key) with a distributed shuffle. It solves parallel processing of huge datasets on commodity clusters.

## 2. Architecture & Data Flow
1. Inputs split across workers.
2. Map tasks emit intermediate pairs.
3. Shuffle partitions by key to reducers.
4. Reduce tasks aggregate and write outputs.
5. Framework handles retries of failed tasks and speculative execution.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Simple model for massive parallel batch jobs.
  * Automatic fault tolerance for task failures.
* **Disadvantages/Risks:**
  * High disk shuffle overhead; poor fit for iterative algorithms.
  * Superseded in many stacks by DAG engines (Spark) and streams.

## 4. Alternatives
**Spark/Flink-style DAG engines**; **SQL warehouses** for many aggregations without custom code.

## 5. Team Guidelines & Use Cases
**SHOULD** understand MapReduce as the conceptual base for modern batch engines. **SHOULD NOT** implement raw MapReduce when a managed SQL/DAG engine meets the need.
