---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/collation-locales-defaults.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

========================================

# Collation Locales and Default Parameters

.. include:: /includes/extracts/collation-description.rst

## Behavior

.. include:: /includes/collation-variants.rst

See the `collation page <collation>` for a full description of collation behavior and syntax.

## Supported Languages and Locales

MongoDB's collation feature supports the following languages. The following table lists the supported languages and the associated locales as defined by [ICU Locale ID](https://unicode-org.github.io/icu/userguide/locale/#locale). [#missing-locale]_

.. include:: /includes/collation-locale-table.rst

> **Tip:** To explicitly specify simple binary comparison, specify `locale`
value of `"simple"`. `simple` is the default.

To request support for a locale, please file a JIRA ticket with the [Server project](https://jira.mongodb.org/browse/SERVER)

## Collation Default Parameters

A collation document contains several `optional parameters<collation-document-fields>` in addition to the required `locale` parameter. Depending on which `locale` you use, the default parameters may be different. See the `collation page <collation>` for a full description of collation syntax.

The following default parameters are consistent across all locales:

- `caseLevel : false`
- `strength : 3`
- `numericOrdering : false`
- `maxVariable : punct`
The default collation is `locale: "simple"`.

The following table shows the default collation parameters which may vary across different locales:

.. include:: /includes/collation-defaults-table.rst
