---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/queries.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
---

## Queries

query

SELECT

The previous chapters explained how to create tables, how to fill them with data, and how to manipulate that data. Now we finally discuss how to retrieve the data from the database.

## Overview

The process of retrieving or the command to retrieve data from a database is called a query. In SQL the SELECT command is used to specify queries. The general syntax of the `SELECT` command is

```
WITH with_queries SELECT select_list FROM table_expression sort_specification
```

The following sections describe the details of the select list, the table expression, and the sort specification. `WITH` queries are treated last since they are an advanced feature.

A simple kind of query has the form:

```
SELECT * FROM table1;
```

Assuming that there is a table called `table1`, this command would retrieve all rows and all user-defined columns from `table1`. (The method of retrieval depends on the client application. For example, the `psql` program will display an ASCII-art table on the screen, while client libraries will offer functions to extract individual values from the query result.) The select list specification `*` means all columns that the table expression happens to provide. A select list can also select a subset of the available columns or make calculations using the columns. For example, if `table1` has columns named `a`, `b`, and `c` (and perhaps others) you can make the following query:

```
SELECT a, b + c FROM table1;
```

(assuming that `b` and `c` are of a numerical data type). See `queries-select-lists` for more details.

`FROM table1` is a simple kind of table expression: it reads just one table. In general, table expressions can be complex constructs of base tables, joins, and subqueries. But you can also omit the table expression entirely and use the `SELECT` command as a calculator:

```
SELECT 3 * 4;
```

This is more useful if the expressions in the select list return varying results. For example, you could call a function this way:

```
SELECT random();
```

## Table Expressions

table expression

A table expression computes a table. The table expression contains a `FROM` clause that is optionally followed by `WHERE`, `GROUP BY`, and `HAVING` clauses. Trivial table expressions simply refer to a table on disk, a so-called base table, but more complex expressions can be used to modify or combine base tables in various ways.

The optional `WHERE`, `GROUP BY`, and `HAVING` clauses in the table expression specify a pipeline of successive transformations performed on the table derived in the `FROM` clause. All these transformations produce a virtual table that provides the rows that are passed to the select list to compute the output rows of the query.

## The `FROM` Clause

The FROM clause derives a table from one or more other tables given in a comma-separated table reference list.

```
FROM table_reference , table_reference , ...
```

A table reference can be a table name (possibly schema-qualified), or a derived table such as a subquery, a `JOIN` construct, or complex combinations of these. If more than one table reference is listed in the `FROM` clause, the tables are cross-joined (that is, the Cartesian product of their rows is formed; see below). The result of the `FROM` list is an intermediate virtual table that can then be subject to transformations by the `WHERE`, `GROUP BY`, and `HAVING` clauses and is finally the result of the overall table expression.

ONLY

When a table reference names a table that is the parent of a table inheritance hierarchy, the table reference produces rows of not only that table but all of its descendant tables, unless the key word `ONLY` precedes the table name. However, the reference produces only the columns that appear in the named table -- any columns added in subtables are ignored.

You can write `*` after the table name to explicitly specify that descendant tables are included, which is the opposite of `ONLY`. There is no real reason to write `*` any more, because searching descendant tables has been the default behavior since PostgreSQL version 10. However, it remains supported for compatibility with older releases.

## Joined Tables

join

A joined table is a table derived from two other (real or derived) tables according to the rules of the particular join type. Inner, outer, and cross-joins are available. The general syntax of a joined table is

```
T1 join_type T2  join_condition 
```

Joins of all types can be chained together, or nested: either or both `T1` and `T2` can be joined tables. Parentheses can be used around `JOIN` clauses to control the join order. In the absence of parentheses, `JOIN` clauses nest left-to-right.

- ```
 T1 CROSS JOIN T2
  ```
  
  For every possible combination of rows from `T1` and `T2` (i.e., a Cartesian product), the joined table will contain a row consisting of all columns in `T1` followed by all columns in `T2`. If the tables have N and M rows respectively, the joined table will have N * M rows.    `FROM T1 CROSS JOIN T2` is equivalent to `FROM T1 INNER JOIN T2 ON TRUE` (see below). It is also equivalent to `FROM T1, T2`.   This latter equivalence does not hold exactly when more than two tables appear, because `JOIN` binds more tightly than comma. For example `FROM T1 CROSS JOIN T2 INNER JOIN T3 ON condition` is not the same as `FROM T1, T2 INNER JOIN T3 ON condition` because the `condition` can reference `T1` in the first case but not the second.
- ```
  T1 { INNER | { LEFT | RIGHT | FULL } OUTER } JOIN T2 ON boolean_expression
  T1 { INNER | { LEFT | RIGHT | FULL } OUTER } JOIN T2 USING ( join column list )
  T1 NATURAL { INNER | { LEFT | RIGHT | FULL } OUTER } JOIN T2
  ```
 
 The words `INNER` and `OUTER` are optional in all forms. `INNER` is the default; `LEFT`, `RIGHT`, and `FULL` imply an outer join. The join condition is specified in the `ON` or `USING` clause, or implicitly by the word `NATURAL`. The join condition determines which rows from the two source tables are considered to match, as explained in detail below. The possible types of qualified join are: `INNER JOIN` For each row R1 of T1, the joined table has a row for each row in T2 that satisfies the join condition with R1.
- First, an inner join is performed. Then, for each row in T1 that does not satisfy the join condition with any row in T2, a joined row is added with null values in columns of T2. Thus, the joined table always has at least one row for each row in T1.
- First, an inner join is performed. Then, for each row in T2 that does not satisfy the join condition with any row in T1, a joined row is added with null values in columns of T1. This is the converse of a left join: the result table will always have a row for each row in T2.
- First, an inner join is performed. Then, for each row in T1 that does not satisfy the join condition with any row in T2, a joined row is added with null values in columns of T2. Also, for each row of T2 that does not satisfy the join condition with any row in T1, a joined row with null values in the columns of T1 is added.

 

 

The `ON` clause is the most general kind of join condition: it takes a Boolean value expression of the same kind as is used in a `WHERE` clause. A pair of rows from `T1` and `T2` match if the `ON` expression evaluates to true.

 

