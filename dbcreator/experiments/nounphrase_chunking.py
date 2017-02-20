from dbcreator.core import *
import nltk


def extract_np(psent):

    for index, subtree in enumerate(psent.subtrees()):
        if subtree.label() == 'NP':
            cList = [(word, tag) for i, (word, tag) in enumerate(subtree.leaves())]
            yield cList

text = getContentFromFile('../samples/sample1.txt')

tagged_sentences = getTaggedSentences(text)
print(tagged_sentences)

grammar = "NP: {(<JJ.*>|<RB.*>|<NN.*>)*<NN.*>}"

cp = nltk.RegexpParser(grammar)

for sent in tagged_sentences:
    print('Tagged Sentence: {}'.format(sent))
    result = cp.parse(sent)

    extract_gen = extract_np(result)

    print('Noun Phrases: {}'.format([x for x in extract_gen]))
    print()
