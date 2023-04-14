str="sheena loves eating apple and mango. Her sister also loves eating apple and mango"
l1=str.split(" ")
obj={}
minocc=1
for i in range(0,len(l1)):
    item=l1[i]
    if item in obj:
        obj[item]+=1
    else:
        obj[item]=1

    if(obj[item]>minocc):
        element=item
        minocc=obj[item]
print("Frequency of each words are")
print(obj)
print("frequency of highest occurence", element)
