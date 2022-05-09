def fruits():#function created
    print("apple")
fruits()#function called
#arguments
def fruit(a,b):
    print(a,"and",b,"are beautiful")
fruit("bhavya","bhanu")
#parameters and srguments both are used for the same thing:information passed into a function
#arbitary arguments,*args
def car(*parts):#here the values given in the function call will be stored in the * parameter as tuple
    print("parts of the car are",parts)
car("wheels","glass","engine","doors")
#keyword arguments-we can also send the arguments as key=values syntax
def veg(veg1,veg2,veg3):
    print(veg1,"is very spicy")
veg("mirchi","onion","brinjal")
#Arbitary keyword arguments,**kargs
def details(**name):#here the values are given in the function call will be stored in the ** parameter as dictionary
    print("first name is",name["fname"])
details(fname="vamshi",sname="krishna")
#default paramter value
def count(country = "India"):#if we call the function without passing argument,it will take default value
    print("my country is",country)
count()
count("usa")
count("uk")
#passing a list as argument
def lis(list1):
    for i in list1:
            print(i)
list1=["vamshi","krishna"]
lis(list1)
#pass statement in functions
def pas():
    pass
#lambda -can take any number of arguments,but only have one expression
x=lambda a:a+5
print(x(5))
#multiply argument a with argument b using lambda function
x=lambda a,b:a*b
print(x(5,6))
#use lambda in functions
def fun(n):
    return lambda a:a*n
doubler=fun(5)
print(doubler(6))
