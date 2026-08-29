---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/change-own-password-and-custom-data.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.631423Z"
---
.. _change-password-custom-data:

# Change Your Password and Custom Data

.. default-domain:: mongodb

**meta:** :keywords: on-prem
   :description: Change your password and custom data on self-managed deployments using appropriate privileges and commands.

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Overview

Users with appropriate privileges can change their own passwords and
custom data. :data:`Custom data <admin.system.users.customData>` stores
optional user information.

## Considerations

To generate a strong password for use in this procedure, you can use the
``openssl`` utility's ``rand`` command. For example, issue ``openssl
rand`` with the following options to create a base64-encoded string of 48
pseudo-random bytes:

.. code-block:: bash

   openssl rand -base64 48

.. _change-own-password-prereq:

## Prerequisites

**include:** /includes/access-change-own-password-and-custom-data.rst

**include:** /includes/steps/change-own-password-and-custom-data-prereq.rst

## Procedure

**include:** /includes/steps/change-own-password-and-custom-data.rst