from nltk import RegexpParser
from nltk import sent_tokenize, word_tokenize
from nltk.tag import pos_tag
from dbcreator.models import *

def getContentFromFile(filename):
    with open(filename) as f:
        content = f.readlines()
    return str(''.join(content)).replace('\n',' ')


def getTaggedSentences(text):

    sentenses = sent_tokenize(text)
    sentenses = [word_tokenize(sent) for sent in sentenses]
    sentenses = [pos_tag(sent) for sent in sentenses]

    temp = []

    for taggedSent in sentenses:
        t = []
        for index, taggedWord in enumerate(taggedSent):
            t.append((taggedWord[0], taggedWord[1], index))

        temp.append(t)

    sentenses = temp

    return sentenses

def getEntitiesWithAttributes(taggedSents):
    pass

def extract_np(psent):
    for subtree in psent.subtrees():
        if subtree.label() == 'NP':
            yield [(word, tag, index) for word, tag, index in subtree.leaves()]


def getChunkedSentences(taggedSents):
    grammar = "NP: {(<JJ.*>|<RB.*>|<NN.*>)*<NN.*>}"

    cp = RegexpParser(grammar)

    chunkList = []

    for sent in taggedSents:
        result = cp.parse(sent)

        # creating a generator
        extract_gen = extract_np(result)

        chunkList.append([x for x in extract_gen])

    return chunkList
