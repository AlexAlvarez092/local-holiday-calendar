# ADR 0004: Deploy with a GitHub Actions Pages artifact

- **Status:** Accepted
- **Date:** 2026-11-18

## Context

When holiday data changes on the main branch, the result must be published automatically, and the maintainer must be able to publish manually ([FR-005](../requirements/functional/fr-005-automatic-publication.md)), on GitHub Pages ([CON-001](../requirements/constraints/con-001-github-pages-hosting.md)).

## Decision

A GitHub Actions workflow runs the generator ([ADR 0002](0002-python-generator.md)) and publishes its output folder with `actions/upload-pages-artifact` and `actions/deploy-pages`. It is triggered by pushes to the main branch that change any `data/*.yaml` file, and manually with `workflow_dispatch`. Generated files are not committed.

## Alternatives considered

- **Commit generated files to a `gh-pages` branch:** pollutes history with generated content and needs write access to the repository.
- **Commit generated files to a folder of the main branch:** mixes sources and generated output and creates extra commits on every change.
- **Also trigger on changes to the generator code:** not needed; code fixes are published with a manual run.

## Consequences

- The repository contains only sources; the published site always matches the last successful run.
- GitHub Pages must be configured to use GitHub Actions as its source.
