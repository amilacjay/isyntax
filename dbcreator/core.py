from nltk import RegexpParser
from nltk import sent_tokenize, word_tokenize
from nltk.tag import pos_tag
from dbcreator.models import *

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


def getChunkedSentences(taggedSents):
    # grammar = "NP: {(<JJ.*>|<RB.*>|<NN.*>)*<NN.*>}"

    grammar = r"""
    NP: {<NN.*><IN><NN.*>}
        {(<JJ.*>|<RB.*>|<NN.*>)*<NN.*>}
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
        firstLine = "DROP TABLE IF EXISTS {} CASCADE; CREATE TABLE {} (".format(entity.name(), entity.name())
        queryBody = '\n'
        delimiter = ',\n'
        lastLine = "\n);\n\n"

        attributeList = entity.getAttributes()
        for i, attribute in enumerate(attributeList):
            uniqueKW = ' UNIQUE'
            attributeLine = '\t{} {}{}'.format(attribute.name(), attribute.dtype, uniqueKW if attribute.isUnique else '')
            if i != len(attributeList) - 1:
                attributeLine = attributeLine + delimiter
            queryBody = queryBody + attributeLine

        wholeSQL = wholeSQL + (firstLine + queryBody + lastLine)

    return wholeSQL
