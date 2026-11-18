"""Renders the static website page (ADR 0003)."""

from jinja2 import Environment, PackageLoader, select_autoescape

from holiday_calendar.domain import Locality
from holiday_calendar.site_config import subscription_url

_environment = Environment(
    loader=PackageLoader("holiday_calendar"),
    autoescape=select_autoescape(["html", "j2"]),
)


def render_index(localities: list[Locality]) -> str:
    entries = [
        {"name": locality.name, "url": subscription_url(locality)} for locality in localities
    ]
    return _environment.get_template("index.html.j2").render(localities=entries)
