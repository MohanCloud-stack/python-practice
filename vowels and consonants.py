print("count the total number of vowles and consonants")
str=input().lower()
vcount=0
ccount=0
for i in range(0,len(str)):
    if(str[i] == 'a' or str[i] == 'e' or str[i] == 'o' or str[i] == 'u'):
        vcount+=1
    elif(str[i]>='a'and str[i]<='z'):
        ccount+=1

print("no of vowels",vcount)
print("no of consonants",ccount)
