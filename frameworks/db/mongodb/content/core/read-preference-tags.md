---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/read-preference-tags.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=============================

# Read Preference Tag Set Lists

If a replica set member or members are associated with :rsconf:`~members[n].tags`, you can specify a tag set list (array of tag sets) in the read preference to target those members.

To `configure <replica-set-configuration-document>` a member with tags, set :rsconf:`members[n].tags` to a document that contains the tag name and value pairs. The value of the tags must be a string.

```javascript
{ "<tag1>": "<string1>", "<tag2>": "<string2>",... }
```

Then, you can include a tag set list in the read preference to target tagged members. A tag set list is an array of tag sets, where each tag set contains one or more tag/value pairs.

```javascript
[ { "<tag1>": "<string1>", "<tag2>": "<string2>",... }, ... ]
```

To find replica set members, MongoDB tries each document in succession until a match is found.  See `read-pref-order-matching` for details.

For example, if a secondary member has the following :rsconf:`members[n].tags`:

```javascript
{ "region": "South", "datacenter": "A" }
```

Then, the following tag set lists can direct read operations to the aforementioned secondary (or other members with the same tags):

```javascript
[ { "region": "South", "datacenter": "A" }, { } ]     // Find members with both tag values. If none are found, read from any eligible member.
[ { "region": "South" }, { "datacenter": "A" }, { } ] // Find members with the specified region tag. Only if not found, then find members with the specified datacenter tag. If none are found, read from any eligible member.
[ { "datacenter": "A" }, { "region": "South" }, { } ] // Find members with the specified datacenter tag. Only if not found, then find members with the specified region tag. If none are found, read from any eligible member.
[ { "region": "South" }, { } ]                        // Find members with the specified region tag value. If none are found, read from any eligible member.
[ { "datacenter": "A" }, { } ]                        // Find members with the specified datacenter tag value. If none are found, read from any eligible member.
[ { } ]                                               // Find any eligible member.
```

## Order of Tag Matching

If the tag set list contains multiple documents, MongoDB tries each document in succession until a match is found. Once a match is found, that tag set is used to find all eligible matching members, and the remaining tag sets are ignored. If no members match any of the tag sets, the read operation returns with an error.

> **Tip:** To avoid an error if no members match any of the tag specifications,
you can add an empty document `{ }` as the last element of the tag
set list to read from any eligible member.

For example, consider the following tag set list with three tag sets:

```javascript
[ { "region": "South", "datacenter": "A" },  { "rack": "rack-1" }, { } ]  
```

First, MongoDB tries to find members tagged with both `"region": "South"` and `"datacenter": "A"`.

```none
{ "region": "South", "datacenter": "A" }
```

- If a member is found, the remaining tag sets are not considered.
Instead, MongoDB uses this tag set to find all eligible members.

- Else, MongoDB tries to find members with the tags specified in the
second document

```none
  { "rack": "rack-1" }

- If a member is found tagged, the remaining tag set is not considered.
 Instead, MongoDB uses this tag set to find all eligible members.

- Else, the third document is considered. 

 .. code-block:: none
    :copyable: false

    { }

 The empty document matches any eligible member.
```

## Tag Set List and Read Preference Modes

Tags are not compatible with mode :readmode:`primary`, and in general, only apply when `selecting <replica-set-read-preference-behavior-member-selection>` a `secondary` member of a set for a read operation. However, the :readmode:`nearest` read mode, when combined with a tag set list, selects the matching member with the lowest network latency. This member may be a primary or secondary.

For information on the interaction between the `modes <replica-set-read-preference-modes>` and tag set lists, refer to the `specific read preference mode documentation <replica-set-read-preference-modes>`.

For information on configuring tag set lists, see the `/tutorial/configure-replica-set-tag-sets` tutorial.
