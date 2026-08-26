"""world_db.py - Database utility functions.

This has just two functions:

One to build the SQLite World database from CSV files, and
One to open an existing SQLite database and verify that it contains the required tables.

You should not need to modify this file.
It works for this dataset.

Author: Denise Case
Date: 2026-08
"""

from pathlib import Path
import sqlite3

import pandas as pd

__all__: list[str] = [
    "build_db",
    "get_connection",
]


def build_db(
    city_file: Path,
    country_file: Path,
    country_language_file: Path,
    database_file: Path,
) -> None:
    """Build the SQLite World database from CSV source files."""

    source_files: list[Path] = [
        city_file,
        country_file,
        country_language_file,
    ]

    for source_file in source_files:
        if not source_file.is_file():
            raise FileNotFoundError(f"Required source file not found: {source_file}")

        if source_file.stat().st_size == 0:
            raise RuntimeError(f"Required source file is empty: {source_file}")

    city_df: pd.DataFrame = pd.read_csv(city_file)
    country_df: pd.DataFrame = pd.read_csv(country_file)
    country_language_df: pd.DataFrame = pd.read_csv(country_language_file)

    database_file.unlink(missing_ok=True)

    with sqlite3.connect(database_file) as connection:
        city_df.to_sql(
            "city",
            connection,
            if_exists="replace",
            index=False,
        )

        country_df.to_sql(
            "country",
            connection,
            if_exists="replace",
            index=False,
        )

        country_language_df.to_sql(
            "countrylanguage",
            connection,
            if_exists="replace",
            index=False,
        )


def get_connection(
    database_file: Path,
    required_tables: set[str],
) -> sqlite3.Connection:
    """Open an existing SQLite database and verify required tables."""
    if not database_file.is_file():
        raise FileNotFoundError(f"SQLite database not found: {database_file}")

    database_uri: str = f"file:{database_file.resolve().as_posix()}?mode=ro"

    connection: sqlite3.Connection = sqlite3.connect(
        database_uri,
        uri=True,
    )

    table_rows = connection.execute(
        """
        SELECT name
        FROM sqlite_master
        WHERE type = 'table';
        """
    ).fetchall()

    available_tables: set[str] = {table_name for (table_name,) in table_rows}

    missing_tables: set[str] = required_tables - available_tables

    if missing_tables:
        connection.close()
        raise RuntimeError(
            "SQLite database is missing required tables: "
            f"{', '.join(sorted(missing_tables))}"
        )

    return connection
