---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/security-mongodb-configuration.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.560426Z"
---
.. _ip-binding:

# IP Binding in Self-Managed Deployments

.. default-domain:: mongodb

**meta:** :keywords: on-prem
   :description: Configure IP binding for `mongod` and `mongos` to ensure secure access on trusted networks, using options like `net.bindIpAll` for broader address binding.

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Overview

MongoDB binaries, :binary:`mongod` and :binary:`mongos`, bind to
localhost by default. If the :setting:`net.ipv6` configuration file
setting or the ``--ipv6`` command line option is set for the binary,
the binary additionally binds to the localhost IPv6 address.

## Considerations

**warning:** Make sure that your :binary:`~bin.mongod` and :binary:`~bin.mongos`
   instances are only accessible on trusted networks. If your system
   has more than one network interface, bind MongoDB programs to the
   private or internal network interface.

If the :setting:`net.ipv6` configuration file setting or the ``--ipv6``
command line option is set for the binary, the binary additionally
binds to the localhost IPv6 address.

**include:** /includes/fact-bind-to-all-ips.rst

**seealso:** - :ref:`security-firewalls`
   - :ref:`configuration-security`