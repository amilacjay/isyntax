from dbcreator.core import *
from dbcreator.models import *
import nltk


# text = getContentFromFile('../samples/sample2.txt.txt')


## primary data sets
# tagged_sentences = getTaggedSentences(text)
# chunked_sents = getChunkedSentences(tagged_sentences)
#
#
# print(tagged_sentences)
# print(chunked_sents)

data = csv_reader('../knowledge_base/entities.csv')

for d in data:
    print(d)
