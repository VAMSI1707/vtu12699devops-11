#inheritance allows to define a class that inherits all the methods and properties from another class
#parent class is also known as base class
#child class is also known as derived class
class person:
    x=45
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def printname(self):
        print("firstname is",self.fname)
class student(person):
    print(person.x)
p=student("vamshi","krishna")
p.printname()
#super() function-it will make the child class inherit all the methods and properties from its parent
class test:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def fun(self):
        print(self.fname,self.lname)
class child(test):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)#by using super() method you don not have to use the name of parent class,it will automatically inherit
c=child("vamshi","krishna")
c.fun()


