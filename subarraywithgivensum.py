nums=[1,4,20,3,10,5]
sum=24
j=0
temp=[]
for i in range(0,len(nums)):
    cursum=nums[i]
    if cursum==sum:
        break
    else:
        for j in range(i+1,len(nums)):
            cursum=cursum+nums[j]
            if cursum==sum:
                a=i
                b=j
                print(i,j)
for k in range(a,b+1):
    temp.append(nums[k])
print(temp)
 
