import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from Project_v2.element_identifier import *


__author__ = 'ChaminiKD'


def getTokenz(S):
    tokenz = nltk.word_tokenize(S)
    print("tokens :", tokenz)
    remove_stopWords(tokenz)

#remove escape words
def remove_stopWords(tokenz):
    filtered_words = [word for word in tokenz if word not in stopwords.words('english')]
    print("filtered_words : ", filtered_words)
    escapeWords = ['what', 'who', 'whose', 'is', 'a', 'at', 'is', '.', ',', '(', ')']

    resultWords = [word for word in filtered_words if word.lower() not in escapeWords]
    print("resultWords :", resultWords)
    pos_tagging(resultWords)

# POS tagging the remaining words
def pos_tagging(S):
    tagged = nltk.pos_tag(S)
    print(tagged)
    sort_nouns(tagged)
