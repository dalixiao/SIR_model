class Test:
    def __init__(self):
        pass

    def methodA(self):
        self.var1 = 3

    def methodB(self):
        self.methodA()
        print(self.var1)

test = Test()
test.methodB()
