import pytest

from conftest import VALID_YEAR, write_year
from holiday_calendar.data_loader import DataError, load_years


def test_loads_valid_year(data_dir):
    write_year(data_dir, "2026.yaml", VALID_YEAR)

    [year] = load_years(data_dir)

    assert year.year == 2026
    assert set(year.local) == {"Gijón", "Oviedo"}


def test_no_year_files_is_valid(data_dir):
    (data_dir / "README.md").write_text("# Holiday data", encoding="utf-8")

    assert load_years(data_dir) == []


@pytest.mark.parametrize(
    ("file_name", "content", "message"),
    [
        ("holidays.yaml", VALID_YEAR, "file name must be <year>.yaml"),
        ("2026.yml", VALID_YEAR, "file name must be <year>.yaml"),
        ("2026.yaml", "national: [", "invalid YAML"),
        ("2026.yaml", VALID_YEAR + "  Oviedo:\n    - date: 2026-05-01\n      name: X\n", "duplicate key"),
        ("2026.yaml", VALID_YEAR.replace("regional:", "autonomic:"), "top-level keys"),
        ("2026.yaml", VALID_YEAR.replace("national:\n  - date: 2026-01-01\n    name: Año Nuevo", "national: []"), "national must be a non-empty list"),
        ("2026.yaml", VALID_YEAR + "  Siero: []\n", "local.Siero must be a non-empty list"),
        ("2026.yaml", VALID_YEAR.replace("name: Año Nuevo", "name: Año Nuevo\n    type: x"), "exactly the fields date and name"),
        ("2026.yaml", VALID_YEAR.replace("name: Año Nuevo", "name: ''"), "name must be a non-empty string"),
        ("2026.yaml", VALID_YEAR.replace("2026-01-01", "'2026-01-01'"), "must be a date"),
        ("2026.yaml", VALID_YEAR.replace("2026-01-01", "2026-02-30"), "invalid YAML"),
        ("2026.yaml", VALID_YEAR.replace("2026-01-01", "2025-01-01"), "does not belong to 2026"),
    ],
)
def test_rejects_invalid_data(data_dir, file_name, content, message):
    write_year(data_dir, file_name, content)

    with pytest.raises(DataError) as error:
        load_years(data_dir)

    assert any(message in reported for reported in error.value.errors)


def test_rejects_locality_names_with_same_identifier_across_files(data_dir):
    write_year(data_dir, "2026.yaml", VALID_YEAR)
    write_year(data_dir, "2027.yaml", VALID_YEAR.replace("2026", "2027").replace("Gijón", "Gijon"))

    with pytest.raises(DataError, match="same identifier 'gijon'"):
        load_years(data_dir)
