---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/guides/prompt-engineering/use-constrained-outputs.mdx"
source_commit: "67df07b8d807a960f2e53d9ec2a9c49513ca2379"
source_commit_short: "67df07b"
source_commit_date: "2026-07-21T05:35:38-07:00"
generated_at: "2026-07-25T19:08:22.278990Z"
---
# Use Constrained Outputs

---
title: "Use constrained outputs"
sidebarTitle: "Use constrained outputs"
description: "Set clear boundaries and rules for the model's responses to improve accuracy, consistency, and utility"
"twitter:title": "Use Constrained Outputs - Prompt Engineering Techniques"
---

import QuestionsSection from "/snippets/questions-section.mdx";

## What are constrained outputs

Constrained outputs involve instructing the LLM to generate responses that adhere to specific limitations or formats. This could mean setting a word limit, specifying a response type (like "yes" or "no"), or requiring the output to match a particular pattern or structure.

## How to implement constrained outputs

1. **Set clear instructions**: Be explicit about the constraints you want the model to follow.
2. **Specify the format**: Define the exact format or pattern you expect.
3. **Limit the length**: Set boundaries on the response length, such as word or character counts.
4. **Use controlled vocabularies**: Restrict the model to use only certain words or phrases.
5. **Provide templates**: Offer a template that the model should fill in.

## Example

<AccordionGroup>
  <Accordion title="Example 1: Binary Classification.">
  Limiting the response to 'Approved' or 'Denied' ensures consistency and simplifies automated processing.

**Prompt:**

```
Review the following application and respond with 'Approved' or 'Denied' only.

Application Details: [Applicant's information and criteria]

Decision:
```

</Accordion>

  <Accordion title="Example 2: Short Answer Generation.">
  By specifying that the answer should be in one sentence, you prevent the model from providing overly long or off-topic responses.  **Prompt:**

**Prompt:**

```
Based on the text below, answer the question in one sentence.

Text: 'The Great Barrier Reef is the world's largest coral reef system located in Australia.'

Question: 'Where is the Great Barrier Reef located?'

Answer:
```

  </Accordion>

  <Accordion title="Example 3: Technical writing.">
  Setting an exact word limit challenges the model to be concise and focus on the most important information.

    **Prompt:**

```
Summarize the following article in exactly 50 words.

[Insert article text]

Summary (50 words):
```

  </Accordion>

</AccordionGroup>

## Why use constrained outputs

- **Increase precision**: Helps the model provide exactly what you need without unnecessary information.
- **Enhance consistency**: Ensures uniformity across multiple outputs, which is crucial for tasks like data entry or form filling.
- **Simplify parsing**: Makes it easier to programmatically process the responses.
- **Reduce errors**: Minimizes the chance of irrelevant or incorrect information creeping into the output.

<QuestionsSection />
