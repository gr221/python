
class A(object):
    def __init__(self, *args, **kwargs):
        #super(A,self).__init__()
        print("A")

class B(object):
    def __init__(self, *args, **kwargs):
        #super(B,self).__init__()
        print("B")

class C(A,B):
    def __init__(self, *args, **kwargs):
        super(C,self).__init__(self, *args, **kwargs)
        print("C")


c = C()
print(C.__mro__)
