---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/server-side-javascript.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

:orphan:

======================

# Server-side JavaScript

> **Important:** .. include:: /includes/server-side-js-deprecated.rst
`Map-reduce <map-reduce>` is deprecated starting in MongoDB 5.0.

MongoDB provides the following commands, methods, and operator that perform server-side execution of JavaScript code:

- :dbcommand:`mapReduce` and the corresponding :binary:`~bin.mongosh`
method :method:`db.collection.mapReduce()`.  For more information, see `/core/map-reduce`.

- :query:`$where` operator that evaluates a JavaScript expression or a
function in order to query for documents.

- :group:`$accumulator` and :expression:`$function` aggregation
operations that allows users to define custom aggregation expressions.

You can also specify a JavaScript file to :binary:`~bin.mongosh` to run on the server. For more information, see `running-js-scripts-in-mongo-on-mongod-host`

.. include:: /includes/extracts/admonition-js-prevalence-methods.rst

If you do not need to perform server-side execution of JavaScript code, see `disable-server-side-js`.

.. include:: /includes/fact-selinux-server-side-js.rst

## Running `.js` files via a `mongosh` Instance on the Server

You can specify a JavaScript (`.js`) file to :binary:`~bin.mongosh` to execute the file on the server. This is a good technique for performing batch administrative work. When you run :binary:`~bin.mongosh` on the server, connecting via the localhost interface, the connection is fast with low latency.

## Disable Server-Side Execution of JavaScript

.. include:: /includes/fact-disable-javascript-with-noscript.rst

## Behavior

### Concurrency

Refer to the individual method or operator documentation for any concurrency information. See also the `concurrency table <faq-concurrency-operations-locks>`.

### Unsupported Array and String Functions

.. include:: /includes/fact-6.0-js-engine-change.rst
