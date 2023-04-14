print("Enter the number to check for amstrong")
n=int(input())
s=n
b=len(str(n))
sum=0
while n!=0:
    r=n%10
    sum=sum+(r**b)
    n=n//10

if sum == s:
    print("it is a amstrong number")
else:
    print("it is not amstrong number")
