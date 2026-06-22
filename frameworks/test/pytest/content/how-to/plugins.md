---
type: "Framework Learn Page"
framework: "pytest"
source_repo: "https://github.com/pytest-dev/pytest"
source_branch: "main"
source_path: "doc/en/how-to/plugins.rst"
source_commit: "d2466e3a9655f75d25719bcc4510cdbcb39cf10d"
source_commit_short: "d2466e3a"
source_commit_date: "2026-06-21T06:49:47+02:00"
generated_at: "2026-06-21T11:47:50Z"
---

# How to install and use plugins

This section talks about installing and using third party plugins. For writing your own plugins, please refer to `writing-plugins`.

Installing a third party plugin can be easily done with `pip`:

```bash
 pip install pytest-NAME
 pip uninstall pytest-NAME
```

If a plugin is installed, `pytest` automatically finds and integrates it, there is no need to activate it.

Here is a little annotated list for some popular plugins:

- :pypi:`pytest-django`: write tests
for [django](https://docs.djangoproject.com/) apps, using pytest integration.

- :pypi:`pytest-twisted`: write tests
for [twisted](https://twistedmatrix.com/) apps, starting a reactor and processing deferreds from test functions.

- :pypi:`pytest-cov`:
coverage reporting, compatible with distributed testing

- :pypi:`pytest-xdist`:
to distribute tests to CPUs and remote hosts, to run in boxed mode that allows pytest to survive segmentation faults, to run in looponfailing mode, automatically re-running failing tests on file changes.

- :pypi:`pytest-instafail`:
to report failures while the test run is happening.

- :pypi:`pytest-bdd`:
to write tests using behaviour-driven testing.

- :pypi:`pytest-timeout`:
to timeout tests based on function marks or global definitions.

- :pypi:`pytest-pep8`:
a `--pep8` option to enable PEP8 compliance checking.

- :pypi:`pytest-flakes`:
check source code with pyflakes.

- :pypi:`allure-pytest`:
report test results via [allure-framework](https://github.com/allure-framework/).

To see a complete list of all plugins with their latest testing status against different pytest and Python versions, please visit `plugin-list`.

You may also discover more plugins through a pytest- pypi.org search.

## Requiring/Loading plugins in a test module or conftest file

You can require plugins in a test module or a conftest file using :globalvar:`pytest_plugins`:

```python
 pytest_plugins = ("myapp.testsupport.myplugin",)
```

When the test module or conftest plugin is loaded the specified plugins will be loaded as well.

> **Note:**  Requiring plugins using a `pytest_plugins` variable in non-root
 `conftest.py` files is deprecated. See
 `full explanation <requiring plugins in non-root conftests>`
 in the Writing plugins section.

> **Note:** The name `pytest_plugins` is reserved and should not be used as a
name for a custom plugin module.

## Finding out which plugins are active

If you want to find out which plugins are active in your environment you can type:

```bash
 pytest --trace-config
```

and will get an extended test header which shows activated plugins and their names. It will also print local plugins aka `conftest.py <conftest.py plugins>` files when they are loaded.

## Deactivating / unregistering a plugin by name

You can prevent plugins from loading or unregister them:

```bash
 pytest -p no:NAME
```

This means that any subsequent try to activate/load the named plugin will not work.

If you want to unconditionally disable a plugin for a project, you can add this option to your configuration file:

Alternatively to disable it only in certain environments (for example in a CI server), you can set `PYTEST_ADDOPTS` environment variable to `-p no:name`.

See `findpluginname` for how to obtain the name of a plugin.

## Disabling plugins from autoloading

If you want to disable plugins from loading automatically, instead of requiring you to manually specify each plugin with :option:`-p` or :envvar:`PYTEST_PLUGINS`, you can use :option:`--disable-plugin-autoload` or :envvar:`PYTEST_DISABLE_PLUGIN_AUTOLOAD`.

```bash
export PYTEST_DISABLE_PLUGIN_AUTOLOAD=1
export PYTEST_PLUGINS=NAME,NAME2
pytest
```

```bash
pytest --disable-plugin-autoload -p NAME -p NAME2
```

.. versionadded:: 8.4

> **Note:** :option:`-p` and :envvar:`PYTEST_PLUGINS` are both ways to explicitly control which
plugins are loaded, but they serve slightly different use-cases.
* :option:`-p` loads (or disables with `-p no:<name>`) a plugin by name or entry point
  for a specific pytest invocation, and is processed early during startup.
* :envvar:`PYTEST_PLUGINS` is a comma-separated list of Python modules that are imported
  and registered as plugins during startup. This mechanism is commonly used by test
  suites, for example when testing a plugin.
When explicitly controlling plugin loading (especially with
:envvar:`PYTEST_DISABLE_PLUGIN_AUTOLOAD` or :option:`--disable-plugin-autoload`),
avoid specifying the same plugin via multiple mechanisms. Registering the same plugin
more than once can lead to errors during plugin registration.

Examples:

```bash
# Disable auto-loading and load only specific plugins for this invocation
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -p xdist
```

```bash
# Disable auto-loading and load plugin modules during startup
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 PYTEST_PLUGINS=mymodule.plugin,xdist pytest
```
