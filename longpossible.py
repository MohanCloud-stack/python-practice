def longpossiblestring(str):
    temp=[]
    if(len(str)) > 0:
        str.sort(key=len)
        first,last=str[0],str[-1]
        for i in  range(len(first)):
            if(first[i] == last[i]):
                temp.append(first[i])
            else:
                return " ".join(temp)
    return " ".join(temp)
print(longpossiblestring(["flower","flow","flight"]))
