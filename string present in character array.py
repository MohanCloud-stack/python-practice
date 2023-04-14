l1=['A','B','C','D','E','F','A','B','F']
s1="GHI"
count=0
for i in s1:
    count=0
    for j in range(0,len(l1)):
        if(i == l1[j]):
            count=count+1
            break
    
if(count>=1):
        print("charcter present in list")
else:
        print("character not present in list")
