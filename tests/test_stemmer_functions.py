from aklstemmer.helpers.words import get_words

from aklstemmer import stemmer


valid_words = get_words()


def test_stem_pre():
    stems = {
        "parayaw": "dayaw",
        "pangablit": "kablit",
        "pangingisda": "isda",
        "pangangablit": "kablit",
        "pamahaw": "bahaw",
        "pamasyar": "pasyar",
        "pamamahaw": "bahaw",
        "pamamasyar": "pasyar",
        "panumdum": "dumdum",
        "panigarilyo": "sigarilyo",
        "panahi": "tahi",
        "panunumdum": "dumdum",
        "paninigarilyo": "sigarilyo",
        "pananahi": "tahi",
    }
    for s in stems:
        assert stems[s] in stemmer.get_stem_candidates(
            s, valid_words + list(stems.values())
        )


def test_stem_inf():
    stems = {
        "linahog": "eahog",
        "inabot": "abot",
        "sinueat": "sueat",
        "chineck": "check",
        "splinit": "split",
    }
    for s in stems:
        assert stems[s] in stemmer.get_stem_candidates(
            s, valid_words + list(stems.values())
        )


def test_stem_suf():
    stems = {
        "eot": "eon",
        "bayari": "bayad",
        "sugilanon": "sugid",
        "agyan": "agi",
        "tubwan": "tubo",
        "tauhan": "tao",
        "inuman": "inom",
        "kingkihan": "kingki",
        "paitin": "paet",
        "buksa": "bukas",
        "tamna": "tanom",
    }
    for s in stems:
        assert stems[s] in stemmer.get_stem_candidates(
            s, valid_words + list(stems.values())
        )


def test_stem_rep():
    stems = {
        "aabot": "abot",
        "babakae": "bakae",
        "cecheck": "check",
        "chcheck": "check",
        "checheck": "check",
        "sisplit": "split",
        "spsplit": "split",
        "spisplit": "split",
        "splsplit": "split",
        "splisplit": "split",
    }
    for s in stems:
        assert stems[s] in stemmer.get_stem_candidates(
            s, valid_words + list(stems.values())
        )


def test_stem_dup():
    stems = {
        "ano-ano": "ano",
        "panga-pangako": "pangako",
        "anu-ano": "ano",
        "iba't-iba": "iba",
        "tawung-tawo": "tawo",
        "ating-atin": "atin",
        "hapung-hapon": "hapon",
        "ibat-iba": "iba",
        "libut-libo": "libo",
    }
    for s in stems:
        assert stems[s] in stemmer.get_stem_candidates(
            s, valid_words + list(stems.values())
        )
