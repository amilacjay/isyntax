from nltk import *


sentence = "The Washington Monument is the most prominent structure in Washington, D.C. and one of the city's early attractions. It was built in honor of George Washington, who led the country to independence and then became its first President."
wt = word_tokenize(sentence)
pt = pos_tag(wt)
# ne = ne_chunk(pt, binary=True)
#
# print(ne)



def extract(sent):
    for t in sent.subtrees():
        if t.label() == 'NE':
            yield [(word, tag) for word, tag in t.leaves()]


def getNamedEntities(text):
    neSents = ne_chunk(text, binary=True)

    extract_ne_gen = extract(neSents)
    neList = []
    neList.append([x for x in extract_ne_gen])
    print(neList)
    return neList

def removeNEs(tsents):
    newList = getNamedEntities(tsents)
    flattenedList = [item for list_1 in newList for list_2 in list_1 for item in list_2]
    print(flattenedList)
    for item in flattenedList:
        if item in tsents:
            tsents.remove(item)
#
removeNEs(pt)









