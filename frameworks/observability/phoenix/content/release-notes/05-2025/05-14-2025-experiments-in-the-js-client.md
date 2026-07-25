---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/05-2025/05-14-2025-experiments-in-the-js-client.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.901580Z"
---
# 05 14 2025 Experiments In The Js Client

---
title: "05.14.2025: Experiments in the JS client"
---

<Update label="05.14.2025">

## Experiments In The JS Client

<Frame>
  <iframe 
    src="https://cdn.iframe.ly/4vqTlUCW" 
    width={1000} 
    height={400}
    allowFullScreen
  />
</Frame>

You can now run Experiments using the Phoenix JS client! Use Experiments to test different iterations of your applications over a set of test cases, then evaluate the results.

This release includes:

* Native tracing of tasks and evaluators
* Async concurrency queues
* Support for any evaluator (including bring your own evals)

### Code Implementation

```javascript
import { createClient } from "@arizeai/phoenix-client";
import {
  asEvaluator,
  runExperiment,
} from "@arizeai/phoenix-client/experiments";
import type { Example } from "@arizeai/phoenix-client/types/datasets";
import { Factuality } from "autoevals";
import OpenAI from "openai";

const phoenix = createClient();
const openai = new OpenAI();

/** Your AI Task */
const task = async (example: Example) => {
  const response = await openai.chat.completions.create({
    model: "gpt-4o",
    messages: [
      { role: "system", content: "You are a helpful assistant." },
      { role: "user", content: JSON.stringify(example.input, null, 2) },
    ],
  });
  return response.choices[0]?.message?.content ?? "No response";
};

await runExperiment({
  dataset: "dataset_id",
  experimentName: "experiment_name",
  client: phoenix,
  task,
  evaluators: [
    asEvaluator({
      name: "Factuality",
      kind: "LLM",
      evaluate: async (params) => {
        const result = await Factuality({
          output: JSON.stringify(params.output, null, 2),
          input: JSON.stringify(params.input, null, 2),
          expected: JSON.stringify(params.expected, null, 2),
        });
        return {
          score: result.score,
          label: result.name,
          explanation: (result.metadata?.rationale as string) ?? "",
          metadata: result.metadata ?? {},
        };
      },
    }),
  ],
});
```
</Update>

