from dbcreator.core import *
from dbcreator.models import *
import nltk


text = getContentFromFile('../samples/sample1.txt')


## primary data sets
tagged_sentences = getTaggedSentences(text)
chunked_sents = getChunkedSentences(tagged_sentences)



