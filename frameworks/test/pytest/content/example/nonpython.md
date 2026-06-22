---
type: "Framework Learn Page"
framework: "pytest"
source_repo: "https://github.com/pytest-dev/pytest"
source_branch: "main"
source_path: "doc/en/example/nonpython.rst"
source_commit: "d2466e3a9655f75d25719bcc4510cdbcb39cf10d"
source_commit_short: "d2466e3a"
source_commit_date: "2026-06-21T06:49:47+02:00"
generated_at: "2026-06-21T11:47:50Z"
---

# Working with non-python tests

## A basic example for specifying tests in Yaml files

Here is an example `conftest.py` (extracted from Ali Afshar's special purpose pytest-yamlwsgi plugin).   This `conftest.py` will  collect `test*.yaml` files and will execute the yaml-formatted content as custom tests:

.. include:: nonpython/conftest.py

You can create a simple example file:

.. include:: nonpython/test_simple.yaml

and if you installed :pypi:`PyYAML` or a compatible YAML-parser you can now execute the test specification:

```pytest
 nonpython $ pytest test_simple.yaml
 =========================== test session starts ============================
 platform linux -- Python 3.x.y, pytest-9.x.y, pluggy-1.x.y
 rootdir: /home/sweet/project/nonpython
 collected 2 items

 test_simple.yaml F.                                                  [100%]

 ================================= FAILURES =================================
 ______________________________ usecase: hello ______________________________
 usecase execution failed
    spec failed: 'some': 'other'
    no further details known at this point.
 ========================= short test summary info ==========================
 FAILED test_simple.yaml::hello - usecase execution failed
 ======================= 1 failed, 1 passed in 0.12s ========================
```

You get one dot for the passing `sub1: sub1` check and one failure. Obviously in the above `conftest.py` you'll want to implement a more interesting interpretation of the yaml-values.  You can easily write your own domain-specific testing language this way.

> **Note:**  `repr_failure(excinfo)` is called for representing test failures.
 If you create custom collection nodes you can return an error
 representation string of your choice.  It
 will be reported as a (red) string.

`reportinfo()` is used for representing the test location and is also consulted when reporting in `verbose` mode. It should return a tuple `(path, lineno, description)`, where:

- `path` is the path shown in reports (usually `self.path` or `self.fspath`).
- `lineno` is a zero-based line number, or `0` when no specific line applies.
- `description` is a short label shown for the collected item:
```pytest
 nonpython $ pytest -v
 =========================== test session starts ============================
 platform linux -- Python 3.x.y, pytest-9.x.y, pluggy-1.x.y -- $PYTHON_PREFIX/bin/python
 cachedir: .pytest_cache
 rootdir: /home/sweet/project/nonpython
 collecting ... collected 2 items

 test_simple.yaml::hello FAILED                                       [ 50%]
 test_simple.yaml::ok PASSED                                          [100%]

 ================================= FAILURES =================================
 ______________________________ usecase: hello ______________________________
 usecase execution failed
    spec failed: 'some': 'other'
    no further details known at this point.
 ========================= short test summary info ==========================
 FAILED test_simple.yaml::hello - usecase execution failed
 ======================= 1 failed, 1 passed in 0.12s ========================
```

While developing your custom test collection and execution it's also interesting to look at the collection tree:

```pytest
 nonpython $ pytest --collect-only
 =========================== test session starts ============================
 platform linux -- Python 3.x.y, pytest-9.x.y, pluggy-1.x.y
 rootdir: /home/sweet/project/nonpython
 collected 2 items

 <Package nonpython>
   <YamlFile test_simple.yaml>
     <YamlItem hello>
     <YamlItem ok>

 ======================== 2 tests collected in 0.12s ========================
```
