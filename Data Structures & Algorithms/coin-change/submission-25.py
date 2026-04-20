class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        opt=[float("inf")]*(amount+1)
        opt[0]=0
        
        for c in coins:
            for i in range(1,len(opt)):
                if c>i:
                    continue
                opt[i]=min(opt[i],opt[i-c]+1)
        return -1 if opt[-1]==float("inf") else opt[-1]
        