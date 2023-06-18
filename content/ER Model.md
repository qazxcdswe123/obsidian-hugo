---
aliases: []
date created: Jun 12th, 2023
date modified: Jun 12th, 2023
---

## Terminology
- Entity: a “thing” or “object” in the real world that is distinguishable from all other objects.
- Entity set: a set of entities of the same type that share the same properties, or attributes.
- Attributes: An entity is represented by a set of attributes
- Weak Entity Set: one whose existence is dependent on another entity set, called identifying entity set.
	- instead of associating a primary key with a weak entity, we use the primary key of the identifying entity, along with extra attributes, called discriminator attributes to uniquely identify a weak entity.

## Mapping Cardinalities
One is directed cuz it's targeted.  
![image.png](https://img.ynchen.me/2023/06/fda59acad77d9416b3f8bf2ad0b69f6d.webp)

### Participation
On set $E$ in a relationship set $R$
- Total: every entity in $E$ participate in at least one relationship in $R$
	- We indicate total participation of an entity in a relationship set using double lines.  
 ![image.png](https://img.ynchen.me/2023/06/798df0a88029e71239a52dc60f60c80a.webp)

- Partial: otherwise

## Weak Entity Set
In E-R diagrams, a weak entity set is depicted via a **double rectangle** with the discriminator being underlined with a dashed line. 
The relationship set connecting the weak entity set to the identifying strong entity set is depicted by a **double diamond**. 

![image.png](https://img.ynchen.me/2023/06/a319b2a35c1be554bbe35ab7689882ff.webp)

The figure also illustrates the use of double lines to indicate that the participation of the (weak) entity set section in the relationship sec course is total, meaning that every section must be related via sec course to some course. Finally, the arrow from sec course to course indicates that each section is related to a single course.

In general, a weak entity set must have a **total participation** in its identifying relationship set, and the relationship is **many-to-one toward the identifying entity set.**

## Links
- [[Database Design]]