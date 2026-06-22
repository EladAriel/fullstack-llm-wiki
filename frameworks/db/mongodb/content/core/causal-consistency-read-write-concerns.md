---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/causal-consistency-read-write-concerns.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================================

# Causal Consistency and Read and Write Concerns

With MongoDB's `causally consistent client sessions <sessions>`, different combinations of read and write concerns provide different `causal consistency guarantees <causal-consistency-guarantees>`.

The following table lists the specific guarantees that various combinations provide:

If you want causal consistency with data durability, then, as seen from the table, only read operations with :readconcern:`"majority"` read concern and write operations with :writeconcern:`"majority"` write concern can guarantee all four causal consistency guarantees. That is, `causally consistent client sessions <sessions>` can only guarantee causal consistency for:

- Read operations with :readconcern:`"majority"` read concern; in other
words, the read operations that return data that has been acknowledged by a majority of the replica set members and is durable.

- Write operations with :writeconcern:`"majority"` write concern;
in other words, the write operations that request acknowledgment that the operation has been applied to a majority of the replica set's voting members.

If you want causal consistency without data durability (meaning that writes may be rolled back), then write operations with :writeconcern:`{ w: 1 } <\<number\>>` write concern can also provide causal consistency.

> **Note:** The other combinations of read and write concerns may also satisfy
all four causal consistency guarantees in some situations, but not
necessarily in all situations.

The read concern :readconcern:`"majority"` and write concern :writeconcern:`"majority"` ensure that the four causal consistency guarantees hold even in `circumstances (such as with a network partition) <edge-cases>` where two members in a replica set transiently believe that they are the primary. And while both primaries can complete writes with :writeconcern:`{ w: 1 } <\<number\>>` write concern, only one primary will be able to complete writes with :writeconcern:`"majority"` write concern.

For example, consider a situation where a network partition divides a five member replica set:

.. figure:: /images/network-partition-two-primaries.svg

## Scenarios

To illustrate the read and write concern requirements, the following scenarios have a client issue a sequence of operations with various combination of read and write concerns to the replica set:

- `causal-rc-majority-wc-majority`
- `causal-rc-majority-wc-1`
- `causal-rc-local-wc-majority`
- `causal-rc-local-wc-1`
### Read Concern `"majority"` and Write concern `"majority"`

The use of read concern :readconcern:`"majority"` and write concern :writeconcern:`"majority"` in a causally consistent session provides the following causal consistency guarantees:

|checkmark| Read own writes  |checkmark| Monotonic reads  |checkmark| Monotonic writes  |checkmark| Writes follow reads

> **Note:** During the transient period with two primaries, because only `P`\
:sub:`new` can fulfill writes with :writeconcern:`{ w: "majority" }
<"majority">` write concern, a client session can issue the
following sequence of operations successfully:
.. list-table::
   :header-rows: 1
   * - Sequence
     - Example
   * - | 1. Write\ :sub:`1` with write concern :writeconcern:`"majority"`  to  `P`\ :sub:`new`
       | 2. Read\ :sub:`1` with read concern :readconcern:`"majority"` to `S`\ :sub:`2`
       | 3. Write\ :sub:`2` with write concern :writeconcern:`"majority"` to `P`\ :sub:`new`
       |
       | 4. Read\ :sub:`2` with read concern :readconcern:`"majority"` to `S`\ :sub:`3`
     - | For item `A`, update `qty` to `50`.
       | Read item `A`.
       | For items with `qty` less than or equal to `50`,
       | update `restock` to `true`.
       | Read item `A`.
.. figure:: /images/causal-rc-majority-wc-majority.svg
   :alt: State of data with two primaries using read concern majority and write concern majority
   :figwidth: 550px
