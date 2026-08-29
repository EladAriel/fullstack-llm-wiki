---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/rs.addArb.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.898336Z"
---
# rs.addArb() (mongosh method)

**meta:** :description: Add an arbiter to a replica set using `rs.addArb(host)` and ensure proper IP binding for secure access.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Description

**method:** rs.addArb(host)

   Adds a new :term:`arbiter` to an existing replica set.

   ``rs.add(<host>, true)`` is functionally the same as 
   ``rs.addArb(<host>)``. You can use these commands interchangeably.

   .. include:: /includes/admonition-multiple-arbiters.rst

   The :method:`rs.addArb()` method takes the following parameter:


   .. list-table::
      :header-rows: 1
      :widths: 20 20 80
   
      * - Parameter
   
        - Type
   
        - Description
   
      * - ``host``
   
        - string
   
        - Specifies the hostname and optionally the port number of the arbiter
          member to add to replica set.

## Compatibility

This method is available in deployments hosted in the following environments:

**include:** /includes/fact-environments-onprem-only.rst

## IP Binding

**include:** /includes/fact-default-bind-ip.rst

**include:** /includes/important-hostnames.rst