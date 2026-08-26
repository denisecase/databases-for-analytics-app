# Concepts

> Key concepts introduced in this module.

<!--
Only the first sentence/paragraph of h3 entries
are used for the integrated quiz.

Wrap code terms in double asterisks
rather than single backticks so they can be read aloud.
-->

## 1. Data Sources and Sinks

### Data source

A **data source** is the system, file, service, or
database from which data is obtained for a particular task.

Examples include CSV files, relational databases, document databases,
spreadsheets, APIs, and cloud systems.

### Data sink

A **data sink** is the destination where data is written, stored, or delivered.

A sink might be a database, file, DataFrame,
data warehouse, or another application.

### Source and sink depend on direction

The same system can be a **source** in one workflow and a **sink** in another.

For example, SQLite is a sink when CSV data is loaded into it,
then becomes a source when SQL retrieves data from it.

<!-- markdownlint-disable MD013 -->

| Example Workflow                     | Source                  | Sink            |
| ------------------------------------ | ----------------------- | --------------- |
| Load CSV files into SQLite           | CSV files               | SQLite database |
| Run SQL and load results into pandas | Database                | DataFrame       |
| Export a DataFrame to CSV            | DataFrame               | CSV file        |
| Export query results                 | Database                | CSV file        |
| Load prepared data into a warehouse  | Files or source systems | Data warehouse  |

<!-- markdownlint-enable MD013 -->

### Data movement

**Data movement** is the transfer of data from one
location, format, or system to another.

Common examples include importing data into a database,
exporting query results,
and moving data between databases and analytics tools.

## 2. Ways Databases Run

### Embedded database

An **embedded database** runs within the application using it
rather than requiring a separately managed database server.

SQLite and DuckDB are common embedded databases.

### Client-server database

A **client-server database** runs as a database server that
accepts connections from other programs called clients.

MySQL, PostgreSQL, Microsoft SQL Server,
and Oracle Database commonly use this model.

### Managed cloud database

A **managed cloud database** is operated by a cloud provider
rather than installed and maintained directly by the user.

Cloud platforms can provide transactional databases,
analytical databases, and large-scale data warehouses.

## 3. Common Database Systems

<!-- markdownlint-disable MD013 -->

| Database / System    | Type                      | How It Runs                               | Common Use                                                   |
| -------------------- | ------------------------- | ----------------------------------------- | ------------------------------------------------------------ |
| SQLite               | Relational                | Embedded; commonly stored in a local file | Local applications, learning, testing, lightweight analytics |
| DuckDB               | Relational and analytical | Embedded                                  | Local analytics and analytical SQL                           |
| MySQL                | Relational                | Client-server                             | Web applications and general-purpose databases               |
| PostgreSQL           | Relational                | Client-server                             | Applications, analytics, and complex SQL                     |
| Microsoft SQL Server | Relational                | Client-server                             | Business systems, reporting, and Microsoft environments      |
| Oracle Database      | Relational                | Client-server                             | Large enterprise systems                                     |
| MongoDB              | Document                  | Client-server                             | Flexible and nested document data                            |
| Snowflake            | Cloud data warehouse      | Managed cloud service                     | Large-scale analytics and data warehousing                   |
| Google BigQuery      | Cloud data warehouse      | Managed cloud service                     | Large-scale analytical queries                               |
| Amazon Redshift      | Cloud data warehouse      | Managed cloud service                     | Data warehousing and analytics in AWS                        |

<!-- markdownlint-enable MD013 -->

## 4. Files and Databases

### Data file versus database

A **data file** stores data in a file format, while a **database**
provides software for managing and querying stored data.

CSV and Parquet are data file formats,
while SQLite, DuckDB, PostgreSQL, and MySQL are database systems.

<!-- markdownlint-disable MD013 -->

| Storage / Database | General Style                    | Important Distinction                                            |
| ------------------ | -------------------------------- | ---------------------------------------------------------------- |
| CSV                | Data file format                 | Simple text-based tabular data                                   |
| Parquet            | Data file format                 | Column-oriented format designed for efficient analytical storage |
| SQLite             | Embedded relational database     | Database engine runs locally with the application                |
| DuckDB             | Embedded analytical database     | Designed especially for analytical SQL workloads                 |
| PostgreSQL         | Server-based relational database | A separate database server accepts client connections            |

<!-- markdownlint-enable MD013 -->

## 5. Databases in Analytics

### Database to DataFrame

A common analytics workflow uses SQL to retrieve selected data from a database
and load the result into a **DataFrame**.

The database handles storage and querying,
while tools such as pandas can continue the analysis
and create visualizations.

### DataFrame to database

Data can also move from a **DataFrame** into a database.

This is useful when transformed or prepared data
needs to be stored persistently for later use.

### Persistent storage

**Persistent storage** keeps data available after the program using it stops running.

Database records and saved files persist,
while an unsaved Python DataFrame normally exists only
while the program is running.

### Generated database

A **generated database** can be created from source data
rather than serving as the original source itself.

For example, CSV files can remain the source data
while a SQLite database is generated from them
for querying and analysis.

---

[◄ Back to Home](index.md)
