# Radlibs for Python


Welcome! This is a small, fun package. Remember MadLibs from childhood roadtrips? This is something of 
a parody of that, updated a bit. [There is also an R version of this package: https://skirmer.github.io/radlibs/.](https://skirmer.github.io/radlibs/)

To get started immediately, you can use the base function: `radlibs.makeRadlibs()`. Just pass a string that
includes any number of the following words, and it will fill in something (hopefully) funny!

* noun
* plural
* verb
* adjective
* adverb
* interjection
* celebrity
* place

And I hope to add support for more in the future. If you would like to generate RadLibs for your 
own use case, using your own sample of words (joke for family, for example), you can pass in your own
pandas dataframe containing, at minimum, a `word` column and a `pos` column indicating its part of speech. 
The contents of both columns need to be all lowercase.

## I need parts of speech help

If you don't know the parts of speech for a dataset you want to use, I am also including a 
function that can assign these for you. While it is not hugely comprehensive, `radlibs.posTagger()` will match your dataset to slightly more than 250,000 words already tagged with part of speech. 

Happy RadLibbing!

## Installation

This package is not currently available on PyPi, I'm working on it. To install from source, clone this repo, then type 

```
cd radlibs-py
pip install .
``` 

from the command line inside the `radlibs-py` folder. You could also run `make install` if you like.

## Credits

My thanks to https://github.com/tomasengelthaler/HumorNorms for the default dataset of words with 
humor ratings. Thanks to https://www.kaggle.com/vered1986/propernames-categories/version/1 for 
the list of proper nouns I started with.


