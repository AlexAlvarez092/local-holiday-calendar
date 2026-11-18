# Overview

## Goal

Provide a website where people can subscribe, with one click, to a calendar containing every public holiday that applies to a given locality of Asturias.

## Current situation

Public holidays are published every year in official bulletins: national holidays in the BOE and regional and local holidays of Asturias in the BOPA. People have to look them up and add them to their calendar application by hand.

## Scope

**In scope**

- Every active (not Dropped) requirement in [functional/](functional/).

**Out of scope**

- Localities outside Asturias.
- Automatic retrieval of holiday data from official sources or APIs.

## Users

| Role | Description |
|------|-------------|
| Visitor | Anyone who wants the public holidays of a locality in their own calendar application. |
| Maintainer | Person who keeps the holiday data up to date in the repository. |

## Glossary

| Term | Definition |
|------|------------|
| Locality | Municipality (concejo) of Asturias listed on the website. |
| National holiday | Public holiday that applies to all of Spain. |
| Regional holiday | Public holiday that applies to the whole Principality of Asturias. |
| Local holiday | Public holiday that applies only to one locality. |
| Applicable holidays | National, regional and local holidays that apply to a given locality. |
| Subscription URL | Public URL of an iCalendar (`.ics`) feed that calendar applications can subscribe to and refresh periodically. |
