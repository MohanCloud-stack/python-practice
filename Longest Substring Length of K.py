Given a String and a character K, find longest substring length of K.

Input : test_str = ‘abcaaaacbbaa’, K = b 
Output : 2 
Explanation : b occurs twice, 2 > 1. 

Input : test_str = ‘abcaacccbbaa’, K = c 
Output : 3 
Explanation : Maximum times c occurs is 3.

print("enter the string to be read")
str=input()
print("enter the substring to be compared")
k=input()
count=0
minocc=1
for i in str:
    if(i==k):
        count+=1
    else:
        count=0

    if(count>minocc):
        minocc=count

print(minocc)
