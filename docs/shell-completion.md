# Shell completion

`unitconv` does not ship completion scripts, and it has no `--completion`
flag to generate them. It is a stdlib `argparse` program with no
dependencies, so there is nothing to enable — but the unit tables are a good
fit for completion, and you can wire it up yourself in a few lines. This page
gives a working bash and zsh function for that.

## Why bother

The three positional arguments are a value, a unit to convert from, and a
unit to convert to (see [`usage.md`](usage.md)). The common pairs are easy to
type from memory, but the tables also carry historical and scientific units
whose abbreviations are not guessable — `rop`, `xu`, `ri`, `prc` for length,
`mna`, `pcl`, `scwt` for mass. See
[`history-of-units.md`](history-of-units.md) for what those are.

The bigger win is the third argument. Mixing categories is an error, so this
fails:

```bash
unitconv 2 ft kg
```

```
error: cannot convert 'ft' to 'kg'
```

Completion can rule that out before you press enter: once the from-unit is
`ft`, the only useful candidates for the to-unit are the other length units.
Both functions below do that — after `unitconv 2 lb ` they offer the twelve
mass units and nothing else, so the conversion you tab your way into always
runs:

```bash
unitconv 1 scwt lb
```

```
1.0 scwt = 100.0 lb
```

This works because no abbreviation appears in more than one table, which
means the from-unit alone is enough to pick the candidate list. Temperature
units are matched case-insensitively by the CLI, but the length and mass
lookups are case-sensitive — the functions below offer the canonical
spellings, so `Gm` completes correctly.

## bash

Save this as `~/.local/share/bash-completion/completions/unitconv`, or source
it from your `~/.bashrc`:

```bash
_unitconv() {
    local length="mm cm m km in ft yd mi rop nm pc xu ri mil rd Gm ch prc"
    local mass="mg dg g kg dr oz ozt lb st mna pcl scwt"
    local temp="c f k"
    local cur=${COMP_WORDS[COMP_CWORD]}
    local pool

    case $COMP_CWORD in
        2) pool="$length $mass $temp" ;;
        3)
            case " $length " in *" ${COMP_WORDS[2]} "*) pool=$length ;; esac
            case " $mass " in *" ${COMP_WORDS[2]} "*) pool=$mass ;; esac
            case " $temp " in *" ${COMP_WORDS[2]} "*) pool=$temp ;; esac
            ;;
        *) return ;;
    esac

    COMPREPLY=($(compgen -W "$pool" -- "$cur"))
}
complete -F _unitconv unitconv
```

The first argument is a number, so nothing is offered for it. If the
from-unit is not a known unit, `pool` stays empty and you get no suggestions
rather than a misleading list.

## zsh

Save this as `_unitconv` in a directory on your `fpath` — `~/.zfunc` is a
common choice, added with `fpath=(~/.zfunc $fpath)` before `compinit` runs in
your `~/.zshrc`:

```zsh
#compdef unitconv

_unitconv() {
    local -a length mass temp
    length=(mm cm m km in ft yd mi rop nm pc xu ri mil rd Gm ch prc)
    mass=(mg dg g kg dr oz ozt lb st mna pcl scwt)
    temp=(c f k)

    case $CURRENT in
        2) _message 'numeric value' ;;
        3) compadd -a length mass temp ;;
        4)
            local from=$words[3]
            if (( $length[(I)$from] )); then
                compadd -a length
            elif (( $mass[(I)$from] )); then
                compadd -a mass
            elif (( $temp[(I)$from] )); then
                compadd -a temp
            fi
            ;;
    esac
}

_unitconv "$@"
```

`$words` and `$CURRENT` are 1-indexed and include the command itself, which
is why the unit positions are 3 and 4 here but 2 and 3 in the bash version.
`$length[(I)$from]` returns the index of `$from` in the array, or 0 if it is
absent, so it doubles as the membership test.

Both functions hardcode the unit lists, so they will drift if units are added
to the tables. `unitconv` has no `--list-units` flag to generate them from,
so re-check them against `src/unitconv/convert.py` if a conversion you expect
is missing from the suggestions.
