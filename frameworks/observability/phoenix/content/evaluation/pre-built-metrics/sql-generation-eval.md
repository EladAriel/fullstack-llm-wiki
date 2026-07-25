---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/evaluation/pre-built-metrics/sql-generation-eval.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.928375Z"
---
# Sql Generation Eval

---
title: "SQL Generation"
description: "SQL Generation is a common approach to using an LLM. In many cases the goal is to take a human description of the query and generate matching SQL to the human description."
---

<Warning>
**Legacy Evaluator:** This evaluator is from phoenix-evals 1.x and will be removed in a future version. You can migrate the template to a custom evaluator as shown below.
</Warning>

**Example of a Question:**\
How many artists have names longer than 10 characters?

**Example Query Generated:**

SELECT COUNT(ArtistId) \nFROM artists \nWHERE LENGTH(Name) > 10

The goal of the SQL generation Evaluation is to determine if the SQL generated is correct based on the question asked.

<Card title="Google Colab" href="https://colab.research.google.com/drive/1e_gxetWuIsve0LWP__qjosHT0D_RGelA?usp=sharing" icon="/images/image-10.png" horizontal >
colab.research.google.com
</Card>

## SQL Eval Template

```
You are tasked with determining if the SQL generated appropriately answers a given
instruction taking into account its generated query and response.

<data>

<instruction>
{question}
</instruction>

<reference_query>
{query_gen}
</reference_query>

<response>
{response}
</response>

</data>

Your response should be a single word: either "correct" or "incorrect".
You must assume that the db exists and that columns are appropriately named.
You must take into account the response as additional information to determine the
correctness.

"correct" indicates that the SQL query correctly solves the instruction.
"incorrect" indicates that the SQL query does not correctly solve the instruction.
```

## Running an SQL Generation Eval

```python
from phoenix.evals import ClassificationEvaluator
from phoenix.evals.llm import LLM

SQL_EVAL_TEMPLATE = """You are tasked with determining if the SQL generated appropriately answers a given
instruction taking into account its generated query and response.

<data>

<instruction>
{question}
</instruction>

<reference_query>
{query_gen}
</reference_query>

<response>
{response}
</response>

</data>

You must assume that the db exists and that columns are appropriately named.
You must take into account the response as additional information to determine the correctness.
"correct" means the SQL query correctly answers the instruction.
"incorrect" means the SQL query does not correctly answer the instruction."""

sql_evaluator = ClassificationEvaluator(
    name="sql_generation",
    prompt_template=SQL_EVAL_TEMPLATE,
    model=LLM(provider="openai", model="gpt-4o"),
    choices={"incorrect": 0, "correct": 1},
)

result = sql_evaluator.evaluate({
    "question": "How many artists have names longer than 10 characters?",
    "query_gen": "SELECT COUNT(ArtistId) FROM artists WHERE LENGTH(Name) > 10",
    "response": "42"
})
```
