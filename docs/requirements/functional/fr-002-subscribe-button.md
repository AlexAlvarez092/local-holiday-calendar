# FR-002: Subscribe button

- **Priority:** Must
- **Status:** Implemented

Each locality in the list ([FR-001](fr-001-locality-list.md)) has a button that opens the subscription URL of that locality's calendar, so the visitor's calendar application offers to subscribe to it.

## Acceptance criteria

- Given a visitor on a device with Apple Calendar, When they click the button of a locality, Then Apple Calendar asks whether to subscribe to that locality's calendar.
- Given a visitor subscribed to a locality's calendar in Apple Calendar, When a holiday is added, corrected or removed and the calendar is published again, Then Apple Calendar shows the change within one day.
- Given a visitor subscribed to a locality's calendar in Google Calendar, When a holiday is added, corrected or removed and the calendar is published again, Then Google Calendar shows the change after its own next refresh.
