Based on [[Set Theory]]

## Selection
- $\sigma_{predicate} (R)$ : (horizontal)
- `SELECT * FROM R WHERE a_id = 'a2'`

## Projection
- $\uppi$ : retains only desired columns (vertical)
Projection takes in a relation and outputs a relation with tuples that contain only specified attributes.
- `SELECT b_id-100, a_id FROM R WHERE a_id = 'a2'`

## Union
- $S1 \cap S2 = S1 - (S1 - S2)$
- `(SELECT * FROM R) UNION ALL (SELECT * FROM S)`

## Intersection
- `(SELECT * FROM R) INTERSECT (SELECT * FROM S)`

## Difference
- `(SELECT * FROM R) EXCEPT (SELECT * FROM S)`

## Product
- `(SELECT * FROM R) CROSS JOIN (SELECT * FROM S)`
- `SELECT * FROM R, S`

## Join
Get tuples from both $r$ and $s$ and put on restriction $\theta$ on them.
$r \bowtie_{\theta} s = \sigma_{\theta} (r \times s)$
- `SELECT * FROM R JOIN S USING (ATTRIBUTE1, ATTRIBUTE2...)`

- Natural Join
	- $R \bowtie S = \uppi_{unq} \; \sigma_{cond}(R \times S)$
	- Remove the duplicate column (Natural)