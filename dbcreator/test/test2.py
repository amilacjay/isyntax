from nltk.stem import WordNetLemmatizer

wnl = WordNetLemmatizer()

# def isplural(word):
#     lemma = wnl.lemmatize(word, 'n')
#     plural = True if word is not lemma else False
#     return plural, lemma
#
# # nounls = ['geese', 'mice', 'bars', 'foos', 'foo',
# #                 'families', 'family', 'dog', 'dogs']
#
# nounls = ['employee', 'employees', 'doctor', 'doctors']
#
# for nn in nounls:
#     isp, lemma = isplural(nn)
#     print (nn, lemma, isp)


lemma = wnl.lemmatize('locations')
print(lemma)