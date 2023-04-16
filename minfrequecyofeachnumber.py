print("enter the String that has to be tested")
str=[3,4,5,6,6,6,6,6,7,8,9,9,0,1,2]
minocc=1
obj={}
item=" "
for i in range(0,len(str)):
    element=str[i]
    if element in obj:
        obj[element]+=1
    else:
        obj[element]=1
     
res=dict(sorted(obj.items()))
for key in res:
    if(res[key]==1):
        print(key)
        break;
    
