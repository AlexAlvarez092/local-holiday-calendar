"""Holiday domain: localities, holidays and the events of each locality's calendar."""

import re
import unicodedata
from collections.abc import Iterable, Mapping
from dataclasses import dataclass, field
from datetime import date

MERGED_NAME_SEPARATOR = " y "


@dataclass(frozen=True)
class Holiday:
    date: date
    name: str


@dataclass(frozen=True)
class YearHolidays:
    year: int
    national: tuple[Holiday, ...]
    regional: tuple[Holiday, ...]
    local: Mapping[str, tuple[Holiday, ...]] = field(default_factory=dict)

    def applicable_to(self, locality_name: str) -> tuple[Holiday, ...]:
        """National, regional and local holidays of a locality, in that order."""
        return self.national + self.regional + self.local.get(locality_name, ())


def locality_id(name: str) -> str:
    """URL identifier of a locality: lowercase, without accents, hyphen-separated."""
    without_accents = "".join(
        char for char in unicodedata.normalize("NFKD", name) if not unicodedata.combining(char)
    )
    return re.sub(r"[^a-z0-9]+", "-", without_accents.lower()).strip("-")


@dataclass(frozen=True)
class Locality:
    name: str

    @property
    def id(self) -> str:
        return locality_id(self.name)


def localities(years: Iterable[YearHolidays]) -> list[Locality]:
    names = {name for year in years for name in year.local}
    return sorted((Locality(name) for name in names), key=lambda locality: locality.id)


def calendar_events(locality: Locality, years: Iterable[YearHolidays]) -> list[Holiday]:
    """One event per date; holidays sharing a date are merged into a single event."""
    names_by_date: dict[date, list[str]] = {}
    for year in years:
        for holiday in year.applicable_to(locality.name):
            names_by_date.setdefault(holiday.date, []).append(holiday.name)
    return [
        Holiday(day, MERGED_NAME_SEPARATOR.join(names))
        for day, names in sorted(names_by_date.items())
    ]
