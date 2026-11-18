# ADR 0002: Python generator

- **Status:** Accepted
- **Date:** 2026-11-18

## Context

A workflow must turn the holiday data ([ADR 0001](0001-yaml-holiday-data-per-year.md)) into calendars and a website ([FR-005](../requirements/functional/fr-005-automatic-publication.md)).

## Decision

The generator is written in Python. It reads the data, validates it, and writes the calendars and the website into an output folder.

## Alternatives considered

- **TypeScript or JavaScript (Node.js):** viable, but not preferred by the maintainer.
- **Go:** compiled binary is unnecessary for a small build-time script.

## Consequences

- Mature libraries exist for YAML, iCalendar and HTML templating.
- The workflow needs a Python runtime and the project's dependencies.
