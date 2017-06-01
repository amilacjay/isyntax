import numpy as np

# relation = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
#
# fdependencies = [[['A', 'B'],['C', 'E', 'F', 'G', 'H']],
#                  [['A'],['D']],
#                  [['F'],['G']],
#                  [['B','F'],['H']],
#                  [['B', 'C', 'H'],['A', 'D', 'E', 'F', 'G']],
#                  [['B', 'C','F'],['A', 'D', 'E']]]



# relation = ['A', 'B', 'C', 'D', 'E']
#
# fdependencies = [[['A', 'B'],['E']],
#                  [['B','C'],['A']],
#                  [['D','E'],['A']]]

relation = ['A', 'B', 'C']

fdependencies = [[['A'],['B']],
                 [['B'],['C']],
                 [['B'],['A']]]




# determinants = [x[0] for x in fdependencies]
determinants = [['A'],['B']]


def getDependencyMatrix(dets, skeys, fds):
    dm = []
    for i, d in enumerate(dets):
        row = []
        for k in skeys:

            list = [fd[1][0] for fd in fds if fd[0]==d]

            if k in d:
                row.append(2)
            elif k in list:
                row.append(1)
            else:
                row.append(0)

        dm.append(row)
    return dm

DM = getDependencyMatrix(determinants, relation, fdependencies)

DG = np.zeros((len(determinants), len(determinants)), dtype=np.int)

print(DM)
print(DG)

def getDirectedGraph(dets, dm, dg, skeys):
    for i, det in enumerate(dets):
        for j, det in enumerate(dets):
            indexList = [skeys.index(skey) for skey in det]
            valueList = [dm[i][index] for index in indexList]

            for v in valueList:
                if v != 0 and dg[i][j] != -1:
                    dg[i][j] = 1
                else:
                    dg[i][j] = -1



getDirectedGraph(determinants, DM, DG, relation)

print(DG)


def getDependencyClosure(matrix, graph, dets, fds, relation):
    closure = matrix.copy()

    for r in range(len(graph)):
        for c in range(len(graph)):
            if r != c and graph[r][c] != -1:
                det = dets[c]
                skeys = fds[c][1]
                # skeys = [fd[1][0] for fd in fds if fd[0]==det]
                skeyIndexList = [relation.index(sk) for sk in skeys]

                for i in range(len(closure)):
                    for j in skeyIndexList:
                        if matrix[i][j] != 0 and matrix[i][j] != 2:
                            # matrix[i][j] = 0
                            closure[r][j] = ''.join(det)

    return closure


dClosure = getDependencyClosure(DM, DG, determinants, fdependencies, relation)


print(dClosure)


def circularDependency(dependencyMetrix, closure):
    for r in range(len(dependencyMetrix)):
        for c in range(len(dependencyMetrix[0])):
            if closure[r][c] is str:
                if findOne(r, c, c, len(dependencyMetrix)) and dependencyMetrix[r][c]==1:
                    closure[r][c]=1



def findOne(i, j, k, n):
    if(dClosure[j][k]==1 and n>=1):
        return 0
    elif(n<1):
        return 1
    else:
        return findOne(i, dClosure[i][k], k, n-1)


circularDependency(DM, dClosure)


# print(dClosure)






