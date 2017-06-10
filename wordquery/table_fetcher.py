__author__ = 'ChaminiKD'

import xml.etree.cElementTree as etree

xml_file = "company_new.xml"


# tab_att_list = []

def table_extractor():
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
            # print("--", lists)
    return lists


list_ref = []
PKeyList = []


def get_referenceTable(tab, con_att):
    xmlDoc = open(xml_file, 'r')
    xmlDocData = xmlDoc.read()
    xmlDocTree = etree.XML(xmlDocData)

    for ingredient in xmlDocTree.iter('tables'):
        for s in ingredient:
            for e in s.iter('attribute'):
                if str(e.find('referencedTable').text).lower() != 'none':
                    list_ref.append(
                        [s.attrib['tbname'], e.find('referencedTable').text, e.find('referencedColumn').text])
                if str(e.find('columnKey').text).lower() == 'pri':
                    PKeyList.append([e.attrib['attname'], s.attrib['tbname']])
    # print("*",list_ref)
    refList = []
    for t in tab:
        for l in list_ref:
            if l[0] == t:
                ref = l[1]
                refList.append(ref)
    # print("reference tables :", refList)
    return refList


# def ref_column(reference_list, list):
#     ref_table = []
#     ref_column = []
#     for r in reference_list:
#         for ls in list:
#             for l in ls:
#                 # print(l[0])
#                 if l[0] == r:
#                     ref_table.append(l[0])
#     # print(ref_table)


def check_reftable(attlist, reflist, con_attrib):
    varlist = []
    for table in attlist:
        varlist.append((table[0])[0])

    indexes = []
    for ref in reflist:
        indexes.append(varlist.index(ref))

    for index in indexes:
        lower_attlist = [[x.lower() for x in (attlist[index])[1]]]  # convert to lower case
        if str(con_attrib[0]).lower() in lower_attlist[0]:
            return index





def get_primaryKey(table_name):
    for key in PKeyList:
        if key[1] == table_name:
            return key[0]

#
# tab = ['employee']
# con_att = ['department_name']
# identified_attributes = ['Department_number', 'Manager_ssn']
# val = 'Headquarters'
#
# reference_list = get_referenceTable(tab, con_att)
# list_table = table_extractor()
# index_selected = check_reftable(list_table, reference_list, con_att)
# ref_tables = (list_table[index_selected])[0]
# create_twoTable_query(ref_tables[0], tab[0], list_ref, identified_attributes, val, con_att)
# # reference_col = ref_column(reference_list , list)
