---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/external/togetherai.mdx"
source_commit: "607c855f787d6cc66e83692874bf90f880a08d62"
source_commit_short: "607c855"
source_commit_date: "2026-08-25T19:59:29-04:00"
generated_at: "2026-08-29T09:39:42.278731Z"
---
# Helicone Observability

Helicone is a streamlined tool that seamlessly integrates into any existing codebase, regardless of the programming language. This is achieved by providing a new base URL endpoint that proxies the traffic to TogetherAI.

Helicone offers a range of features, primarily used for:

- Data Ingestion and normalization with other LLM providers
- Prompt application analytics and insights
- Caching to economize on requests

For more information, visit Helicone's [documentation](https://docs.helicone.ai) or [contact us](https://helicone.ai/contact).

# Getting Started

### 1. Create a Helicone Account

Start by creating a Helicone account and obtaining your API key from the [Helicone Dashboard](https://www.helicone.ai/signin).

### 2. Implement Helicone

Wherever you use the TogetherAI API, simply substitute the base URL with `https://together.helicone.ai` and include the `Helicone-Auth` header with your Helicone API key.

```python
TOGETHER_API_KEY = os.environ.get("TOGETHER_API_KEY")
HELICONE_API_KEY = os.environ.get("HELICONE_API_KEY")

client = OpenAI(
  api_key=TOGETHER_API_KEY,
  # base_url='https://api.together.xyz/v1', Old
  base_url='https://together.helicone.ai/v1', # Change to Helicone
  default_headers={
    "Helicone-Auth": f"Bearer {HELICONE_API_KEY}", # Add Helicone API Key
  }
)
```

### 3. Start Utilizing Helicone

Congratulations! You are now using Helicone to proxy your requests to TogetherAI. You can now leverage Helicone's features such as data ingestion, caching, and analytics.
