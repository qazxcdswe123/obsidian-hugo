---
aliases: []
date created: May 26th, 2023
date modified: May 28th, 2023
---

## Concepts
- [[Document Database]]

### Collections
MongoDB stores data records as [documents](https://www.mongodb.com/docs/manual/reference/glossary/#std-term-document) (specifically [BSON documents](https://www.mongodb.com/docs/manual/core/document/#std-label-bson-document-format)) which are gathered together in [collections](https://www.mongodb.com/docs/manual/reference/glossary/#std-term-collection). A [database](https://www.mongodb.com/docs/manual/reference/glossary/#std-term-database) stores one or more collections of documents.

- [[Database Sharding]]

## Operations

### Insertion
 - [`db.collection.insertMany()`](https://www.mongodb.com/docs/manual/reference/method/db.collection.insertMany/#mongodb-method-db.collection.insertMany)  
 insert new [documents](https://www.mongodb.com/docs/manual/core/document/) into the `movies` collection.

```sql
db.movies.insertMany([
   {
      title: 'Titanic',
      year: 1997,
      genres: [ 'Drama', 'Romance' ],
      rated: 'PG-13',
      languages: [ 'English', 'French', 'German', 'Swedish', 'Italian', 'Russian' ],
      released: ISODate("1997-12-19T00:00:00.000Z"),
      awards: {
         wins: 127,
         nominations: 63,
         text: 'Won 11 Oscars. Another 116 wins & 63 nominations.'
      },
      cast: [ 'Leonardo DiCaprio', 'Kate Winslet', 'Billy Zane', 'Kathy Bates' ],
      directors: [ 'James Cameron' ]
   },
   {
      title: 'The Dark Knight',
      year: 2008,
      genres: [ 'Action', 'Crime', 'Drama' ],
      rated: 'PG-13',
      languages: [ 'English', 'Mandarin' ],
      released: ISODate("2008-07-18T00:00:00.000Z"),
      awards: {
         wins: 144,
         nominations: 106,
         text: 'Won 2 Oscars. Another 142 wins & 106 nominations.'
      },
      cast: [ 'Christian Bale', 'Heath Ledger', 'Aaron Eckhart', 'Michael Caine' ],
      directors: [ 'Christopher Nolan' ]
   }
])
```

### Find All