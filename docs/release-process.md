# Release process

`unitconv` uses two long-lived branches. `dev` is the integration branch and
the repository default; `main` is the release branch. Work lands on `dev`
first and reaches `main` only as part of a release.

## Branches and pull requests

Feature and fix branches are cut from `dev`, named `feat/*` or `fix/*` (or
`docs/*`, `chore/*` for non-code work), and opened as pull requests back into
`dev`. Nothing is pushed directly to `main`.

Every pull request runs three checks — `test`, `code-review`, and `flaky` —
which also run on pushes to `dev` and `main`. All three must pass before a
merge. `flaky` is deliberately unreliable on some branches; if it is the only
failure, re-run the job rather than changing code.

## Cutting a release

A release is a pull request from `dev` into `main`. The steps:

1. Confirm `dev` is green and holds everything intended for the release.
2. Bump `version` in `pyproject.toml`.
3. In `CHANGELOG.md`, rename the `## Unreleased` heading to the new version
   with its date, and open a fresh empty `## Unreleased` section above it.
4. Commit both files to `dev`.
5. Open a pull request from `dev` into `main`, wait for checks, and merge.
6. Tag the merge commit on `main` with the version and push the tag.

### Worked example: 0.1.0 to 0.2.0

`pyproject.toml` changes on one line:

```toml
version = "0.2.0"
```

`CHANGELOG.md` gains a new empty section and retitles the old one:

```markdown
## Unreleased

## 0.2.0 - 2026-09-11

- Add `rop` to the length table.
- Add troy ounce to the supported mass units.
```

Then commit, promote, and tag:

```bash
git switch dev
git commit -am "chore(release): 0.2.0"
git push
gh pr create --base main --head dev --title "Release 0.2.0"
# after checks pass and the PR is merged
git switch main && git pull
git tag v0.2.0 && git push origin v0.2.0
```

## After the release

Pull `main` and `dev` locally so both are current, and delete the merged
feature branches that went into the release. The version in `pyproject.toml`
is not bumped again until the next release is cut, so `dev` carries the
released version number plus an accumulating `## Unreleased` section between
releases.