The `USING` clause is a shorthand that allows you to take advantage of the specific situation where both sides of the join use the same name for the joining column(s). It takes a comma-separated list of the shared column names and forms a join condition that includes an equality comparison for each one. For example, joining `T1` and `T2` with `USING (a, b)` produces the join condition `ON T1.a = T2.a AND T1.b = T2.b`.

 

Furthermore, the output of `JOIN USING` suppresses redundant columns: there is no need to print both of the matched columns, since they must have equal values. While `JOIN ON` produces all columns from `T1` followed by all columns from `T2`, `JOIN USING` produces one output column for each of the listed column pairs (in the listed order), followed by any remaining columns from `T1`, followed by any remaining columns from `T2`.

 

join natural natural join Finally, `NATURAL` is a shorthand form of `USING`: it forms a `USING` list consisting of all column names that appear in both input tables. As with `USING`, these columns appear only once in the output table. If there are no common column names, `NATURAL JOIN` behaves like `CROSS JOIN`.

 

`USING` is reasonably safe from column changes in the joined relations since only the listed columns are combined. `NATURAL` is considerably more risky since any schema changes to either relation that cause a new matching column name to be present will cause the join to combine that new column as well.

 
 
 

 

To put this together, assume we have tables `t1`:

```
num | name
-----+------
1 | a
2 | b
3 | c
```

and `t2`:

```
num | value
-----+-------
1 | xxx
3 | yyy
5 | zzz
```

then we get the following results for the various joins:

```
=> SELECT * FROM t1 CROSS JOIN t2;
num | name | num | value
-----+------+-----+-------
1 | a | 1 | xxx
1 | a | 3 | yyy
1 | a | 5 | zzz
2 | b | 1 | xxx
2 | b | 3 | yyy
2 | b | 5 | zzz
3 | c | 1 | xxx
3 | c | 3 | yyy
3 | c | 5 | zzz
(9 rows)

=> SELECT * FROM t1 INNER JOIN t2 ON t1.num = t2.num;
num | name | num | value
-----+------+-----+-------
1 | a | 1 | xxx
3 | c | 3 | yyy
(2 rows)

=> SELECT * FROM t1 INNER JOIN t2 USING (num);
num | name | value
-----+------+-------
1 | a | xxx
3 | c | yyy
(2 rows)

=> SELECT * FROM t1 NATURAL INNER JOIN t2;
num | name | value
-----+------+-------
1 | a | xxx
3 | c | yyy
(2 rows)

=> SELECT * FROM t1 LEFT JOIN t2 ON t1.num = t2.num;
num | name | num | value
-----+------+-----+-------
1 | a | 1 | xxx
2 | b | |
3 | c | 3 | yyy
(3 rows)

=> SELECT * FROM t1 LEFT JOIN t2 USING (num);
num | name | value
-----+------+-------
1 | a | xxx
2 | b |
3 | c | yyy
(3 rows)

=> SELECT * FROM t1 RIGHT JOIN t2 ON t1.num = t2.num;
num | name | num | value
-----+------+-----+-------
1 | a | 1 | xxx
3 | c | 3 | yyy
| | 5 | zzz
(3 rows)

=> SELECT * FROM t1 FULL JOIN t2 ON t1.num = t2.num;
num | name | num | value
-----+------+-----+-------
1 | a | 1 | xxx
2 | b | |
3 | c | 3 | yyy
| | 5 | zzz
(4 rows)
```

 

The join condition specified with `ON` can also contain conditions that do not relate directly to the join. This can prove useful for some queries but needs to be thought out carefully. For example:

```
=> SELECT * FROM t1 LEFT JOIN t2 ON t1.num = t2.num AND t2.value = 'xxx';
num | name | num | value
-----+------+-----+-------
1 | a | 1 | xxx
2 | b | |
3 | c | |
(3 rows)
```

Notice that placing the restriction in the `WHERE` clause produces a different result:

```
=> SELECT * FROM t1 LEFT JOIN t2 ON t1.num = t2.num WHERE t2.value = 'xxx';
num | name | num | value
-----+------+-----+-------
1 | a | 1 | xxx
(1 row)
```

This is because a restriction placed in the `ON` clause is processed before the join, while a restriction placed in the `WHERE` clause is processed after the join. That does not matter with inner joins, but it matters a lot with outer joins.

 

 

 

## Table and Column Aliases

 
 alias
 in the FROM clause
 

 
 label
 alias
 

 

A temporary name can be given to tables and complex table references to be used for references to the derived table in the rest of the query. This is called a table alias.

 

To create a table alias, write

```
FROM table_reference AS alias
```

or

```
FROM table_reference alias
```

The `AS` key word is optional noise. `alias` can be any identifier.

 

A typical application of table aliases is to assign short identifiers to long table names to keep the join clauses readable. For example:

```
SELECT * FROM some_very_long_table_name s JOIN another_fairly_long_name a ON s.id = a.num;
```

 

The alias becomes the new name of the table reference so far as the current query is concerned -- it is not allowed to refer to the table by the original name elsewhere in the query. Thus, this is not valid:

```
SELECT * FROM my_table AS m WHERE my_table.a > 5; -- wrong
```

 

Table aliases are mainly for notational convenience, but it is necessary to use them when joining a table to itself, e.g.:

```
SELECT * FROM people AS mother JOIN people AS child ON mother.id = child.mother_id;
```

 

Parentheses are used to resolve ambiguities. In the following example, the first statement assigns the alias `b` to the second instance of `my_table`, but the second statement assigns the alias to the result of the join:

```
SELECT * FROM my_table AS a CROSS JOIN my_table AS b ...
SELECT * FROM (my_table AS a CROSS JOIN my_table) AS b ...
```

 

Another form of table aliasing gives temporary names to the columns of the table, as well as the table itself:

```
FROM table_reference AS alias ( column1 , column2 , ... )
```

If fewer column aliases are specified than the actual table has columns, the remaining columns are not renamed. This syntax is especially useful for self-joins or subqueries.

 

When an alias is applied to the output of a `JOIN` clause, the alias hides the original name(s) within the `JOIN`. For example:

```
SELECT a.* FROM my_table AS a JOIN your_table AS b ON ...
```

is valid SQL, but:

```
SELECT a.* FROM (my_table AS a JOIN your_table AS b ON ...) AS c
```

is not valid; the table alias `a` is not visible outside the alias `c`.

 

 

 

## Subqueries

 
 subquery
 

 

