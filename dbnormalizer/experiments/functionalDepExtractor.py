import itertools
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import xml.etree.ElementTree

# The symbols to remove
signs = ['.', '+', ',']

# attribute list
attributes = []

# The keyword set
keywords = ['depends', 'decides', 'based', 'relies']


# Read the scenario file from inputs
def readfile(name):
    scenario = open('../input/' + name, 'r')
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


# # identifying the reference table
# def table_reader(lists):
#     for singleList in lists:
#         print(singleList)


# get attribute names from the XML
def table_names(file):
    database = xml.etree.ElementTree.parse('../output/' + file).getroot()
    for a in database.iter('attribute'):
        attributes.append(a.attrib['attname'])
    return attributes


# converting to functional dependencies
def get_functionaldep(content):
    lhs = []
    rhs = []
    for con in content:
        if keywords[0] in con:
            x = con.index(keywords[0])
            lhs.append(con[:x])
            rhs.append(con[(x + 1):])
        if keywords[1] in con:
            x = con.index(keywords[1])
            rhs.append(con[:x])
            lhs.append(con[(x + 1):])
        if keywords[2] in con:
            x = con.index(keywords[2])
            lhs.append(con[:x])
            rhs.append(con[(x + 1):])
        if keywords[3] in con:
            x = con.index(keywords[3])
            lhs.append(con[:x])
            rhs.append(con[(x + 1):])
    # return lhs and rhs keys
    fds = []
    index = 0
    for y in rhs:
        fds.append([y, lhs[index]])
        index += 1
    return fds


# restructure the keys based on the XML data taken from the database
def restructure_keys(fds, attrib):
    final = []
    for x in fds:
        for y in x:
            index = 0
            loop = 0
            simplelist = []
            # s = [word for word in x if word.lower() not in [y.lower() for y in attrib]]
            for S in y:
                if isattribute(S, attrib) == 0 and loop == 0 and (index + 1) < len(y):
                    temp = y[index] + '_' + y[index + 1]
                    if isattribute(temp, attrib) == -1:
                        simplelist.append(temp)
                    loop = loop + 1
                elif loop == 1:
                    loop = loop - 1
                    index = index + 1
                    continue
                elif isattribute(S, attrib) == -1 and loop == 0:
                    simplelist.append(S)
                index = index + 1
            final.append(simplelist)
    restructured_final = []
    for i, v in enumerate(final):
        if i % 2 == 0:
            restructured_final.append([final[i], final[i + 1]])
        elif i % 2 != 0:
            continue
    return restructured_final


# checks if the word is in the attribute list or not
def isattribute(word, attrib):
    if word.lower() not in [y.lower() for y in attrib]:
        return 0
    else:
        return -1


