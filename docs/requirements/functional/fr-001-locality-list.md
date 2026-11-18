# FR-001: Locality list

- **Priority:** Must
- **Status:** Accepted

The website shows a list with every locality present in the holiday data ([CON-002](../constraints/con-002-manual-holiday-data.md)). The initial data contains Oviedo, Gijón, Avilés, Llanera, Siero and Lugones.

## Acceptance criteria

- Given a visitor opens the website, When the page loads, Then every locality present in the holiday data is shown.
- Given a locality is added to the holiday data, When the website is published again ([FR-005](fr-005-automatic-publication.md)), Then the list shows that locality.
- Given a locality is removed from the holiday data, When the website is published again, Then the list no longer shows that locality and its calendar is no longer published.
