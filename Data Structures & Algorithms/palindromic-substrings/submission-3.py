class Solution:
    def countSubstrings(self, s: str) -> int:
       
        res=0
        
        def palindrom(L,R):
            nonlocal res
            while L>=0 and R<len(s) and s[L]==s[R]:
                res+=1
                L-=1
                R+=1
            
        for i in range(len(s)):
            palindrom(i,i)
            palindrom(i,i+1)
        return res

        