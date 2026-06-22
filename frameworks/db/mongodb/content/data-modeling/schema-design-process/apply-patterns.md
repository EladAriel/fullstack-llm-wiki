---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/data-modeling/schema-design-process/apply-patterns.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=====================

# Apply Design Patterns

Schema design patterns are ways to optimize your data model for your application's access patterns. They improve application performance and reduce schema complexity. Schema design patterns affect how your data is stored and what data is returned to your application.

For a list of schema design patterns and examples, see the [Building with Patterns](https://www.mongodb.com/blog/post/building-with-patterns-a-summary)_ MongoDB blog series.

## About this Task

Before you implement schema design patterns, consider the problem that you are trying to solve. Each schema design pattern has different use cases and tradeoffs for data consistency, performance, and complexity.

Implementing a pattern without understanding your application and the data it needs can degrade application performance and cause unnecessary complications.

## Example

Consider the following example patterns used by a movie theater franchise:

- The schema contains a `movie` collection and a `theater`
collection. The schema uses the `subset pattern <group-data-subset-pattern>` to duplicate a subset of information from the `movie` collection in the `theater` collection. The subset pattern reduces the size of documents returned to the application and improves read performance.

- The `movie` collection contains a `total_views` field, which uses
the `computed pattern <model-computed-data>` to calculate a running total of the number of times that customers view a movie across all of the theaters where the movie is shown.

### movie Collection

```javascript
db.movie.insertOne(
  {
    _id: 1,
    title: "Titanic",
    year: 1997,
    director: "James Cameron",
    runtime: 194,
    distributor: "Paramount Pictures",
    languages: [ "English" ],
    total_views: 3500
  }
)
```

### theater Collection

```javascript
db.theater.insertMany(
  [
    {
      name: "Downtown Cinemas",
      address: {
        street: "2212 Taylor Street",
        state: "NY"
      },
      movies: [
        {
           movie_id: 1,
           title: "Titanic",
           runtime: 194,
           views: 1500
        }
      ]
    },
    {
      name: "Midtown Theater",
      address: {
        street: "1232 5th Street",
        state: "NY"
      },
      movies: [
        {
           movie_id: 1,
           title: "Titanic",
           runtime: 194,
           views: 2000
        }
      ]
    }
  ]
)
```

## Learn More

- `data-models-application-context`
- `data-modeling-duplicate-data`
- `data-modeling-data-consistency`
