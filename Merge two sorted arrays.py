num1=[5,8,9]
num2=[4,7,8]
n1=len(num1)
n2=len(num2)
res=[0 for i in range(n1+n2)]
i=0
j=0
k=0
while(i<n1 and j<n2):
    if(num1[i]<num2[j]):
        res[k]=num2[j]
        k+=1
        j+=1
    else:
        res[k]=num1[i]
        k+=1
        i+=1


    while(i<n1):
        res[k]=num1[i]
        k=k+1
        i=i+1
    while(j<n2):
        res[k]=num2[j]
        k=k+1
        j=j+1

final=res.sort()
print(res)

