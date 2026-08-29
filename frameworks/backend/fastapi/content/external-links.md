---
type: "Framework Learn Page"
framework: "FastAPI"
source_repo: "https://github.com/fastapi/fastapi.git"
source_branch: "master"
source_path: "docs/en/docs/external-links.md"
source_commit: "49033471594ea5d99a80abdf1043231b7791ee49"
source_commit_short: "4903347"
source_commit_date: "2026-08-26T17:53:57+00:00"
generated_at: "2026-08-29T09:38:49.700411Z"
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
