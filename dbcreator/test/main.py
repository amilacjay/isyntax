from dbcreator.core import *
from dbcreator.models import *
import nltk


text = getContentFromFile('../samples/sample1.txt')

tagged_sentences = getTaggedSentences(text)

# entities = getEntitiesWithAttributes(tagged_sentences)
