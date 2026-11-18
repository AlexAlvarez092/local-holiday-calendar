# FR-005: Automatic publication

- **Priority:** Must
- **Status:** Implemented

When changes to the holiday data are pushed to the main branch, a workflow processes the data, generates the calendars ([FR-003](fr-003-calendar-content.md)), updates the locality list ([FR-001](fr-001-locality-list.md)) and publishes the result. The maintainer can also start the workflow manually.

## Acceptance criteria

- Given the maintainer pushes a change to the holiday data to the main branch, When the workflow finishes, Then the published website and calendars reflect the change without any other manual step.
- Given a push to the main branch that does not change the holiday data, When it is pushed, Then the workflow does not run.
- Given the maintainer starts the workflow manually, When it finishes, Then the website and calendars are published from the current data and code of the main branch.
- Given the holiday data is invalid ([ADR 0001](../../adr/0001-yaml-holiday-data-per-year.md)), When the workflow runs, Then it fails, reports the error and leaves the published website and calendars unchanged.
