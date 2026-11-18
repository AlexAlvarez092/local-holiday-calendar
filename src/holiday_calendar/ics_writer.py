"""Writes a locality's calendar as iCalendar (ADR 0006)."""

from datetime import datetime, timedelta

from icalendar import Calendar, Event, vDuration

from holiday_calendar.domain import Holiday, Locality
from holiday_calendar.site_config import SITE_HOST

REFRESH_INTERVAL = timedelta(days=1)


def calendar_name(locality: Locality) -> str:
    return f"Festivos de {locality.name}"


def render_calendar(locality: Locality, events: list[Holiday], stamp: datetime) -> bytes:
    calendar = Calendar()
    calendar.add("prodid", "-//local-holiday-calendar//ES")
    calendar.add("version", "2.0")
    calendar.add("calscale", "GREGORIAN")
    calendar.add("name", calendar_name(locality))
    calendar.add("x-wr-calname", calendar_name(locality))
    calendar.add("refresh-interval", vDuration(REFRESH_INTERVAL), parameters={"VALUE": "DURATION"})
    calendar.add("x-published-ttl", vDuration(REFRESH_INTERVAL))
    for holiday in events:
        event = Event()
        event.add("uid", f"{holiday.date.isoformat()}-{locality.id}@{SITE_HOST}")
        event.add("dtstamp", stamp)
        event.add("dtstart", holiday.date)
        event.add("dtend", holiday.date + timedelta(days=1))
        event.add("summary", holiday.name)
        calendar.add_component(event)
    return calendar.to_ical()
