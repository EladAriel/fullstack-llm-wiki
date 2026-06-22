---
type: "Framework Learn Page"
framework: "pytest"
source_repo: "https://github.com/pytest-dev/pytest"
source_branch: "main"
source_path: "doc/en/example/customdirectory.rst"
source_commit: "d2466e3a9655f75d25719bcc4510cdbcb39cf10d"
source_commit_short: "d2466e3a"
source_commit_date: "2026-06-21T06:49:47+02:00"
generated_at: "2026-06-21T11:47:50Z"
---

# Using a custom directory collector

By default, pytest collects directories using `pytest.Package, for directories with _init__.py` files, and `pytest.Dir` for other directories. If you want to customize how a directory is collected, you can write your own `pytest.Directory` collector, and use :hook:`pytest_collect_directory` to hook it up.

## A basic example for a directory manifest file

Suppose you want to customize how collection is done on a per-directory basis. Here is an example `conftest.py` plugin that allows directories to contain a `manifest.json` file, which defines how the collection should be done for the directory. In this example, only a simple list of files is supported, however you can imagine adding other keys, such as exclusions and globs.

.. include:: customdirectory/conftest.py

You can create a `manifest.json` file and some test files:

.. include:: customdirectory/tests/manifest.json

.. include:: customdirectory/tests/test_first.py

.. include:: customdirectory/tests/test_second.py

.. include:: customdirectory/tests/test_third.py

And you can now execute the test specification:

```pytest
 customdirectory $ pytest
 =========================== test session starts ============================
 platform linux -- Python 3.x.y, pytest-9.x.y, pluggy-1.x.y
 rootdir: /home/sweet/project/customdirectory
 configfile: pytest.ini
 collected 2 items

 tests/test_first.py .                                                [ 50%]
 tests/test_second.py .                                               [100%]

 ============================ 2 passed in 0.12s =============================
```

Notice how `test_three.py` was not executed, because it is not listed in the manifest.

You can verify that your custom collector appears in the collection tree:

```pytest
 customdirectory $ pytest --collect-only
 =========================== test session starts ============================
 platform linux -- Python 3.x.y, pytest-9.x.y, pluggy-1.x.y
 rootdir: /home/sweet/project/customdirectory
 configfile: pytest.ini
 collected 2 items

 <Dir customdirectory>
   <ManifestDirectory tests>
     <Module test_first.py>
       <Function test_1>
     <Module test_second.py>
       <Function test_2>

 ======================== 2 tests collected in 0.12s ========================
```
