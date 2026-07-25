---
type: "Framework Learn Page"
framework: "sqlalchemy"
source_repo: "https://github.com/sqlalchemy/sqlalchemy"
source_branch: "main"
source_path: "doc/build/core/selectable.rst"
source_commit: "aa1a5575358d3aa14953b04dced02f4763fed2e7"
source_commit_short: "aa1a5575"
source_commit_date: "2026-07-23T18:02:59Z"
generated_at: "2026-07-25T11:50:45Z"
---

# SELECT and Related Constructs

The term "selectable" refers to any object that represents database rows. In SQLAlchemy, these objects descend from `_expression.Selectable, the most prominent being expression.Select, which represents a SQL SELECT statement. A subset of expression.Selectable is expression.FromClause`, which represents objects that can be within the FROM clause of a `.Select statement. A distinguishing feature of expression.FromClause is the expression.FromClause.c attribute, which is a namespace of all the columns contained within the FROM clause (these elements are themselves expression.ColumnElement` subclasses).

## Selectable Foundational Constructors

Top level "FROM clause" and "SELECT" constructors.

## Selectable Modifier Constructors

Functions listed here are more commonly available as methods from `_sql.FromClause and sql.Selectable elements, for example, the sql.alias function is usually invoked via the sql.FromClause.alias` method.

## Selectable Class Documentation

The classes here are generated using the constructors listed at `selectable_foundational_constructors` and `fromclause_modifier_constructors`.

## Label Style Constants

Constants used with the `_sql.GenerativeSelect.set_label_style` method.

> **Seealso:**  `_sql.Select.set_label_style`
 `_sql.Select.get_label_style`