Subqueries specifying a derived table must be enclosed in parentheses. They may be assigned a table alias name, and optionally column alias names (as in `queries-table-aliases`). For example:

```
FROM (SELECT * FROM table1) AS alias_name
```

 

This example is equivalent to `FROM table1 AS alias_name`. More interesting cases, which cannot be reduced to a plain join, arise when the subquery involves grouping or aggregation.

 

A subquery can also be a `VALUES` list:

```
FROM (VALUES ('anne', 'smith'), ('bob', 'jones'), ('joe', 'blow'))
AS names(first, last)
```

Again, a table alias is optional. Assigning alias names to the columns of the `VALUES` list is optional, but is good practice. For more information see `queries-values`.

 

According to the SQL standard, a table alias name must be supplied for a subquery. PostgreSQL allows `AS` and the alias to be omitted, but writing one is good practice in SQL code that might be ported to another system.

 

 

 

## Table Functions

 table function

 
 function
 in the FROM clause
 

 

Table functions are functions that produce a set of rows, made up of either base data types (scalar types) or composite data types (table rows). They are used like a table, view, or subquery in the `FROM` clause of a query. Columns returned by table functions can be included in `SELECT`, `JOIN`, or `WHERE` clauses in the same manner as columns of a table, view, or subquery.

 

Table functions may also be combined using the `ROWS FROM` syntax, with the results returned in parallel columns; the number of result rows in this case is that of the largest function result, with smaller results padded with null values to match.

```
function_call WITH ORDINALITY AS table_alias (column_alias , ... )
ROWS FROM( function_call , ... ) WITH ORDINALITY AS table_alias (column_alias , ... )
```

 

If the `WITH ORDINALITY` clause is specified, an additional column of type `bigint` will be added to the function result columns. This column numbers the rows of the function result set, starting from 1. (This is a generalization of the SQL-standard syntax for `UNNEST ... WITH ORDINALITY`.) By default, the ordinal column is called `ordinality`, but a different column name can be assigned to it using an `AS` clause.

 

The special table function `UNNEST` may be called with any number of array parameters, and it returns a corresponding number of columns, as if `UNNEST` (`functions-array`) had been called on each parameter separately and combined using the `ROWS FROM` construct.

```
UNNEST( array_expression , ... ) WITH ORDINALITY AS table_alias (column_alias , ... )
```

 

If no `table_alias` is specified, the function name is used as the table name; in the case of a `ROWS FROM()` construct, the first function's name is used.

 

If column aliases are not supplied, then for a function returning a base data type, the column name is also the same as the function name. For a function returning a composite type, the result columns get the names of the individual attributes of the type.

 

Some examples:

```
CREATE TABLE foo (fooid int, foosubid int, fooname text);

CREATE FUNCTION getfoo(int) RETURNS SETOF foo AS $$
SELECT * FROM foo WHERE fooid = $1;
$$ LANGUAGE SQL;

SELECT * FROM getfoo(1) AS t1;

SELECT * FROM foo
WHERE foosubid IN (
SELECT foosubid
FROM getfoo(foo.fooid) z
WHERE z.fooid = foo.fooid
);

CREATE VIEW vw_getfoo AS SELECT * FROM getfoo(1);

SELECT * FROM vw_getfoo;
```

 

In some cases it is useful to define table functions that can return different column sets depending on how they are invoked. To support this, the table function can be declared as returning the pseudo-type `record` with no `OUT` parameters. When such a function is used in a query, the expected row structure must be specified in the query itself, so that the system can know how to parse and plan the query. This syntax looks like:

```
function_call AS alias (column_definition , ... )
function_call AS alias (column_definition , ... )
ROWS FROM( ... function_call AS (column_definition , ... ) , ... )
```

 

When not using the `ROWS FROM()` syntax, the `column_definition` list replaces the column alias list that could otherwise be attached to the `FROM` item; the names in the column definitions serve as column aliases. When using the `ROWS FROM()` syntax, a `column_definition` list can be attached to each member function separately; or if there is only one member function and no `WITH ORDINALITY` clause, a `column_definition` list can be written in place of a column alias list following `ROWS FROM()`.

 

Consider this example:

```
SELECT *
FROM dblink('dbname=mydb', 'SELECT proname, prosrc FROM pg_proc')
AS t1(proname name, prosrc text)
WHERE proname LIKE 'bytea%';
```

The `contrib-dblink-function` function (part of the `dblink` module) executes a remote query. It is declared to return `record` since it might be used for any kind of query. The actual column set must be specified in the calling query so that the parser knows, for example, what `*` should expand to.

 

This example uses `ROWS FROM`:

```
SELECT *
FROM ROWS FROM
(
json_to_recordset('[{"a":40,"b":"foo"},{"a":"100","b":"bar"}]')
AS (a INTEGER, b TEXT),
generate_series(1, 3)
) AS x (p, q, s)
ORDER BY p;

p | q | s
-----+-----+---
40 | foo | 1
100 | bar | 2
| | 3
```

It joins two functions into a single `FROM` target. `json_to_recordset()` is instructed to return two columns, the first `integer` and the second `text`. The result of `generate_series()` is used directly. The `ORDER BY` clause sorts the column values as integers.

 

 

 

## `LATERAL` Subqueries

 
 LATERAL
 in the FROM clause
 

 

Subqueries appearing in `FROM` can be preceded by the key word `LATERAL`. This allows them to reference columns provided by preceding `FROM` items. (Without `LATERAL`, each subquery is evaluated independently and so cannot cross-reference any other `FROM` item.)

 

Table functions appearing in `FROM` can also be preceded by the key word `LATERAL`, but for functions the key word is optional; the function's arguments can contain references to columns provided by preceding `FROM` items in any case.

 

A `GRAPH_TABLE` `FROM` item can also always contain lateral references.

 

A `LATERAL` item can appear at the top level in the `FROM` list, or within a `JOIN` tree. In the latter case it can also refer to any items that are on the left-hand side of a `JOIN` that it is on the right-hand side of.

 

When a `FROM` item contains `LATERAL` cross-references, evaluation proceeds as follows: for each row of the `FROM` item providing the cross-referenced column(s), or set of rows of multiple `FROM` items providing the columns, the `LATERAL` item is evaluated using that row or row set's values of the columns. The resulting row(s) are joined as usual with the rows they were computed from. This is repeated for each row or set of rows from the column source table(s).

 

