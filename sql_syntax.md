# SQL Syntax Basics

CRUD - Create, Read, Update, Delete

## INSERT (C part of CRUD)

```sql
INSERT INTO cities (city, country, latitude, longitude)
VALUES ('London', 'UK', 51.5074, -0.1278);
```

## SELECT (R part of CRUD)

```* = all```

```sql
SELECT * FROM cities

SELECT city FROM cities

SELECT id, city, country, latitude, longitude FROM cities
```

### Filtering the data

[Read about the syntax here](https://www.sqlitetutorial.net/sqlite-where/)

```sql
SELECT * FROM cities WHERE id = 1

SELECT id, name FROM cities WHERE id = 1

SELECT id, name FROM cities WHERE latitude IS NULL

SELECT * FROM cities WHERE name LIKE '%ro'

SELECT * FROM cities WHERE name LIKE 'Ta%'

SELECT * FROM cities WHERE name = 'Tallinn'

SELECT * FROM cities WHERE latitude BETWEEN 50 AND 52
```

## UPDATE (U part of CRUD)