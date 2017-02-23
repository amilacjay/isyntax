from operator import itemgetter
import xml.etree.ElementTree as ET
import nltk
from nltk.corpus import wordnet
from nltk.metrics import *

__author__ = 'ChaminiKD'


# def sort_nouns(taggs):
#     nouns = [word for word, pos in taggs if pos == 'NN']
#     print("nouns list :", nouns)
def getContentFromFile(filename):
    with open(filename) as f:
        content = f.readlines()
    return str(''.join(content)).replace('\n', ' ')


def extract_np(psent):
    for subtree in psent.subtrees():
        if subtree.label() == 'NP':
            yield ' '.join(word for word, tag in subtree.leaves())


def chunk_nouns(tags):
    # grammar = "NP: {(<JJ.*>|<RB.*>|<NN.*>)*<NN.*>}"
    grammar = "NP: {<NNS>*<NN>*}"

    cp = nltk.RegexpParser(grammar)
    result = cp.parse(tags)
    extract_gen = extract_np(result)
    # text_file.write('Noun Phrases: {}'.format([x for x in extract_gen]))
    return [x for x in extract_gen]


# retrieve table names from company.xml
def get_Table_names():
    tree = ET.parse("company.xml")
    tables = [el.attrib.get('tbname') for el in tree.findall('.//table')]
    return tables


# retrieve attribute names from company.xml
def get_attribute_names():
    tree = ET.parse("company.xml")
    attributes = [el.attrib.get('attname') for el in tree.findall('.//attribute')]
    return attributes


# def identify_tables(nouns):
#     table_list = get_Table_names()
#     print("Table list", table_list)
#     for n in nouns:
#         combine = []
#         for x in table_list:
#             dist = edit_distance(n.lower(), x.lower())
#             combine.append([n, x, dist])
#
#         temp = []
#         for a in combine:
#             if n == a[0]:
#                 temp.append([a[1], a[2]])
#         temp.sort(key=lambda x: x[1])
#         for x in temp:
#             print(x[0], x[1])
#
#             if x[1] == 0:
#                 print("table found : " + x[0])
#
#         print("***********")
#     identify_attributes(nouns)
#
#
# def identify_attributes(nouns):
#     attrbute_list = get_attribute_names()
#     print("Attribute list", attrbute_list)
#     for n in nouns:
#         count = []
#         for y in attrbute_list:
#             dist = edit_distance(n.lower(), y.lower())
#             count.append([n, y, dist])
#         temp = []
#         for a in count:
#             if n == a[0]:
#                 temp.append([a[1], a[2]])
#         temp.sort(key=lambda x: x[1])
#         for x in temp:
#             print(x[0], x[1])
#
#             if x[1] == 0:
#                 print("attribute found : " + x[0])
#
#         print("***********")
#

def extract_tables(nouns):
    table_file = open('out/table_editDistance.txt', 'w')
    table_list = get_Table_names()
    # print("Table list", table_list)
    list1 = []
    for n in nouns:
        count = []
        temp = []
        for y in table_list:
            dist = edit_distance(n.lower(), y.lower())
            count.append([n, y, dist])
        # print(count)
        temp = sorted(count, key=itemgetter(2))
        list1.append(temp)
        # print(temp)
        # print(temp[0], temp[1], temp[2])
        table_file.write(str(temp))
        table_file.write("\n")
        # return temp
    return list1


def extract_attributes(nouns):
    att_file = open('out/attribute_editDistance.txt', 'w')
    attribute_list = get_attribute_names()
    # print("Attribute list", attribute_list)
    list2 = []
    for n in nouns:
        count = []
        temp = []
        for y in attribute_list:
            dist = edit_distance(n.lower(), y.lower())
            count.append([n, y, dist])
        # print(count)
        temp = sorted(count, key=itemgetter(2))
        # print(temp)
        list2.append(temp)
        att_file.write(str(temp))
        att_file.write("\n")
    return list2


table_knowledgebase_file = open('out/table_knowledgebase.txt', 'w')
att_knowledgebase_file = open('out/attribute_knowledgebase.txt', 'w')


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

# def write_file(name , values):
#     file= open('out/'+name+'.txt', 'w')
#     print("#########################")
#     file.write(str(values))
#     print("#########################")
#     file.close()

table_synset_file = open('out/table_synset.txt', 'w')
def tableIdentifier(knowledgeBase, nounList):
    try:
        list = []
        temp = []
        # for a in knowledgeBase:
        # for x in a[1]:
        for n in nounList:
            syn = wordnet.synsets(n, pos='n')
            for a in knowledgeBase:
                for x in a[1]:
                    # print(syn)
                    sim = x.wup_similarity(syn[0])
                    table_synset_file.write(str([n, syn[0] , ':' , x , '=' , sim]))
                    table_synset_file.write("\n")
                    # temp.append([n, syn[0], ":", x, "=", sim])
                    if sim >= 0.7:
                        #print("table found:", a[0])
                        list.append(a[0])
                        return list
    except:
        tab = find_tables(nounList)
        return tab

att_synset_file = open('out/attribute_synset.txt', 'w')
def attributeIdentifier(knowledgeBase, nounList):
    list2 = []
    try:
        for n in nounList:
            syn = wordnet.synsets(n, pos='n')
            for a in knowledgeBase:
                for x in a[1]:
                    # print(syn)
                    sim = x.wup_similarity(syn[0])
                    att_synset_file.write(str([n, syn[0] , ':' , x , '=' , sim]))
                    att_synset_file.write("\n")
                    # print(n, syn[0], ":", x, "=", sim)
                    if sim >= 0.75:
                        #print("attribute found:", a[0])
                        list2.append(a[0])
        if not list2:
                    at = find_attributes(nounList)
                    return at

                    # else:
                    #     at = find_attributes(nounList)
                    #     return at

        print(list2)
        return list2
    except:
        att = find_attributes(nounList)
        return att


def find_tables(noun_list):
    list = extract_tables(noun_list)
    tabList = []
    for a in list:
        # print(a)
        for l in a :
            if l[2] <= 4:
                # print(l[1])
                # print((a[0])[1])
                tabList.append(l[1])
    return set(tabList)

def find_attributes(noun_list):
    list = extract_attributes(noun_list)
    attList = []
    for a in list:
        # print(a)
        for l in a :
            if l[2] <= 4:
                # print(l[1])
                # print((a[0])[1])
                attList.append(l[1])
    return set(attList)





# asd = setSementicKB('tables', ['department', 'dependent', 'employee'])
# assw = tableIdentifier(asd, ['labourer'])

# print(asd)
# for a in asd:
#     for x in a[1]:
#         print(x.name()+" = "+x.definition())
