class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        amount=[0]*(len(s)+1)
        amount[0]=1
        if s[0]!="0":
            amount[1]=1
        else:
            amount[1]=0
        for i in range(1,len(s)):
   
            if s[i-1]=="1"  or s[i-1]=="2" and  0<=int (s[i])<=6:
                if  s[i]=="0":
                    amount[i+1]=amount[i-1]
                else:
                    amount[i+1]=amount[i]+amount[i-1]
                
            elif s[i]=="0" and (s[i-1]=="0" or int(s[i-1])>2):
                amount[i+1]=0
            else:
                amount[i+1]=amount[i]
        return amount[-1]




