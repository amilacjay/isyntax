from nltk import RegexpParser
from nltk import sent_tokenize, word_tokenize
from nltk.tag import pos_tag
from nltk import ne_chunk

from dbcreator.models import DataType


def getContentFromFile(filename):
    with open(filename) as f:
        content = f.readlines()
    return str(''.join(content)).replace('\n',' ')


def getTaggedSentences(text):
    sentences = sent_tokenize(text)
    sentences = [word_tokenize(sent) for sent in sentences]
    sentences = [pos_tag(sent) for sent in sentences]

    temp = []

    for taggedSent in sentences:
        t = []
        for index, taggedWord in enumerate(taggedSent):
            t.append((taggedWord[0], taggedWord[1], index))

        temp.append(t)

    sentences = temp

    return sentences


def extract_np(psent):
    for subtree in psent.subtrees():
        if subtree.label() == 'NP':
            yield [(word, tag, index) for word, tag, index in subtree.leaves()]


# def extract_ne(tsent):
#     for t in tsent.subtrees():
#         if t.label() == 'NE':
#             yield [(word, tag) for word, tag in t.leaves()]


# def getNamedEntities(taggedSents):
#     neSents = ne_chunk(taggedSents, binary=True)
#
#     extract_ne_gen = extract_ne(neSents)
#     neList = []
#     neList.append([x for x in extract_ne_gen])
#     flattenedList = [item for list_1 in neList for list_2 in list_1 for item in list_2]
#
#     return flattenedList


# def removeNamedEntities(tSents):
#     nEntities = getNamedEntities(tSents)
#     flattenedList = [item for list_1 in nEntities for list_2 in list_1 for item in list_2]
#     for item in flattenedList:
#         if item in tSents:
#             tSents.remove(item)


def getChunkedSentences(taggedSents):
    grammar = r"""
    NP: {<NN.*><IN><NN.*><NN.*>?}
        {<NN.*><IN>(<VB.*>|<DT>)<NN.*>}
        {<NN.*><TO><DT><NN.*>}
        {((<JJ.*>|<RB.*>|<NN.*>)*|<VBG>?)<NN.*>}
    """

    cp = RegexpParser(grammar)

    chunkList = []

    for sent in taggedSents:
        result = cp.parse(sent)

        # creating a generator
        extract_gen = extract_np(result)

        chunkList.append([x for x in extract_gen])

    return chunkList


def createSQLScript(entities):
    wholeSQL = ''
    for entity in entities:
        firstLine = "DROP TABLE IF EXISTS {} CASCADE;\nCREATE TABLE {} (".format(entity.name(), entity.name())
        # firstLine = "CREATE TABLE {} (".format(entity.name())
        queryBody = '\n'
        delimiter = ',\n'
        lastLine = "\n);\n\n"

        attributeList = entity.getAttributes()
        keys = [atr.name() for atr in attributeList if atr.isUnique == True]
        primaryKeyLine = ',\n\tPRIMARY KEY('+ ','.join(keys) +')'

        for i, attribute in enumerate(attributeList):
            dTypeSize = '(50)'
            uniqueKW = ' UNIQUE'
            notnullKW = ' NOT NULL'

            attributeLine = '\t{} {}{}{}{}'.format(attribute.name(), attribute.dtype, dTypeSize if attribute.dtype == DataType.VARCHAR else '' ,
                                               uniqueKW if attribute.isUnique else '', notnullKW if attribute.isNotNull else '')

            if i != len(attributeList) - 1:
                attributeLine = attributeLine + delimiter
            queryBody = queryBody + attributeLine

        wholeSQL = wholeSQL + (firstLine + queryBody + primaryKeyLine + lastLine)

    return wholeSQL


def csv_reader(filename):
    with open(filename) as f:
        content = f.readlines()
    return [s.strip() for s in str(''.join(content)).split(',')]



# def extract_relations(taggedSents):
#     grammar = "NP: {<NN.*><NN.*><IN><NN.*>}"
#
#     # { < NN. * > < VB. * > < VB. * > < TO > < DT > < NN. * >}
#     # { < NN. * > < VB. * > * < IN > < DT > < NN. * >}
#     #         {<NN.*><VB.*><JJ><NN.*>}
#     # grammar = """r
#     # NP: {<NN.*>(<NN.*>|<VB.*>)(<IN>|<JJ>|<VB.*>)<NN.*>}
#     #     {<NN.*><VB.*>(<IN>|<VB.*>)<TO><DT><NN.*>}
#     # """
#
#     cp = RegexpParser(grammar)
#
#     relationList = []
#     for tSent in taggedSents:
#         result = cp.parse(tSent)
#
#         extract_gen = extract_np(result)
#
#         relationList.append([x for x in extract_gen])
#
#         # for item in relationList:
#         #     for index, re in enumerate(item):
#         #         if re[2][1] == 'IN':
#         #             hIndex = re[2][2]
#         #             for i, chunk in enumerate(relationList[index]):
#         #                 print(chunk[0][3])
#         #                 if chunk[0][2] < hIndex:
#         #                     relative_1 = chunk[0][0]
#         #                     print(relative_1)
#         #                 if chunk[0][2] > hIndex:
#         #                     relative_2 = chunk[0][3]
#         #                     print(relative_2)

