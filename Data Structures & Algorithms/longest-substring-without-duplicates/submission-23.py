class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        if not s:
            return res
        j=0
        i=0
        substring=set()
        while j<len(s):
            while  s[j] in substring:
                substring.remove(s[i])
                i+=1
            substring.add(s[j])
            res=max(res,j-i+1)
            j+=1
        return res