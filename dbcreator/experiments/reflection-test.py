class Primary:
    pass

class Secondary:
    pass

class A(Primary):
    def execute(self, x, y):
        print("Class A " + str((x, y)))

class B(Primary):
    def execute(self, x, y):
        print("Class B" + str((x,y)))

class C(Secondary):
    def execute(self, x):
        print("Class C " + x)

class D:
    pass


classList = [A, B, C, D]


for clz in classList:
    obj = clz()
    if isinstance(obj, Primary):
        obj.execute('a', 'b')
    elif isinstance(obj, Secondary):
        obj.execute("Secondary")