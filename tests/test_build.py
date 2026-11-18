from datetime import UTC, datetime

import pytest
from icalendar import Calendar

from conftest import VALID_YEAR, write_year
from holiday_calendar.build import build
from holiday_calendar.data_loader import DataError

STAMP = datetime(2026, 11, 19, tzinfo=UTC)


def test_builds_index_and_one_calendar_per_locality(data_dir, tmp_path):
    write_year(data_dir, "2026.yaml", VALID_YEAR)
    output = tmp_path / "site"

    build(data_dir, output, STAMP)

    index = (output / "index.html").read_text(encoding="utf-8")
    assert 'href="webcal://alexalvarez092.github.io/local-holiday-calendar/calendars/gijon.ics"' in index
    assert 'href="webcal://alexalvarez092.github.io/local-holiday-calendar/calendars/oviedo.ics"' in index
    assert index.index("Gijón") < index.index("Oviedo")
    assert sorted(path.name for path in (output / "calendars").iterdir()) == ["gijon.ics", "oviedo.ics"]
    Calendar.from_ical((output / "calendars" / "oviedo.ics").read_bytes())


def test_empty_data_builds_page_without_localities(data_dir, tmp_path):
    output = tmp_path / "site"

    build(data_dir, output, STAMP)

    assert "Todavía no hay concejos disponibles." in (output / "index.html").read_text(encoding="utf-8")


def test_invalid_data_writes_nothing(data_dir, tmp_path):
    write_year(data_dir, "2026.yaml", "national: [")
    output = tmp_path / "site"

    with pytest.raises(DataError):
        build(data_dir, output, STAMP)

    assert not output.exists()


def test_refuses_non_empty_output_directory(data_dir, tmp_path):
    output = tmp_path / "site"
    output.mkdir()
    (output / "keep.txt").write_text("x", encoding="utf-8")

    with pytest.raises(FileExistsError):
        build(data_dir, output, STAMP)
