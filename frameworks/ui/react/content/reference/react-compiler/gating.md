---
type: "Framework Learn Page"
framework: "React"
source_repo: "https://github.com/reactjs/react.dev"
source_branch: "main"
source_path: "src/content/reference/react-compiler/gating.md"
source_commit: "7c36f7ac329fe3cf2e11222edce9a535158c2cab"
source_commit_short: "7c36f7a"
source_commit_date: "2026-08-24T10:33:57-07:00"
generated_at: "2026-08-29T09:40:25.510382Z"
---
# Gating

---
title: gating
---

<Intro>

The `gating` option enables conditional compilation, allowing you to control when optimized code is used at runtime.

</Intro>

```js
{
  gating: {
    source: 'my-feature-flags',
    importSpecifierName: 'shouldUseCompiler'
  }
}
```

<InlineToc />

---

## Reference {/*reference*/}

### `gating` {/*gating*/}

Configures runtime feature flag gating for compiled functions.

#### Type {/*type*/}

```
{
  source: string;
  importSpecifierName: string;
} | null
```

#### Default value {/*default-value*/}

`null`

#### Properties {/*properties*/}

- **`source`**: Module path to import the feature flag from
- **`importSpecifierName`**: Name of the exported function to import

#### Caveats {/*caveats*/}

- The gating function must return a boolean
- Both compiled and original versions increase bundle size
- The import is added to every file with compiled functions

---

## Usage {/*usage*/}

### Basic feature flag setup {/*basic-setup*/}

1. Create a feature flag module:

```js
// src/utils/feature-flags.js
export function shouldUseCompiler() {
  // your logic here
  return getFeatureFlag('react-compiler-enabled');
}
```

2. Configure the compiler:

```js
{
  gating: {
    source: './src/utils/feature-flags',
    importSpecifierName: 'shouldUseCompiler'
  }
}
```

3. The compiler generates gated code:

```js
// Input
function Button(props) {
  return <button>{props.label}</button>;
}

// Output (simplified)
import { shouldUseCompiler } from './src/utils/feature-flags';

const Button = shouldUseCompiler()
  ? function Button_optimized(props) { /* compiled version */ }
  : function Button_original(props) { /* original version */ };
```

Note that the gating function is evaluated once at module time, so once the JS bundle has been parsed and evaluated the choice of component stays static for the rest of the browser session.

---

## Troubleshooting {/*troubleshooting*/}

### Feature flag not working {/*flag-not-working*/}

Verify your flag module exports the correct function:

```js
// ❌ Wrong: Default export
export default function shouldUseCompiler() {
  return true;
}

// ✅ Correct: Named export matching importSpecifierName
export function shouldUseCompiler() {
  return true;
}
```

### Import errors {/*import-errors*/}

Ensure the source path is correct:

```js
// ❌ Wrong: Relative to babel.config.js
{
  source: './src/flags',
  importSpecifierName: 'flag'
}

// ✅ Correct: Module resolution path
{
  source: '@myapp/feature-flags',
  importSpecifierName: 'flag'
}

// ✅ Also correct: Absolute path from project root
{
  source: './src/utils/flags',
  importSpecifierName: 'flag'
}
```
