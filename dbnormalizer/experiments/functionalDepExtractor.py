from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import xml.etree.ElementTree

# The symbols to remove
signs = ['.', '+', ',']

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


# get attribute names from the XML
def table_names(file):
    database = xml.etree.ElementTree.parse('..\output\\' + file).getroot()
    for a in database.iter('attribute'):
        attributes.append(a.attrib['attname'])
    return attributes


# converting to functional dependencies
def get_functionaldep(content):
    lhs = []
    rhs = []
    for con in content:
        x = con.index(keywords[0])
        lhs.append(con[:x])
        rhs.append(con[(x + 1):])
    print("lhs", lhs)
    print("rhs", rhs)
    # return lhs and rhs keys
    fds = ([lhs, rhs])
    return fds


# restructure the keys based on the XML data taken from the database
def restructure_keys(fds, attrib):
    final = []
    for x in fds:
        for y in x:
            index = 0
            loop = 0
            lhs = []
            # s = [word for word in x if word.lower() not in [y.lower() for y in attrib]]
            for S in y:
                if isattribute(S, attrib) == 0 and loop == 0:
                    temp = y[index] + '_' + y[index + 1]
                    if isattribute(temp, attrib) == -1:
                        lhs.append(temp)
                    loop = loop + 1
                elif loop == 1:
                    loop = loop - 1
                    index = index + 1
                    continue
                elif isattribute(S, attrib) == -1 and loop == 0:
                    lhs.append(S)
                index = index + 1
            final.append(lhs)
    print("restructured", final)


# checks if the word is in the attribute list or not
def isattribute(word, attrib):
    if word.lower() not in [y.lower() for y in attrib]:
        return 0
    else:
        return -1


content = readfile('scenario.txt')
x = table_names('company_new.xml')
print(x)
s = get_functionaldep(extractor(content))
restructure_keys(s, x)
