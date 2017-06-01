from nltk import *

# from nltk.corpus import wordnet as w
#
# print(w.synsets('school')[0].hyponyms())

# str = 'pp'
# x = ['a', 'b', 'c']
#
# j = 0
# if x[j] in str:
#     print(True)
# else:
#     print(False)

print(pos_tag(word_tokenize("Each reviewer's first name, last name, phone number, affiliation, and topics of interest are also recorded.")))