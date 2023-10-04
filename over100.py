li=[]
n=int(input("enter the limit"))
print("enter the integers")
for i in range (0,n):
    e=int(input())
    if e>100:
        li.append("over")
    else:
        li.append(e)
print("",li)
