class Analyzer:
    def __init__(self, fds, keys, relation, candidateKeys, subs):
        self.fds = fds
        self.primary = keys
        self.relation = relation
        self.candiKeys = candidateKeys
        self.subset = subs
        self.fdClosure = []
        for each in fds:
            self.fdClosure.append(each)

    def checkOneNF(self):
        return self.fds

    def checkTwoNF(self):
        return 'asd'

    def checkThreeNF(self):
        return 'asd'

    # Armstrong's Axiom of reflectivity
    def reflexitivity(self):
        for rel in self.relation:
            self.fdClosure.append(
                [[rel], [rel]]
            )
        for sset in self.subset:
            for sub in sset[1]:
                self.fdClosure.append([sset[0],[sub]])
        return self.fdClosure

    # Armstrong's Axiom of Augmentation
    # def augmentation(self):
    #     for att in self.relation:
    #         for one in self.fdClosure:
    #             print(one, "**")

    def removeDup(self):
        return self.fdClosure

    def getLHS(self, lst):
        lhsList = []
        for item in lst:
            lhsList.append(item[0])
        return lhsList

    def getRHS(self, lst):
        rhsList = []
        for item in lst:
            rhsList.append(item[1])
        return rhsList


candidateKeys = ['A', 'C']

R = ['A', 'B', 'C', 'D', 'E', 'F']

funcdeps = [
    [['A'], ['B']],
    [['C'], ['D']],
]

subset = [[['A'], ['D', 'E']]]

# test
test = Analyzer(funcdeps, '', R, candidateKeys, subset)

test.reflexitivity()
# print(i[0], '->', i[1])

# test.augmentation()

for a in test.removeDup():
    print(a)
# for a in test.getLHS():
#     for b in test.getRHS():
#         print(a, '->', b)
