from datetime import date

import pytest

from holiday_calendar.domain import Holiday, Locality, YearHolidays, calendar_events, localities, locality_id


@pytest.mark.parametrize(
    ("name", "expected"),
    [("Gijón", "gijon"), ("Avilés", "aviles"), ("San Martín del Rey Aurelio", "san-martin-del-rey-aurelio"), (" Llanes (Este) ", "llanes-este")],
)
def test_locality_id(name, expected):
    assert locality_id(name) == expected


YEAR_2026 = YearHolidays(
    2026,
    national=(Holiday(date(2026, 1, 1), "Año Nuevo"),),
    regional=(Holiday(date(2026, 9, 8), "Día de Asturias"),),
    local={
        "Gijón": (Holiday(date(2026, 9, 8), "Fiesta local"),),
        "Oviedo": (Holiday(date(2026, 9, 21), "San Mateo"),),
    },
)
YEAR_2027 = YearHolidays(2027, national=(Holiday(date(2027, 1, 1), "Año Nuevo"),), regional=(), local={"Oviedo": ()})


def test_localities_are_sorted_by_id_across_years():
    assert [locality.name for locality in localities([YEAR_2026, YEAR_2027])] == ["Gijón", "Oviedo"]


def test_calendar_events_merge_same_date_in_national_regional_local_order():
    events = calendar_events(Locality("Gijón"), [YEAR_2026])

    assert events == [
        Holiday(date(2026, 1, 1), "Año Nuevo"),
        Holiday(date(2026, 9, 8), "Día de Asturias y Fiesta local"),
    ]


def test_calendar_events_cover_all_years_and_exclude_other_localities():
    events = calendar_events(Locality("Gijón"), [YEAR_2026, YEAR_2027])

    assert Holiday(date(2026, 9, 21), "San Mateo") not in events
    assert Holiday(date(2027, 1, 1), "Año Nuevo") in events
