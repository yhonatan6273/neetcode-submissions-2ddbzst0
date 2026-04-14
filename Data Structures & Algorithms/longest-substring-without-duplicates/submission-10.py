class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
       
        res=1
        i=0
        j=0
        substring=set()
        while j<len(s):

            if i==j:
                substring.add(s[j])
                j+=1
                continue
            if s[j] in substring:
                while s[j] in substring:
                    substring.remove(s[i])
                    i+=1
            substring.add(s[j])
            res=max(res,j-i+1)
            j+=1

        return res
        