A trivial example of `LATERAL` is

```
SELECT * FROM foo, LATERAL (SELECT * FROM bar WHERE bar.id = foo.bar_id) ss;
```

This is not especially useful since it has exactly the same result as the more conventional

```
SELECT * FROM foo, bar WHERE bar.id = foo.bar_id;
```

`LATERAL` is primarily useful when the cross-referenced column is necessary for computing the row(s) to be joined. A common application is providing an argument value for a set-returning function. For example, supposing that `vertices(polygon)` returns the set of vertices of a polygon, we could identify close-together vertices of polygons stored in a table with:

```
SELECT p1.id, p2.id, v1, v2
FROM polygons p1, polygons p2,
LATERAL vertices(p1.poly) v1,
LATERAL vertices(p2.poly) v2
WHERE (v1 v2) v2) 5
```

and:

```
FROM a INNER JOIN b ON (a.id = b.id) WHERE b.val > 5
```

or perhaps even:

```
FROM a NATURAL JOIN b WHERE b.val > 5
```

Which one of these you use is mainly a matter of style. The `JOIN` syntax in the `FROM` clause is probably not as portable to other SQL database management systems, even though it is in the SQL standard. For outer joins there is no choice: they must be done in the `FROM` clause. The `ON` or `USING` clause of an outer join is not equivalent to a `WHERE` condition, because it results in the addition of rows (for unmatched input rows) as well as the removal of rows in the final result.

 

Here are some examples of `WHERE` clauses:

```
SELECT ... FROM fdt WHERE c1 > 5

SELECT ... FROM fdt WHERE c1 IN (1, 2, 3)

SELECT ... FROM fdt WHERE c1 IN (SELECT c1 FROM t2)

SELECT ... FROM fdt WHERE c1 IN (SELECT c3 FROM t2 WHERE c2 = fdt.c1 + 10)

SELECT ... FROM fdt WHERE c1 BETWEEN (SELECT c3 FROM t2 WHERE c2 = fdt.c1 + 10) AND 100

SELECT ... FROM fdt WHERE EXISTS (SELECT c1 FROM t2 WHERE c2 > fdt.c1)
```

`fdt` is the table derived in the `FROM` clause. Rows that do not meet the search condition of the `WHERE` clause are eliminated from `fdt`. Notice the use of scalar subqueries as value expressions. Just like any other query, the subqueries can employ complex table expressions. Notice also how `fdt` is referenced in the subqueries. Qualifying `c1` as `fdt.c1` is only necessary if `c1` is also the name of a column in the derived input table of the subquery. But qualifying the column name adds clarity even when it is not needed. This example shows how the column naming scope of an outer query extends into its inner queries.

 

 

 

## The `GROUP BY` and `HAVING` Clauses

 
 GROUP BY
 

 
 grouping
 

 

After passing the `WHERE` filter, the derived input table might be subject to grouping, using the `GROUP BY` clause, and elimination of group rows using the `HAVING` clause.

```
SELECT select_list
FROM ...
WHERE ...
GROUP BY grouping_column_reference , grouping_column_reference...
```

 

The GROUP BY clause is used to group together those rows in a table that have the same values in all the columns listed. The order in which the columns are listed does not matter. The effect is to combine each set of rows having common values into one group row that represents all rows in the group. This is done to eliminate redundancy in the output and/or compute aggregates that apply to these groups. For instance:

```
=> SELECT * FROM test1;
x | y
---+---
a | 3
c | 2
b | 5
a | 1
(4 rows)

=> SELECT x FROM test1 GROUP BY x;
x
---
a
b
c
(3 rows)
```

 

In the second query, we could not have written `SELECT * FROM test1 GROUP BY x`, because there is no single value for the column `y` that could be associated with each group. The grouped-by columns can be referenced in the select list since they have a single value in each group.

 

In general, if a table is grouped, columns that are not listed in `GROUP BY` cannot be referenced except in aggregate expressions. An example with aggregate expressions is:

```
=> SELECT x, sum(y) FROM test1 GROUP BY x;
x | sum
---+-----
a | 4
b | 5
c | 2
(3 rows)
```

Here `sum` is an aggregate function that computes a single value over the entire group. More information about the available aggregate functions can be found in `functions-aggregate`.

 

Grouping without aggregate expressions effectively calculates the set of distinct values in a column. This can also be achieved using the `DISTINCT` clause (see `queries-distinct`).

 

Here is another example: it calculates the total sales for each product (rather than the total sales of all products):

```
SELECT product_id, p.name, (sum(s.units) * p.price) AS sales
FROM products p LEFT JOIN sales s USING (product_id)
GROUP BY product_id, p.name, p.price;
```

In this example, the columns `product_id`, `p.name`, and `p.price` must be in the `GROUP BY` clause since they are referenced in the query select list (but see below). The column `s.units` does not have to be in the `GROUP BY` list since it is only used in an aggregate expression (`sum(...)`), which represents the sales of a product. For each product, the query returns a summary row about all sales of the product.

 functional dependency

 

If the products table is set up so that, say, `product_id` is the primary key, then it would be enough to group by `product_id` in the above example, since name and price would be functionally dependent on the product ID, and so there would be no ambiguity about which name and price value to return for each product ID group.

 

In strict SQL, `GROUP BY` can only group by columns of the source table, but PostgreSQL extends this to also allow `GROUP BY` to group by columns in the select list. Grouping by value expressions instead of simple column names is also allowed (but `GROUP BY` expressions cannot contain aggregate functions or window functions).

 

PostgreSQL also supports the syntax `GROUP BY ALL`, which is equivalent to explicitly writing all select-list entries that do not contain either an aggregate function or a window function. This can greatly simplify ad-hoc exploration of data. As an example, these queries are equivalent:

```
=> SELECT a, b, a + b, sum(c) FROM test1 GROUP BY ALL;
a | b | ?column? | sum
---+---+----------+----
1 | 4 | 5 | 9
2 | 5 | 7 | 12
3 | 6 | 9 | 15
(3 rows)

=> SELECT a, b, a + b, sum(c) FROM test1 GROUP BY a, b, a + b;
a | b | ?column? | sum
---+---+----------+----
1 | 4 | 5 | 9
2 | 5 | 7 | 12
3 | 6 | 9 | 15
(3 rows)
```

 
 HAVING
 

 

