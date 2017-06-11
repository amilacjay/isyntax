import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re
import nltk
from nltk.corpus import wordnet

__author__ = 'ChaminiKD'

# xml_file = 'company_new.xml'

table_knowledgebase_file = open('../out/table_knowledgebase.txt', 'w')
att_knowledgebase_file = open('../out/attribute_knowledgebase.txt', 'w')

#create knowledgebase
def setSementicKB(type, list):
    knowledgeBase = []
    if type == 'tables':
        table_list = list
        for x in table_list:
            syns = wordnet.synsets(x, pos='n')
            # table_knowledgebase_file.write("hello")
            table_knowledgebase_file.write(str([x, syns]))
            table_knowledgebase_file.write("\n")
            knowledgeBase.append([x, syns])
    if type == 'att':
        att_list = list
        for x in att_list:
            syns = wordnet.synsets(x, pos='n')
            att_knowledgebase_file.write(str([x, syns]))
            att_knowledgebase_file.write("\n")
            knowledgeBase.append([x, syns])
    return knowledgeBase


def add_space(token):
    ilist = []
    index = 0
    while index < len(token):
        index = token.find("'", index)
        if index == -1:
            break
        else:
            token = (token[:index+1] + ' ' + token[index+1:])
            index+=1
        index += 1
    # print("PPPPPPPPPPPPPPPPPPP", ilist)
    # for x in ilist:
    #     token = (token[:x + 1] + ' ' + token[x + 1:])
    return (token)


# extract the value from the user query
def getvalue(S):
    pattern = re.compile('\'[A-Za-z0-9 _-]*\'', re.IGNORECASE)
    listofHits = re.findall(pattern, S)
    value = []
    if listofHits:
        for hitWord in listofHits:
            value.append(hitWord)
            S = S.replace(hitWord, " ", 1)
            # return value, S

    else:
        value = ''
        # return 0, S
        # print("No value provided by the user")
    return value, S


# tokenize
def getTokenz(S):
    tokenz = nltk.word_tokenize(S)
    return tokenz


# remove escape words
# def remove_stopWords(tokenz):
#     filtered_words = [word for word in tokenz if word not in stopwords.words('english')]
#     escapeWords = ['what', 'who', 'whose', 'display', 'is', 'a', 'at', 'is', '.', ',', '(', ')', 'equal', 'equals',
#                    'greaterthan']
#     resultWords = [word for word in filtered_words if word.lower() not in escapeWords]
#     return resultWords


# remove escape words from pos tag list
def remove_escapeWords(content):
    contentnew = []
    # print(content)
    for x in content:
        filtered_words = [word for word in x if word not in stopwords.words('english')]
        escapeWords = ['what', 'who', 'whose', 'display', 'is', 'a', 'at', 'is', 'of', '.', ',', '(', ')', 'equal',
                       'equals', 'greaterthan', '\'' , 'lessthan' , 'details']
        resultWords = [word for word in filtered_words if word.lower() not in escapeWords]
        if len(resultWords) > 1:
            contentnew.append(tuple(resultWords))
    return contentnew


# POS tagging
def pos_tagging(S):
    tagged = nltk.pos_tag(S)
    return tagged
