---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/csfle/tutorials/kmip/kmip-automatic.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
