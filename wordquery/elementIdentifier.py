from operator import itemgetter
import xml.etree.ElementTree as ET
import nltk
from nltk.corpus import wordnet
from nltk.metrics import *

__author__ = 'ChaminiKD'
xml_file = 'company_new.xml'
expression_list = [("equals", "="), ("greater than", ">"), ("less than", "<"), ("greater than or equal", ">="),
                   ("less than or equal", "<="),
                   ("notequal", "<>"), ("greaterthan", ">"), ("lessthan", "<"), ("greater than or equal to", ">="),
                   ("less than or equal to", "<="), ("like", "like"), ("equal", "="), ("order by", "order by"),
                   ("equal to", "=")]


def identify_expressions(remaining_sentence):
    temp = []
    symbol = []
    indx = 0

    for word in remaining_sentence:
        for elm in expression_list:
            if elm[0] == word:
                temp.append([word, indx , elm[1]])
                # print(word + " is in " + str(indx))
                # temp[0].extend(str(indx))
                # temp[indx][1].append(elm[1])
                # word[0].append(remaining_sentence.index(word))
                symbol.append([elm[1], indx ])
        indx = indx + 1
    return temp, symbol


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
    # grammar = "NP: {<NNS>*<NN>*}"
    # cp = nltk.RegexpParser(grammar)
    # result = cp.parse(tags)
    # extract_gen = extract_np(result)
    # return [x for x in extract_gen]

    tlist = []
    for t in tags:
        if t[1] == 'NN' or t[1] == 'NNS':
            tlist.append(t[0])
    return tlist


# retrieve table names from company.xml
def get_Table_names(xml_file):
    tree = ET.parse(xml_file)
    tables = [el.attrib.get('tbname') for el in tree.findall('.//table')]
    return tables


# retrieve attribute names from company.xml
def get_attribute_names(xmlfile):
    tree = ET.parse(xmlfile)
    attributes = [el.attrib.get('attname') for el in tree.findall('.//attribute')]
    return attributes


def extract_tables(nouns):
    table_file = open('out/table_editDistance.txt', 'w')
    table_list = get_Table_names(xml_file)

    list1 = []
    for n in nouns:
        count = []
        temp = []
        for y in table_list:
            dist = edit_distance(n.lower(), y.lower())
            count.append([n, y, dist])
        temp = sorted(count, key=itemgetter(2))
        list1.append(temp)
        # print(temp)
        # print(temp[0], temp[1], temp[2])
        table_file.write(str(temp))
        table_file.write("\n")
    return list1


def extract_attributes(nouns):
    att_file = open('out/attribute_editDistance.txt', 'w')
    attribute_list = get_attribute_names(xml_file)
    # print("Attribute list", attribute_list)
    list2 = []
    for n in nouns:
        count = []
        temp = []
        for y in attribute_list:
            dist = edit_distance(n.lower(), y.lower())
            count.append([n, y, dist])
        temp = sorted(count, key=itemgetter(2))
        list2.append(temp)
        att_file.write(str(temp))
        att_file.write("\n")
    return list2


table_synset_file = open('out/table_synset.txt', 'w')


def tableIdentifier(knowledgeBase, nounList):
    try:
        list = []
        temp = []
        n_list = []
        for n in nounList:
            syn = wordnet.synsets(n, pos='n')
            for a in knowledgeBase:
                for x in a[1]:
                    sim = x.wup_similarity(syn[0])
                    table_synset_file.write(str([n, syn[0], ':', x, '=', sim]))
                    table_synset_file.write("\n")
                    # temp.append([n, syn[0], ":", x, "=", sim])
                    if sim >= 0.75:
                        # print("table found:", a[0])
                        list.append(a[0])
                        n_list.append(n)
                        return list, n_list
    except:
        tab, n_list = find_tables(nounList)
        return tab, n_list


att_synset_file = open('out/attribute_synset.txt', 'w')


def attributeIdentifier(knowledgeBase, nounList):
    list2 = []
    new_list = []
    for n in nounList:
        try:
            syn = wordnet.synsets(n, pos='n')
            for a in knowledgeBase:
                for x in a[1]:
                    sim = x.wup_similarity(syn[0])
                    att_synset_file.write(str([n, syn[0], ':', x, '=', sim]))
                    att_synset_file.write("\n")

                    if sim >= 0.75:
                        list2.append(a[0])
        except:
            new_list = []
            new_list.append(n)
            att = find_attributes(new_list)
            list2.extend(att)
            # print(":::::::::::", list2)
    return list2


def find_tables(noun_list):
    list = extract_tables(noun_list)
    tabList = []
    n_list = []
    for a in list:
        for l in a:
            if l[2] <= 3:
                tabList.append(l[1])
                n_list.append(l[0])
    return set(tabList), n_list


def find_attributes(noun_list):
    list = extract_attributes(noun_list)
    attList = []
    for a in list:
        for l in a:
            if l[2] <= 3:
                attList.append(l[1])
    return set(attList)
