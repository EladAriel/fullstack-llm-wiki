---
type: "Framework Learn Page"
framework: "React"
source_repo: "https://github.com/reactjs/react.dev"
source_branch: "main"
source_path: "src/content/reference/react-dom/components/option.md"
source_commit: "7c36f7ac329fe3cf2e11222edce9a535158c2cab"
source_commit_short: "7c36f7a"
source_commit_date: "2026-08-24T10:33:57-07:00"
generated_at: "2026-08-29T09:40:25.511846Z"
---
# Option

---
title: "<option>"
---

<Intro>

The [built-in browser `<option>` component](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/option) lets you render an option inside a [`<select>`](/reference/react-dom/components/select) box.

```js
<select>
  <option value="someOption">Some option</option>
  <option value="otherOption">Other option</option>
</select>
```

</Intro>

<InlineToc />

---

## Reference {/*reference*/}

### `<option>` {/*option*/}

The [built-in browser `<option>` component](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/option) lets you render an option inside a [`<select>`](/reference/react-dom/components/select) box.

```js
<select>
  <option value="someOption">Some option</option>
  <option value="otherOption">Other option</option>
</select>
```

[See more examples below.](#usage)

#### Props {/*props*/}

`<option>` supports all [common element props.](/reference/react-dom/components/common#common-props)

Additionally, `<option>` supports these props:

* [`disabled`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/option#disabled): A boolean. If `true`, the option will not be selectable and will appear dimmed.
* [`label`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/option#label): A string. Specifies the meaning of the option. If not specified, the text inside the option is used.
* [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/option#value): The value to be used [when submitting the parent `<select>` in a form](/reference/react-dom/components/select#reading-the-select-box-value-when-submitting-a-form) if this option is selected.

#### Caveats {/*caveats*/}

* React does not support the `selected` attribute on `<option>`. Instead, pass this option's `value` to the parent [`<select defaultValue>`](/reference/react-dom/components/select#providing-an-initially-selected-option) for an uncontrolled select box, or [`<select value>`](/reference/react-dom/components/select#controlling-a-select-box-with-a-state-variable) for a controlled select.

---

## Usage {/*usage*/}

### Displaying a select box with options {/*displaying-a-select-box-with-options*/}

Render a `<select>` with a list of `<option>` components inside to display a select box. Give each `<option>` a `value` representing the data to be submitted with the form.

[Read more about displaying a `<select>` with a list of `<option>` components.](/reference/react-dom/components/select)

<Sandpack>

```js
export default function FruitPicker() {
  return (
    <label>
      Pick a fruit:
      <select name="selectedFruit">
        <option value="apple">Apple</option>
        <option value="banana">Banana</option>
        <option value="orange">Orange</option>
      </select>
    </label>
  );
}
```

```css
select { margin: 5px; }
```

</Sandpack>

