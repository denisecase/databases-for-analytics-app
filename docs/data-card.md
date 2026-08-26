# World Database Data Card

## Overview

The **World** sample database contains related data
about countries, cities, and languages.

This project uses the data to practice relational databases,
SQL queries, joins, pandas DataFrames, and Python visualizations.

## Source and Credit

The data comes from the official **MySQL World sample database**
distributed by Oracle.

- [MySQL: Setting Up the World Database](https://dev.mysql.com/doc/world-setup/en/)
- [MySQL Example Databases](https://dev.mysql.com/doc/index-other.html)

The sample data used in the MySQL World database is
**Copyright Statistics Finland**.

The CSV files in this repository were generated from the
official MySQL **world.sql** sample database.

## Data Files

| File                    | Grain                             |  Rows |
| ----------------------- | --------------------------------- | ----: |
| **city.csv**            | One city                          | 4,079 |
| **country.csv**         | One country                       |   239 |
| **countrylanguage.csv** | One country-language relationship |   984 |

## Relationships

The tables are related through shared keys:

- **city.CountryCode** --> **country.Code**
- **countrylanguage.CountryCode** --> **country.Code**

One country can have many cities (1:M).

One country can have many country-language records (1:M).

## SQLite Database

The project also includes **data/world.sqlite**,
a SQLite version of the same related data.

SQLite provides a lightweight relational database
that can be queried directly from Python
without requiring a separate database server.
It's an easy, file-based way to use SQL on related tables when the
dataset is small and can fit easily into memory.

## Notes

This is a sample instructional dataset
rather than current authoritative demographic data.

Use it to practice database concepts and analytics techniques,
not as a source for current population, political,
geographic, or language statistics.

---

[◄ Back to Home](index.md)
