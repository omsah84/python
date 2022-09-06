class parent:
    def fun(self):
        print("this is a parent class function");

class hell:
    # def fun2(self):
        print("hell");

class child(parent,hell):
    def fun1(self):
        print("this is child class");

ob = child();
ob.fun1();
ob.fun();
# ob.fun2();

