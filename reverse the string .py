str="geeks quiz practice code"
res=str.split(" ")
print(res)
temp=[]
for i in range(len(res)-1,-1,-1):
    temp.append(res[i])
print(temp)

# Python code
# To reverse words in a given string

# input string
string = "geeks quiz practice code"
# reversing words in a given string
s = string.split()[::-1]
l = []
for i in s:
	# appending reversed words to l
	l.append(i)
# printing reverse words
print(" ".join(l))
