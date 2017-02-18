from dbcreator.core import *
import nltk


def extract_np(psent):
    for subtree in psent.subtrees():
        if subtree.label() == 'NP':
            yield ' '.join(word for word, tag in subtree.leaves())

text = getContentFromFile('../samples/sample1.txt')

tagged_sentences = getTaggedSentences(text)

grammar = "NP: {(<JJ.*>|<RB.*>|<NN.*>)*<NN.*>}"

cp = nltk.RegexpParser(grammar)

for sent in tagged_sentences:
    print('Tagged Sentence: {}'.format(sent))
    result = cp.parse(sent)

    extract_gen = extract_np(result)

    print('Noun Phrases: {}'.format([x for x in extract_gen]))
    print()
