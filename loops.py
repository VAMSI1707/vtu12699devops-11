#if -else statements
if 5>2:
    print("yes")
#short hand if-else
print("yes") if 5<2 else print("no")
#nested if
x=20
if x%2==0:
    if x>10:
        print("even and more than 10")
    else:
        print("!!!")
#pass statement-if you dont want to keep content inside if statement then give pass and also used to avoid error
if 5>2:
    pass
#while loop
i=0
while i<5:
    print("vamshi")
    i+=1
#break statement-used to stop the loop even the while condition is true
i=1
while i<5:
    print(i)
    if i==3:
        break
    i+=1
#continue statement-used to stop the current iteration and continue the next iteration
i=0
while i<6:
    i += 1
    if i==3:
        continue
    print(i)
#else statement in while loops
i=0
while i<=5:
    print(i)
    i+=1
else:
    print("i is greater than 5")
#for loops
x="vamshi"
l=[]
for i in x:
    l.append(i)
    print(i)
print(l)
#range()
for i in range(6):
    print(i)
for j in range(1,4):
    print(j)
for k in range(5):
    if k==3:
        break
    print(k)
else:
    print("completed")#if the loop breaks the esle bolck is not executed
#nested for loops
fruits=["apple","banana","grapes"]
color=["red","yellow","violet"]
for x in fruits:
    for y in color:
        print(x,y)