
class A(object):
    at1 = 2
    def m1(self):
        pass
    def m2(self, x):
        return x + self.at1
    def __init__(self, z):
        self.z = z
    def __del__(self):
        pass
    #ToString()
    def __repr__(self):
        pass

class B(A):
    def  __init__(self):
        super(self, 2)
        A.__init__(z=1)
        self.s = 1
        v = 2

b = B(2)
b.m1(2)
a = A(2)
print(a.z)
