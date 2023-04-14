random_list = ['A', 'A', 'B', 'C', 'B', 'D', 'D', 'A', 'B']
obj={}
minocc=1

for i in range(0,len(random_list)):
    item=random_list[i]
    if item in obj:
        obj[item]+=1
    else:
        obj[item]=1
    
    if(obj[item]>minocc):
        element=item
        minocc=obj[item]

print(obj)
print("maximum frequnecy",element)
