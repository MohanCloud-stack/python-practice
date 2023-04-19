nums=[12,35,1,10,34,1]
nums.sort()
for i in range(len(nums)-2,-1,-1):
    if(nums[i]!=nums[len(nums)-1]):
        break
print(nums[i])
