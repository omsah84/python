class example:
    def __init__(self,name):
        self._name =name;
    
    def __show(self):
        print("this ia a private number function")

ob =example("hell");
ob._name;
ob._example__show();