import xml.etree.ElementTree
import dbnormalizer.experiments.functionalDepExtractor as extract
import dbnormalizer.experiments.amila_test as depMatrix


def table_names(file):
    table_primary = []
    relations = []
    database = xml.etree.ElementTree.parse('..\output\\' + file).getroot()
    for a in database.iter('table'):
        primary = []
        attributes = []
        for x in a.iter('attribute'):
            attributes.append(x.attrib['attname'])
            if str(x.find('columnKey').text).lower() == 'pri':
                primary.append(x.attrib['attname'])
        relations.append([a.attrib['tbname'], attributes])
        table_primary.append([a.attrib['tbname'], primary])
    return relations, table_primary


# get the relevant dependencies from the list
def get_relevantDep(fds, primary, atts):
    alldep = []
    for i, key in enumerate(primary):
        relevantfds = []
        for fd in fds:
            if [fds for fds in fd[0] if fds in key[1]] and len(fd[0]) <= len(key[1]):
                relevantfds.append(fd)
        for at in atts:
            print("atts,",atts)
            if [fds for fds in fd[0] if fds in at[1]]:
                relevantfds.append(fd)
        alldep.append([key[0], key[1], relevantfds])
    return alldep


def normalize(dep, relation):
    rel, fds = '', []
    for d in dep:
        for v in relation:
            if str(v[0]).lower() == str(d[0]).lower():
                ind = v
                print("functional dep", d[2])
                print("relation", ind)
                rel = ind[1]
        fds = d[2]
        # DM, determinents = depMatrix.dependencyMatrix(rel, fds)
        # print("DM")
        # print(DM)
        #
        # DG = depMatrix.directedGraph(DM, determinents, rel)
        # print("DG")
        # print(DG)
        #
        # DC = depMatrix.dependencyClosure(DM, DG, determinents, rel, fds)
        # print(DC)
        #
        # CDC = depMatrix.circularDependency(DM, DC)
        # print("CDC")
        # print(CDC)


file_name = "example_scenario.txt"
xml_file = 'example.xml'

content = extract.readfile(file_name)
x = extract.table_names(xml_file)
s = extract.get_functionaldep(extract.extractor(content))
fds = extract.restructure_keys(s, x)
tables, primary = table_names(xml_file)
dependencies = get_relevantDep(fds, primary, tables)
normalize(dependencies, tables)
