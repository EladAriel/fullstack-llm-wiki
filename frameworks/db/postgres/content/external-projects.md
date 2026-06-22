---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/external-projects.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
---

## External Projects

PostgreSQL is a complex software project, and managing the project is difficult. We have found that many enhancements to PostgreSQL can be more efficiently developed separately from the core project.

## Client Interfaces

interfaces
externally maintained

There are only two client interfaces included in the base PostgreSQL distribution: - libpq is included because it is the primary C language interface, and because many other client interfaces are built on top of it. - ECPG is included because it depends on the server-side SQL grammar, and is therefore sensitive to changes in PostgreSQL itself. All other language interfaces are external projects and are distributed separately. A [list of language interfaces](https://wiki.postgresql.org/wiki/List_of_drivers) is maintained on the PostgreSQL wiki. Note that some of these packages are not released under the same license as PostgreSQL. For more information on each language interface, including licensing terms, refer to its website and documentation.

[https://wiki.postgresql.org/wiki/List_of_drivers](https://wiki.postgresql.org/wiki/List_of_drivers)

## Administration Tools

administration tools
externally maintained

There are several administration tools available for PostgreSQL. The most popular is `[pgAdmin](https://www.pgadmin.org/)`, and there are several commercially available ones as well.

## Procedural Languages

procedural language
externally maintained

PostgreSQL includes several procedural languages with the base distribution: PL/pgSQL, PL/Tcl, PL/Perl, and PL/Python.

In addition, there are a number of procedural languages that are developed and maintained outside the core PostgreSQL distribution. A list of [procedural languages](https://wiki.postgresql.org/wiki/PL_Matrix) is maintained on the PostgreSQL wiki. Note that some of these projects are not released under the same license as PostgreSQL. For more information on each procedural language, including licensing information, refer to its website and documentation.

[https://wiki.postgresql.org/wiki/PL_Matrix](https://wiki.postgresql.org/wiki/PL_Matrix)

## Extensions

extension
externally maintained

PostgreSQL is designed to be easily extensible. For this reason, extensions loaded into the database can function just like features that are built in. The `contrib/` directory shipped with the source code contains several extensions, which are described in `contrib`. Other extensions are developed independently, like `[PostGIS](https://postgis.net/)`. Even PostgreSQL replication solutions can be developed externally. For example, `[Slony-I](https://www.slony.info)` is a popular primary/standby replication solution that is developed independently from the core project.
