# FR-003: Calendar content

- **Priority:** Must
- **Status:** Accepted

The project generates one calendar per locality, named "Festivos de <locality>", containing all its applicable holidays (national, regional and local), each as an all-day event. When several applicable holidays fall on the same date, they form a single event whose name joins their names with " y ", in the order national, regional, local.

## Acceptance criteria

- Given the holiday data of a year, When the calendar of a locality is generated, Then it contains every national, regional and local holiday of that locality for that year, and no local holiday of another locality.
- Given a holiday in the calendar, When it is shown in a calendar application, Then it appears as an all-day event on the correct date.
- Given a regional holiday "Día de Asturias" and a local holiday "San Mateo" on the same date for a locality, When its calendar is generated, Then it contains a single event "Día de Asturias y San Mateo" on that date.
- Given a subscription to the calendar of Gijón, When it is added, Then the calendar is named "Festivos de Gijón".
