str=input("enter a word")
occur=dict()
words=str.split()
for i in words:
    if i in occur:
        occur[i]+=1
    else:
        occur[i]=1
print ("the occurance of each word is",occur)
    
