from pathlib import Path

import pytest

VALID_YEAR = """\
national:
  - date: 2026-01-01
    name: Año Nuevo
regional:
  - date: 2026-09-08
    name: Día de Asturias
local:
  Gijón:
    - date: 2026-09-08
      name: Fiesta local
  Oviedo:
    - date: 2026-09-21
      name: San Mateo
"""


@pytest.fixture
def data_dir(tmp_path: Path) -> Path:
    directory = tmp_path / "data"
    directory.mkdir()
    return directory


def write_year(data_dir: Path, file_name: str, content: str) -> None:
    (data_dir / file_name).write_text(content, encoding="utf-8")
