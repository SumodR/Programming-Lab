elem=input("enter a word")
vowels=['a','e','i','o','u']
lists=[]
for x in elem:
    if x in vowels and x not in lists:
        lists.append(x)
print(lists)
