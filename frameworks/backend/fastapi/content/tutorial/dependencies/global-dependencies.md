---
type: "Framework Learn Page"
framework: "FastAPI"
source_repo: "https://github.com/fastapi/fastapi.git"
source_branch: "master"
source_path: "docs/en/docs/tutorial/dependencies/global-dependencies.md"
source_commit: "49033471594ea5d99a80abdf1043231b7791ee49"
source_commit_short: "4903347"
source_commit_date: "2026-08-26T17:53:57+00:00"
generated_at: "2026-08-29T09:38:49.727314Z"
---
# Global Dependencies { #global-dependencies }

For some types of applications you might want to add dependencies to the whole application.

Similar to the way you can [add `dependencies` to the *path operation decorators*](dependencies-in-path-operation-decorators.md), you can add them to the `FastAPI` application.

In that case, they will be applied to all the *path operations* in the application:

{* ../../docs_src/dependencies/tutorial012_an_py310.py hl[17] *}


And all the ideas in the section about [adding `dependencies` to the *path operation decorators*](dependencies-in-path-operation-decorators.md) still apply, but in this case, to all of the *path operations* in the app.

## Dependencies for groups of *path operations* { #dependencies-for-groups-of-path-operations }

Later, when reading about how to structure bigger applications ([Bigger Applications - Multiple Files](../../tutorial/bigger-applications.md)), possibly with multiple files, you will learn how to declare a single `dependencies` parameter for a group of *path operations*.
