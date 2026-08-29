---
type: "Framework Learn Page"
framework: "Beanie"
source_repo: "https://github.com/BeanieODM/beanie"
source_branch: "main"
source_path: "docs/publishing.md"
source_commit: "aa290b5739b52c7f62e43e37724b63038d1e5a81"
source_commit_short: "aa290b5"
source_commit_date: "2026-08-07T10:16:44-06:00"
generated_at: "2026-08-29T09:38:56.937903Z"
---
# Publishing a New Version of Beanie

Beanie releases are created manually by the project owner, `roman-right`.
Merging a pull request or pushing to `main` never publishes a package.

## Repository and PyPI setup

Before the first manual release, configure these controls outside the
repository:

1. Keep `main` protected and do not grant release permissions to other users.
2. Create a GitHub environment named `pypi` and restrict deployments to
   `roman-right`.
3. In PyPI's Trusted Publisher settings for `beanie`, set the owner to
   `BeanieODM`, repository to `beanie`, workflow file to
   `github-actions-publish-project.yml`, and environment to `pypi`.

The workflow also checks the triggering GitHub account and runs only for
`roman-right`.

## Prepare a release

1. Create a release PR that updates all of the following to the same version:
   - `pyproject.toml` (`project.version`)
   - `beanie/__init__.py` (`__version__`)
   - `docs/changelog.md`
2. Merge the release PR after the test workflow succeeds.
3. On the merged commit, create and push an annotated tag whose name exactly
   matches the package version. For example:

   ```bash
   git tag -a 2.2.0 -m "Release 2.2.0"
   git push origin 2.2.0
   ```

## Publish to PyPI

1. Open the **Publish project** GitHub Actions workflow.
2. Select **Run workflow**.
3. Enter the exact annotated tag name, for example `2.2.0`, and run it from
   `main`.

The workflow rejects lightweight tags and tags outside `main` history. It then
checks out the tag, builds the package, and verifies that the wheel metadata
version matches the tag before publishing with PyPI Trusted Publishing.

## Create the GitHub release

After a successful PyPI publication, create the matching GitHub release from
the same tag.
