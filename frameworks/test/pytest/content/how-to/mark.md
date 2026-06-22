---
type: "Framework Learn Page"
framework: "pytest"
source_repo: "https://github.com/pytest-dev/pytest"
source_branch: "main"
source_path: "doc/en/how-to/mark.rst"
source_commit: "d2466e3a9655f75d25719bcc4510cdbcb39cf10d"
source_commit_short: "d2466e3a"
source_commit_date: "2026-06-21T06:49:47+02:00"
generated_at: "2026-06-21T11:47:50Z"
---

# How to mark test functions with attributes

By using the `pytest.mark` helper you can easily set metadata on your test functions. You can find the full list of builtin markers in the `API Reference<marks ref>`. Or you can list all the markers, including builtin and custom, using the CLI - :code:`pytest --markers`.

Here are some of the builtin markers:

- `usefixtures <usefixtures>` - use fixtures on a test function or class
- `filterwarnings <filterwarnings>` - filter certain warnings of a test function
- `skip <skip>` - always skip a test function
- `skipif <skipif>` - skip a test function if a certain condition is met
- `xfail <xfail>` - produce an "expected failure" outcome if a certain
condition is met

- `parametrize <parametrizemark>` - perform multiple calls
to the same test function.

It's easy to create custom markers or to apply markers to whole test classes or modules. Those markers can be used by plugins, and also are commonly used to `select tests <mark run>` on the command-line with the :option:`-m` option.

See `mark examples` for examples which also serve as documentation.

> **Note:**  Marks can only be applied to tests, having no effect on
 `fixtures <fixtures>`.

## Registering marks

You can register custom marks in your configuration file like this:

Note that everything past the `:` after the mark name is an optional description.

Alternatively, you can register new markers programmatically in a `pytest_configure <initialization-hooks>` hook:

```python
 def pytest_configure(config):
     config.addinivalue_line(
         "markers", "env(name): mark test to run only on named environment"
     )
```

Registered marks appear in pytest's help text and do not emit warnings (see the next section). It is recommended that third-party plugins always `register their markers <registering-markers>`.

## Raising errors on unknown marks

Unregistered marks applied with the `@pytest.mark.name_of_the_mark` decorator will always emit a warning in order to avoid silently doing something surprising due to mistyped names. As described in the previous section, you can disable the warning for custom marks by registering them in your configuration file or using a custom `pytest_configure` hook.

When the :confval:`strict_markers` configuration option is set, any unknown marks applied with the `@pytest.mark.name_of_the_mark` decorator will trigger an error. You can enforce this validation in your project by setting :confval:`strict_markers` in your configuration:
