#!/usr/bin/python
from nltk.stem.porter import *
stemmer = PorterStemmer()


print(stemmer.stem(input('Enter a string:')))
