"""Function for assigning part of speech to words
"""

import pandas as pd
import feather

def posTagger(wordDF):
    path = 'pos_lexicon.feather'
    wordset = feather.read_dataframe(path)

    tagged_wordDF = pd.merge(wordset, wordDF, on='word', how = 'inner')

    return(tagged_wordDF)