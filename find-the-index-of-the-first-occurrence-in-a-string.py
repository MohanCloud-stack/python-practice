print("enter the haystack")
haystack=input()
print("enter the needle")
needle=input()
temp=[]
if needle in haystack:
    for i in range(len(haystack)):
        if haystack[i:i+len(needle)]==needle:
            temp.append(i)


print(min(temp))

    
