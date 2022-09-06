from abc import ABC;


class parent(ABC):
    def func(self):
        pass;
    def intro(self):
        print("this is an abstract clas")

class child(parent):
    def func(self):
        print("abc")

class child1(parent):
    def func(self):
        print("xyz")

ob = child();
ob1=child1();
ob.intro()
