"""Public address of the published site (ADR 0005)."""

from holiday_calendar.domain import Locality

SITE_HOST = "alexalvarez092.github.io"
SITE_PATH = "/local-holiday-calendar/"
CALENDARS_DIR = "calendars"


def calendar_path(locality: Locality) -> str:
    return f"{CALENDARS_DIR}/{locality.id}.ics"


def subscription_url(locality: Locality) -> str:
    return f"webcal://{SITE_HOST}{SITE_PATH}{calendar_path(locality)}"
