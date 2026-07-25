---
type: "Framework Learn Page"
framework: "Material UI"
source_repo: "https://github.com/mui/material-ui.git"
source_branch: "master"
source_path: "docs/data/material/customization/shape/shape.md"
source_commit: "4d5fe7254baa7e97e38b516f37c7af13128468b7"
source_commit_short: "4d5fe725"
source_commit_date: "2026-07-24T12:25:49+03:00"
generated_at: "2026-07-25T13:39:40.963318Z"
---
# Shape

<p class="description">The shape is a design token that helps control the border radius of components.</p>

The `shape` contains a single property, `borderRadius`, with the default value of `4px`.
Several components use this value to set consistent border radii across the library.

## Custom shape

To add custom shapes, create a theme with the `shape` key:

```js
import { createTheme } from '@mui/material/styles';

const theme = createTheme({
  shape: {
    borderRadius: 8,
    borderRadiusSm: 4, // new property
    borderRadiusMd: 8, // new property
    borderRadiusLg: 16, // new property
    borderRadiusXl: 24, // new property
  },
});
```

### TypeScript

If you're using TypeScript you need to use [module augmentation](/material-ui/guides/typescript/#customization-of-theme) to extend **new** shape properties to the theme.

```ts
declare module '@mui/material/styles' {
  interface Shape {
    borderRadiusSm: number;
    borderRadiusMd: number;
    borderRadiusLg: number;
    borderRadiusXl: number;
  }

  interface ShapeOptions {
    borderRadiusSm?: number;
    borderRadiusMd?: number;
    borderRadiusLg?: number;
    borderRadiusXl?: number;
  }
}
```
