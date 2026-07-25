---
type: "Framework Learn Page"
framework: "FastAPI"
source_repo: "https://github.com/fastapi/fastapi.git"
source_branch: "master"
source_path: "docs/en/docs/external-links.md"
source_commit: "255b912928904e3ba5980425a54d6837c8bd1a1c"
source_commit_short: "255b9129"
source_commit_date: "2026-07-24T21:15:37Z"
generated_at: "2026-07-25T11:50:10Z"
---

---
include_yaml:
  topic_repos: data/topic_repos.yml
---

# External Links

**FastAPI** has a great community constantly growing.

There are many posts, articles, tools, and projects related to **FastAPI**.

You could easily use a search engine or video platform to find many resources related to FastAPI.

/// note

Before, this page used to list links to external articles.

But now that FastAPI is the backend framework with the most GitHub stars across languages, and the most starred and used framework in Python, it no longer makes sense to attempt to list all articles written about it.

///

## GitHub Repositories

Most starred [GitHub repositories with the topic `fastapi`](https://github.com/topics/fastapi):

{% for repo in topic_repos.repos %}

<a href={{repo.html_url}} target="_blank">★ {{repo.stars}} - {{repo.name}}</a> by <a href={{repo.owner_html_url}} target="_blank">@{{repo.owner_login}}</a>.

{% endfor %}
