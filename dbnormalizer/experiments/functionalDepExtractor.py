from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import xml.etree.ElementTree

# The symbols to remove
signs = ['.', '+']
tables = []
attributes = []


def readfile(name):
    scenario = open('..\input\\' + name, 'r')
    contents = scenario.read()
    return contents


def extractor(fileContent):
    removed = []
    sentences = sent_tokenize(fileContent)
    for sent in sentences:
        tokens = word_tokenize(sent)
        filtered = [word for word in tokens if word not in stopwords.words('english')]
        print(filtered)
        # for token in filtered:
        #     att.append(token)
        filtered = remove(signs, filtered)
        removed.append(filtered)
    tablereader(removed)
    return removed


def remove(signList, tokens):
    temp = [word for word in tokens if word not in signList]
    return temp


# identifying the reference table
def tablereader(lists):
    for singleList in lists:
        print(singleList)


# get Table names from the XML
def tablenames(file):
    database = xml.etree.ElementTree.parse('..\output\\' + file).getroot()
    for a in database.iter('table'):
        tables.append(a)
    return tables

content = readfile('scenario.txt')
x = tablenames('company_new.xml')
for a in x:
    print(a.keys())
extractor(content)
