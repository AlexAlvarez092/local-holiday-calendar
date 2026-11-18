from datetime import UTC, date, datetime, timedelta

from icalendar import Calendar

from holiday_calendar.domain import Holiday, Locality
from holiday_calendar.ics_writer import render_calendar


def test_calendar_is_parsable_with_all_day_events_stable_uids_and_refresh_hints():
    stamp = datetime(2026, 11, 19, tzinfo=UTC)
    events = [Holiday(date(2026, 9, 8), "Día de Asturias y Fiesta local")]

    calendar = Calendar.from_ical(render_calendar(Locality("Gijón"), events, stamp))

    assert calendar["X-WR-CALNAME"] == "Festivos de Gijón"
    assert calendar["NAME"] == "Festivos de Gijón"
    assert calendar["REFRESH-INTERVAL"].params["VALUE"] == "DURATION"
    assert calendar["REFRESH-INTERVAL"].dt == timedelta(days=1)
    assert calendar["X-PUBLISHED-TTL"] == "P1D"
    [event] = calendar.walk("VEVENT")
    assert event["UID"] == "2026-09-08-gijon@alexalvarez092.github.io"
    assert event["SUMMARY"] == "Día de Asturias y Fiesta local"
    assert event.decoded("DTSTART") == date(2026, 9, 8)
    assert event.decoded("DTEND") == date(2026, 9, 9)
    assert event["DTSTART"].params["VALUE"] == "DATE"