If a table has been grouped using `GROUP BY`, but only certain groups are of interest, the `HAVING` clause can be used, much like a `WHERE` clause, to eliminate groups from the result. The syntax is:

```
SELECT select_list FROM ... WHERE ... GROUP BY ... HAVING boolean_expression
```

Expressions in the `HAVING` clause can refer both to grouped expressions and to ungrouped expressions (which necessarily involve an aggregate function).

 

Example:

```
=> SELECT x, sum(y) FROM test1 GROUP BY x HAVING sum(y) > 3;
x | sum
---+-----
a | 4
b | 5
(2 rows)

=> SELECT x, sum(y) FROM test1 GROUP BY x HAVING x CURRENT_DATE - INTERVAL '4 weeks'
GROUP BY product_id, p.name, p.price, p.cost
HAVING sum(p.price * s.units) > 5000;
```

In the example above, the `WHERE` clause is selecting rows by a column that is not grouped (the expression is only true for sales during the last four weeks), while the `HAVING` clause restricts the output to groups with total gross sales over 5000. Note that the aggregate expressions do not necessarily need to be the same in all parts of the query.

 

If a query contains aggregate function calls, but no `GROUP BY` clause, grouping still occurs: the result is a single group row (or perhaps no rows at all, if the single row is then eliminated by `HAVING`). The same is true if it contains a `HAVING` clause, even without any aggregate function calls or `GROUP BY` clause.

 

 

 

## `GROUPING SETS`, `CUBE`, and `ROLLUP`

 
 GROUPING SETS
 
 
 CUBE
 
 
 ROLLUP
 

 

More complex grouping operations than those described above are possible using the concept of grouping sets. The data selected by the `FROM` and `WHERE` clauses is grouped separately by each specified grouping set, aggregates computed for each group just as for simple `GROUP BY` clauses, and then the results returned. For example:

```
=> SELECT * FROM items_sold;
brand | size | sales
-------+------+-------
Foo | L | 10
Foo | M | 20
Bar | M | 15
Bar | L | 5
(4 rows)

=> SELECT brand, size, sum(sales) FROM items_sold GROUP BY GROUPING SETS ((brand), (size), ());
brand | size | sum
-------+------+-----
Foo | | 30
Bar | | 20
| L | 15
| M | 35
| | 50
(5 rows)
```

 

Each sublist of `GROUPING SETS` may specify zero or more columns or expressions and is interpreted the same way as though it were directly in the `GROUP BY` clause. An empty grouping set means that all rows are aggregated down to a single group (which is output even if no input rows were present), as described above for the case of aggregate functions with no `GROUP BY` clause.

 

References to the grouping columns or expressions are replaced by null values in result rows for grouping sets in which those columns do not appear. To distinguish which grouping a particular output row resulted from, see `functions-grouping-table`.

 

A shorthand notation is provided for specifying two common types of grouping set. A clause of the form

```
ROLLUP ( e1, e2, e3, ... )
```

represents the given list of expressions and all prefixes of the list including the empty list; thus it is equivalent to

```
GROUPING SETS (
( e1, e2, e3, ... ),
...
( e1, e2 ),
( e1 ),
( )
)
```

This is commonly used for analysis over hierarchical data; e.g., total salary by department, division, and company-wide total.

 

A clause of the form

```
CUBE ( e1, e2, ... )
```

represents the given list and all of its possible subsets (i.e., the power set). Thus

```
CUBE ( a, b, c )
```

is equivalent to

```
GROUPING SETS (
( a, b, c ),
( a, b ),
( a, c ),
( a ),
( b, c ),
( b ),
( c ),
( )
)
```

 

The individual elements of a `CUBE` or `ROLLUP` clause may be either individual expressions, or sublists of elements in parentheses. In the latter case, the sublists are treated as single units for the purposes of generating the individual grouping sets. For example:

```
CUBE ( (a, b), (c, d) )
```

is equivalent to

```
GROUPING SETS (
( a, b, c, d ),
( a, b ),
( c, d ),
( )
)
```

and

```
ROLLUP ( a, (b, c), d )
```

is equivalent to

```
GROUPING SETS (
( a, b, c, d ),
( a, b, c ),
( a ),
( )
)
```

 

The `CUBE` and `ROLLUP` constructs can be used either directly in the `GROUP BY` clause, or nested inside a `GROUPING SETS` clause. If one `GROUPING SETS` clause is nested inside another, the effect is the same as if all the elements of the inner clause had been written directly in the outer clause.

 

If multiple grouping items are specified in a single `GROUP BY` clause, then the final list of grouping sets is the Cartesian product of the individual items. For example:

```
GROUP BY a, CUBE (b, c), GROUPING SETS ((d), (e))
```

is equivalent to

```
GROUP BY GROUPING SETS (
(a, b, c, d), (a, b, c, e),
(a, b, d), (a, b, e),
(a, c, d), (a, c, e),
(a, d), (a, e)
)
```

 

ALL GROUP BY ALL DISTINCT GROUP BY DISTINCT When specifying multiple grouping items together, the final set of grouping sets might contain duplicates. For example:

```
GROUP BY ROLLUP (a, b), ROLLUP (a, c)
```

is equivalent to

```
GROUP BY GROUPING SETS (
(a, b, c),
(a, b),
(a, b),
(a, c),
(a),
(a),
(a, c),
(a),
()
)
```

If these duplicates are undesirable, they can be removed using the `DISTINCT` clause directly on the `GROUP BY`. Therefore:

```
GROUP BY DISTINCT ROLLUP (a, b), ROLLUP (a, c)
```

is equivalent to

```
GROUP BY GROUPING SETS (
(a, b, c),
(a, b),
(a, c),
(a),
()
)
```

This is not the same as using `SELECT DISTINCT` because the output rows may still contain duplicates. If any of the ungrouped columns contains NULL, it will be indistinguishable from the NULL used when that same column is grouped.

 

The construct `(a, b)` is normally recognized in expressions as a row constructor. Within the `GROUP BY` clause, this does not apply at the top levels of expressions, and `(a, b)` is parsed as a list of expressions as described above. If for some reason you need a row constructor in a grouping expression, use `ROW(a, b)`.

 

 

 

