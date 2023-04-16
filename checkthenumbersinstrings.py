print("enter the numbers including the strings")
str=input()
num="0123456789"
count=0
temp=[]
for i in range(0,len(str)):
    if(str[i] in num):
        count+=1
        temp.append(str[i])
        res=" ".join(temp)
print(res)
