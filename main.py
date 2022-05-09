x=str(3)
y=str(46)
z=float(2)
x,y,z="orange","banana","apple"
a=b=c="vamshi"
fruits=["banana","apple","orange"]
g,h,i=fruits
print(x+y+z+a,b,c,g,h,i)
#variables that are created outside of the methods are known as Global variables and are used where ever the program
#varibales that are created inside the method are known as local variable and are used only inside that particular method itself
Global=64
def myfun():
    Local=45
    print(Global+2)
    print(Local+4)
myfun()
#to create a global variable inside a particular method we can use global keyword
def myfun1():
    global k
    k="awesome"
myfun1()
print("python is "+k)
#python numbers
#int
#float
#complex
#strip() function - used to remove whitespaces
a="    vamsi krishna"
print(a)
print(a.strip())
#string format-used to combine numbers and strings
a=5
b="vamshi krishna has {} rupees"
print(b.format(a))
v=21
b=20
a="vamshi is {} years old and bhanu is {} years old"
print(a.format(v,b))
#escape character
print("This is \"vamshi\" from veltech university")
#string methods
#capitalize()-converts first character to upper case
a="vamshi krishna"
print(a.capitalize())
#casefold()-converts string into lower case
a="VAMSI KRISHNA"
print(a.casefold())
#center()-returns a centered string
a="vamshi krishna"
print(a.center(40))
#python booleans
print(10>5)
print(5>10)
print(10 == 9)
print(bool(5))
#check if an object is an integer or not
x=45
print(isinstance(x,float))
#operators
#floor division
print(8.97//3)
x=0
x+=3
print(x)
#identify operators
x=4
y=5
print(x is y)
print(x is not y)
#membership operator
x="vamshi"
y="v"
print(y in x)
print(y not in x)
#change item value in list
listi=["apple", "banana", "grapes"]
listi[1]= "pine apple"
print(listi)
#change the range of item values in the list
listi=["apple", "banana", "grapes"]
listi[1:2]=["blackcurrent"]
print(listi)
listi[1:]=["blueberry"]
print(listi)
#insert items into list
listi=["apple", "banana", "grapes"]
listi.insert(1, "bluberry")
print(listi)
#extend a list with another list
listi=["apple", "banana", "grapes"]
list1=["brinjal","carrot"]
listi.extend(list1)
print(listi)
#extend function is used to add different iterable objects
listi=["apple", "banana", "grapes"]
tuple=("rabbit","dog")
listi.extend(tuple)
print(listi)
#remove items from list
listi=["apple", "banana", "grapes"]
listi.remove("banana")
print(listi)
listi.pop()
print(listi)
listi.append("orange")
listi.pop(0)
print(listi)
#delete key word in lists
listi=["apple", "banana", "grapes"]
del listi[0]
print(listi)
#clear in list
listi=["apple", "banana", "grapes"]
listi.clear()
print(listi)
#for loop through list
listi=["apple", "banana", "grapes"]
for i in range(len(listi)):
    print(listi[i])
#looping using list comprehension
listi=["apple", "banana", "grapes"]
[print(x) for x in listi]
#list comprehension
listi=["apple", "banana", "grapes"]
newlist=[]
for i in listi:
    newlist.append(i)
print(newlist)
#sorting the list
listi=["pine apple", "apple", "banana", "grapes"]
listi.sort()
print(listi)
#sorting list descending order
listi=["pine apple", "apple", "banana", "grapes"]
listi.sort(reverse=True)
print(listi)
#case sensitive sorting
listi=["Pine apple", "apple", "Banana", "grapes"]
listi.sort()
print(listi)
#case insensitive sorting
listi=["Pine apple", "apple", "Banana", "grapes"]
listi.sort(key = str.lower)
print(listi)
#reverse order
listi=["Pine apple", "apple", "Banana", "grapes"]
listi.reverse()
print(listi)
#copy list
listi=["Pine apple", "apple", "Banana", "grapes"]
mylist=listi.copy()
print(mylist)
newlist=list(mylist)
print(newlist)



