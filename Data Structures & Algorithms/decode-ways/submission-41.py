class Solution:
    def numDecodings(self, s: str) -> int:
        l=1
        if s[0]=="0":
            r=0
        else:
            r=1
        for i in range (1,len(s)):
            temp=r
            if s[i]=="0":
                if s[i-1]!="1" and  s[i-1]!="2":
                    return 0
                else:
                    r=l
                   
           
            elif s[i-1]=="1" or (s[i-1]=="2" and 1<=int (s[i])<=6):
                
                r=l+r

            else:
                r=r
            l=temp
        return r
                
            

            
        