class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        temp=[]
        if(len(strs)) > 0:
            strs1=sorted(strs)
            first,last=strs1[0],strs1[-1]
            for i in  range(len(first)):
                if(len(last) > i and last[i] == first[i]):
                    temp.append(first[i])
                else:
                    return "".join(temp)
        return "".join(temp)
