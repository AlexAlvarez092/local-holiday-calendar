# NFR-001: Calendar compatibility

- **Category:** Compatibility
- **Priority:** Must
- **Status:** Implemented

Generated calendars follow the iCalendar standard (RFC 5545). The supported calendar applications are Apple Calendar (macOS and iOS) and Google Calendar.

## Acceptance criteria

- Given a generated calendar, When it is parsed by the automated tests ([ADR 0007](../../adr/0007-python-tooling-and-checks.md)), Then no errors are reported.
- Given a subscription URL, When it is added to Apple Calendar, Then the subscription succeeds and the holidays are shown.
- Given a subscription URL, When it is added by hand to Google Calendar ("From URL"), Then the subscription succeeds and the holidays are shown.