.. list-table::
   :class: no-outer-border
   :widths: 20 80
   * - |checkmark| **Read own writes**
     - | Read\ :sub:`1` reads data from `S`\ :sub:`2` that reflects a state after Write\ :sub:`1`.
       | Read\ :sub:`2` reads data from `S`\ :sub:`3` that
         reflects a state after Write\ :sub:`1` followed by Write\
         :sub:`2`.
   * - |checkmark| **Monotonic reads**
     - Read\ :sub:`2` reads data from `S`\ :sub:`3` that reflects
       a state after Read\ :sub:`1`.
   * - |checkmark| **Monotonic writes**
     - Write\ :sub:`2` updates data on `P`\ :sub:`new` that
       reflects a state after Write\ :sub:`1`.
   * - |checkmark| **Writes follow reads**
     - Write\ :sub:`2` updates data on `P`\ :sub:`new` that
       reflects a state of the data after Read\ :sub:`1` (meaning
       that an earlier state reflects the data read by Read\ :sub:`1`).

> **Note:** Consider an alternative sequence where Read\ :sub:`1` with read
concern :readconcern:`"majority"` routes to `S`\ :sub:`1`:
.. list-table::
   :header-rows: 1
   * - Sequence
     - Example
   * - | 1. Write\ :sub:`1` with write concern :writeconcern:`"majority"`  to  `P`\ :sub:`new`
       | 2. Read\ :sub:`1` with read concern :readconcern:`"majority"` to `S`\ :sub:`1`
       | 3. Write\ :sub:`2` with write concern :writeconcern:`"majority"` to `P`\ :sub:`new`
       |
       | 4. Read\ :sub:`2` with with read concern :readconcern:`"majority"` to `S`\ :sub:`3`
     - | For item `A`, update `qty` to `50`.
       | Read item `A`.
       | For items with `qty` less than or equal to `50`,
       | update `restock` to `true`.
       | Read item `A`.
In this sequence, Read\ :sub:`1` cannot return until the
majority commit point has advanced on `P`\ :sub:`old`. This cannot
occur until `P`\ :sub:`old` and `S`\ :sub:`1` can communicate
with the rest of the replica set; at which time, `P`\ :sub:`old`
has stepped down (if not already), and the two members sync
(including Write\ :sub:`1`) from the other members of the
replica set.
.. list-table::
   :class: no-outer-border
   :widths: 20 80
   * - |checkmark| **Read own writes**
     - | Read\ :sub:`1` reflects a state of data after Write\
         :sub:`1`, albeit after the network partition has healed
         and the member has sync'ed from the other members of the
         replica set.
       | Read\ :sub:`2` reads data from `S`\ :sub:`3` that
         reflects a state after Write\ :sub:`1` followed by Write\
         :sub:`2`.
   * - |checkmark| **Monotonic reads**
     - Read\ :sub:`2` reads data from `S`\ :sub:`3` that reflects
       a state after Read\ :sub:`1` (meaning that an earlier state is
       reflected in the data read by Read\ :sub:`1`).
   * - |checkmark| **Monotonic writes**
     - Write\ :sub:`2` updates data on `P`\ :sub:`new` that
       reflects a state after Write\ :sub:`1`.
   * - |checkmark| **Writes follow reads**
     - Write\ :sub:`2` updates data on `P`\ :sub:`new` that
       reflects a state of the data after Read\ :sub:`1` (meaning
       that an earlier state reflects the data read by Read\ :sub:`1`).

### Read Concern `"majority"` and Write concern `{w: 1}`

The use of read concern :readconcern:`"majority"` and write concern :writeconcern:`{ w: 1 } <\<number\>>` in a causally consistent session provides the following causal consistency guarantees if you want causal consistency with data durability:

|xmark| Read own writes  |checkmark| Monotonic reads  |xmark| Monotonic writes  |checkmark| Writes follow reads

If you want causal consistency without data durability:

|checkmark| Read own writes  |checkmark| Monotonic reads  |checkmark| Monotonic writes  |checkmark| Writes follow reads

