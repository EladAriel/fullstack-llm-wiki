---
type: "Framework Learn Page"
framework: "SQLAlchemy"
source_repo: "https://github.com/sqlalchemy/sqlalchemy"
source_branch: "main"
source_path: "doc/build/faq/installation.rst"
source_commit: "85cafd1a131fa8afeeeab23151940480b3fb0042"
source_commit_short: "85cafd1"
source_commit_date: "2026-08-28T20:17:49+00:00"
generated_at: "2026-08-29T09:39:27.542919Z"
---
# Installation

**contents:** :local:
    :class: faq
    :backlinks: none

.. _faq_asyncio_installation:

## I'm getting an error about greenlet not being installed when I try to use asyncio

The ``greenlet`` dependency is not install by default in the 2.1 series.
To install including ``greenlet``, you need to add the ``asyncio``
`setuptools extra <https://packaging.python.org/en/latest/tutorials/installing-packages/#installing-setuptools-extras>`_
to the ``pip install`` command:

**sourcecode:** text

    pip install sqlalchemy[asyncio]

For more background, see :ref:`asyncio_install`.


**seealso:** :ref:`asyncio_install`

