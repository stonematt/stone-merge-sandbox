# Contributing

Changes to `unitconv` arrive the same way whether they add a unit, fix a
factor, or only touch documentation: a branch cut from `dev`, a pull request
back into `dev`, and three green checks. The branch names, the check names,
and how `dev` eventually reaches `main` are covered in
[`release-process.md`](release-process.md); this page is about what to do
before the pull request is open.

Most contributions are a new entry in one of the factor tables, which means
a factor, a test, and — if the change is user-facing — a changelog bullet.
Anchor the factor to the category's base unit rather than to a neighbouring
unit, for the reason described in
[`why-a-base-unit.md`](why-a-base-unit.md), and give the source for the
number in the commit message if it is not a defined exact value. Temperature
is the exception: those conversions do not go through a base unit at all, so
adding a scale means adding conversion functions rather than a table row —
see [`temperature-scales.md`](temperature-scales.md).

Before opening the pull request:

- Run the test suite and add a case covering the unit or behaviour you
  changed.
- Add a `CHANGELOG.md` bullet under `## Unreleased` if a user could see the
  difference, following
  [`changelog-conventions.md`](changelog-conventions.md).
- Update the affected docs page — a new unit belongs in the supported-unit
  list a reader would check first.
- Keep the change to one category, since a pull request that touches both
  the length and mass tables is two reviews in one.
- Check that what you are adding is not deliberately absent; the omissions
  are listed in [`limitations.md`](limitations.md).
