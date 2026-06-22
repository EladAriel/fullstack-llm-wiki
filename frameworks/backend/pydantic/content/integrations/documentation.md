---
type: "Framework Learn Page"
framework: "pydantic"
source_repo: "https://github.com/pydantic/pydantic"
source_branch: "main"
source_path: "docs/integrations/documentation.md"
source_commit: "363728fe0b353db1a1fcb44aac5c38fd96a8cc20"
source_commit_short: "363728fe"
source_commit_date: "2026-06-20T11:20:58+01:00"
generated_at: "2026-06-21T11:37:01Z"
---

Pydantic uses [MkDocs](https://www.mkdocs.org/) for documentation, together with
[mkdocstrings](https://mkdocstrings.github.io/). As such, you can make use of Pydantic's
Sphinx object inventory to cross-reference the Pydantic API documentation.

=== "Sphinx"

    In your [Sphinx configuration](https://www.sphinx-doc.org/en/master/usage/configuration.html),
    add the following to the [`intersphinx` extension configuration](https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html#configuration):

    ```python {test="skip"}
    intersphinx_mapping = {
        'pydantic': ('https://pydantic.dev/docs/validation/latest', None),  # (1)!
    }
    ```

    1. You can also use `dev` instead of `latest` to target the latest documentation build, up to date
       with the [`main`](https://github.com/pydantic/pydantic/tree/main) branch.

=== "mkdocstrings"

    In your [MkDocs configuration](https://www.mkdocs.org/user-guide/configuration/), add the following
    import to your [mkdocstrings plugin configuration](https://mkdocstrings.github.io/usage/#cross-references-to-other-projects-inventories):

    ```yaml
    plugins:
    - mkdocstrings:
        handlers:
          python:
            import:
            - https://pydantic.dev/docs/validation/latest/objects.inv  # (1)!
    ```

    1. You can also use `dev` instead of `latest` to target the latest documentation build, up to date
       with the [`main`](https://github.com/pydantic/pydantic/tree/main) branch.
