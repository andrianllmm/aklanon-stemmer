# AklStemmer

**A Python library for Aklanon word stemming.**


## About

[aklstemmer](src/aklstemmer/) reduces all forms of Aklanon-inflected words, which can include out-of-vocabulary (OOV) words and Aklanon-English intrawords, to their base or root. It uses iterative and combinative affix removal, reduplication reduction, and application of transformation rules to derive candidates or possible stems of the word. The list of candidates is filtered based on a list of valid words and acceptability conditions. The best candidate is then chosen based on affix and reduplication length and number of contraction and transformation occurrences.


## Installation

To install the latest development version from GitHub, use:

```bash
pip install git+https://github.com/andrianllmm/aklanon-stemmer.git@main
```


## Usage

aklstemmer acts as a standalone library that can be imported via `from aklstemmer import stemmer`.

To get the stem of a word use the function `get_stem()`. This takes a word and returns its stem as a `Stem` object (basically a string with affixes, reduplication, transformations, etc. as additional attributes)
```python
stem = stemmer.get_stem("nagsueat")
print(stem)
# Output: 'sueat'
```

Since `get_stem` returns a `Stem` object, the affixes, reduplication, transformations, etc. used in the stemming process can be accessed as attributes.
```python
prefix = stem.pre
print(prefix)
# Output: 'nag'

suffix = stem.suf
print(suffix)
# Output: None
```

To get the stem of each word in a text use the function `get_stems()`. This takes a text and returns the stem of each word as a list of `Stem` objects.
```python
stems = stemmer.get_stems("nagsueat, binasa, ag gision")
print(stems)
# Output: ['sueat', 'basa', 'at', 'gisi']
```

To get all the stem candidates of a word use the function `get_stem_candidates`. This takes a word and returns the possible stems as a list of `Stem` objects. This is helpful for loose checking considering candidate selection is not perfect.
```python
candidates = stemmer.get_stem_candidates("bukot")
print(candidates)
# Output: ['bukot', 'buko', 'bukon']
```


## Accuracy

The accuracy of aklstemmer is yet to be tested.


## Issues

* List of valid words: The default list of valid words was manually encoded from the book [A Study of the Aklanon Dialect, Vol 2](https://files.eric.ed.gov/fulltext/ED145704.pdf) which is still not complete at the moment.
* List of affixes: The list of affixes used is supplied by common affixes and manually combining them which is unreliable it lacks a reliable source.
* Candidate selection: The process for selecting the best candidate can be further optimized to reduce stemming errors.

If you encounter any issues or bugs, please report them on the [GitHub issues page](#).


## Contributing

This project welcomes contributions and suggestions. Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.


## License

This project is licensed under the [GPL-3.0 License](LICENSE).

---

For more information contact [maagmaandrian@gmail.com](mailto:maagmaandrian@gmail.com) with any additional questions or comments.