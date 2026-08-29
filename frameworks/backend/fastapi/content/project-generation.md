---
type: "Framework Learn Page"
framework: "FastAPI"
source_repo: "https://github.com/fastapi/fastapi.git"
source_branch: "master"
source_path: "docs/en/docs/project-generation.md"
source_commit: "49033471594ea5d99a80abdf1043231b7791ee49"
source_commit_short: "4903347"
source_commit_date: "2026-08-26T17:53:57+00:00"
generated_at: "2026-08-29T09:38:49.702280Z"
---
# Full Stack FastAPI Template { #full-stack-fastapi-template }

Templates, while they typically come with a specific setup, are designed to be flexible and customizable. This allows you to modify and adapt them to your project's requirements, making them an excellent starting point. 🏁

You can use this template to get started, as it includes a lot of the initial setup, security, database and some API endpoints already done for you.

GitHub Repository: [Full Stack FastAPI Template](https://github.com/fastapi/full-stack-fastapi-template)

## Full Stack FastAPI Template - Technology Stack and Features { #full-stack-fastapi-template-technology-stack-and-features }

- ⚡ [**FastAPI**](https://fastapi.tiangolo.com) for the Python backend API.
  - 🧰 [SQLModel](https://sqlmodel.tiangolo.com) for the Python SQL database interactions (ORM).
  - 🔍 [Pydantic](https://pydantic.dev/docs/), used by FastAPI, for the data validation and settings management.
  - 💾 [PostgreSQL](https://www.postgresql.org) as the SQL database.
- 🚀 [React](https://react.dev) for the frontend.
  - 💃 Using TypeScript, hooks, Vite, and other parts of a modern frontend stack.
  - 🎨 [Tailwind CSS](https://tailwindcss.com) and [shadcn/ui](https://ui.shadcn.com) for the frontend components.
  - 🤖 An automatically generated frontend client.
  - 🧪 [Playwright](https://playwright.dev) for End-to-End testing.
  - 🦇 Dark mode support.
- 🐋 [Docker Compose](https://www.docker.com) for development and production.
- 🔒 Secure password hashing by default.
- 🔑 JWT (JSON Web Token) authentication.
- 📫 Email based password recovery.
- ✅ Tests with [Pytest](https://pytest.org).
- 📞 [Traefik](https://traefik.io) as a reverse proxy / load balancer.
- 🚢 Deployment instructions using Docker Compose, including how to set up a frontend Traefik proxy to handle automatic HTTPS certificates.
- 🏭 CI (continuous integration) and CD (continuous deployment) based on GitHub Actions.
