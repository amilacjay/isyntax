from nltk import *

#
# text = 'Employee assign to project. Project managed by manager.'

# text = "The company is organized into departments. Each department has a unique name, a unique number, and a particular employee who manages the department. We keep track of the start date when that employee began managing  the department.A department may have several locations.A department controls a number of projects, each of which has a unique name, a unique number, and a single location.We store each employee's name, Social Security Number, address, salary, sex, and Birth Date."

text = 'Each pharmacy selling drugs and has a price for each.'

wt = word_tokenize(text)
pt = pos_tag(wt)

print(pt)

# primary data sets
# tagged_sentences = getTaggedSentences(text)
# # chunked_sents = getChunkedSentences(tagged_sentences)
#
#
# print(tagged_sentences)
# # print(chunked_sents)

# x = [1, 2, 3, 4, 5]
# y = ['red', 'blue', 'green', 'yellow', 'white']
#
# myDict = {}

# my_dict = {'name':'Jack', 'age': 26}
#
# # Output: Jack
# print(my_dict['name'])
#
# # Output: 26
# print(my_dict.get('age'))

#
# def extract_np(psent):
#     for subtree in psent.subtrees():
#         if subtree.label() == 'NP':
#             yield [(word, tag, index) for word, tag, index in subtree.leaves()]
#
#
# def extract_relations(taggedSents):
#     # grammar = "NP: {<NN><VB><TO><VB>}"
#
#     grammar = r"""
#         NP: {<NN.*><IN><NN.*><NN.*>}
#             {<NN.*><TO><DT><NN.*>}
#             {(<JJ.*>|<RB.*>|<NN.*>)*<NN.*>}
#         """
#
#     cp = RegexpParser(grammar)
#     print(cp)
#
#     relationList = []
#
#     for tSent in taggedSents:
#         result = cp.parse(tSent)
#
#         extract_gen = extract_np(result)
#
#         relationList.append([x for x in extract_gen])
#
#     print(relationList)
#     return relationList
#
# extract_relations(pt)


# """r
#     NP: {<NN.*><VB.*><PRP><NN.*>}
#         {<NN.*><VB.*><TO><VB>}
#         {<VB><VB.*><IN><NN.*>}
#     """