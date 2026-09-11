# Changelog conventions

`CHANGELOG.md` is the human-readable record of what changed between
releases. This page covers what belongs in it and how entries are worded.
For the release-time mechanics — retitling `## Unreleased`, bumping the
version, tagging — see [`release-process.md`](release-process.md).

## What gets an entry

Anything a user of `unitconv` would notice: a new supported unit, a change
to output formatting, a new or renamed CLI argument, a fixed conversion
factor. If someone could run the command before and after and see a
difference, it belongs in the changelog.

Changes that leave behaviour untouched do not get an entry — test-only
commits, refactors, CI configuration, and documentation. These are still
worth committing with a clear message; the commit history is the record for
them, not the changelog.

## Writing an entry

Entries are single-line bullets under the current `## Unreleased` heading.
Start with a verb in the imperative — Add, Fix, Change, Remove — and name
the user-facing thing, with unit names in backticks. One entry per change,
even when several land in the same pull request.

The commit subject is usually most of the way there. Dropping the
Conventional Commits prefix and writing the unit as it appears on the
command line is the whole transformation:

```
feat(core): add ri to supported length units
```

becomes:

```markdown
## Unreleased

- Add `ri` to the supported length units.
```

Avoid pointing at internals. "Add `ri` to the length factor table" names a
module detail that readers of the changelog do not have, whereas the
supported-units phrasing describes what they can now type.

## Ordering and grouping

Within a section, keep entries in the order they landed — append to the
bottom rather than sorting or reordering. The list stays short enough
between releases that grouping by category is not worth the overhead; if a
release ever grows large enough to need `### Added` and `### Fixed`
subheadings, introduce them at release time rather than maintaining them in
`## Unreleased`.
