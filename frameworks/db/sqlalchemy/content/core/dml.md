---
type: "Framework Learn Page"
framework: "SQLAlchemy"
source_repo: "https://github.com/sqlalchemy/sqlalchemy"
source_branch: "main"
source_path: "doc/build/core/dml.rst"
source_commit: "85cafd1a131fa8afeeeab23151940480b3fb0042"
source_commit_short: "85cafd1"
source_commit_date: "2026-08-28T20:17:49+00:00"
generated_at: "2026-08-29T09:39:27.509978Z"
---
# Insert, Updates, Deletes

INSERT, UPDATE and DELETE statements build on a hierarchy starting
with :class:`.UpdateBase`.   The :class:`_expression.Insert` and :class:`_expression.Update`
constructs build on the intermediary :class:`.ValuesBase`.

**currentmodule:** sqlalchemy.sql.expression

.. _dml_foundational_consructors:

## DML Foundational Constructors

Top level "INSERT", "UPDATE", "DELETE" constructors.

**autofunction:** delete

**autofunction:** insert

**autofunction:** update


## DML Class Documentation Constructors

Class documentation for the constructors listed at
:ref:`dml_foundational_consructors`.

**autoclass:** Delete
   :members:

   .. automethod:: Delete.where

   .. automethod:: Delete.filter

   .. automethod:: Delete.filter_by

   .. automethod:: Delete.with_dialect_options

   .. automethod:: Delete.returning

   .. automethod:: Delete.ext

   .. automethod:: Delete.apply_syntax_extension_point

**autoclass:** Insert
   :members:

   .. automethod:: Insert.with_dialect_options

   .. automethod:: Insert.values

   .. automethod:: Insert.returning

   .. automethod:: Insert.ext

   .. automethod:: Insert.apply_syntax_extension_point

**autoclass:** Update
   :members:

   .. automethod:: Update.returning

   .. automethod:: Update.where

   .. automethod:: Update.filter

   .. automethod:: Update.filter_by

   .. automethod:: Update.with_dialect_options

   .. automethod:: Update.values

   .. automethod:: Update.ext

   .. automethod:: Update.apply_syntax_extension_point

**autoclass:** sqlalchemy.sql.expression.UpdateBase
   :members:

**autoclass:** sqlalchemy.sql.expression.ValuesBase
   :members:


