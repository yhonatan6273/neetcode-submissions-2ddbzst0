class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return -1
        helper=[float("inf")]*(amount+1)
        helper[0]=0
        for i in range(1,len(helper)):
            for c in coins:
                cur=helper[i]
                if c>i:
                    continue
                helper[i]=min(cur,helper[i-c]+1)
        if helper[-1]==float("inf"):
            return -1
        return helper[-1]
        
        
        