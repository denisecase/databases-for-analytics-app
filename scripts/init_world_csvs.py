"""init_world_csvs.py - Download MySQL World data and create CSV files.

Author: Denise Case
Date: 2026-08

HOW TO RUN THIS FILE:

From the repository root:

uv run python scripts/init_world_csvs.py

This script downloads the official MySQL World sample database
and creates:

data/raw/city.csv
data/raw/country.csv
data/raw/countrylanguage.csv

The SQLite database is built later by the project app.
"""

# === DECLARE IMPORTS (BRING IN FREE CODE) ===

import csv
from io import BytesIO, TextIOWrapper
from pathlib import Path
import re
from typing import Final
from urllib.error import HTTPError, URLError
from urllib.request import urlopen
from zipfile import BadZipFile, ZipFile

# === DECLARE GLOBAL CONSTANTS ===

WORLD_ZIP_URL: Final[str] = "https://downloads.mysql.com/docs/world-db.zip"

RAW_DATA_DIR: Final[Path] = Path("data") / "raw"

CITY_FILE: Final[Path] = RAW_DATA_DIR / "city.csv"
COUNTRY_FILE: Final[Path] = RAW_DATA_DIR / "country.csv"
COUNTRY_LANGUAGE_FILE: Final[Path] = RAW_DATA_DIR / "countrylanguage.csv"

EXPECTED_COUNTS: Final[dict[str, int]] = {
    "city": 4079,
    "country": 239,
    "countrylanguage": 984,
}

HEADERS: Final[dict[str, list[str]]] = {
    "city": [
        "ID",
        "Name",
        "CountryCode",
        "District",
        "Population",
    ],
    "country": [
        "Code",
        "Name",
        "Continent",
        "Region",
        "SurfaceArea",
        "IndepYear",
        "Population",
        "LifeExpectancy",
        "GNP",
        "GNPOld",
        "LocalName",
        "GovernmentForm",
        "HeadOfState",
        "Capital",
        "Code2",
    ],
    "countrylanguage": [
        "CountryCode",
        "Language",
        "IsOfficial",
        "Percentage",
    ],
}

OUTPUT_FILES: Final[dict[str, Path]] = {
    "city": CITY_FILE,
    "country": COUNTRY_FILE,
    "countrylanguage": COUNTRY_LANGUAGE_FILE,
}

INSERT_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"INSERT\s+INTO\s+`?(city|country|countrylanguage)`?\s+VALUES\s*\((.*)\);",
    flags=re.IGNORECASE,
)


# === DEFINE A FUNCTION TO DOWNLOAD WORLD.SQL ===


def download_world_sql() -> str:
    """Download and return the official MySQL world.sql file.

    Returns:
        The contents of world.sql as text.

    Raises:
        RuntimeError: If the archive cannot be downloaded or read.
    """
    try:
        with urlopen(WORLD_ZIP_URL, timeout=60) as response:
            zip_bytes: bytes = response.read()
    except (HTTPError, URLError, TimeoutError) as exc:
        raise RuntimeError(
            f"Unable to download the official MySQL World database from {WORLD_ZIP_URL}"
        ) from exc

    try:
        with ZipFile(BytesIO(zip_bytes)) as archive:
            sql_names: list[str] = [
                name
                for name in archive.namelist()
                if name.lower().endswith("world.sql")
            ]

            if len(sql_names) != 1:
                raise RuntimeError(
                    "Expected exactly one world.sql file in the MySQL archive."
                )

            with (
                archive.open(sql_names[0]) as sql_file,
                TextIOWrapper(sql_file, encoding="utf-8") as text_file,
            ):
                return text_file.read()

    except BadZipFile as exc:
        raise RuntimeError(
            "The downloaded MySQL World file is not a valid ZIP archive."
        ) from exc


# === DEFINE A FUNCTION TO PARSE ONE INSERT ROW ===


def parse_insert_values(values_text: str) -> list[str | None]:
    """Parse one MySQL INSERT VALUES row.

    Args:
        values_text: Text inside the VALUES parentheses.

    Returns:
        Parsed field values for one row.
    """
    reader = csv.reader(
        [values_text],
        delimiter=",",
        quotechar="'",
        escapechar="\\",
        skipinitialspace=True,
    )

    values: list[str] = next(reader)

    return [None if value.upper() == "NULL" else value for value in values]


# === DEFINE A FUNCTION TO EXTRACT THE THREE TABLES ===


def extract_world_rows(
    sql_text: str,
) -> dict[str, list[list[str | None]]]:
    """Extract World table rows from the MySQL SQL script.

    Args:
        sql_text: Contents of world.sql.

    Returns:
        Rows keyed by table name.
    """
    rows: dict[str, list[list[str | None]]] = {
        "city": [],
        "country": [],
        "countrylanguage": [],
    }

    for line in sql_text.splitlines():
        match = INSERT_PATTERN.search(line)

        if match is None:
            continue

        table_name: str = match.group(1).lower()
        values_text: str = match.group(2)

        rows[table_name].append(parse_insert_values(values_text))

    return rows


# === DEFINE A FUNCTION TO VERIFY THE EXTRACTED DATA ===


def verify_world_rows(
    rows: dict[str, list[list[str | None]]],
) -> None:
    """Verify expected World table row and column counts.

    Args:
        rows: Extracted rows keyed by table name.

    Returns:
        None.

    Raises:
        RuntimeError: If expected data is missing or malformed.
    """
    for table_name, expected_count in EXPECTED_COUNTS.items():
        table_rows = rows[table_name]
        actual_count: int = len(table_rows)

        if actual_count != expected_count:
            raise RuntimeError(
                f"{table_name}: expected {expected_count} rows, found {actual_count}."
            )

        expected_columns: int = len(HEADERS[table_name])

        for row_number, row in enumerate(table_rows, start=1):
            if len(row) != expected_columns:
                raise RuntimeError(
                    f"{table_name}: row {row_number} has "
                    f"{len(row)} columns; expected {expected_columns}."
                )


# === DEFINE A FUNCTION TO WRITE THE CSV FILES ===


def write_world_csvs(
    rows: dict[str, list[list[str | None]]],
) -> None:
    """Write the World tables to CSV files.

    Args:
        rows: Extracted rows keyed by table name.

    Returns:
        None.
    """
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

    for table_name, output_file in OUTPUT_FILES.items():
        with output_file.open(
            "w",
            encoding="utf-8",
            newline="",
        ) as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(HEADERS[table_name])
            writer.writerows(rows[table_name])

        print(f"Wrote {output_file} ({len(rows[table_name]):,} rows)")


# === DEFINE THE MAIN FUNCTION ===


def main() -> None:
    """Download the MySQL World data and create CSV source files."""
    print("Downloading the official MySQL World sample database...")

    sql_text: str = download_world_sql()

    print("Extracting World table data...")

    rows = extract_world_rows(sql_text)

    verify_world_rows(rows)

    print("Writing CSV source files...")

    write_world_csvs(rows)

    print("Success.")
    print("You can now run:")
    print("uv run python -m databases_for_analytics.app")


# === CONDITIONAL EXECUTION GUARD ===

if __name__ == "__main__":
    main()
