---
type: "Framework Learn Page"
framework: "FastAPI"
source_repo: "https://github.com/fastapi/fastapi.git"
source_branch: "master"
source_path: "docs/en/docs/how-to/graphql.md"
source_commit: "0cb4a8e284b450abbccb71c543ad7757de46c0b2"
source_commit_short: "0cb4a8e2"
source_commit_date: "2026-06-20T16:31:34Z"
generated_at: "2026-06-21T07:06:10Z"
---

# GraphQL { #graphql }

As **FastAPI** is based on the **ASGI** standard, it's very easy to integrate any **GraphQL** library also compatible with ASGI.

You can combine normal FastAPI *path operations* with GraphQL on the same application.

/// tip

**GraphQL** solves some very specific use cases.

It has **advantages** and **disadvantages** when compared to common **web APIs**.

Make sure you evaluate if the **benefits** for your use case compensate the **drawbacks**. 🤓

///

## GraphQL Libraries { #graphql-libraries }

Here are some of the **GraphQL** libraries that have **ASGI** support. You could use them with **FastAPI**:

* [Strawberry](https://strawberry.rocks/) 🍓
    * With [docs for FastAPI](https://strawberry.rocks/docs/integrations/fastapi)
* [Ariadne](https://ariadnegraphql.org/)
    * With [docs for FastAPI](https://ariadnegraphql.org/docs/fastapi-integration)
* [Tartiflette](https://tartiflette.io/)
    * With [Tartiflette ASGI](https://tartiflette.github.io/tartiflette-asgi/) to provide ASGI integration
* [Graphene](https://graphene-python.org/)
    * With [starlette-graphene3](https://github.com/ciscorn/starlette-graphene3)

## GraphQL with Strawberry { #graphql-with-strawberry }

If you need or want to work with **GraphQL**, [**Strawberry**](https://strawberry.rocks/) is the **recommended** library as it has the design closest to **FastAPI's** design, it's all based on **type annotations**.

Depending on your use case, you might prefer to use a different library, but if you asked me, I would probably suggest you try **Strawberry**.

Here's a small preview of how you could integrate Strawberry with FastAPI:

{* ../../docs_src/graphql_/tutorial001_py310.py hl[3,22,25] *}

You can learn more about Strawberry in the [Strawberry documentation](https://strawberry.rocks/).

And also the docs about [Strawberry with FastAPI](https://strawberry.rocks/docs/integrations/fastapi).

## Older `GraphQLApp` from Starlette { #older-graphqlapp-from-starlette }

Previous versions of Starlette included a `GraphQLApp` class to integrate with [Graphene](https://graphene-python.org/).

It was deprecated from Starlette, but if you have code that used it, you can easily **migrate** to [starlette-graphene3](https://github.com/ciscorn/starlette-graphene3), that covers the same use case and has an **almost identical interface**.

/// tip

If you need GraphQL, I still would recommend you check out [Strawberry](https://strawberry.rocks/), as it's based on type annotations instead of custom classes and types.

///

## Learn More { #learn-more }

You can learn more about **GraphQL** in the [official GraphQL documentation](https://graphql.org/).

You can also read more about each of those libraries described above in their links.
