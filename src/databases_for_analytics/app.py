"""app.py - Project script (example).

Author: Denise Case
Date: 2026-08

HOW TO RUN THIS FILE:

From the VS Code menu (with only this project open in VS Code),
click "Terminal" / "New Terminal" to
open an integrated Terminal in the root project folder.

Paste the following command and press ENTER or RETURN
to run this file as a script:

uv run python -m databases_for_analytics.app

PROJECT:

Use Python to connect to a SQLite database,
run a SQL query,
load the query result into a pandas DataFrame,
and visualize the result.

SQLite is a lightweight relational database.
Python includes support for SQLite in the Standard Library.

This example shows a common analytics workflow:

1. BUILD a SQLite database from source data files.
2. CONNECT to the database.

With the DB:

1. QUERY the database using SQL.
2. LOAD the query result into a pandas DataFrame.
3. INSPECT the result.
4. VISUALIZE the result.
5. DISPLAY the visualization.

Finally:

ALWAYS CLOSE the database connection.
"""

# === DECLARE IMPORTS (BRING IN FREE CODE) ===

import logging
from pathlib import Path
import sqlite3
from typing import Final

from datafun_toolkit.logger import get_logger, log_header, log_path
import matplotlib.pyplot as plt
import pandas as pd

from databases_for_analytics.world_db import build_db, get_connection

# === CONFIGURE LOGGER ONCE PER MODULE (PYTHON FILE) ===

LOG: logging.Logger = get_logger("DBA", level="INFO")

# === DECLARE GLOBAL CONSTANTS ===

# All of these global variables are CONSTANT.
# They do NOT change while the program runs.
# By convention, constants use UPPERCASE_WITH_UNDERSCORES.
# Final indicates that the value should not be reassigned.

# === LOCATE THE RAW DATA FILES ===

RAW_DATA_DIR: Final[Path] = Path("data") / "raw"

CITY_FILE: Final[Path] = RAW_DATA_DIR / "city.csv"
COUNTRY_FILE: Final[Path] = RAW_DATA_DIR / "country.csv"
COUNTRY_LANGUAGE_FILE: Final[Path] = RAW_DATA_DIR / "countrylanguage.csv"

# === LOCATE THE SQLITE DATABASE ===

DATABASE_FILE: Final[Path] = Path("data") / "world.sqlite"

# === LOCATE THE CHART OUTPUT ===

CHART_DIR: Final[Path] = Path("docs") / "images"
CHART_PATH: Final[Path] = CHART_DIR / "first-chart.png"

# === DECLARE THE LIST OF REQUIRED TABLES ===

REQUIRED_TABLES: Final[set[str]] = {
    "city",
    "country",
    "countrylanguage",
}

# === DETERMINE WHAT ONE ROW REPRESENTS ===

CITY_GRAIN: Final[str] = "one city"
COUNTRY_GRAIN: Final[str] = "one country"
COUNTRY_LANGUAGE_GRAIN: Final[str] = "one country-language relationship"

# === WRITE THE SQL QUERY ===

SQL_QUERY: Final[str] = """
SELECT
    country.Name AS country,
    city.Name AS city,
    city.Population AS population
FROM city
JOIN country
    ON city.CountryCode = country.Code
ORDER BY
    city.Population DESC
LIMIT 10;
"""

# === DETERMINE WHAT ONE ROW REPRESENTS AFTER QUERY ===

QUERY_GRAIN: Final[str] = "one city with its country and population"


# === DEFINE THE MAIN FUNCTION ===


def main() -> None:
    """Entry point when running this file as a Python script.

    Arguments: None.

    Returns: None.
    """
    log_header(LOG, "DBA - PYTHON AND DATABASES")

    LOG.info("===================================")
    LOG.info("START main()")
    LOG.info("===================================")

    LOG.info("-------------------------------")
    LOG.info("01. BUILD the SQLite database.")
    LOG.info("-------------------------------")

    build_db(
        city_file=CITY_FILE,
        country_file=COUNTRY_FILE,
        country_language_file=COUNTRY_LANGUAGE_FILE,
        database_file=DATABASE_FILE,
    )

    log_path(LOG, "SQLite database", path=DATABASE_FILE)
    LOG.info("SQLite database built successfully.")

    LOG.info("-------------------------------")
    LOG.info("02. CONNECT to the SQLite database.")
    LOG.info("-------------------------------")

    connection: sqlite3.Connection = get_connection(
        database_file=DATABASE_FILE,
        required_tables=REQUIRED_TABLES,
    )

    LOG.info("SQLite database connection created.")

    LOG.info(f"City grain: {CITY_GRAIN}")
    LOG.info(f"Country grain: {COUNTRY_GRAIN}")
    LOG.info(f"Country-language grain: {COUNTRY_LANGUAGE_GRAIN}")
    LOG.info(f"Required tables: {sorted(REQUIRED_TABLES)}")

    try:
        LOG.info("-------------------------------")
        LOG.info("DB-1. QUERY the database using SQL.")
        LOG.info("-------------------------------")

        LOG.info(f"\nSQL query:\n{SQL_QUERY}")

        LOG.info("-------------------------------")
        LOG.info("DB-2. LOAD the query result into pandas.")
        LOG.info("-------------------------------")

        try:
            result_df: pd.DataFrame = pd.read_sql_query(
                SQL_QUERY,
                connection,
            )
        except pd.errors.DatabaseError as exc:
            raise RuntimeError(
                "The SQL query could not be executed against the SQLite World database."
            ) from exc

        LOG.info("SQL query completed successfully.")

        LOG.info("-------------------------------")
        LOG.info("DB-3. INSPECT the result.")
        LOG.info("-------------------------------")

        LOG.info(f"Query grain: {QUERY_GRAIN}")
        LOG.info(f"\nQuery result:\n{result_df}")

        if result_df.empty:
            raise RuntimeError("The SQL query completed but returned no rows.")

        LOG.info("-------------------------------")
        LOG.info("DB-4. VISUALIZE the result.")
        LOG.info("-------------------------------")

        population_ax = result_df.plot.bar(
            x="city",
            y="population",
            legend=False,
        )

        population_ax.set_title("Largest Cities by Population")
        population_ax.set_xlabel("City")
        population_ax.set_ylabel("Population")

        plt.tight_layout()

        CHART_DIR.mkdir(parents=True, exist_ok=True)

        population_ax.figure.savefig(
            CHART_PATH,
            bbox_inches="tight",
        )

        log_path(LOG, "Chart", path=CHART_PATH)
        LOG.info("Visualization created and saved successfully.")

        LOG.info("-------------------------------")
        LOG.info("DB-5. DISPLAY the visualization.")
        LOG.info("-------------------------------")

        LOG.info("Close the chart window to continue.")

        plt.show()

    finally:
        # WHY: Always close the database connection when done.
        connection.close()
        LOG.info("SQLite database connection closed.")

    LOG.info("===================================")
    LOG.info("END main() - Executed successfully!")
    LOG.info("===================================")


# === CONDITIONAL EXECUTION GUARD ===

# WHY: This is standard Python "boilerplate" - we copy and paste it
# into every Python script. It is a "conditional execution" guard,
# meaning: if this file is being run as a script, then execute the code
# in the main() function.

if __name__ == "__main__":
    main()
