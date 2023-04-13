num=[23,65,19,90]
print("enter the range of positions for the list")
i=int(input())
j=int(input())
if i < len(num) and j < len(num):
  temp=num[i]
  num[i]=num[j]
  num[j]=temp
  print(num)
else:
  print("index value out of range")
