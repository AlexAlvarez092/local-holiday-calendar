# ADR 0003: Static HTML generated with Jinja2

- **Status:** Accepted
- **Date:** 2026-11-18

## Context

The website shows the locality list ([FR-001](../requirements/functional/fr-001-locality-list.md)) with a subscribe button per locality ([FR-002](../requirements/functional/fr-002-subscribe-button.md)), in Spanish ([NFR-002](../requirements/non-functional/nfr-002-spanish-language.md)), served as static content ([CON-001](../requirements/constraints/con-001-github-pages-hosting.md)).

## Decision

The Python generator ([ADR 0002](0002-python-generator.md)) renders a single static HTML page with CSS from a Jinja2 template. The page uses no JavaScript.

## Alternatives considered

- **Fixed HTML that loads a generated JSON with JavaScript:** adds a runtime dependency on JavaScript and splits the page into two artefacts for no benefit.
- **Static site generator (MkDocs, Pelican):** more tooling than a single page needs.

## Consequences

- The page works without JavaScript and loads fast.
- Any change to the list requires regenerating the page, which the workflow does on every data change.
