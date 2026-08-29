---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/clear-jumbo-flag.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.573820Z"
---
.. _clear-jumbo-flag:

# Clear ``jumbo`` Flag

**meta:** :description: Learn how to manually clear the `jumbo` flag from MongoDB chunks using split or refine shard key methods.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

If MongoDB cannot split a chunk that exceeds the :ref:`specified range
size <sharding-range-size>`, MongoDB labels the chunk as 
:ref:`jumbo <jumbo-chunks>`.

The following procedures outline the steps to manually clear the 
``jumbo`` flag.

## Procedures

.. _preferred-method-clear-jumbo:

### Divisible Chunks

The preferred manual way to clear the ``jumbo`` flag from a chunk is to
attempt to split the chunk. If the chunk is divisible, MongoDB removes
the flag upon successful split of the chunk.

**include:** /includes/steps/clear-jumbo-flag-preferred.rst

### Indivisible Chunks

In some instances, MongoDB cannot split the no-longer ``jumbo`` chunk,
such as a chunk with a range of single shard key value. As such, you
cannot split the chunk to clear the flag.

In such cases, you can either :ref:`change the shard key
<change-a-shard-key>` so that the chunk can become divisible or manually
clear the flag.

### Refine the Shard Key

MongoDB provides the :dbcommand:`refineCollectionShardKey` command. Using the
:dbcommand:`refineCollectionShardKey` command, you can refine a
collection's shard key by adding a suffix field or fields to the
existing key. By adding new field(s) to the shard key, indivisible
jumbo chunks can become divisible.

**include:** /includes/steps/clear-jumbo-flag-refine-key.rst

.. _clear-jumbo-flag-manually:

### Manually Clear the ``jumbo`` Flag for an Indivisible Chunk

To manually clear the ``jumbo`` flag, you can use the 
:dbcommand:`clearJumboFlag` command. If you clear the ``jumbo`` flag for a chunk 
that still exceeds the chunk size, MongoDB will re-label the chunk as ``jumbo`` 
when MongoDB tries to move the chunk.

**important:** Only use this method if the :ref:`preferred method 
   <preferred-method-clear-jumbo>` is *not* applicable.

To manually clear the flag, use the following steps: 

**include:** /includes/steps/clear-jumbo-flag-command.rst

**seealso:** :dbcommand:`refineCollectionShardKey`