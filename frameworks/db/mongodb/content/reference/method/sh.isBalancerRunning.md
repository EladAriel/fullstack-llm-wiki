---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sh.isBalancerRunning.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.930070Z"
---
# sh.isBalancerRunning() (mongosh method)

**meta:** :description: Check if the balancer is running in MongoDB and view the status document with `sh.isBalancerRunning()`.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**method:** sh.isBalancerRunning()

   Returns a document describing the status of the balancer.


   .. |dbcommand| replace:: :dbcommand:`balancerStatus` command
   .. include:: /includes/fact-mongosh-shell-method-alt.rst

## Compatibility

This method is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-atlas-support-no-free.rst

**include:** /includes/fact-environments-onprem-only.rst

## Output Document

The following is an example of a document returned by the command:

.. code-block:: json
   :copyable: false

   {
     mode: 'full',
     inBalancerRound: false,
     numBalancerRounds: Long("1143"),
     ok: 1,
     '$clusterTime': {
        clusterTime: Timestamp({ t: 1639753724, i: 3 }),
        signature: {
           hash: Binary(Buffer.from("0000000000000000000000000000000000000000", "hex"), 0),
           keyId: Long("0")
        }
     },
     operationTime: Timestamp({ t: 1639753724, i: 3 })
   }

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Field
     - Description

   * - ``mode``

     - String that specifies whether the balancer thread is running
       or stopped. Possible values are:

       - "full"
           Balancer thread is running but not necessarily in a
           balancing round.

       - "off"
           Balancer thread is stopped. Chunk balancing cannot occur in
           this mode.
   
   * - ``inBalancerRound``

     - Boolean that specifies if the balancer is currently in a
       balancing round.

   * - ``numBalancerRounds``

     - Number of balancer rounds which have occurred since the
       config servers were started. This value is reset to 0 when 
       the config servers are restarted.

   * - ``ok``

     - See :ref:`Command Response <command-response>`.

   * - ``$clusterTime``

     - See :ref:`Command Response <command-response>`.

   * - ``operationTime``

     - See :ref:`Command Response <command-response>`.

**seealso:** - :method:`sh.enableBalancing()`
   - :method:`sh.disableBalancing()`
   - :method:`sh.getBalancerState()`
   - :method:`sh.setBalancerState()`
   - :method:`sh.startBalancer()`
   - :method:`sh.stopBalancer()`
   - :method:`sh.waitForBalancer()`
   - :method:`sh.waitForBalancerOff()`