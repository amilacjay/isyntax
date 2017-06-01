import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re

__author__ = 'ChaminiKD'

# extract the value from the user query
def getvalue(S):
    pattern = re.compile('\'[A-Za-z0-9 _-]*\'', re.IGNORECASE)
    listofHits = re.findall(pattern, S)
    if listofHits:
        for hitWord in listofHits:
            value = hitWord
            S = S.replace(value, " ", 1)
            # print('Values =', value)
            return value, S

    else:
        return 0, S
        # print("No value provided by the user")


# tokenize
def getTokenz(S):
    tokenz = nltk.word_tokenize(S)
    return tokenz


# remove escape words
def remove_stopWords(tokenz):
    filtered_words = [word for word in tokenz if word not in stopwords.words('english')]
    escapeWords = ['what', 'who', 'whose', 'display', 'is', 'a', 'at', 'is', '.', ',', '(', ')', 'equal', 'equals']
    resultWords = [word for word in filtered_words if word.lower() not in escapeWords]
    return resultWords


# POS tagging
def pos_tagging(S):
    tagged = nltk.pos_tag(S)
    return tagged
