# AklStemmer

**A Python library for Aklanon word stemming.**

[![PyPI version](https://img.shields.io/pypi/v/aklstemmer.svg?style=flat)](https://pypi.org/project/aklstemmer/)
[![Downloads](https://pepy.tech/badge/aklstemmer)](https://pepy.tech/project/aklstemmer)
[![License](https://img.shields.io/github/license/andrianllmm/aklanon-stemmer?style=flat)](https://github.com/andrianllmm/aklanon-stemmer/blob/main/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/andrianllmm/aklanon-stemmer?style=flat)](https://github.com/andrianllmm/aklanon-stemmer/stargazers)
[![CI](https://github.com/andrianllmm/aklanon-stemmer/actions/workflows/ci.yml/badge.svg)](https://github.com/andrianllmm/aklanon-stemmer/actions/workflows/ci.yml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/andrianllmm/aklanon-stemmer/main.svg)](https://results.pre-commit.ci/latest/github/andrianllmm/aklanon-stemmer/main)

## About

AklStemmer is a library that finds the root form of
[Aklanon](https://www.ethnologue.com/language/akl) words. It works on
inflected words, even those with mixed Aklanon-English terms or those not
found in dictionaries. It removes affixes, reduces repeated syllables, and
applies transformation rules to find possible root forms. These are filtered
using a list of valid words and conditions, and the best root is then chosen
based on how much was changed during the process.

## Installation

```sh
pip install aklstemmer
```

## Usage

AklStemmer acts as a standalone library that can be imported via
`from aklstemmer import stemmer`.

### `get_stem`

Gets the root of a word. Takes a word and returns its stem as a `Stem` object
(basically a string with affixes, reduplication, transformations, etc. as
additional attributes).

```python
stem = stemmer.get_stem("nagsueat")
print(stem)
# Output: 'sueat'
```

Since `get_stem` returns a `Stem` object, the properties used in the stemming
process can be accessed as attributes.

```python
prefix = stem.pre
print(prefix)
# Output: 'nag'

suffix = stem.suf
print(suffix)
# Output: None
```

### `get_stems`

Gets the root of each word in a text. Takes a text and returns the stem of
each word as a list of `Stem` objects.

```python
stems = stemmer.get_stems("nagsueat, binasa, ag gision")
print(stems)
# Output: ['sueat', 'basa', 'at', 'gisi']
```

### `get_stem_candidates`

Gets all the stem candidates of a word. Takes a word and returns the possible
stems as a list of `Stem` objects. This is helpful for loose checking,
considering candidate selection is not perfect.

```python
candidates = stemmer.get_stem_candidates("bukot")
print(candidates)
# Output: ['bukot', 'buko', 'bukon']
```

## Accuracy

The accuracy hasn't been tested yet.

## Development

This project uses [uv](https://docs.astral.sh/uv/) for dependency management.

Clone the repo and sync dependencies (including dev and test groups):

```sh
git clone https://github.com/andrianllmm/aklanon-stemmer.git
cd aklanon-stemmer
uv sync --all-groups
```

Run the tests:

```sh
uv run pytest
```

## Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

## License

Distributed under the [MIT License](LICENSE).