> **Note:** During the transient period with two primaries, because both `P`\
:sub:`old` and `P`\ :sub:`new` can fulfill writes with
:writeconcern:`{ w: 1 } <\<number\>>` write concern, a client session
could issue the following sequence of operations
successfully but not be causally consistent **if you want causal
consistency with data durability**:
.. list-table::
   :header-rows: 1
   * - Sequence
     - Example
   * - | 1. Write\ :sub:`1` with write concern :writeconcern:`{ w: 1 } <\<number\>>`  to  `P`\ :sub:`old`
       | 2. Read\ :sub:`1` with read concern :readconcern:`"majority"` to `S`\ :sub:`2`
       | 3. Write\ :sub:`2` with write concern :writeconcern:`{ w: 1 } <\<number\>>` to `P`\ :sub:`new`
       |
       | 4. Read\ :sub:`2` with with read concern :readconcern:`"majority"` to `S`\ :sub:`3`
     - | For item `A`, update `qty` to `50`.
       | Read item `A`.
       | For items with `qty` less than or equal to `50`,
       | update `restock` to `true`.
       | Read item `A`.
.. figure:: /images/causal-rc-majority-wc-1.svg
   :alt: State of data with two primaries using read concern majority and write concern 1
   :figwidth: 450px
In this sequence,
- Read\ :sub:`1` cannot return until the majority commit point has
  advanced on `P`\ :sub:`new` past the time of Write\ :sub:`1`.
- Read\ :sub:`2` cannot return until the majority commit point has
  advanced on `P`\ :sub:`new` past the time of Write\ :sub:`2`.
- Write\ :sub:`1` will roll back when the network partition is healed.
|arrow| If you want causal consistency with data durability
.. list-table::
   :class: no-outer-border
   :widths: 20 80
   * - |xmark| **Read own writes**
     - Read\ :sub:`1` reads data from `S`\ :sub:`2` that doesn't
       reflect a state after Write\ :sub:`1`.
   * - |checkmark| **Monotonic reads**
     - Read\ :sub:`2` reads data from `S`\ :sub:`3` that reflects
       a state after Read\ :sub:`1` (meaning that an earlier state is
       reflected in the data read by Read\ :sub:`1`).
   * - |xmark| **Monotonic writes**
     - Write\ :sub:`2` updates data on `P`\ :sub:`new` that does
       not reflect a state after Write\ :sub:`1`.
   * - |checkmark| **Writes follow reads**
     - Write\ :sub:`2` updates data on `P`\ :sub:`new` that
       reflects a state after Read\ :sub:`1` (meaning that an
       earlier state reflects the data read by Read\
       :sub:`1`).
|arrow| If you want causal consistency without data durability
.. list-table::
   :class: no-outer-border
   :widths: 20 80
   * - |checkmark| **Read own writes**
     - Read\ :sub:`1` reads data from `S`\ :sub:`2`
       that reflects a state equivalent to Write\ :sub:`1` followed
       by rollback of Write\ :sub:`1`.
   * - |checkmark| **Monotonic reads**
     - Read\ :sub:`2` reads data from `S`\ :sub:`3` that reflects
       a state after Read\ :sub:`1` (meaning that an earlier state is
       reflected in the data read by Read\ :sub:`1`).
   * - |checkmark| **Monotonic writes**
     - Write\ :sub:`2` updates data on `P`\ :sub:`new` that is
       equivalent to after Write\ :sub:`1` followed by rollback of Write\
       :sub:`1`.
   * - |checkmark| **Writes follow reads**
     - Write\ :sub:`2` updates data on `P`\ :sub:`new` that
       reflects a state after Read\ :sub:`1` (meaning whose
       earlier state reflects the data read by Read\
       :sub:`1`).

> **Note:** Consider an alternative sequence where Read\ :sub:`1` with
read concern :readconcern:`"majority"` routes to `S`\ :sub:`1`:
.. list-table::
   :header-rows: 1
   * - Sequence
     - Example
   * - | 1. Write\ :sub:`1` with write concern :writeconcern:`{ w: 1 } <\<number\>>`  to  `P`\ :sub:`old`
       | 2. Read\ :sub:`1` with read concern :readconcern:`"majority"` to `S`\ :sub:`1`
       | 3. Write\ :sub:`2` with write concern :writeconcern:`{ w: 1 } <\<number\>>` to `P`\ :sub:`new`
       |
       | 4. Read\ :sub:`2` with with read concern :readconcern:`"majority"` to `S`\ :sub:`3`
     - | For item `A`, update `qty` to `50`.
       | Read item `A`.
       | For items with `qty` less than or equal to `50`,
       | update `restock` to `true`.
       | Read item `A`.
