nums=[1,2,3,5]
i=0
n1=len(nums)
def swap(nums,i,correct):
    temp=nums[i]
    nums[i]=nums[correct]
    nums[correct]=temp
    
while(i<n1):
    correct=nums[i]-1
    if(nums[i]<=n1 and nums[i]!=nums[correct]):
        swap(nums,i,correct)
    else:
        i=i+1

for i in range(0,len(nums)):
    #correct=nums[i]-1
    if(nums[i]==i+1):
        continue
    else:
        break

print(i+1)
