class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=""
        if not s:
            return res
        maxLen=0
        def palindrom(l,r):
            nonlocal res,maxLen
            while l>-1 and r<len(s):
                if s[l]==s[r]:
                    if maxLen<r-l+1:
                        maxLen=r-l+1
                        res=s[l:r+1]
                    r+=1
                    l-=1
                else:
                    break
        for i in range(len(s)):
            palindrom(i,i)
            palindrom(i,i+1)
        return res

        
        