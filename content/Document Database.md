## What
A document database is a database model that represents items in individual objects called documents.

While documents can be grouped together for organization, they don't have to share the same structure and can be designed to uniquely capture the data required to describe the item in question. 

Document databases typically don't support robust join operations to link different documents together, but are often praised for their flexibility and quick time-to-productivity due to their flexibility and ease in representing programmatic data structures.

Instead of storing arbitrary blobs of data, document databases store data in structured formats called documents, often using formats like JSON, BSON, or XML.

## Why
Document databases are a good choice for rapid development because you can change the properties of the data you want to save at any point without altering existing structures or data. You only need to backfill records if you want to. Each document within the database stands on its own with its own system of organization. If you're still figuring out your data structure and your data is mainly composed discrete entries that don't include a lot of cross references, a document database might be a good place to start.