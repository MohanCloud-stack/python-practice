array=[1,2,3,4,5]
k=3
for i in range(0,k):
    temp=array[0]
    for j in range(0,len(array)-1):
        array[j]=array[j+1]
    
    array[len(array)-1]=temp

print(array)
