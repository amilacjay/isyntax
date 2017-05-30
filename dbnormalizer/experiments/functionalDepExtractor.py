from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import xml.etree.ElementTree

# The symbols to remove
signs = ['.', '+']

# attribute list
attributes = []

# The keyword set
keywords = ['depends']


# Read the scenario file from inputs
def readfile(name):
    scenario = open('..\input\\' + name, 'r')
    contents = scenario.read()
    return contents


# Extract the file content
def extractor(fileContent):
    removed = []
    sentences = sent_tokenize(fileContent)
    sentlist = get_sent(sentences, keywords)
    for sent in sentlist:
        tokens = word_tokenize(sent)
        filtered = [word for word in tokens if word not in stopwords.words('english')]
        filtered = remove(signs, filtered)
        removed.append(filtered)
    table_reader(removed)
    print(removed)
    return removed


# A function to extract the necessary sentences
def get_sent(sentences, keywords):
    vlist = []
    for sent in sentences:
        words = sent.split()
        for key in keywords:
            if key in words:
                vlist.append(sent)
    return vlist


# Remove the given set of signs
def remove(signList, tokens):
    temp = [word for word in tokens if word not in signList]
    return temp


# identifying the reference table
def table_reader(lists):
    for singleList in lists:
        print(singleList)


# get Table names from the XML
def table_names(file):
    database = xml.etree.ElementTree.parse('..\output\\' + file).getroot()
    for a in database.iter('attribute'):
        attributes.append(a)
        print(a.attrib)
    return attributes


content = readfile('scenario.txt')
x = table_names('company_new.xml')
extractor(content)
