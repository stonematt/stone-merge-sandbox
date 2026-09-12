# Installation

## Requirements

`unitconv` needs Python 3.9 or newer and nothing else — the converter is pure
standard library, so there are no runtime dependencies to resolve. Installing
puts a single `unitconv` command on your `PATH`; the package itself lives under
`src/unitconv`.

## Installing from a checkout

There is no published package yet, so install from a clone of the repository.
An editable install (`-e`) is the usual choice: the command points back at the
working tree, so edits to the source take effect without reinstalling.

```bash
git clone https://github.com/stonematt/stone-merge-sandbox.git
cd stone-merge-sandbox
pip install -e .
```

To confirm the install worked, run a conversion whose answer you already know:

```bash
unitconv 1 km m
```

```
1.0 km = 1000.0 m
```

If that prints, the entry point is wired up correctly. If the shell reports
`command not found` instead, the script directory for the Python you installed
into is not on your `PATH` — `python -m unitconv.cli 1 km m` invokes the same
code and is a useful way to tell the two failures apart.

## Installing for development

Running the test suite needs `pytest` in addition to the package itself:

```bash
pip install -e . pytest
pytest
```

Working inside a virtual environment keeps the editable install and `pytest`
out of your system Python:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e . pytest
```

Once installed, see [`usage.md`](usage.md) for the command's arguments and
worked conversion examples.
