---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/csfle/tutorials/kmip/kmip-automatic.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

===========================================================

# Use Automatic {+csfle+} with KMIP

## Overview

This guide shows you how to build a {+csfle+} ({+csfle-abbrev+})-enabled application using a Key Management Interoperability Protocol (KMIP)-compliant key provider.

After you complete the steps in this guide, you should have:

- A {+cmk-long+} hosted on a {+kmip-kms+}.
- A working client application that inserts {+in-use-docs+}
using your {+cmk-long+}.

## Before You Get Started

.. include:: /includes/set-up-section.rst

.. include:: /includes/fact-csfle-placeholder.rst

Select the programming language for which you want to see code examples for from the dropdown menu below.

## Learn More

To learn how {+csfle-abbrev+} works, see `<csfle-fundamentals>`.

To learn more about the topics mentioned in this guide, see the following links:

- Learn more about CSFLE components on the `Reference <csfle-reference>` page.
- Learn how {+cmk-long+}s and {+dek-long+}s work on the `<qe-reference-keys-key-vaults>` page.
- See how KMS Providers manage your CSFLE keys on the `<qe-fundamentals-kms-providers>` page.
