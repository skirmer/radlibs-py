"""Function for creating reference of parts of speech
"""


def _generate_word_options():
    worddict = {}

    noun = {
        "descriptors": ["noun", "noun phrase"],
        "wordtype": "noun",
        "regex": "[nN]oun",
    }
    adverb = {"descriptors": ["adverb"], "wordtype": "adverb", "regex": "[aA]dverb"}
    plural = {"descriptors": ["plural"], "wordtype": "plural", "regex": "[pP]lural"}
    verb = {
        "descriptors": ["verb (transitive)", "verb"],
        "wordtype": "verb",
        "regex": "[vV]erb",
    }
    adjective = {
        "descriptors": ["adjective"],
        "wordtype": "adjective",
        "regex": "[aA]djective",
    }
    interjection = {
        "descriptors": ["interjection"],
        "wordtype": "interjection",
        "regex": "[iI]nterjection",
    }
    place = {
        "descriptors": ["city", "state", "country", "region", "place"],
        "wordtype": "place",
        "regex": "[pP]lace",
    }
    celebrity = {
        "descriptors": ["celebrity", "president", "hero", "character"],
        "wordtype": "celebrity",
        "regex": "[cC]elebrity",
    }

    worddict = {
        "noun": noun,
        "adverb": adverb,
        "plural": plural,
        "verb": verb,
        "adjective": adjective,
        "interjection": interjection,
        "place": place,
        "celebrity": celebrity,
    }

    return worddict