## Window Function Processing

 
 window function
 order of execution
 

 

If the query contains any window functions (see `tutorial-window`, `functions-window` and `syntax-window-functions`), these functions are evaluated after any grouping, aggregation, and `HAVING` filtering is performed. That is, if the query uses any aggregates, `GROUP BY`, or `HAVING`, then the rows seen by the window functions are the group rows instead of the original table rows from `FROM`/`WHERE`.

 

When multiple window functions are used, all the window functions having equivalent `PARTITION BY` and `ORDER BY` clauses in their window definitions are guaranteed to see the same ordering of the input rows, even if the `ORDER BY` does not uniquely determine the ordering. However, no guarantees are made about the evaluation of functions having different `PARTITION BY` or `ORDER BY` specifications. (In such cases a sort step is typically required between the passes of window function evaluations, and the sort is not guaranteed to preserve ordering of rows that its `ORDER BY` sees as equivalent.)

 

Currently, window functions always require presorted data, and so the query output will be ordered according to one or another of the window functions' `PARTITION BY`/`ORDER BY` clauses. It is not recommended to rely on this, however. Use an explicit top-level `ORDER BY` clause if you want to be sure the results are sorted in a particular way.

 

 

 

 

## Select Lists

 
 SELECT
 select list
 

 

As shown in the previous section, the table expression in the `SELECT` command constructs an intermediate virtual table by possibly combining tables, views, eliminating rows, grouping, etc. This table is finally passed on to processing by the select list. The select list determines which columns of the intermediate table are actually output.

 

 

## Select-List Items

 
 *
 

 

The simplest kind of select list is `*` which emits all columns that the table expression produces. Otherwise, a select list is a comma-separated list of value expressions (as defined in `sql-expressions`). For instance, it could be a list of column names:

```
SELECT a, b, c FROM ...
```

The columns names `a`, `b`, and `c` are either the actual names of the columns of tables referenced in the `FROM` clause, or the aliases given to them as explained in `queries-table-aliases`. The name space available in the select list is the same as in the `WHERE` clause, unless grouping is used, in which case it is the same as in the `HAVING` clause.

 

If more than one table has a column of the same name, the table name must also be given, as in:

```
SELECT tbl1.a, tbl2.a, tbl1.b FROM ...
```

When working with multiple tables, it can also be useful to ask for all the columns of a particular table:

```
SELECT tbl1.*, tbl2.a FROM ...
```

See `rowtypes-usage` for more about the `table_name``.*` notation.

 

If an arbitrary value expression is used in the select list, it conceptually adds a new virtual column to the returned table. The value expression is evaluated once for each result row, with the row's values substituted for any column references. But the expressions in the select list do not have to reference any columns in the table expression of the `FROM` clause; they can be constant arithmetic expressions, for instance.

 

 

 

## Column Labels

 
 alias
 in the select list
 

 

The entries in the select list can be assigned names for subsequent processing, such as for use in an `ORDER BY` clause or for display by the client application. For example:

```
SELECT a AS value, b + c AS sum FROM ...
```

 

If no output column name is specified using `AS`, the system assigns a default column name. For simple column references, this is the name of the referenced column. For function calls, this is the name of the function. For complex expressions, the system will generate a generic name.

 

The `AS` key word is usually optional, but in some cases where the desired column name matches a PostgreSQL key word, you must write `AS` or double-quote the column name in order to avoid ambiguity. (`sql-keywords-appendix` shows which key words require `AS` to be used as a column label.) For example, `FROM` is one such key word, so this does not work:

```
SELECT a from, b + c AS sum FROM ...
```

but either of these do:

```
SELECT a AS from, b + c AS sum FROM ...
SELECT a "from", b + c AS sum FROM ...
```

For greatest safety against possible future key word additions, it is recommended that you always either write `AS` or double-quote the output column name.

 

The naming of output columns here is different from that done in the `FROM` clause (see `queries-table-aliases`). It is possible to rename the same column twice, but the name assigned in the select list is the one that will be passed on.

 

 

 

## `DISTINCT`

 
 ALL
 SELECT ALL
 
 
 DISTINCT
 SELECT DISTINCT
 

 
 duplicates
 

 

After the select list has been processed, the result table can optionally be subject to the elimination of duplicate rows. The `DISTINCT` key word is written directly after `SELECT` to specify this:

```
SELECT DISTINCT select_list ...
```

(Instead of `DISTINCT` the key word `ALL` can be used to specify the default behavior of retaining all rows.)

 
 null value
 in DISTINCT
 

 

Obviously, two rows are considered distinct if they differ in at least one column value. Null values are considered equal in this comparison.

 

Alternatively, an arbitrary expression can determine what rows are to be considered distinct:

```
SELECT DISTINCT ON (expression , expression ...) select_list ...
```

Here `expression` is an arbitrary value expression that is evaluated for all rows. A set of rows for which all the expressions are equal are considered duplicates, and only the first row of the set is kept in the output. Note that the first row of a set is unpredictable unless the query is sorted on enough columns to guarantee a unique ordering of the rows arriving at the `DISTINCT` filter. (`DISTINCT ON` processing occurs after `ORDER BY` sorting.)

 

The `DISTINCT ON` clause is not part of the SQL standard and is sometimes considered bad style because of the potentially indeterminate nature of its results. With judicious use of `GROUP BY` and subqueries in `FROM`, this construct can be avoided, but it is often the most convenient alternative.

 

 

 

 

## Combining Queries (`UNION`, `INTERSECT`, `EXCEPT`)

 
 UNION
 
 
 INTERSECT
 
 
 EXCEPT
 
 
 set union
 
 
 set intersection
 
 
 set difference
 
 
 set operation
 

 

The results of two queries can be combined using the set operations union, intersection, and difference. The syntax is

```
query1 UNION ALL query2
query1 INTERSECT ALL query2
query1 EXCEPT ALL query2
```

where `query1` and `query2` are queries that can use any of the features discussed up to this point.

 

`UNION` effectively appends the result of `query2` to the result of `query1` (although there is no guarantee that this is the order in which the rows are actually returned). Furthermore, it eliminates duplicate rows from its result, in the same way as `DISTINCT`, unless `UNION ALL` is used.

 

`INTERSECT` returns all rows that are both in the result of `query1` and in the result of `query2`. Duplicate rows are eliminated unless `INTERSECT ALL` is used.

 

