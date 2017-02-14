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

    return sentenses

def getEntitiesWithAttributes(taggedSents):
    pass