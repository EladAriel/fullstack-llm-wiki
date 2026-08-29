---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/develop/ai/search-and-query/advanced-concepts/phonetic_matching.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.829135Z"
---
# Phonetic_Matching

---
aliases:
- /develop/interact/search-and-query/advanced-concepts/phonetic_matching
categories:
- docs
- develop
- stack
- oss
- rs
- rc
- oss
- kubernetes
- clients
description: Details about phonetic matching capabilities
linkTitle: Phonetic
title: Phonetic matching
weight: 52
---

Phonetic matching, for example "Jon" vs. "John", allows searching for terms based on their pronunciation. This capability can be a useful tool when searching for names of people.

Phonetic matching is based on the use of a phonetic algorithm. A phonetic algorithm transforms the input term to an approximate representation of its pronunciation. This allows terms to be indexed and searched by their pronunciation.

As of v1.4, Redis Search, which is included in Redis Open Source, provides phonetic matching of text fields specified with the `PHONETIC` attribute. This causes the terms in such fields to be indexed both by their textual value as well as their phonetic approximation.

Performing a search on `PHONETIC` fields will, by default, also return results for phonetically similar terms. This behavior can be controlled with the [`$phonetic` query attribute]({{< relref "/develop/ai/search-and-query/advanced-concepts/query_attributes" >}}).

## Phonetic algorithms support

Redis currently supports a single phonetic algorithm, the [Double Metaphone](https://en.wikipedia.org/wiki/Metaphone#Double_Metaphone) (DM). It uses the implementation at the [slacy/double-metaphone GitHub site](https://github.com/slacy/double-metaphone), which provides general support for Latin languages.
