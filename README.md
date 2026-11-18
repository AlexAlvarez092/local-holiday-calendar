# Local holiday calendar

Website to subscribe, with one click, to a calendar with all the public holidays of a locality of Asturias.

| Location | Content |
|----------|---------|
| [docs/requirements/](docs/requirements/README.md) | Requirements: goal, scope, users and glossary |
| [docs/requirements/functional/](docs/requirements/functional/) | Functional requirements (`FR-xxx`) |
| [docs/requirements/non-functional/](docs/requirements/non-functional/) | Non-functional requirements (`NFR-xxx`) |
| [docs/requirements/constraints/](docs/requirements/constraints/) | Constraints (`CON-xxx`) |
| [docs/adr/](docs/adr/README.md) | Architecture decision records |
| [data/](data/README.md) | Holiday data and how to update it |

## Development

Requires [uv](https://docs.astral.sh/uv/). Tooling and checks are described in [ADR 0007](docs/adr/0007-python-tooling-and-checks.md).

```sh
uv run pytest                          # run the tests
uv run holiday-calendar data _site     # generate the website and calendars into _site/
```
