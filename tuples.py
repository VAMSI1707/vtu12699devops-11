#tuples
tu=("Pine apple", "apple", "Banana", "grapes")
#want to change item in the tuple first convert tuple to list
list2=list(tu)
list2.insert(1,"cherry")
tu=tuple(list2)
print(tu)
#unpacking a tuple
#we normally assign the value to a variable(tuple) is known as packing
#but we can extract all the values from the tuple and assign to a individual variable
tu=("Pine apple", "apple", "Banana", "grapes")
(pine,apple,banana,grapes)=tu
print(pine)
#using asterisk *
"""if the number of variables is less than the values then you can add a * to the variable name and the values to be assigned to variable as a list"""
tu=("Pine apple", "apple", "Banana", "grapes")
(pine,banana,*apple)=tu
print(apple)
#mutiply tuples
tu=("Pine apple", "apple", "Banana", "grapes")
mytup=2*tu
print(mytup)
#sets={ }
#joining two sets
#union()-used to add two different sets
s={"Pine apple", "apple", "Banana", "grapes"}
s2={"vamshi","krishna"}
s3=s.union(s2)
print(s3)
#update()-used to insert items from one set to another set
s={"Pine apple", "apple", "Banana", "grapes"}
s2={"vamshi","krishna"}
s.update(s2)
print(s)
#intersection_update()-used to keep only the items that are present in two sets and returs into the same set
s3={"vamshi","bhanu"}
s4={"vamshi","vibi"}
s3.intersection_update(s4)
print(s3)
#intersection()-used to keep only the items that are present in two sets and returs into a new set
s3={"vamshi","bhanu"}
s4={"vamshi","vibi"}
s5=s3.intersection(s4)
print(s5)
#dictionaries
d1={"name":"vamshi","age":21}
print(d1["age"])
print(d1.get("name"))
print(d1.keys())
#adding new keys and values to dictionaries
d1={"name":"vamshi","age":21}
d1["gender"]="male"
print(d1.keys())
print(d1.items())
#change values
d1["name"]="krishna"
print(d1)
#update()-to change the values in dictionary
d1.update({"name":"vamshi"})
print(d1)
#update()-it is also used to add new keys and values to the dictionary
#remove kays from dictionary
d1.pop("gender")
print(d1)
d1.popitem()
print(d1)
#we can use del key word to delete a particular key from the dictionary or whole dictionary
d1={"name":"vamshi","age":21}
del d1["age"]
print(d1)
#nested dictionaries
myfamily={
    "child1":{
        "name":"vamshi",
        "age":21
    },
    "child2":{
        "name":"achyuth",
        "age":24
    }
}
print(myfamily.items())
game1={
    "name":"kabaddi"
}
game2={
    "name":"khokho"
}
games={
    "game1":game1,
    "game2":game2
}
print(games.items())