In this sequence:
- Read\ :sub:`1` cannot return until the majority commit point
  has advanced on `S`\ :sub:`1`. This cannot occur until `P`\
  :sub:`old` and `S`\ :sub:`1` can communicate with the rest of
  the replica set. At which time, `P`\ :sub:`old` has stepped down
  (if not already), Write\ :sub:`1` is rolled back from `P`\
  :sub:`old` and `S`\ :sub:`1`, and the two members sync from the
  other members of the replica set.
|arrow| If you want causal consistency with data durability
.. list-table::
   :class: no-outer-border
   :widths: 20 80
   * - |xmark| **Read own writes**
     - The data read by Read\ :sub:`1` doesn't reflect the results
       of Write\ :sub:`1`, which has rolled back.
   * - |checkmark| **Monotonic reads**
     - Read\ :sub:`2` reads data from `S`\ :sub:`3` that reflects
       a state after Read\ :sub:`1` (meaning whose
       earlier state reflects the data read by Read\
       :sub:`1`).
   * - |xmark| **Monotonic writes**
     - Write\ :sub:`2` updates data on `P`\ :sub:`new` that does
       not reflect a state after Write\ :sub:`1`, which had preceded
       Write\ :sub:`2` but has rolled back.
   * - |checkmark| **Writes follow reads**
     - Write\ :sub:`2` updates data on `P`\ :sub:`new` that
       reflects a state after Read\ :sub:`1` (meaning whose
       earlier state reflects the data read by Read\ :sub:`1`).
|arrow| If you want causal consistency without data durability
.. list-table::
   :class: no-outer-border
   :widths: 20 80
   * - |checkmark| **Read own writes**
     - Read\ :sub:`1` returns data that reflects the final result of
       Write\ :sub:`1` since Write\ :sub:`1` ultimately rolls back.
   * - |checkmark| **Monotonic reads**
     - Read\ :sub:`2` reads data from `S`\ :sub:`3` that reflects
       a state after Read\ :sub:`1` (meaning that an earlier state
       reflects the data read by Read\ :sub:`1`).
   * - |checkmark| **Monotonic writes**
     - Write\ :sub:`2` updates data on `P`\ :sub:`new` that is
       equivalent to after Write\ :sub:`1` followed by rollback of Write\
       :sub:`1`.
   * - |checkmark| **Writes follow reads**
     - Write\ :sub:`2` updates data on `P`\ :sub:`new` that
       reflects a state after Read\ :sub:`1` (meaning that an
       earlier state reflects the data read by Read\ :sub:`1`).

### Read Concern `"local"` and Write concern `{w: 1}`

The use of read concern :readconcern:`"local"` and write concern :writeconcern:`{ w: 1 } <\<number\>>` in a causally consistent session cannot guarantee causal consistency.

|xmark| Read own writes  |xmark| Monotonic reads  |xmark| Monotonic writes  |xmark| Writes follow reads

This combination may satisfy all four causal consistency guarantees in some situations, but not necessarily in all situations.

> **Note:** During this transient period, because both `P`\ :sub:`old` and
`P`\ :sub:`new` can fulfill writes with :writeconcern:`{ w: 1 } <\<number\>>` write concern, a
client session could issue the following sequence of operations
successfully but not be causally consistent:
.. list-table::
   :header-rows: 1
   * - Sequence
     - Example
   * - | 1. Write\ :sub:`1` with write concern :writeconcern:`{ w: 1 } <\<number\>>`  to  `P`\ :sub:`old`
       | 2. Read\ :sub:`1` with read concern :readconcern:`"local"` to `S`\ :sub:`1`
       | 3. Write\ :sub:`2` with write concern :writeconcern:`{ w: 1 } <\<number\>>` to `P`\ :sub:`new`
       |
       | 4. Read\ :sub:`2` with read concern :readconcern:`"local"` to `S`\ :sub:`3`
     - | For item `A`, update `qty` to `50`.
       | Read item `A`.
       | For items with `qty` less than or equal to `50`,
       | update `restock` to `true`.
       | Read item `A`.
