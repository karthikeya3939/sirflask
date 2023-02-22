class Base:
    def fn1(self):
        print("Base class")
class Derived(Base):
    def fn2(self):
        print("Derived class")
ob=Derived()
ob.fn1()
ob.fn2()
        
