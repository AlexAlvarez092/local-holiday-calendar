# ADR 0005: webcal subscription URL

- **Status:** Accepted
- **Date:** 2026-11-18

## Context

The subscribe button must make the visitor's calendar application offer to subscribe ([FR-002](../requirements/functional/fr-002-subscribe-button.md), [NFR-001](../requirements/non-functional/nfr-001-calendar-compatibility.md)). Opening an `https://` link to an `.ics` file usually downloads it instead. Subscription URLs must stay stable, because changing them breaks existing subscriptions.

## Decision

The site is served from the default GitHub Pages address, `https://alexalvarez092.github.io/local-holiday-calendar/`. Each locality's calendar is published at `calendars/<id>.ics` under that address, where `<id>` is derived from the locality name: lowercase, accents removed, and every run of characters other than letters and digits replaced by a single hyphen, with no leading or trailing hyphen (for example `Gijón` → `gijon`).

The subscribe button links to that file using the `webcal://` scheme instead of `https://`, for example `webcal://alexalvarez092.github.io/local-holiday-calendar/calendars/gijon.ics`.

## Alternatives considered

- **Explicit identifier in the data:** more to write by hand for no benefit while names are stable.
- **INE municipality code:** stable, but unreadable in URLs.
- **Custom domain:** not needed.
- **Also show the `https://` URL for copying:** not needed for the current requirements.

## Consequences

- Apple Calendar and other applications that handle `webcal://` offer to subscribe directly; Google Calendar needs the URL added by hand.
- Removing a locality removes its file; its subscribers stop receiving updates.
- Renaming a locality changes its URL and behaves as a removal plus an addition.
- Moving to another domain or repository name breaks every existing subscription.
