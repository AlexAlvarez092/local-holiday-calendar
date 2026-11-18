# ADR 0001: YAML holiday data, one file per year

- **Status:** Accepted
- **Date:** 2026-11-18

## Context

Holiday data is maintained by hand in the repository ([CON-002](../requirements/constraints/con-002-manual-holiday-data.md)) and drives the locality list ([FR-001](../requirements/functional/fr-001-locality-list.md)), the calendar content ([FR-003](../requirements/functional/fr-003-calendar-content.md)) and the years covered ([FR-004](../requirements/functional/fr-004-year-coverage.md)). Invalid data must stop publication ([FR-005](../requirements/functional/fr-005-automatic-publication.md)).

## Decision

Holiday data is stored as YAML in the `data/` folder, one file per year named `<year>.yaml` (for example `data/2026.yaml`). Each file has this structure:

```yaml
national:
  - date: 2026-01-01
    name: Año Nuevo
regional:
  - date: 2026-09-08
    name: Día de Asturias
local:
  Oviedo:
    - date: 2026-09-21
      name: San Mateo
```

National and regional holidays are written once per year; local holidays are grouped by locality. The localities of a year are the keys under `local`.

The data is invalid, and the generator fails, when any of these happens:

- A YAML file in `data/` is not named `<year>.yaml` with a four-digit year, is not well-formed YAML, or contains duplicate keys.
- The top-level keys are not exactly `national`, `regional` and `local`.
- `national` or `regional` is not a non-empty list, `local` is not a non-empty mapping, or a locality's list is empty.
- A holiday does not have exactly the fields `date` (a valid date) and `name` (a non-empty string).
- A date does not belong to the year in the file name.
- Two different locality names, in any of the files, produce the same identifier ([ADR 0005](0005-webcal-subscription-url.md)).

A `data/` folder without year files is valid and produces an empty list.

## Alternatives considered

- **Single YAML file for all years:** adding and removing years means editing a growing file instead of adding or deleting one.
- **JSON:** harder to edit by hand and does not allow comments.
- **CSV:** repeats national and regional holidays for every locality, or needs extra columns to express their scope.

## Consequences

- Adding a year is adding a file; removing a past year is deleting one.
- A locality missing from `local` in a year has no local holidays that year.
- The generator cannot tell an incomplete year from a complete one; completeness is ensured by the maintainer's procedure ([data/README.md](../../data/README.md)).
