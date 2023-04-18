str="gfghsisbjknlmkesbestgfgsdcngfgcsdjnisdjnlbestdjsklgfgcdsbestbnjdsgfgdbhisbhsbestdkgfgbbestbestbestbest"
l1=['gfg','is','best']
minocc=1
count=0
obj={}
item=" "
for i in l1:
    if i in str:
        res=str.count(i)
        obj[i]=res
        count+=1
    if (obj[i]>minocc):
        minocc=obj[i]
        item=i
print(item)
