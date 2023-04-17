nums1=[1,2,3,0,0,0]
m = 3
nums2=[2,5,6]
n = 3
i=m-1
j=n-1
k=m+n-1
while(i>=0 and j>=0):
    if(nums1[i]>nums2[j]):
        nums1[k]=nums1[i]
        i=i-1
        k=k-1
    else:
         nums1[k]=nums2[j]
         j=j-1
         k=k-1
#pending elements left out inside the array
while(i>=0):
    nums1[k]=nums1[i]
    k=k-1
    i=i-1
while(j>=0):
    nums1[k]=nums2[j]
    k=k-1
    j=j-1

print(nums1)
