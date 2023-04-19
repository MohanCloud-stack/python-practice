def sorting(nums):
    for i in range(0,len(nums)):
        swapped=False
        for j in range(1,len(nums)-i):
            if(nums[j]<nums[j-1]):
                temp=nums[j]
                nums[j]=nums[j-1]
                nums[j-1]=temp
                swapped=True
        if not swapped:
            break
    return nums
print(sorting([3,1,5,4,2]))
