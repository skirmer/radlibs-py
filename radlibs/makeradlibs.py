"""Function for creating a madlib
"""

import pandas as pd
import feather
import random
import re
import os
from radlibs.generatewordopts import _generateWordOptions
from radlibs.postagger import posTagger

def makeRadlibs(phrase, wordset = 'NA'):

    word_types = _generateWordOptions()

    if (wordset == 'NA'):
        this_dir, this_filename = os.path.split(__file__)
        DATA_PATH = os.path.join(this_dir, "data", "humor_dataset.feather")
        wordset = feather.read_dataframe(DATA_PATH)
        wordset = wordset[wordset['mean'] > 1.2]

        wordset = posTagger(wordset)
        wordset['pos'] = wordset['pos'].str.lower()

        this_dir, this_filename = os.path.split(__file__)
        DATA_PATH = os.path.join(this_dir, "data", "proper_nouns.feather")

        propernouns = feather.read_dataframe(DATA_PATH)

        propernouns.columns = ['word', 'pos']
        wordset = pd.concat([wordset, propernouns], sort=False)

    for key in word_types:
        #wordtype = word_types[key]['wordtype']
        regex = re.compile(word_types[key]['regex'])
        descriptors = word_types[key]['descriptors']

        word_types[key]['count'] = len(regex.findall(phrase))

        word_types[key]['sample'] = random.sample(
            list(wordset[wordset['pos'].isin(descriptors)]['word']),
            word_types[key]['count']
        )

    new_phrase = phrase

    for key in word_types:
        count = word_types[key]['count']
        sample = word_types[key]['sample']
        regex = re.compile(word_types[key]['regex'])

        if (count > 0):
            for word in sample:
                new_phrase = re.sub(regex, word, new_phrase, count = 1)#new_phrase.replace(regex, word, 1) 
        else:
            next
            
    return(new_phrase.capitalize())