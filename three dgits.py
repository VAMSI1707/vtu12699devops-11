x=int(input())
y=int(input())
z=int(input())
value=str(float(x**y/z)).split(".")
first=value[0]
sec=value[1]
second=""
if len(sec)==1:
    second=second+sec[0]+"0"+"0"
elif len(sec)==2:
    second=second+sec[0]+sec[1]+"0"
else:
    second=second+sec[0]+sec[1]+sec[2]
val=first+"."+second
fa=""
for j in val:
    if j==".":
        n= val.index(".")
        if n<=3:
            for i in val:
                fa+=i
        else:
            i=-3
            while i<=3:
                fa+= val[n + i]
                i =i+1
print(fa)








