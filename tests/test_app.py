"""tests/test_app.py - Smoke test for the example.

WHY: Professional Python projects include tests to verify that code runs
     correctly and to catch problems early when changes are made.
     Running tests is part of the standard workflow in every module.

OBS: You do not need to read or modify this file.
"""

import pandas as pd

from databases_for_analytics.app import (
    DATABASE_FILE,
    REQUIRED_TABLES,
    SQL_QUERY,
)
from databases_for_analytics.world_db import get_connection


def test_app_runs() -> None:
    """Confirm the database opens and the example SQL query runs."""
    connection = get_connection(
        database_file=DATABASE_FILE,
        required_tables=REQUIRED_TABLES,
    )

    try:
        result_df: pd.DataFrame = pd.read_sql_query(
            SQL_QUERY,
            connection,
        )

        assert not result_df.empty

    finally:
        connection.close()
