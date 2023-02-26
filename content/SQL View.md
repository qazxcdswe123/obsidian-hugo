---
aliases: []
tags: []
date created: Feb 14th, 2023
date modified: Feb 19th, 2023
---
Equivalent with subqueries in `FROM`

```sql
-- playerid and schoolid is the custom column name
CREATE VIEW CAcollege(playerid, schoolid)
AS 
  SELECT c.playerid, c.schoolid 
  FROM collegeplaying c INNER JOIN schools s
  ON c.schoolid = s.schoolid
  WHERE s.schoolState = 'CA';

CREATE VIEW q2ii(namefirst, namelast, playerid, schoolid, yearid)
AS
  SELECT namefirst, namelast, q.playerid, schoolid, yearid
  FROM q2i q INNER JOIN CAcollege c
  ON q.playerid = c.playerid
  ORDER BY yearid DESC, schoolid, q.playerid;
  ;
```