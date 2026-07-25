---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/tracing/how-to-tracing/importing-and-exporting-traces/importing-existing-traces.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.920506Z"
---
---
title: "Import Existing Traces"
description: "Phoenix supports loading data that contains [OpenInference traces](/docs/phoenix/resources/openinference). This allows you to load an existing dataframe of traces into your Phoenix instance."
---

import ConnectToPhoenixPython from "../../../../snippets/connect-to-phoenix-python.mdx";




Usually these will be traces you've previously saved using [Save All Traces](/docs/phoenix/tracing/how-to-tracing/importing-and-exporting-traces/extract-data-from-spans#save-all-traces).

### Connect to Phoenix

<ConnectToPhoenixPython />

### Importing Traces to an Existing Phoenix Instance

```python
import phoenix as px

# Re-launch the app using trace data
px.launch_app(trace=px.TraceDataset(df))

# Load traces into an existing Phoenix instance from a local file
px.launch_app(trace=px.TraceDataset.load('f7733fda-6ad6-4427-a803-55ad2182b662', directory="/my_saved_traces/"))
```

### Launching a new Phoenix Instance with Saved Traces

You can also launch a temporary version of Phoenix in your local notebook to quickly view the traces. But be warned, this Phoenix instance will only last as long as your notebook environment is running

```python
# Load traces from a dataframe
px.launch_app(trace=px.TraceDataset.load(my_traces))

# Load traces from a local file
px.launch_app(trace=px.TraceDataset.load('f7733fda-6ad6-4427-a803-55ad2182b662', directory="/my_saved_traces/"))
```


