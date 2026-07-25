---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/faq/enable-stream-usage.mdx"
source_commit: "67df07b8d807a960f2e53d9ec2a9c49513ca2379"
source_commit_short: "67df07b"
source_commit_date: "2026-07-21T05:35:38-07:00"
generated_at: "2026-07-25T19:08:22.192618Z"
---
# Enable Stream Usage

---
title: "Incorrect Cost Calculation While Streaming?"
description: "Learn how to accurately calculate costs when using streaming features."
---

To accurately calculate costs when using streaming features, you can either include a `include_usage` key in the body of your request or use the Helicone header.

### Method 1: Request Body

<CodeGroup>

```python Python
client.chat.completions.create(
    model="gpt-4o",
    max_tokens=100,
    messages=[
        {"role": "system", "content": "You are a great storyteller."},
        {"role": "user", "content": "Once upon a time in a galaxy far, far away..."}
    ],
    stream=True,
    stream_options={
        "include_usage": True # set to true
    }
)
```

```ts Typescript
openai.chat.completions.create({
  messages: [
    {
      role: "user",
      content: "Generate an abstract for a course on space.",
    },
  ],
  model: "gpt-4",
  stream = true,
  stream_options: {
    include_usage: true, // set to true
  },
});
```

</CodeGroup>

### Method 2: Helicone Header

You can also enable stream usage by adding the `helicone-stream-usage` header to your request:

<CodeGroup>

```python Python
client = OpenAI(
    # ...
    headers={
        "helicone-stream-usage": "true"
    }
)

client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Hello!"}],
    stream=True
)
```

```ts TypeScript
const openai = new OpenAI({
  // ...
  headers: {
    "helicone-stream-usage": "true",
  },
});

openai.chat.completions.create({
  messages: [{ role: "user", content: "Hello!" }],
  model: "gpt-4",
  stream: true,
});
```

</CodeGroup>
