"""Function for creating a madlib
"""

import pandas as pd
import feather
import random
import re
from radlibs.generatewordopts import _generateWordOptions
from radlibs.postagger import posTagger

def makeRadlibs(phrase, wordset = 'NA'):

    word_types = _generateWordOptions()

    if (wordset == 'NA'):
        path = 'humor_dataset.feather'
        wordset = feather.read_dataframe(path)
        wordset = wordset[wordset['mean'] > 1.2]

        wordset = posTagger(wordset)
        wordset['pos'] = wordset['pos'].str.lower()

        path = 'proper_nouns.feather'
        propernouns = feather.read_dataframe(path)

        propernouns.columns = ['word', 'pos']
        wordset = pd.concat([wordset, propernouns], sort=False)

    for key in word_types:
        #wordtype = word_types[key]['wordtype']
        regex = re.compile(word_types[key]['regex'])
        descriptors = word_types[key]['descriptors']

        word_types[key]['count'] = len(regex.findall(phrase))

        word_types[key]['sample'] = random.sample(
            wordset[wordset['pos'].isin(descriptors)]['word'],
            word_types[key]['count']
        )

    new_phrase = phrase

    for key in word_types:
        count = word_types[key]['count']
        sample = word_types[key]['sample']
        regex = re.compile(word_types[key]['regex'])

        if (count > 0):
            for word in sample:
                new_phrase.replace(regex, word, 1) 
        else:
            next
    

    return(new_phrase)