.. figure:: /images/causal-rc-local-wc-1.svg
   :alt: State of data with two primaries using read concern local and write concern 1
   :figwidth: 450px
.. list-table::
   :class: no-outer-border
   :widths: 20 80
   * - |xmark| Read own writes
     - Read\ :sub:`2` reads data from `S`\ :sub:`3` that only
       reflects a state after Write\ :sub:`2` and not Write\ :sub:`1`
       followed by Write\ :sub:`2`.
   * - |xmark| Monotonic reads
     - Read\ :sub:`2` reads data from `S`\ :sub:`3` that doesn't
       reflect a state after Read\ :sub:`1` (meaning that an earlier
       state doesn't reflect the data read by Read\ :sub:`1`).
   * - |xmark| Monotonic writes
     - Write\ :sub:`2` updates data on `P`\ :sub:`new` that does
       not reflect a state after Write\ :sub:`1`.
   * - |xmark| Write follow read
     - Write\ :sub:`2` updates data on `P`\ :sub:`new` that does
       not reflect a state after Read\ :sub:`1` (meaning that an
       earlier state doesn't reflect the data read by Read\
       :sub:`1`).

### Read Concern `"local"` and Write concern `"majority"`

The use of read concern :readconcern:`"local"` and write concern :writeconcern:`"majority"` in a causally consistent session provides the following causal consistency guarantees:

|xmark| Read own writes  |xmark| Monotonic reads  |checkmark| Monotonic writes  |xmark| Writes follow reads

This combination may satisfy all four causal consistency guarantees in some situations, but not necessarily in all situations.

> **Note:** During this transient period, because only `P`\ :sub:`new` can
fulfill writes with  :writeconcern:`{ w: "majority" } <"majority">` write concern, a client
session could issue the following sequence of operations successfully
but not be causally consistent:
.. list-table::
   :header-rows: 1
   * - Sequence
     - Example
   * - | 1. Write\ :sub:`1` with write concern :writeconcern:`"majority"`  to  `P`\ :sub:`new`
       | 2. Read\ :sub:`1` with read concern :readconcern:`"local"` to `S`\ :sub:`1`
       | 3. Write\ :sub:`2` with write concern :writeconcern:`"majority"`  to `P`\ :sub:`new`
       |
       | 4. Read\ :sub:`2` with read concern :readconcern:`"local"` to `S`\ :sub:`3`
     - | For item `A`, update `qty` to `50`.
       | Read item `A`.
       | For items with `qty` less than or equal to `50`,
       | update `restock` to `true`.
       | Read item `A`.
.. figure:: /images/causal-rc-local-wc-majority.svg
   :alt: State of data with two primaries using read concern local and write concern majority
   :figwidth: 550px
.. list-table::
   :class: no-outer-border
   :widths: 20 80
   * - |xmark| Read own writes.
     - Read\ :sub:`1` reads data from `S`\ :sub:`1` that doesn't
       reflect a state after Write\ :sub:`1`.
   * - |xmark| Monotonic reads.
     - Read\ :sub:`2` reads data from `S`\ :sub:`3` that doesn't
       reflect a state after Read\ :sub:`1` (meaning that an earlier
       state doesn't reflect the data read by Read\ :sub:`1`).
   * - |checkmark| Monotonic writes
     - Write\ :sub:`2` updates data on `P`\ :sub:`new` that
       reflects a state after Write\ :sub:`1`.
   * - |xmark| Write follow read.
     - Write\ :sub:`2` updates data on `P`\ :sub:`new` that does
       not reflect a state after Read\ :sub:`1` (meaning that an
       earlier state doesn't reflect the data read by Read\
       :sub:`1`).
