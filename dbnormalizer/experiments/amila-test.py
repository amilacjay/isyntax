import numpy as np
import copy

def dependencyMatrix(relation, fds):

    determinants = []
    [determinants.append(fd[0]) for fd in fds if fd[0] not in determinants]

    # determinants = list(set(determinants))

    DM = []
    for d in determinants:
        row = []
        for sk in relation:

            determiners = [fd[1][0] for fd in fds if fd[0]==d]

            if sk in d:
                row.append(2)
            elif sk in determiners:
                row.append(1)
            else:
                row.append(0)

        DM.append(row)
    return DM, np.sort(determinants)

def directedGraph(dm, determinents, relation):

    DG = np.zeros((len(determinents), len(determinents)), dtype=np.int)

    for i, detI in enumerate(determinents):
        for j, detJ in enumerate(determinents):
            attrs = detJ
            indexes = [relation.index(d) for d in attrs]
            values = [dm[i][index] for index in indexes]

            for value in values:
                if value != 0 and DG[i][j] != -1:
                    DG[i][j] = 1
                else:
                    DG[i][j] = -1

    return DG

def dependencyClosure(dm, dg, determinents, relation, fds):
    DC = copy.deepcopy(dm)
    for i, dgI in enumerate(dg):
        for j, dgJ in enumerate(dg):
            if(i != j and dg[i][j] != -1):
                # print(determinents[i],' to ',determinents[j])
                det = determinents[j].tolist()
                # print(det)
                skeys = [fd[1][0] for fd in fds if fd[0]==det]
                skeyIndexes = [relation.index(sk) for sk in skeys]
                # print(skeys)
                for s in skeyIndexes:
                    if(dm[i][s] not in [1, 2]):
                        DC[i][s] = ''.join(det)

    return DC

def circularDependency(dm, dc):
    DC = copy.deepcopy(dc)

    for i, row in enumerate(dm):
        for j, col in enumerate(dm[i]):
            if str(DC[i][j]).isalpha():
                if findOne(i, j, j, len(dm), DC) and dm[i][j]==1:
                    DC[i][j] = 1;


    return DC

def findOne(i, j, k, n, dc):
    if dc[i][k]==1 and n>=1:
        return False
    elif n<1:
        return True
    else:
        return findOne(i, dc[i][k], k, n-1, dc)



#### examples


relation = ['A', 'B', 'C']

fds = [
        [['A'],['B']],
        [['B'],['A']],
        [['B'],['C']]
      ]

# relation = ['A', 'B', 'C', 'D', 'E']
#
# fds = [
#         [['A', 'B'],['E']],
#         [['B', 'C'],['A']],
#         [['D', 'E'],['A']]
#       ]


DM, determinents = dependencyMatrix(relation, fds)
print(DM)

DG = directedGraph(DM, determinents, relation)
print(DG)

DC = dependencyClosure(DM, DG, determinents, relation, fds)
print(DC)

CDC = circularDependency(DM, DC)
print(CDC)




