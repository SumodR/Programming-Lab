f=0
s=1
sum=0
n=int(input("Enter limit:"))
if (n>=0):
    print("0\t")
elif (n>=1):
    print(",1")
for i in range(2,n+1):
    sum=f+s
    print(",",sum)
    f=s
    s=sum
