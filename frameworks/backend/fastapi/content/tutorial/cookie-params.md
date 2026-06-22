---
type: "Framework Learn Page"
framework: "FastAPI"
source_repo: "https://github.com/fastapi/fastapi.git"
source_branch: "master"
source_path: "docs/en/docs/tutorial/cookie-params.md"
source_commit: "0cb4a8e284b450abbccb71c543ad7757de46c0b2"
source_commit_short: "0cb4a8e2"
source_commit_date: "2026-06-20T16:31:34Z"
generated_at: "2026-06-21T07:06:10Z"
---

# Cookie Parameters { #cookie-parameters }

You can define Cookie parameters the same way you define `Query` and `Path` parameters.

## Import `Cookie` { #import-cookie }

First import `Cookie`:

{* ../../docs_src/cookie_params/tutorial001_an_py310.py hl[3] *}

## Declare `Cookie` parameters { #declare-cookie-parameters }

Then declare the cookie parameters using the same structure as with `Path` and `Query`.

You can define the default value as well as all the extra validation or annotation parameters:

{* ../../docs_src/cookie_params/tutorial001_an_py310.py hl[9] *}

/// note | Technical Details

`Cookie` is a "sister" class of `Path` and `Query`. It also inherits from the same common `Param` class.

But remember that when you import `Query`, `Path`, `Cookie` and others from `fastapi`, those are actually functions that return special classes.

///

/// note

To declare cookies, you need to use `Cookie`, because otherwise the parameters would be interpreted as query parameters.

///

/// note

Have in mind that, as **browsers handle cookies** in special ways and behind the scenes, they **don't** easily allow **JavaScript** to touch them.

If you go to the **API docs UI** at `/docs` you will be able to see the **documentation** for cookies for your *path operations*.

But even if you **fill the data** and click "Execute", because the docs UI works with **JavaScript**, the cookies won't be sent, and you will see an **error** message as if you didn't write any values.

///

## Recap { #recap }

Declare cookies with `Cookie`, using the same common pattern as `Query` and `Path`.
