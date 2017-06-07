__author__ = 'ChaminiKD'

from operator import itemgetter
import xml.etree.ElementTree as ET
import nltk
from nltk.corpus import wordnet
from nltk.metrics import *

__author__ = 'ChaminiKD'

xml_file = "company_new.xml"

import xml.etree.cElementTree as etree


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
            lists.append([s.attrib['tbname'], lista])
        print(lists)

    a_list = []
    for att in attribute_list:
        for l in lists:
            for t in l[1]:
                if att.lower() == t.lower() and l[0] not in a_list:
                    a_list.append(l[0])
    print(a_list, '+++')

def get_referenceTable():
    xmlDoc = open(xml_file, 'r')
    xmlDocData = xmlDoc.read()
    xmlDocTree = etree.XML(xmlDocData)

    for ingredient in xmlDocTree.iter('tables'):
        for s in ingredient:
            print(s.attrib)

get_referenceTable()
tab = ['employee']
# attribute_list = ['Department_name', 'Name']
# table_extractor(attribute_list)
