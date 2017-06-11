fd = [[['A', 'B'], ['C', 'D', 'E', 'F']],
      [['A'], ['C', 'D']]]
# fd = [[['ssn','Pnumber'],['Hours']],[['ssn'],['Ename']],[['Pnumber'],['Pname','Plocation']]]


def check_transitive(fds):
    for i, v in enumerate(fds):
        for ind, x in enumerate(fds):
            if ind != i and len(x[0]) < len(v[0]):
                print(x[0], v[0])
                print(str(x[0])not in str(v[0]))
                print("transitive dependency exist")

check_transitive(fd)