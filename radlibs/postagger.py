"""Function for assigning part of speech to words
"""

import pandas as pd
import feather
import os


def posTagger(wordDF):

    this_dir, this_filename = os.path.split(__file__)
    DATA_PATH = os.path.join(this_dir, "data", "pos_lexicon.feather")
    wordset = feather.read_dataframe(DATA_PATH)

    tagged_wordDF = pd.merge(wordset, wordDF, on="word", how="inner")

    return tagged_wordDF
