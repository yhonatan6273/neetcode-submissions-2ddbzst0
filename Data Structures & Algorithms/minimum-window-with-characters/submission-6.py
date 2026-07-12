from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res=""
        minLen=float("inf")
        table=Counter(t)
        copy=table.copy()
        for i in range(len(s)):
            if s[i] in copy:
                j=i
                while j<len(s):
                    if s[j] in copy:
                        copy[s[j]]-=1

                        if copy[s[j]]==0:
                            del copy[s[j]]

                            if len(copy)==0:
                                if minLen>j-i+1:
                                    res=s[i:j+1]
                                    minLen=j-i+1

                                break
                    j+=1
            for key,val in table.items():
                copy[key]=val
        return res




        