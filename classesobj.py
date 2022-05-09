#a class is a blueprint for creating objects
#python is a object oriented programming language.almost every thing in python is an object
class car:
    car1="audi"
    print(car1)
    def __init__(self,age,name):#all classes have a init function which is always executed when the class is being initiated
        self.name=name
        print(name,age,self.name)


obj=car(25,"vamshi")
print(obj.car1)
class myclass:
    def car(self,name,age):
        self.name=name
        print(name,age)
    def vehicle(self):
        print(self.name)
obj1=myclass()
obj1.car("vamshi",21)
obj1.vehicle()
#self parameter=it is a current instance of the class and used to access the variables that belongs to the class
class test:
    def fun(sillyobj,name,age):#here we used sillyobj instead of self
        sillyobj.name=name
    def fun1(abc):#here we used abc instead of self.But both sillyobj and abc refers to same that means self
        print(abc.name)
obj2=test()
obj2.fun("vamshi",21)
obj2.fun1()
#modify and delete object properties
class test1:
    def mod(self,x):
        pass
ob=test1()
ob.mod(45)
ob.x=25
print(ob.x)
class test2:
    def delete(self):
        x=45
        print(x)
object=test2()
del object#it shows an error becuase the created object is deleted here
object.delete()