`EXCEPT` returns all rows that are in the result of `query1` but not in the result of `query2`. (This is sometimes called the difference between two queries.) Again, duplicates are eliminated unless `EXCEPT ALL` is used.

 

In order to calculate the union, intersection, or difference of two queries, the two queries must be union compatible, which means that they return the same number of columns and the corresponding columns have compatible data types, as described in `typeconv-union-case`.

 

Set operations can be combined, for example

```
query1 UNION query2 EXCEPT query3
```

which is equivalent to

```
(query1 UNION query2) EXCEPT query3
```

As shown here, you can use parentheses to control the order of evaluation. Without parentheses, `UNION` and `EXCEPT` associate left-to-right, but `INTERSECT` binds more tightly than those two operators. Thus

```
query1 UNION query2 INTERSECT query3
```

means

```
query1 UNION (query2 INTERSECT query3)
```

You can also surround an individual `query` with parentheses. This is important if the `query` needs to use any of the clauses discussed in following sections, such as `LIMIT`. Without parentheses, you'll get a syntax error, or else the clause will be understood as applying to the output of the set operation rather than one of its inputs. For example,

```
SELECT a FROM b UNION SELECT x FROM y LIMIT 10
```

is accepted, but it means

```
(SELECT a FROM b UNION SELECT x FROM y) LIMIT 10
```

not

```
SELECT a FROM b UNION (SELECT x FROM y LIMIT 10)
```

 

 

 

## Sorting Rows (`ORDER BY`)

 
 sorting
 

 
 ORDER BY
 

 

After a query has produced an output table (after the select list has been processed) it can optionally be sorted. If sorting is not chosen, the rows will be returned in an unspecified order. The actual order in that case will depend on the scan and join plan types and the order on disk, but it must not be relied on. A particular output ordering can only be guaranteed if the sort step is explicitly chosen.

 

The `ORDER BY` clause specifies the sort order:

```
SELECT select_list
FROM table_expression
ORDER BY sort_expression1 ASC | DESC NULLS { FIRST | LAST }
, sort_expression2 ASC | DESC NULLS { FIRST | LAST } ...
```

The sort expression(s) can be any expression that would be valid in the query's select list. An example is:

```
SELECT a, b FROM table1 ORDER BY a + b, c;
```

When more than one expression is specified, the later values are used to sort rows that are equal according to the earlier values. Each expression can be followed by an optional `ASC` or `DESC` keyword to set the sort direction to ascending or descending. `ASC` order is the default. Ascending order puts smaller values first, where smaller is defined in terms of the `` operator. Actually, PostgreSQL uses the default B-tree operator class for the expression's data type to determine the sort ordering for `ASC` and `DESC`. Conventionally, data types will be set up so that the `` operators correspond to this sort ordering, but a user-defined data type's designer could choose to do something different.

 
 

 

The `NULLS FIRST` and `NULLS LAST` options can be used to determine whether nulls appear before or after non-null values in the sort ordering. By default, null values sort as if larger than any non-null value; that is, `NULLS FIRST` is the default for `DESC` order, and `NULLS LAST` otherwise.

 

Note that the ordering options are considered independently for each sort column. For example `ORDER BY x, y DESC` means `ORDER BY x ASC, y DESC`, which is not the same as `ORDER BY x DESC, y DESC`.

 

A `sort_expression` can also be the column label or number of an output column, as in:

```
SELECT a + b AS sum, c FROM table1 ORDER BY sum;
SELECT a, max(b) FROM table1 GROUP BY a ORDER BY 1;
```

both of which sort by the first output column. Note that an output column name has to stand alone, that is, it cannot be used in an expression -- for example, this is not correct:

```
SELECT a + b AS sum, c FROM table1 ORDER BY sum + c; -- wrong
```

This restriction is made to reduce ambiguity. There is still ambiguity if an `ORDER BY` item is a simple name that could match either an output column name or a column from the table expression. The output column is used in such cases. This would only cause confusion if you use `AS` to rename an output column to match some other table column's name.

 

`ORDER BY` can be applied to the result of a `UNION`, `INTERSECT`, or `EXCEPT` combination, but in this case it is only permitted to sort by output column names or numbers, not by expressions.

 

 

 

## `LIMIT` and `OFFSET`

 
 LIMIT
 

 
 OFFSET
 

 

`LIMIT` and `OFFSET` allow you to retrieve just a portion of the rows that are generated by the rest of the query:

```
SELECT select_list
FROM table_expression
ORDER BY ...
LIMIT { count | ALL }
OFFSET start
```

 

If a limit count is given, no more than that many rows will be returned (but possibly fewer, if the query itself yields fewer rows). `LIMIT ALL` is the same as omitting the `LIMIT` clause, as is `LIMIT` with a NULL argument.

 

`OFFSET` says to skip that many rows before beginning to return rows. `OFFSET 0` is the same as omitting the `OFFSET` clause, as is `OFFSET` with a NULL argument.

 

If both `OFFSET` and `LIMIT` appear, then `OFFSET` rows are skipped before starting to count the `LIMIT` rows that are returned.

 

When using `LIMIT`, it is important to use an `ORDER BY` clause that constrains the result rows into a unique order. Otherwise you will get an unpredictable subset of the query's rows. You might be asking for the tenth through twentieth rows, but tenth through twentieth in what ordering? The ordering is unknown, unless you specified `ORDER BY`.

 

The query optimizer takes `LIMIT` into account when generating query plans, so you are very likely to get different plans (yielding different row orders) depending on what you give for `LIMIT` and `OFFSET`. Thus, using different `LIMIT`/`OFFSET` values to select different subsets of a query result will give inconsistent results unless you enforce a predictable result ordering with `ORDER BY`. This is not a bug; it is an inherent consequence of the fact that SQL does not promise to deliver the results of a query in any particular order unless `ORDER BY` is used to constrain the order.

 

The rows skipped by an `OFFSET` clause still have to be computed inside the server; therefore a large `OFFSET` might be inefficient.

 

 

 

## `VALUES` Lists

 
 VALUES
 

 

`VALUES` provides a way to generate a constant table that can be used in a query without having to actually create and populate a table on-disk. The syntax is

```
VALUES ( expression [, ...] ) [, ...]
```

