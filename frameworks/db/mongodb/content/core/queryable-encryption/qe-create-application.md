---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/queryable-encryption/qe-create-application.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

========================================================================

# Create your {+qe+} Enabled Application

## Overview

This guide shows you how to build an application that implements {+qe+} to automatically encrypt and decrypt document fields.

After you complete the steps in this guide, you should have a working client application that is ready for inserting documents with fields encrypted with your {+cmk-long+}.

## Before You Start

Ensure you have completed the following prerequisite tasks before creating your application:

#. `Install a {+qe+} compatible driver and dependencies <qe-install>`

#. `Install and configure a query analysis component <qe-csfle-install-library>`

#. `Create a {+cmk-long+} <qe-create-cmk>`

If you are using `mongocryptd`, your application requires write permissions on the working directory to create the `mongocryptd.pid` file.

## Procedure

## Next Steps

After installing a driver and dependencies, creating a {+cmk-long+}, and creating your application, see `Overview: Use {+qe+} <qe-overview-use-qe>` to encrypt and query data.
