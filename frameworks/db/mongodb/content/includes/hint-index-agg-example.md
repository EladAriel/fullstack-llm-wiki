---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/hint-index-agg-example.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

The `movies` collection in the `sample_mflix` database contains documents similar to these:

```javascript
{ 
   title: "The Shawshank Redemption", 
   year: 1994, rated: "R", 
   imdb: { rating: 9.3, votes: 1513145, id: 111161 }
},
{ 
   title: "The Godfather", 
   year: 1972, 
   rated: "R", 
   imdb: { rating: 9.2, votes: 1038358, id: 68646 }
},
{ 
   title: "The Dark Knight",
   year: 2008, rated: "PG-13", 
   imdb: { rating: 9, votes: 1495351, id: 468569 }
},
{ 
   title: "Forrest Gump",
   year: 1994, 
   rated: "PG-13", 
   imdb: { rating: 8.8, votes: 1087227, id: 109830 }
}
```

Assume the following indexes exist on the `movies` collection:

The following aggregation operation includes the `hint` option to force the usage of the specified index:
