---
type: "Framework Learn Page"
framework: "FastAPI"
source_repo: "https://github.com/fastapi/fastapi.git"
source_branch: "master"
source_path: "docs/en/docs/advanced/wsgi.md"
source_commit: "0cb4a8e284b450abbccb71c543ad7757de46c0b2"
source_commit_short: "0cb4a8e2"
source_commit_date: "2026-06-20T16:31:34Z"
generated_at: "2026-06-21T07:06:10Z"
---

# Including WSGI - Flask, Django, others { #including-wsgi-flask-django-others }

You can mount WSGI applications as you saw with [Sub Applications - Mounts](sub-applications.md), [Behind a Proxy](behind-a-proxy.md).

For that, you can use the `WSGIMiddleware` and use it to wrap your WSGI application, for example, Flask, Django, etc.

## Using `WSGIMiddleware` { #using-wsgimiddleware }

/// note

This requires installing `a2wsgi` for example with `pip install a2wsgi`.

///

You need to import `WSGIMiddleware` from `a2wsgi`.

Then wrap the WSGI (e.g. Flask) app with the middleware.

And then mount that under a path.

{* ../../docs_src/wsgi/tutorial001_py310.py hl[1,3,23] *}

/// note

Previously, it was recommended to use `WSGIMiddleware` from `fastapi.middleware.wsgi`, but it is now deprecated.

It's advised to use the `a2wsgi` package instead. The usage remains the same.

Just ensure that you have the `a2wsgi` package installed and import `WSGIMiddleware` correctly from `a2wsgi`.

///

## Check it { #check-it }

Now, every request under the path `/v1/` will be handled by the Flask application.

And the rest will be handled by **FastAPI**.

If you run it and go to [http://localhost:8000/v1/](http://localhost:8000/v1/) you will see the response from Flask:

```txt
Hello, World from Flask!
```

And if you go to [http://localhost:8000/v2](http://localhost:8000/v2) you will see the response from FastAPI:

```JSON
{
    "message": "Hello World"
}
```
