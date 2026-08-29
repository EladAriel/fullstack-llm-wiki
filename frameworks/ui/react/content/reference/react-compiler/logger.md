---
type: "Framework Learn Page"
framework: "React"
source_repo: "https://github.com/reactjs/react.dev"
source_branch: "main"
source_path: "src/content/reference/react-compiler/logger.md"
source_commit: "7c36f7ac329fe3cf2e11222edce9a535158c2cab"
source_commit_short: "7c36f7a"
source_commit_date: "2026-08-24T10:33:57-07:00"
generated_at: "2026-08-29T09:40:25.509435Z"
---
# Logger

---
title: logger
---

<Intro>

The `logger` option provides custom logging for React Compiler events during compilation.

</Intro>

```js
{
  logger: {
    logEvent(filename, event) {
      console.log(`[Compiler] ${event.kind}: ${filename}`);
    }
  }
}
```

<InlineToc />

---

## Reference {/*reference*/}

### `logger` {/*logger*/}

Configures custom logging to track compiler behavior and debug issues.

#### Type {/*type*/}

```
{
  logEvent: (filename: string | null, event: LoggerEvent) => void;
} | null
```

#### Default value {/*default-value*/}

`null`

#### Methods {/*methods*/}

- **`logEvent`**: Called for each compiler event with the filename and event details

#### Event types {/*event-types*/}

- **`CompileSuccess`**: Function successfully compiled
- **`CompileError`**: Function skipped due to errors
- **`CompileDiagnostic`**: Non-fatal diagnostic information
- **`CompileSkip`**: Function skipped for other reasons
- **`PipelineError`**: Unexpected compilation error
- **`Timing`**: Performance timing information

#### Caveats {/*caveats*/}

- Event structure may change between versions
- Large codebases generate many log entries

---

## Usage {/*usage*/}

### Basic logging {/*basic-logging*/}

Track compilation success and failures:

```js
{
  logger: {
    logEvent(filename, event) {
      switch (event.kind) {
        case 'CompileSuccess': {
          console.log(`✅ Compiled: ${filename}`);
          break;
        }
        case 'CompileError': {
          console.log(`❌ Skipped: ${filename}`);
          break;
        }
        default: {}
      }
    }
  }
}
```

### Detailed error logging {/*detailed-error-logging*/}

Get specific information about compilation failures:

```js
{
  logger: {
    logEvent(filename, event) {
      if (event.kind === 'CompileError') {
        console.error(`\nCompilation failed: ${filename}`);
        console.error(`Reason: ${event.detail.reason}`);

        if (event.detail.description) {
          console.error(`Details: ${event.detail.description}`);
        }

        if (event.detail.loc) {
          const { line, column } = event.detail.loc.start;
          console.error(`Location: Line ${line}, Column ${column}`);
        }

        if (event.detail.suggestions) {
          console.error('Suggestions:', event.detail.suggestions);
        }
      }
    }
  }
}
```

