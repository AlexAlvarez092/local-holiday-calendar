# ADR 0007: Python tooling and checks

- **Status:** Accepted
- **Date:** 2026-11-19

## Context

The generator is written in Python ([ADR 0002](0002-python-generator.md)) and must reject invalid data ([ADR 0001](0001-yaml-holiday-data-per-year.md)) and produce valid calendars ([NFR-001](../requirements/non-functional/nfr-001-calendar-compatibility.md)). Contributors and the workflows need the same reproducible environment.

## Decision

- **Runtime and dependencies:** Python 3.13, managed with `uv` through `pyproject.toml` and a committed `uv.lock`.
- **Tests:** written with `pytest` and run with `uv run pytest`. They cover data validation and parse the generated `.ics` files with the `icalendar` library to check their content.
- **Pull request checks:** a GitHub Actions workflow runs the tests and validates the data in `data/` on every pull request to the main branch. The publication workflow ([ADR 0004](0004-deploy-with-github-actions-pages-artifact.md)) runs them too before deploying.

## Alternatives considered

- **pip with `requirements.txt`:** no lock file for transitive dependencies.
- **Poetry:** slower and heavier than `uv` for the same result.
- **unittest:** more verbose than `pytest`.
- **Online iCalendar validator checked by hand:** not repeatable.

## Consequences

- Invalid data and broken calendars are detected before merging.
- Contributors need `uv` installed.
