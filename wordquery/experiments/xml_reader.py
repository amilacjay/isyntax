from operator import itemgetter
import xml.etree.ElementTree as ET
import nltk
from nltk.corpus import wordnet
from nltk.metrics import *

__author__ = 'ChaminiKD'

xml_file = "company_new.xml"

from xml.dom.minidom import parse
import xml.dom.minidom

# # Open XML document using minidom parser
# DOMTree = xml.dom.minidom.parse(xml_file)
# collection = DOMTree.documentElement
# if collection.hasAttribute("shelf"):
#    print ("Root element : %s" % collection.getAttribute("shelf"))
#
# # Get all the movies in the collection
# tables = collection.getElementsByTagName("table")
#
# # Print detail of each movie.
# for table in tables:
#    print ("*****Table*****")
#    if table.hasAttribute("tbname"):
#       print ("Name: %s" % table.getAttribute("tbname"))
#       print(table.getAttribute("attributes"))
#
#    attributes = table.getElementsByTagName('attributes')[0].textContent
#    print(attributes)
#
import xml.etree.cElementTree as etree

xmlDoc = open('company_new.xml', 'r')
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
#
# for i in lists:
#     print(i[1])
