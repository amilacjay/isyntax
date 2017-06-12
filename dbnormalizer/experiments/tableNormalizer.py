import xml.etree.ElementTree
import dbnormalizer.experiments.functionalDepExtractor as extract
import dbnormalizer.experiments.Normalization_algo as depMatrix


def table_names(file):
    relations = []
    database = xml.etree.ElementTree.parse('../output/' + file).getroot()
    for a in database.iter('table'):
        primary = []
        attributes = []
        for x in a.iter('attribute'):
            attributes.append(x.attrib['attname'])
            if str(x.find('columnKey').text).lower() == 'pri':
                primary.append(x.attrib['attname'])
        relations.append([a.attrib['tbname'], attributes,primary])
    return relations


# get the relevant dependencies from the list
def get_relevantDep(fds, primary):
    alldep = []
    for i, key in enumerate(primary):
        relevantfds = []
        for fd in fds:
            if [fds for fds in fd[0] if fds in key[2]] and len(fd[0]) <= len(key[1]):
                relevantfds.append(fd)
            if [fds for fds in fd[0] if fds in key[1] and (fds not in relevantfds)]:
                relevantfds.append(fd)
        alldep.append([key[0], key[2], relevantfds])
    return alldep


def normalize(dep, relation):
    for i in range(len(relation)):

        fds = dep[i][2]
        rel = relation[i][1]

        # ind = v
        # print("Table Name,", v[0])
        # print("functional dep", d[2])
        # print("relation", ind)
        # rel = ind[1]

        # fds = d[2]
        # print("fds",fds)
        DM, determinents = depMatrix.dependencyMatrix(rel, fds)
        # print("DM")
        # print(DM)

        DG = depMatrix.directedGraph(DM, determinents, rel)
        # print("DG")
        # print(DG)

        DC = depMatrix.dependencyClosure(DM, DG, determinents, rel, fds)
        # print(DC)

        CDC = depMatrix.circularDependency(DM, DC)
        # print("CDC")
        # print(CDC)

        depMatrix.to3NF(CDC, rel, fds)




def start_normalizer(file_name="example_scenario.txt", xml_file="example.xml"):

    content = extract.readfile(file_name)
    x = extract.table_names(xml_file)
    s = extract.get_functionaldep(extract.extractor(content))

    fds = extract.restructure_keys(s, x)

    tables = table_names(xml_file)

    dependencies = get_relevantDep(fds, tables)

    normalize(dependencies, tables)
