# ADR 0006: iCalendar generation

- **Status:** Accepted
- **Date:** 2026-11-19

## Context

Calendars must contain all-day events ([FR-003](../requirements/functional/fr-003-calendar-content.md)), reflect changes in subscribed applications within one day ([FR-002](../requirements/functional/fr-002-subscribe-button.md)) and follow RFC 5545 ([NFR-001](../requirements/non-functional/nfr-001-calendar-compatibility.md)).

## Decision

The generator writes the `.ics` files with the `icalendar` Python library:

- **Events:** `DTSTART` as a date (`VALUE=DATE`) and `DTEND` as the following date, so events are all-day and independent of time zones.
- **UID:** `<date>-<id>@alexalvarez092.github.io`, where `<id>` is the locality identifier ([ADR 0005](0005-webcal-subscription-url.md)), for example `2026-09-21-oviedo@alexalvarez092.github.io`.
- **Calendar name:** `X-WR-CALNAME` and `NAME` set to the name required by FR-003.
- **Refresh hint:** `REFRESH-INTERVAL;VALUE=DURATION:P1D` and `X-PUBLISHED-TTL:P1D`.

## Alternatives considered

- **UID including the holiday name:** the date and locality already identify the single event per date.
- **Explicit UID in the data:** more to write by hand for no benefit.
- **Writing the iCalendar text by hand:** error-prone escaping and line folding.

## Consequences

- Regenerating the calendars keeps the same UIDs, so applications do not duplicate events.
- Correcting a holiday's date changes its UID; the old event is removed and a new one added.
- Refresh hints are suggestions; Google Calendar uses its own interval, which can exceed one day.
