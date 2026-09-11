# unitconv

A small command-line unit converter for length, mass, and temperature.

## Install

```bash
pip install -e .
```

## Usage

```bash
unitconv 1 km m
# 1.0 km = 1000.0 m

unitconv 100 c f
# 100.0 c = 212.0 f

unitconv 5 lb kg
# 5.0 lb = 2.267961850425 kg
```

Supported length units: `mm`, `cm`, `m`, `km`, `in`, `ft`, `yd`, `mi`.
Supported mass units: `mg`, `g`, `kg`, `oz`, `lb`.
Supported temperature units: `c`, `f`, `k`.

See [`docs/usage.md`](docs/usage.md) for more detail.

## Development

```bash
pip install -e . pytest
pytest
```

## License

MIT, see [LICENSE](LICENSE).
