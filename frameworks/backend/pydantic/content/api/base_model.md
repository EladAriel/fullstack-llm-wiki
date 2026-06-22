---
type: "Framework Learn Page"
framework: "pydantic"
source_repo: "https://github.com/pydantic/pydantic"
source_branch: "main"
source_path: "docs/api/base_model.md"
source_commit: "363728fe0b353db1a1fcb44aac5c38fd96a8cc20"
source_commit_short: "363728fe"
source_commit_date: "2026-06-20T11:20:58+01:00"
generated_at: "2026-06-21T11:37:01Z"
---

Pydantic models are simply classes which inherit from `BaseModel` and define fields as annotated attributes.

::: pydantic.BaseModel
    options:
        show_root_heading: true
        merge_init_into_class: false
        group_by_category: false
        # explicit members list so we can set order and include `__init__` easily
        members:
          - __init__
          - model_config
          - model_fields
          - model_computed_fields
          - __pydantic_core_schema__
          - model_extra
          - model_fields_set
          - model_construct
          - model_copy
          - model_dump
          - model_dump_json
          - model_json_schema
          - model_parametrized_name
          - model_post_init
          - model_rebuild
          - model_validate
          - model_validate_json
          - model_validate_strings

::: pydantic.create_model
    options:
        show_root_heading: true
