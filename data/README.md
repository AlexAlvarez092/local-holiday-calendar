# Holiday data

This folder holds the holiday data from which the calendars and the website are generated. The file naming, structure and validation rules are defined in [ADR 0001](../docs/adr/0001-yaml-holiday-data-per-year.md).

## Updating the holidays

1. **Get the official holidays** of the year from the official bulletins: national holidays from the BOE, and regional and local holidays of Asturias from the BOPA.
2. **Create a branch** from `main`, following [CONTRIBUTING.md](../CONTRIBUTING.md):

   ```sh
   git switch main
   git pull
   git switch -c chore/update-holidays-2027
   ```

3. **Edit the data** in this folder:
   - **New year:** create `<year>.yaml` (for example `2027.yaml`) only when the national, regional and local holidays of every locality have been published, so no calendar is published with an incomplete year.
   - **Correct a year:** edit its existing `<year>.yaml`.
   - **Add or remove a locality:** add or remove its entry under `local` in the files of the affected years.
   - **Remove a past year:** delete its `<year>.yaml`. Keep the current year and, once complete, the next one.
4. **Check the data locally** with `uv run pytest` ([ADR 0007](../docs/adr/0007-python-tooling-and-checks.md)).
5. **Commit and push** the branch:

   ```sh
   git add data/
   git commit -m "chore: add 2027 holidays"
   git push -u origin chore/update-holidays-2027
   ```

6. **Open a pull request** to `main` using the template, for example with `gh pr create --base main --fill`. Wait for its checks to pass and get it reviewed.
7. **Merge the pull request.** This runs the publication workflow ([ADR 0004](../docs/adr/0004-deploy-with-github-actions-pages-artifact.md)).
8. **Check the result** in the repository's **Actions** tab, or with `gh run watch`.

## If the workflow fails

The previous website and calendars stay online ([FR-005](../docs/requirements/functional/fr-005-automatic-publication.md)). Open the failed run in the **Actions** tab and read the reported error:

- **Invalid data:** fix it in a new pull request and merge it.
- **Temporary failure** (for example a GitHub outage): select **Re-run jobs** on the failed run, or start the workflow manually with **Run workflow**.
