print("enter the string to check whether it is palindrome")
str=input()
start=0
flag=0
mid=len(str)//2
last=len(str)-1
while(start<=mid):
    if(str[start]==str[last]):
        start+=1
        last-=1
    else:
        flag=1
        break

if flag==0:
    print("it is a palindrome")
else:
    print("it is not a palindrome")
        
