---
type: "Framework Learn Page"
framework: "pytest"
source_repo: "https://github.com/pytest-dev/pytest"
source_branch: "main"
source_path: "doc/en/index.rst"
source_commit: "d2466e3a9655f75d25719bcc4510cdbcb39cf10d"
source_commit_short: "d2466e3a"
source_commit_date: "2026-06-21T06:49:47+02:00"
generated_at: "2026-06-21T11:47:50Z"
generated_filename: "_source_index.md"
---

# pytest: helps you write better programs

## Contents

- getting-started
- how-to/index
- reference/index
- explanation/index
- example/index

## Contents

- changelog
- contributing
- backwards-compatibility
- sponsor
- tidelift
- license
- contact

## Contents

- pytest @ PyPI <https://pypi.org/project/pytest/>
- pytest @ GitHub <https://github.com/pytest-dev/pytest/>
- Issue Tracker <https://github.com/pytest-dev/pytest/issues>
- PDF Documentation <https://media.readthedocs.org/pdf/pytest/latest/pytest.pdf>

The `pytest` framework makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries.

**PyPI package name**: :pypi:`pytest`

## A quick example

```python
 # content of test_sample.py
 def inc(x):
     return x + 1

 def test_answer():
     assert inc(3) == 5
```

To execute it:

```pytest
 $ pytest
 =========================== test session starts ============================
 platform linux -- Python 3.x.y, pytest-9.x.y, pluggy-1.x.y
 rootdir: /home/sweet/project
 collected 1 item

 test_sample.py F                                                     [100%]

 ================================= FAILURES =================================
 _______________________________ test_answer ________________________________

     def test_answer():
 >       assert inc(3) == 5
 E       assert 4 == 5
 E        +  where 4 = inc(3)

 test_sample.py:6: AssertionError
 ========================= short test summary info ==========================
 FAILED test_sample.py::test_answer - assert 4 == 5
 ============================ 1 failed in 0.12s =============================
```

Due to `pytest`'s detailed assertion introspection, only plain `assert` statements are used. See `Get started <getstarted>` for a basic introduction to using pytest.

## Features

- Detailed info on failing `assert statements <assert>` (no need to remember `self.assert*` names)
- `Auto-discovery <test discovery>` of test modules and functions
- `Modular fixtures <fixture>` for managing small or parametrized long-lived test resources
- Can run `unittest <unittest>` (including trial) test suites out of the box
- Python 3.10+ or PyPy 3
- Rich plugin architecture, with over 1300+ `external plugins <plugin-list>` and thriving community
## Documentation

- `Get started <get-started>` - install pytest and grasp its basics in just twenty minutes
- `How-to guides <how-to>` - step-by-step guides, covering a vast range of use-cases and needs
- `Reference guides <reference>` - includes the complete pytest API reference, lists of plugins and more
- `Explanation <explanation>` - background, discussion of key topics, answers to higher-level questions
## Bugs/Requests

Please use the [GitHub issue tracker](https://github.com/pytest-dev/pytest/issues) to submit bugs or request features.

## Support pytest

Open Collective is an online funding platform for open and transparent communities. It provides tools to raise money and share your finances in full transparency.

It is the platform of choice for individuals and companies that want to make one-time or monthly donations directly to the project.

See more details in the pytest collective.

## pytest for enterprise

Available as part of the Tidelift Subscription.

The maintainers of pytest and thousands of other packages are working with Tidelift to deliver commercial support and maintenance for the open source dependencies you use to build your applications. Save time, reduce risk, and improve code health, while paying the maintainers of the exact dependencies you use.

[Learn more.](https://tidelift.com/subscription/pkg/pypi-pytest?utm_source=pypi-pytest&utm_medium=referral&utm_campaign=enterprise&utm_term=repo)

### Security

If you have found an issue that you believe is a security vulnerability, please do not create an issue -- instead, report it via a [new security advisory](https://github.com/pytest-dev/pytest/security/advisories/new)_.
