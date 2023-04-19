print("enter the range")
n=int(input())
temp=" "
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print("\r")
for i in range(1,n+1):
    for j in range(n+1,i,-1):
        print("*",end=" ")
    print("\r")
  
