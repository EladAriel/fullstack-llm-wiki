---
type: "Framework Learn Page"
framework: "FastAPI"
source_repo: "https://github.com/fastapi/fastapi.git"
source_branch: "master"
source_path: "docs/en/docs/virtual-environments.md"
source_commit: "49033471594ea5d99a80abdf1043231b7791ee49"
source_commit_short: "4903347"
source_commit_date: "2026-08-26T17:53:57+00:00"
generated_at: "2026-08-29T09:38:49.702429Z"
---
# Virtual Environments { #virtual-environments }

When you work with Python projects, you should use a **virtual environment** to isolate the packages installed for each project.

For FastAPI projects, I recommend using [uv](https://docs.astral.sh/uv/) to manage the project, its dependencies, and its virtual environment.

## Create a Project { #create-a-project }

Install `uv` using the [official installation guide](https://docs.astral.sh/uv/getting-started/installation/), and then create a project:

<div class="termy">

```console
$ uv init awesome-project --bare
$ cd awesome-project
$ uv add "fastapi[standard]"
```

</div>

`uv` creates a virtual environment for the project automatically. You don't need to create or activate one yourself.

Run commands inside the project environment with `uv run`, for example:

<div class="termy">

```console
$ uv run fastapi dev
```

</div>

## Learn More { #learn-more }

Read the [Virtual Environments guide](https://tiangolo.com/guides/virtual-environments/) to learn how virtual environments work underneath, including activation and the alternative `python -m venv` and `pip` workflow.
