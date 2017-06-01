__author__ = 'ChaminiKD'
import xml.etree.ElementTree as ET
from operator import itemgetter
from nltk.corpus import wordnet
from nltk.metrics import *

# retrieve table names from company.xml
def get_Table_names():
    tree = ET.parse("company_new.xml")
    tables = [el.attrib.get('tbname') for el in tree.findall('.//table')]
    return tables


table_knowledgebase_file = open('tab_knowledgebase.txt', 'w')


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
    # if type == 'att':
    #     att_list = list
    #     for x in att_list:
    #         syns = wordnet.synsets(x, pos='n')
    #         att_knowledgebase_file.write(str([x, syns]))
    #         att_knowledgebase_file.write("\n")
    #         knowledgeBase.append([x, syns])

    return knowledgeBase



# att_list = get_attribute_names()
# att = setSementicKB('att', att_list)


def extract_tables(nouns):
    table_file = open('table_editDistance.txt', 'w')
    table_list = get_Table_names()
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


def find_tables(noun_list):
    list = extract_tables(noun_list)
    tabList = []
    n_list = []
    for a in list:
        # print(a)
        for l in a:
            if l[2] <= 4:
                # print(l[1])
                # print((a[0])[1])
                tabList.append(l[1])
                n_list.append(l[0])
    return set(tabList), n_list


table_synset_file = open('synsets.txt', 'w')


def tableIdentifier(knowledgeBase, nounList):
    try:
        list = []
        temp = []
        n_list = []
        # for a in knowledgeBase:
        # for x in a[1]:
        for n in nounList:
            syn = wordnet.synsets(n, pos='n')
            for a in knowledgeBase:
                for x in a[1]:
                    # print(syn)
                    sim = x.wup_similarity(syn[0])
                    table_synset_file.write(str([n, syn[0], ':', x, '=', sim]))
                    table_synset_file.write("\n")
                    table_synset_file.write("\n")
                    # temp.append([n, syn[0], ":", x, "=", sim])
                    if sim >= 0.7:
                        # print("table found:", a[0])
                        list.append(a[0])
                        n_list.append(n)
                        return list, n_list
    except:
        tab, n_list = find_tables(nounList)
        return tab, n_list



table_list = get_Table_names()
asd = setSementicKB('tables', table_list)

correct_noun_list = ["employee", "department", "dependent", "department locations", "project", "workplace"]
identified_table, n_list = tableIdentifier(asd, correct_noun_list)
print("table = ", identified_table)
