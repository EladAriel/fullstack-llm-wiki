---
type: "Framework Learn Page"
framework: "React"
source_repo: "https://github.com/reactjs/react.dev"
source_branch: "main"
source_path: "src/content/reference/eslint-plugin-react-hooks/lints/config.md"
source_commit: "7c36f7ac329fe3cf2e11222edce9a535158c2cab"
source_commit_short: "7c36f7a"
source_commit_date: "2026-08-24T10:33:57-07:00"
generated_at: "2026-08-29T09:40:25.519956Z"
---
# Config

---
title: config
---

<Intro>

Validates the compiler [configuration options](/reference/react-compiler/configuration).

</Intro>

## Rule Details {/*rule-details*/}

React Compiler accepts various [configuration options](/reference/react-compiler/configuration)  to control its behavior. This rule validates that your configuration uses correct option names and value types, preventing silent failures from typos or incorrect settings.

### Invalid {/*invalid*/}

Examples of incorrect code for this rule:

```js
// ❌ Unknown option name
module.exports = {
  plugins: [
    ['babel-plugin-react-compiler', {
      compileMode: 'all' // Typo: should be compilationMode
    }]
  ]
};

// ❌ Invalid option value
module.exports = {
  plugins: [
    ['babel-plugin-react-compiler', {
      compilationMode: 'everything' // Invalid: use 'all' or 'infer'
    }]
  ]
};
```

### Valid {/*valid*/}

Examples of correct code for this rule:

```js
// ✅ Valid compiler configuration
module.exports = {
  plugins: [
    ['babel-plugin-react-compiler', {
      compilationMode: 'infer',
      panicThreshold: 'critical_errors'
    }]
  ]
};
```

## Troubleshooting {/*troubleshooting*/}

### Configuration not working as expected {/*config-not-working*/}

Your compiler configuration might have typos or incorrect values:

```js
// ❌ Wrong: Common configuration mistakes
module.exports = {
  plugins: [
    ['babel-plugin-react-compiler', {
      // Typo in option name
      compilationMod: 'all',
      // Wrong value type
      panicThreshold: true,
      // Unknown option
      optimizationLevel: 'max'
    }]
  ]
};
```

Check the [configuration documentation](/reference/react-compiler/configuration) for valid options:

```js
// ✅ Better: Valid configuration
module.exports = {
  plugins: [
    ['babel-plugin-react-compiler', {
      compilationMode: 'all', // or 'infer'
      panicThreshold: 'none', // or 'critical_errors', 'all_errors'
      // Only use documented options
    }]
  ]
};
```
