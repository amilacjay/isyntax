import nltk
from nltk import sent_tokenize, word_tokenize
from nltk.tag import pos_tag
# from Project_v2.element_identifier import *

__author__ = 'ChaminiKD'


def extract_np(psent):
    for subtree in psent.subtrees():
        if subtree.label() == 'NP':
            yield ' '.join(word for word, tag in subtree.leaves())


def getContentFromFile(filename):
    with open(filename) as f:
        content = f.readlines()
    return str(''.join(content)).replace('\n', ' ')


def getTaggedSentences(text):
    sentenses = sent_tokenize(text)
    sentenses = [word_tokenize(sent) for sent in sentenses]
    sentenses = [pos_tag(sent) for sent in sentenses]

    return sentenses


text = getContentFromFile('removed_sample3.txt')

tagged_sentences = getTaggedSentences(text)

# grammar = "NP: {(<JJ.*>|<RB.*>|<NN.*>)*<NN.*>}"
grammar = "NP: {<NNS>*<NN>*}"

cp = nltk.RegexpParser(grammar)

text_file = open("tagged_sent.txt", "w")

for sent in tagged_sentences:
    print('Tagged Sentence: {}'.format(sent))
    text_file.write('Tagged Sentence: {}'.format(sent))
    text_file.write("\n")

    result = cp.parse(sent)

    extract_gen = extract_np(result)

    # print('Noun Phrases: {}'.format([x for x in extract_gen]))
    # print()
    text_file.write('Noun Phrases: {}'.format([x for x in extract_gen]))
    text_file.write("\n")
    text_file.write("\n")

text_file.close()

# identify_tables(extract_gen)