Each parenthesized list of expressions generates a row in the table. The lists must all have the same number of elements (i.e., the number of columns in the table), and corresponding entries in each list must have compatible data types. The actual data type assigned to each column of the result is determined using the same rules as for `UNION` (see `typeconv-union-case`).

 

As an example:

```
VALUES (1, 'one'), (2, 'two'), (3, 'three');
```

will return a table of two columns and three rows. It's effectively equivalent to:

```
SELECT 1 AS column1, 'one' AS column2
UNION ALL
SELECT 2, 'two'
UNION ALL
SELECT 3, 'three';
```

By default, PostgreSQL assigns the names `column1`, `column2`, etc. to the columns of a `VALUES` table. The column names are not specified by the SQL standard and different database systems do it differently, so it's usually better to override the default names with a table alias list, like this:

```
=> SELECT * FROM (VALUES (1, 'one'), (2, 'two'), (3, 'three')) AS t (num,letter);
num | letter
-----+--------
1 | one
2 | two
3 | three
(3 rows)
```

 

Syntactically, `VALUES` followed by expression lists is treated as equivalent to:

```
SELECT select_list FROM table_expression
```

and can appear anywhere a `SELECT` can. For example, you can use it as part of a `UNION`, or attach a `sort_specification` (`ORDER BY`, `LIMIT`, and/or `OFFSET`) to it. `VALUES` is most commonly used as the data source in an `INSERT` command, and next most commonly as a subquery.

 

For more information see `sql-values`.

 

 

 

## `WITH` Queries (Common Table Expressions)

 
 WITH
 in SELECT
 

 
 common table expression
 WITH
 

 

`WITH` provides a way to write auxiliary statements for use in a larger query. These statements, which are often referred to as Common Table Expressions or CTEs, can be thought of as defining temporary tables that exist just for one query. Each auxiliary statement in a `WITH` clause can be a `SELECT`, `INSERT`, `UPDATE`, `DELETE`, or `MERGE`; and the `WITH` clause itself is attached to a primary statement that can also be a `SELECT`, `INSERT`, `UPDATE`, `DELETE`, or `MERGE`.

 

 

## `SELECT` in `WITH`

 

The basic value of `SELECT` in `WITH` is to break down complicated queries into simpler parts. An example is:

```
WITH regional_sales AS (
SELECT region, SUM(amount) AS total_sales
FROM orders
GROUP BY region
), top_regions AS (
SELECT region
FROM regional_sales
WHERE total_sales > (SELECT SUM(total_sales)/10 FROM regional_sales)
)
SELECT region,
product,
SUM(quantity) AS product_units,
SUM(amount) AS product_sales
FROM orders
WHERE region IN (SELECT region FROM top_regions)
GROUP BY region, product;
```

which displays per-product sales totals in only the top sales regions. The `WITH` clause defines two auxiliary statements named `regional_sales` and `top_regions`, where the output of `regional_sales` is used in `top_regions` and the output of `top_regions` is used in the primary `SELECT` query. This example could have been written without `WITH`, but we'd have needed two levels of nested sub-`SELECT`s. It's a bit easier to follow this way.

 

 

 

## Recursive Queries

 

RECURSIVE in common table expressions The optional `RECURSIVE` modifier changes `WITH` from a mere syntactic convenience into a feature that accomplishes things not otherwise possible in standard SQL. Using `RECURSIVE`, a `WITH` query can refer to its own output. A very simple example is this query to sum the integers from 1 through 100:

```
WITH RECURSIVE t(n) AS (
VALUES (1)
UNION ALL
SELECT n+1 FROM t WHERE n = '2010-10-01' AND
"date" (o IS orders WHERE o.ordered_when = current_date) COLUMNS (c.name AS customer_name));
```

The graph query part happens inside the `GRAPH_TABLE` construct. As far as the rest of the query is concerned, this acts like a table function in that it produces a computed table as output. Like other `FROM` clause elements, table alias and column alias names can be assigned to the result, and the result can be joined with other tables, subsequently filtered, and so on, for example:

```
SELECT ... FROM GRAPH_TABLE (mygraph MATCH ... COLUMNS (...)) AS myresult (a, b, c) JOIN othertable USING (a) WHERE b > 0 ORDER BY c;
```

 

The `GRAPH_TABLE` clause consists of the graph name, followed by the keyword `MATCH`, followed by a graph pattern expression (see below), followed by the keyword `COLUMNS` and a column list.

 

 

 

## Graph Patterns

 

The core of the graph querying functionality is the graph pattern, which appears after the keyword `MATCH`. Formally, a graph pattern consists of one or more path patterns. A path is a sequence of graph elements, starting and ending with a vertex and alternating between vertices and edges. A path pattern is a syntactic expressions that matches paths.

 

A path pattern thus matches a sequence of vertices and edges. The simplest possible path pattern is

```
()
```

which matches a single vertex. The next simplest pattern would be

```
()-[]->()
```

which matches a vertex followed by an edge followed by a vertex. The characters `()` are a vertex pattern and the characters `-[]->` are an edge pattern.

 

These characters can also be separated by whitespace, for example:

```
( ) - [ ] - > ( )
```

 

A way to remember these symbols is that in visual representations of property graphs, vertices are usually circles (like `()`) and edges have rectangular labels (like `[]`).

 

The above patterns would match any vertex, or any two vertices connected by any edge, which isn't very interesting. Normally, we want to search for elements (vertices and edges) that have certain characteristics. These characteristics are written in between the parentheses or brackets. (This is also called an element pattern filler.) Typically, we would search for elements with a certain label. This is written by `IS labelname`. For example, this would match all vertices with the label `person`:

```
(IS person)
```

The next example would match a vertex with the label `person` connected to a vertex with the label `account` connected by an edge with the label `has`.

```
(IS person)-[IS has]->(IS account)
```

Multiple labels can also be matched, using or semantics:

```
(IS person)-[IS has]->(IS account|creditcard)
```

 

Recall that edges are directed. The other direction is also possible in a path pattern, for example:

```
(IS account)(IS account)
(IS account)(a IS account)
COLUMNS (p.name AS person_name, h.since AS has_account_since, a.num AS account_number)
```

`WHERE` clauses can be used inside element patterns to filter matches:

```
(IS person)-[IS has]->(a IS account WHERE a.type = 'savings')
```
