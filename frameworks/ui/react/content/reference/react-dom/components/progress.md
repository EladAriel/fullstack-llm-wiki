---
type: "Framework Learn Page"
framework: "React"
source_repo: "https://github.com/reactjs/react.dev"
source_branch: "main"
source_path: "src/content/reference/react-dom/components/progress.md"
source_commit: "7c36f7ac329fe3cf2e11222edce9a535158c2cab"
source_commit_short: "7c36f7a"
source_commit_date: "2026-08-24T10:33:57-07:00"
generated_at: "2026-08-29T09:40:25.510786Z"
---
# Progress

---
title: "<progress>"
---

<Intro>

The [built-in browser `<progress>` component](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/progress) lets you render a progress indicator.

```js
<progress value={0.5} />
```

</Intro>

<InlineToc />

---

## Reference {/*reference*/}

### `<progress>` {/*progress*/}

To display a progress indicator, render the [built-in browser `<progress>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/progress) component.

```js
<progress value={0.5} />
```

[See more examples below.](#usage)

#### Props {/*props*/}

`<progress>` supports all [common element props.](/reference/react-dom/components/common#common-props)

Additionally, `<progress>` supports these props:

* [`max`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/progress#max): A number. Specifies the maximum `value`. Defaults to `1`.
* [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/progress#value): A number between `0` and `max`, or `null` for indeterminate progress. Specifies how much was done.

---

## Usage {/*usage*/}

### Controlling a progress indicator {/*controlling-a-progress-indicator*/}

To display a progress indicator, render a `<progress>` component. You can pass a number `value` between `0` and the `max` value you specify. If you don't pass a `max` value, it will assumed to be `1` by default.

If the operation is not ongoing, pass `value={null}` to put the progress indicator into an indeterminate state.

<Sandpack>

```js
export default function App() {
  return (
    <>
      <progress value={0} />
      <progress value={0.5} />
      <progress value={0.7} />
      <progress value={75} max={100} />
      <progress value={1} />
      <progress value={null} />
    </>
  );
}
```

```css
progress { display: block; }
```

</Sandpack>
