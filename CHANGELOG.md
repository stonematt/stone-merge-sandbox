# Changelog

All notable changes to this project will be documented in this file.

## Unreleased

- Initial release of length, mass, and temperature conversion.
- Smoke test note: automerge-a (2026-09-11T07:33).
- Smoke test note: automerge-b (2026-09-11T07:34).
- Smoke test note: automerge-c (2026-09-11T07:34).
- Add `bc` to the supported length units.
- Add `au` to the supported length units.
- Add `Tm` to the supported length units.
- Add `dam` to the supported length units.
- Add `pol` to the supported length units.
- Add `szh` to the supported length units.
- Add `vst` to the supported length units.
- Add `fur` to the supported length units.
- Add `plm` to the supported length units.
- Add `hh` to the supported length units.
- Add `cbl` to the supported length units.
- Add `hnk` to the supported length units.
- Add `lmin` to the supported length units.
- Add `eld` to the supported length units.
- Add `agt` to the supported length units.
- Add `lgu` to the supported length units.
- Add a design notes page covering the library and CLI layers, how a
  conversion category is chosen, and why results are plain floats.
- Add a rounding behaviour page covering full-precision output, trailing-digit
  artifacts, and how to round at the point of use.
- Add a CLI exit codes page covering the three codes, which stream carries the
  message, and why a capitalised unit exits `1`.
- Add a Python API examples page covering the imports, chaining temperature
  through Celsius, handling an unknown unit, and why unit case matters.
