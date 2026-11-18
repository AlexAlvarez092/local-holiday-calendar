"""Generates the website and calendars from the holiday data."""

import argparse
import sys
from datetime import UTC, datetime
from pathlib import Path

from holiday_calendar.data_loader import DataError, load_years
from holiday_calendar.domain import calendar_events, localities
from holiday_calendar.ics_writer import render_calendar
from holiday_calendar.site_config import calendar_path
from holiday_calendar.site_renderer import render_index


def build(data_dir: Path, output_dir: Path, stamp: datetime) -> None:
    """Validates all data before writing anything; output_dir must be empty or missing."""
    years = load_years(data_dir)
    if output_dir.exists() and any(output_dir.iterdir()):
        raise FileExistsError(f"output directory {output_dir} is not empty")

    listed = localities(years)
    for locality in listed:
        target = output_dir / calendar_path(locality)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(render_calendar(locality, calendar_events(locality, years), stamp))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "index.html").write_text(render_index(listed), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("data_dir", type=Path, help="folder with the <year>.yaml files")
    parser.add_argument("output_dir", type=Path, help="empty or missing folder for the site")
    args = parser.parse_args()
    try:
        build(args.data_dir, args.output_dir, datetime.now(UTC))
    except DataError as error:
        print("Invalid holiday data:", *error.errors, sep="\n  ", file=sys.stderr)
        sys.exit(1)
    except FileExistsError as error:
        print(error, file=sys.stderr)
        sys.exit(1)
