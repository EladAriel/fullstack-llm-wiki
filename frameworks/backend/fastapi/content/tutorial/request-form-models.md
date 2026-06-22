---
type: "Framework Learn Page"
framework: "FastAPI"
source_repo: "https://github.com/fastapi/fastapi.git"
source_branch: "master"
source_path: "docs/en/docs/tutorial/request-form-models.md"
source_commit: "0cb4a8e284b450abbccb71c543ad7757de46c0b2"
source_commit_short: "0cb4a8e2"
source_commit_date: "2026-06-20T16:31:34Z"
generated_at: "2026-06-21T07:06:10Z"
---

# Form Models { #form-models }

You can use **Pydantic models** to declare **form fields** in FastAPI.

/// note

To use forms, first install [`python-multipart`](https://github.com/Kludex/python-multipart).

Make sure you create a [virtual environment](../virtual-environments.md), activate it, and then install it, for example:

```console
$ pip install python-multipart
```

///

/// note

This is supported since FastAPI version `0.113.0`. 🤓

///

## Pydantic Models for Forms { #pydantic-models-for-forms }

You just need to declare a **Pydantic model** with the fields you want to receive as **form fields**, and then declare the parameter as `Form`:

{* ../../docs_src/request_form_models/tutorial001_an_py310.py hl[9:11,15] *}

**FastAPI** will **extract** the data for **each field** from the **form data** in the request and give you the Pydantic model you defined.

## Check the Docs { #check-the-docs }

You can verify it in the docs UI at `/docs`:

<div class="screenshot">
<img src="/img/tutorial/request-form-models/image01.png">
</div>

## Forbid Extra Form Fields { #forbid-extra-form-fields }

In some special use cases (probably not very common), you might want to **restrict** the form fields to only those declared in the Pydantic model. And **forbid** any **extra** fields.

/// note

This is supported since FastAPI version `0.114.0`. 🤓

///

You can use Pydantic's model configuration to `forbid` any `extra` fields:

{* ../../docs_src/request_form_models/tutorial002_an_py310.py hl[12] *}

If a client tries to send some extra data, they will receive an **error** response.

For example, if the client tries to send the form fields:

* `username`: `Rick`
* `password`: `Portal Gun`
* `extra`: `Mr. Poopybutthole`

They will receive an error response telling them that the field `extra` is not allowed:

```json
{
    "detail": [
        {
            "type": "extra_forbidden",
            "loc": ["body", "extra"],
            "msg": "Extra inputs are not permitted",
            "input": "Mr. Poopybutthole"
        }
    ]
}
```

## Summary { #summary }

You can use Pydantic models to declare form fields in FastAPI. 😎
