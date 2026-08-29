---
type: "Framework Learn Page"
framework: "FastAPI"
source_repo: "https://github.com/fastapi/fastapi.git"
source_branch: "master"
source_path: "docs/en/docs/how-to/authentication-error-status-code.md"
source_commit: "49033471594ea5d99a80abdf1043231b7791ee49"
source_commit_short: "4903347"
source_commit_date: "2026-08-26T17:53:57+00:00"
generated_at: "2026-08-29T09:38:49.709923Z"
---
# Use Old 403 Authentication Error Status Codes { #use-old-403-authentication-error-status-codes }

Before FastAPI version `0.122.0`, when the integrated security utilities returned an error to the client after a failed authentication, they used the HTTP status code `403 Forbidden`.

Starting with FastAPI version `0.122.0`, they use the more appropriate HTTP status code `401 Unauthorized`, and return a sensible `WWW-Authenticate` header in the response, following the HTTP specifications, [RFC 7235](https://datatracker.ietf.org/doc/html/rfc7235#section-3.1), [RFC 9110](https://datatracker.ietf.org/doc/html/rfc9110#name-401-unauthorized).

But if for some reason your clients depend on the old behavior, you can revert to it by overriding the method `make_not_authenticated_error` in your security classes.

For example, you can create a subclass of `HTTPBearer` that returns a `403 Forbidden` error instead of the default `401 Unauthorized` error:

{* ../../docs_src/authentication_error_status_code/tutorial001_an_py310.py hl[9:13] *}

/// tip

Notice that the function returns the exception instance, it doesn't raise it. The raising is done in the rest of the internal code.

///
