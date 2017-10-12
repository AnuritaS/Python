#!/usr/bin/python
'''Get a string from the user. Preprocess the string obtained using Porter Stemming algorithm'''

from nltk.stem.porter import *
stemmer = PorterStemmer()
print(stemmer.stem(input('Enter a string:')))
