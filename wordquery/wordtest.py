import xml

from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import *

#sent = "what are the department location"
sent = "what are the department names of the departments"

stemmer = PorterStemmer()

from pattern.en import pluralize, singularize

def extractor(sent):
    tokens = []
    removed = []
    sentences = sent_tokenize(sent)
    for sent in sentences:
        tokens = word_tokenize(sent)
        filtered = [word for word in tokens if word not in stopwords.words('english')]
        # removed.append(filtered)
    print(filtered)
    for w in filtered:
        st = stemmer.stem(w)
        print(singularize(w))
        # print(st)
        tokens.append(st)
    # singles = [stemmer.stem(r) for r in removed]

    return tokens


def table_names(file):
    attributes = []
    database = xml.etree.ElementTree.parse(file).getroot()
    for a in database.iter('attribute'):
        attributes.append(a.attrib['attname'])
    print(attributes)
    return attributes


# restructure the keys based on the XML data taken from the database
def restructure_keys(sent, attrib):
    global simplelist
    for x in sent:
        for y in x:
            index = 0
            loop = 0
            simplelist = []
            # s = [word for word in x if word.lower() not in [y.lower() for y in attrib]]
            if isattribute(y, attrib) == 0 and loop == 0 and (index + 1) < len(x):
                temp = x[index] + '_' + x[index + 1]
                if isattribute(temp, attrib) == -1:
                    simplelist.append(temp)
                loop += 1
            elif loop == 1:
                loop -= 1
                index += 1
                continue
            elif isattribute(y, attrib) == -1 and loop == 0:
                simplelist.append(y)
            index += 1
    print("restructured", simplelist)


def isattribute(word, attrib):
    if word.lower() not in [y.lower() for y in attrib]:
        return 0
    else:
        return -1


tokens = extractor(sent)
asd = table_names("company_new.xml")
print("tokens: ", tokens)
restructure_keys(tokens, asd)
