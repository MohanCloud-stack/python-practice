def largest(arr,n):
    
    for i in range(0,len(arr)):
        max=arr[i]
        if(max>arr[i]):
            max=arr[i]
        
    return max



arr=[10,20,45]
n=len(arr)
print(largest(arr,n))
