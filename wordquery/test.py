__author__ = 'ChaminiKD'

from operator import itemgetter
import xml.etree.ElementTree as ET
import nltk
from nltk.corpus import wordnet
from nltk.metrics import *
import xml.etree.cElementTree as etree

__author__ = 'ChaminiKD'

xml_file = "company_new.xml"
# tab_att_list = []

def table_extractor(attribute_list):
    xmlDoc = open(xml_file, 'r')
    xmlDocData = xmlDoc.read()
    xmlDocTree = etree.XML(xmlDocData)

    lists = []
    for ingredient in xmlDocTree.iter('tables'):
        for s in ingredient:
            lista = []
            for a in s:
                for i in a:
                    lista.append(i.attrib['attname'])
            lists.append([[s.attrib['tbname']], lista])
        print(lists)
    # return lists

    a_list = []
    for att in attribute_list:
        for l in lists:
            for t in l:
                if str(att.lower() == t).lower() and l[0] not in a_list:
                    a_list.append(l[0])
    print(a_list, '+++')


def get_referenceTable(tab, con_att):
    xmlDoc = open(xml_file, 'r')
    xmlDocData = xmlDoc.read()
    xmlDocTree = etree.XML(xmlDocData)

    list = []

    for ingredient in xmlDocTree.iter('tables'):
        for s in ingredient:
            for e in s.iter('attribute'):
                if str(e.find('referencedTable').text).lower() != 'none':
                    # print(s.attrib['tbname'], e.find('referencedTable').text, e.find('referencedColumn').text)
                    list.append([s.attrib['tbname'], e.find('referencedTable').text, e.find('referencedColumn').text])
    refList= []
    for t in tab:
        for l in list:
            if l[0] == t:
                ref = l[1]
                refList.append(ref)
    print("reference tables :",refList)
    return refList

def ref_column(reference_list ,list):
    ref_table = []
    ref_column = []
    for r in reference_list:
        for ls in list:
            for l in ls:
                # print(l[0])
                if l[0] == r :
                    ref_table.append(l[0])
    print(ref_table)


tab = ['employee']
con_att = ['departmentname']

reference_list = get_referenceTable(tab, con_att)
#print(reference_list)
list = table_extractor(con_att)
# reference_col = ref_column(reference_list , list)













