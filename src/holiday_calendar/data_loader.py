"""Loads and validates the yearly holiday YAML files (ADR 0001)."""

import re
from datetime import date
from pathlib import Path
from typing import Any

import yaml

from holiday_calendar.domain import Holiday, YearHolidays, locality_id

YEAR_FILE_PATTERN = re.compile(r"^(\d{4})\.yaml$")
TOP_LEVEL_KEYS = ("national", "regional", "local")
HOLIDAY_FIELDS = {"date", "name"}


class DataError(Exception):
    def __init__(self, errors: list[str]):
        super().__init__("\n".join(errors))
        self.errors = errors


class _UniqueKeyLoader(yaml.SafeLoader):
    pass


def _construct_unique_mapping(loader: yaml.SafeLoader, node: yaml.MappingNode, deep: bool = False):
    seen = set()
    for key_node, _ in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in seen:
            raise yaml.constructor.ConstructorError(
                None, None, f"duplicate key {key!r}", key_node.start_mark
            )
        seen.add(key)
    return loader.construct_mapping(node, deep)


_UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_unique_mapping
)


def load_years(data_dir: Path) -> list[YearHolidays]:
    """Returns the holidays of every year file, or raises DataError listing all problems."""
    errors: list[str] = []
    years: list[YearHolidays] = []
    for path in sorted(data_dir.glob("*.y*ml")):
        match = YEAR_FILE_PATTERN.match(path.name)
        if not match:
            errors.append(f"{path.name}: file name must be <year>.yaml")
            continue
        year = _load_year(path, int(match.group(1)), errors)
        if year is not None:
            years.append(year)
    _check_locality_ids(years, errors)
    if errors:
        raise DataError(errors)
    return years


def _load_year(path: Path, year: int, errors: list[str]) -> YearHolidays | None:
    try:
        content = yaml.load(path.read_text(encoding="utf-8"), Loader=_UniqueKeyLoader)
    except (yaml.YAMLError, ValueError) as error:
        errors.append(f"{path.name}: invalid YAML: {error}")
        return None

    file_errors: list[str] = []
    if not isinstance(content, dict) or set(content) != set(TOP_LEVEL_KEYS):
        file_errors.append(f"top-level keys must be exactly {', '.join(TOP_LEVEL_KEYS)}")
        errors.extend(f"{path.name}: {error}" for error in file_errors)
        return None

    national = _holidays(content["national"], "national", year, file_errors)
    regional = _holidays(content["regional"], "regional", year, file_errors)
    local: dict[str, tuple[Holiday, ...]] = {}
    if not isinstance(content["local"], dict) or not content["local"]:
        file_errors.append("local must be a non-empty mapping of locality names to lists")
    else:
        for name, holidays in content["local"].items():
            if not isinstance(name, str) or not name.strip():
                file_errors.append(f"local: locality name {name!r} must be a non-empty string")
                continue
            local[name] = _holidays(holidays, f"local.{name}", year, file_errors)

    errors.extend(f"{path.name}: {error}" for error in file_errors)
    if file_errors:
        return None
    return YearHolidays(year, national, regional, local)


def _holidays(items: Any, where: str, year: int, errors: list[str]) -> tuple[Holiday, ...]:
    if not isinstance(items, list) or not items:
        errors.append(f"{where} must be a non-empty list")
        return ()
    holidays = []
    for index, item in enumerate(items):
        position = f"{where}[{index}]"
        if not isinstance(item, dict) or set(item) != HOLIDAY_FIELDS:
            errors.append(f"{position} must have exactly the fields date and name")
            continue
        day, name = item["date"], item["name"]
        if type(day) is not date:
            errors.append(f"{position}.date must be a date (YYYY-MM-DD)")
        elif day.year != year:
            errors.append(f"{position}.date {day} does not belong to {year}")
        if not isinstance(name, str) or not name.strip():
            errors.append(f"{position}.name must be a non-empty string")
        if type(day) is date and day.year == year and isinstance(name, str) and name.strip():
            holidays.append(Holiday(day, name.strip()))
    return tuple(holidays)


def _check_locality_ids(years: list[YearHolidays], errors: list[str]) -> None:
    names_by_id: dict[str, set[str]] = {}
    for year in years:
        for name in year.local:
            names_by_id.setdefault(locality_id(name), set()).add(name)
    if "" in names_by_id:
        names = ", ".join(sorted(names_by_id.pop("")))
        errors.append(f"localities {names} produce an empty identifier")
    for identifier, names in sorted(names_by_id.items()):
        if len(names) > 1:
            errors.append(
                f"localities {', '.join(sorted(names))} produce the same identifier {identifier!r}"
            )
