---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/crud/ruby-delete-documents.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

This page uses the following :ruby:`MongoDB Ruby Driver </>` methods:

- :ruby-api:`Mongo::Collection#delete_many()
<Collection.html#delete_many-instance_method>`

- :ruby-api:`Mongo::Collection#delete_one()
<Collection.html#delete_one-instance_method>`

.. include:: /includes/driver-examples/examples-intro.rst

## Delete All Documents

To delete all documents from a collection, pass an empty `filter<document-query-filter>` document `{}` to the :ruby-api:`Mongo::Collection#delete_many() <Collection.html#delete_many-instance_method>` method.

.. include:: /includes/fact-delete-all-inventory.rst

Upon successful execution, the :ruby-api:`delete_many() <Collection.html#delete_many-instance_method>` method returns an instance of :ruby-api:`Mongo::Operation::Result <Operation/Result.html>`, whose `deleted_count` attribute contains the number of documents that matched the filter.

## Delete All Documents that Match a Condition

.. include:: /includes/fact-delete-condition-inventory.rst

To specify equality conditions, use `<field> => <value>` expressions in the `query filter document <document-query-filter>`:

```ruby
{ <field1> => <value1>, ... }
```

A `query filter document <document-query-filter>` can use the `query operators <query-selectors>` to specify conditions in the following form:

```ruby
{ <field1> => { <operator1> => <value1> }, ... }
```

To delete all documents that match a deletion criteria, pass a `filter <document-query-filter>` parameter to the :ruby-api:`delete_many() <Collection.html#delete_many-instance_method>` method.

.. include:: /includes/fact-remove-condition-inv-example.rst

Upon successful execution, the :ruby-api:`delete_many() <Collection.html#delete_many-instance_method>` method returns an instance of :ruby-api:`Mongo::Operation::Result <Operation/Result.html>`, whose `deleted_count` attribute contains the number of documents that matched the filter.

## Delete Only One Document that Matches a Condition

To delete at most a single document that matches a specified filter (even though multiple documents may match the specified filter) use the :ruby-api:`Mongo::Collection#delete_one() <Collection.html#delete_one-instance_method>` method.

.. include:: /includes/fact-remove-one-condition-inv-example.rst

> **Seealso:** - :ruby-api:`Mongo::Collection#delete_many()
  <Collection.html#delete_many-instance_method>`
- :ruby-api:`Mongo::Collection#delete_one()
  <Collection.html#delete_one-instance_method>`
