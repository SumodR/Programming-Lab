l1=[]
l2=[]
l3=[]
n1=int(input("enter the limit"))
print("enter the elements")
for i in range(0,n1):
    l1.append(int(input()))
n2=int(input("enter the limit"))
print("enter the value")
for i in range(0,n2):
    l2.append(int(input()))
if len(l1)==len(l2):
    print("list are of same length")
else:
    print("list are of different length")
if sum(l1)==sum(l2):
    print("the sum of elements are same")
else:
    print("the sum of elements are not same")
for i in l1:
    if i in l2:
        l3.append(i)
print("values occured",l3)
