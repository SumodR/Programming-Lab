s=int(input("enter the start year"))
e=int(input("enter the end year"))
years=[]
for i in range(s,e+1):
    if i%400==0:
        years.append(i)
    elif i%4==0 and i%100!=0:
        years.append(i)
print("leap years are \n")
print(years)
