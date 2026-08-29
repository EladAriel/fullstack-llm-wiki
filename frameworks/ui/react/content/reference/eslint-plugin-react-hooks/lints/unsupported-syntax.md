---
type: "Framework Learn Page"
framework: "React"
source_repo: "https://github.com/reactjs/react.dev"
source_branch: "main"
source_path: "src/content/reference/eslint-plugin-react-hooks/lints/unsupported-syntax.md"
source_commit: "7c36f7ac329fe3cf2e11222edce9a535158c2cab"
source_commit_short: "7c36f7a"
source_commit_date: "2026-08-24T10:33:57-07:00"
generated_at: "2026-08-29T09:40:25.517636Z"
---
# Unsupported Syntax

---
title: unsupported-syntax
---

<Intro>

Validates against syntax that React Compiler does not support. If you need to, you can still use this syntax outside of React, such as in a standalone utility function.

</Intro>

## Rule Details {/*rule-details*/}

React Compiler needs to statically analyze your code to apply optimizations. Features like `eval` and `with` make it impossible to statically understand what the code does at compile time, so the compiler can't optimize components that use them.

### Invalid {/*invalid*/}

Examples of incorrect code for this rule:

```js
// ❌ Using eval in component
function Component({ code }) {
  const result = eval(code); // Can't be analyzed
  return <div>{result}</div>;
}

// ❌ Using with statement
function Component() {
  with (Math) { // Changes scope dynamically
    return <div>{sin(PI / 2)}</div>;
  }
}

// ❌ Dynamic property access with eval
function Component({propName}) {
  const value = eval(`props.${propName}`);
  return <div>{value}</div>;
}
```

### Valid {/*valid*/}

Examples of correct code for this rule:

```js
// ✅ Use normal property access
function Component({propName, props}) {
  const value = props[propName]; // Analyzable
  return <div>{value}</div>;
}

// ✅ Use standard Math methods
function Component() {
  return <div>{Math.sin(Math.PI / 2)}</div>;
}
```

## Troubleshooting {/*troubleshooting*/}

### I need to evaluate dynamic code {/*evaluate-dynamic-code*/}

You might need to evaluate user-provided code:

```js {expectedErrors: {'react-compiler': [3]}}
// ❌ Wrong: eval in component
function Calculator({expression}) {
  const result = eval(expression); // Unsafe and unoptimizable
  return <div>Result: {result}</div>;
}
```

Use a safe expression parser instead:

```js
// ✅ Better: Use a safe parser
import {evaluate} from 'mathjs'; // or similar library

function Calculator({expression}) {
  const [result, setResult] = useState(null);

  const calculate = () => {
    try {
      // Safe mathematical expression evaluation
      setResult(evaluate(expression));
    } catch (error) {
      setResult('Invalid expression');
    }
  };

  return (
    <div>
      <button onClick={calculate}>Calculate</button>
      {result && <div>Result: {result}</div>}
    </div>
  );
}
```

<Note>

Never use `eval` with user input - it's a security risk. Use dedicated parsing libraries for specific use cases like mathematical expressions, JSON parsing, or template evaluation.

</Note>